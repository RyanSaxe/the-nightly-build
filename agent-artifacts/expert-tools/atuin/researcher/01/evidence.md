# Evidence record: expert-tools/atuin (01)

The evidence supports every capability claim in the commission from Atuin's own
repository and documentation. Confirmed from primary source: history is stored
as rows in a local SQLite database with the exact context fields the commission
names (working directory, exit code, duration, session, hostname) plus timestamp
and three newer fields (author, intent, shell); interactive Ctrl-R and up-arrow
are rebound to a full-screen search UI; `atuin search` supports command-line
filters by that recorded context, and the concrete "failed commands in this
directory" example the commission wants is exactly `atuin search --exclude-exit
0 --cwd .`; sync is optional and end-to-end encrypted, using a PASETO v4 envelope
scheme; self-hosting is supported; the project is actively maintained (frequent
releases through August 2026, MIT-licensed, written in Rust). The record is thin
in exactly one place, and it is the strongest case against the tool: the
end-to-end encryption protects only *sync*. The local SQLite database is stored
**unencrypted** (stated in the source), and the sync server, though it cannot
read command text, still sees per-host record metadata (host id, record counts,
and timestamps). Both facts come from primary source and are recorded below; the
commission already flags the sync-server trust question, and the local-plaintext
point strengthens it rather than contradicting the angle. A secondary forensic
write-up is included as independent confirmation that the local database is a
real exposure vector, not a hypothetical one.

Source code was read from a clone of `atuinsh/atuin` pinned at commit
`4f99379c77e1137ca26ef2851b0dbe4d265c59e7` (the state of `main` on 2026-08-10).
Citations point to each file's own page on the default branch; line references
are to that commit.

## Sources

```text
URL:         https://github.com/atuinsh/atuin/blob/main/README.md
Kind:        primary — the project's own README, authored by the maintainers; owns the top-level capability and encryption claims.
Establishes: Atuin replaces shell history with a SQLite database and records additional per-command context; sync is optional and fully encrypted, self-hosted or on the maintainer's server; ctrl-r and up are rebound (configurable) to a full-screen search UI; filter modes (session / directory / global) switch via ctrl-r; the old history file is not replaced.
Paraphrase:  Atuin stores shell history in a SQLite database and logs exit code, cwd, hostname, session, and command duration. It offers optional, fully encrypted sync between machines via an Atuin server; the maintainer states she could not access user data even if she wanted to because all sync is encrypted. The feature list names rebinding ctrl-r and up to a full-screen search UI and switching filter modes (current session, directory, or globally) via ctrl-r.
Locators:    Intro paragraph; "## Features" list.
Quote:       "Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands." / "As all history sync is encrypted, I couldn't access your data even if I wanted to." / "search for all successful `make` commands, recorded after 3pm yesterday: atuin search --exit 0 --after \"yesterday 3pm\" make"
```

```text
URL:         https://github.com/atuinsh/atuin/blob/main/crates/atuin-client/src/history.rs
Kind:        primary — the source definition of the client-side history entry; owns the exact per-command context fields and the local-storage-is-plaintext fact.
Establishes: The exact fields Atuin captures per command, and that the client stores history unencrypted locally and only encrypts before sending to the server.
Paraphrase:  The `History` struct fields are: id (client-generated, stored as client_id), timestamp, duration, exit (exit code), command, cwd (working directory when the command ran), session (per-terminal session id), hostname, author (who wrote the command — human or automation/agent identity), intent (optional rationale), deleted_at (soft-delete timestamp), and shell (the shell used). A doc comment states the client stores data unencrypted and encrypts only before sync. `KNOWN_AGENTS` lists AI agent author values ("claude-code", "codex", "copilot", "opencode", "pi"), so the author field distinguishes human vs. agent commands.
Locators:    `pub struct History` (lines ~152–180); comment "Client stores data unencrypted, and only encrypts it before sending to the server." (line ~141); `KNOWN_AGENTS` (line ~24).
Quote:       "Client stores data unencrypted, and only encrypts it before sending to the server."
```

```text
URL:         https://github.com/atuinsh/atuin/blob/main/crates/atuin-client/migrations/20210422143411_create_history.sql
Kind:        primary — the database schema migration; owns the "it is SQLite with these columns" claim independently of prose.
Establishes: The history table is SQLite with columns id, timestamp, duration, exit, command, cwd, session, hostname, a uniqueness constraint on (timestamp, cwd, command), and indexes on timestamp and command. Later migrations add columns: shell (20260709214605_shell.sql), and author + intent (20260224000100_history_author_intent.sql).
Paraphrase:  The original migration creates a `history` table keyed by a text id with integer timestamp/duration/exit and text command/cwd/session/hostname, unique on (timestamp, cwd, command). Separate later migrations `alter table history add column` for shell, author, and intent, matching the History struct.
Locators:    create_history.sql (full file); shell.sql; history_author_intent.sql.
Quote:       "create table if not exists history ( id text primary key, timestamp integer not null, duration integer not null, exit integer not null, command text not null, cwd text not null, session text not null, hostname text not null, unique(timestamp, cwd, command) );"
```

```text
URL:         https://github.com/atuinsh/atuin/blob/main/crates/atuin-common/src/encryption/paseto_v4.rs
Kind:        primary — the implementation of the sync encryption; owns the exact encryption design, not a prose summary of it.
Establishes: Sync encryption is a PASETO v4 (local) / PASERK v4 envelope scheme. Each record gets its own randomly generated 32-byte content-encryption key (CEK); the record data is encrypted with the CEK, and the CEK is itself wrapped (encrypted) by the user's master key. Master key is 32 bytes, generated from OS randomness, stored locally, and exportable via mnemonic (BIP39). This is client-side / envelope encryption ("key wrapping").
Paraphrase:  `encrypt_sync` generates a random per-record CEK, base64-encodes and JSON-packs the payload, builds a PASETO v4 local token with a random nonce, and returns `EncryptedData { raw: <token>, cek: <CEK wrapped by the master key> }`. The design rationale comment (by @conradludgate) explains the random-per-record CEK is standard envelope/key-wrapping encryption and makes key rotation cheap (re-wrap the CEK, not the data). The `Key` type is 32 bytes, zeroized on drop, never serialized so it cannot go over the wire. `Key::generate` draws 32 bytes of OS randomness. Note: the ambient cipher is PASETO v4 local (XChaCha20 + BLAKE2b keyed MAC); the `crypto_secretbox`/XSalsa20Poly1305 import is used only as a source of 32 random key bytes, not as the record cipher.
Locators:    `encrypt_sync` (lines ~486–601) and its doc comment "## CEK?" / "Why a random content-encryption key?"; `struct Key([u8;32])` (line ~113); `EncryptedData` (lines ~433–445).
Quote:       "This cypher has a \"content encryption key\", which is a random 32B key, for each record. Each given data slice gets its own encryption key, which, itself, is encrypted with the given `key` parameter."
```

```text
URL:         https://github.com/atuinsh/atuin/blob/main/crates/atuin-domain/src/record.rs
Kind:        primary — the record envelope that wraps the encrypted payload for sync; owns what the server can and cannot see.
Establishes: The encrypted unit is the record's `data` (EncryptedData). The surrounding record carries, in the clear, a record id, an integer idx (per-host, per-tag record index), the host id, a tag (e.g. "history"), a version string, and a timestamp (nanoseconds). These travel unencrypted so the server can order and de-duplicate records.
Paraphrase:  `Record<Data>` has id, idx (unique per host+tag), host (HostId + name), timestamp, version, tag, and the payload data. Only `data` is the encrypted `EncryptedData`; the id/idx/host/tag/version/timestamp form the `AdditionalData` used as the encryption's implicit assertion and are visible to the server. This is the precise boundary behind the "server can't read your commands but sees metadata" claim: content is encrypted, per-host record counts and timing are not.
Locators:    `pub struct Record<Data>` (lines ~64–80); `pub struct AdditionalData` (lines ~37–52); `EncryptedData` re-export (line 3).
Quote:       "The integer record ID. This is only unique per (host, tag)."
```

```text
URL:         https://github.com/atuinsh/atuin/blob/main/crates/atuin-client/src/settings.rs
Kind:        primary — the client configuration defaults; owns the default sync address, sync cadence, and daemon-is-opt-in facts.
Establishes: Default sync server is https://api.atuin.sh. Auto-sync defaults to on (auto_sync = true) with a default sync_frequency of "5m". The background daemon is opt-in: daemon.enabled defaults to false and daemon.autostart defaults to false (daemon.sync_frequency default 300s when enabled).
Paraphrase:  `DEFAULT_SYNC_URL` is api.atuin.sh. Config defaults set auto_sync true and sync_frequency "5m"; the daemon block defaults enabled=false and autostart=false. So the always-present cost is the SQLite database plus the shell hook; the daemon is an optional addition the user turns on, not a default.
Locators:    DEFAULT_SYNC_URL (line ~42); defaults block set_default("auto_sync", true) (line ~1463), ("sync_frequency", "5m") (line ~1467), ("daemon.enabled", false) (line ~1515), ("daemon.autostart", false) (line ~1516).
Quote:       ".set_default(\"auto_sync\", true)?" / ".set_default(\"sync_frequency\", \"5m\")?" / ".set_default(\"daemon.enabled\", false)?"
```

```text
URL:         https://docs.atuin.sh/18.18/reference/search/
Kind:        primary — the project's own documentation for the `atuin search` command; owns the exact CLI flags.
Establishes: The full flag surface of `atuin search` and the documented worked examples, including the "failed commands in this directory" query.
Paraphrase:  Flags include --cwd/-c (directory to list history for), --exclude-cwd, --exit/-e (filter by exit code), --exclude-exit, --before, --after, --interactive/-i (open the TUI), --limit, --offset, --reverse, --delete / --delete-it-all, --human, --format/-f (fields {command} {directory} {duration} {user} {host} {time} {exit} {relativetime}), and --inline-height. Documented examples: `atuin search --exit 0 cargo` (successful cargo commands); `atuin search --exclude-exit 0 --before 01/04/2021 --cwd .` (failed commands in the current directory before a date); `atuin search --delete --exit 0 --after "yesterday 3pm" cargo`.
Locators:    Flags table; "Examples" section.
Quote:       "--exclude-exit — Don't include commands that exited with this value" / example: "atuin search --exclude-exit 0 --before 01/04/2021 --cwd ."
```

```text
URL:         https://docs.atuin.sh/18.18/guide/shell-integration/
Kind:        primary — project documentation for the shell hook; owns what the integration installs.
Establishes: The integration installs a preexec hook (records command text, timestamp, working directory before a command runs) and a precmd hook (runs after completion, recording exit/duration). Adding `eval "$(atuin init <shell>)"` activates the hooks. Supported shells: Bash, Zsh, Fish, Nushell, xonsh, PowerShell. It sets environment variables including ATUIN_SESSION, ATUIN_HISTORY_ID.
Paraphrase:  Atuin's init hook wires preexec/precmd (or the shell's equivalent) so each command is captured with its context, and rebinds keys (see key-binding page). Six shells are supported.
Locators:    "What Gets Installed" / hooks description; supported-shells list.
Quote:       "Preexec hook: Runs before each command executes. Atuin records the command text, timestamp, and working directory. Precmd hook: Runs after each command completes."
```

```text
URL:         https://docs.atuin.sh/18.18/configuration/key-binding/
Kind:        primary — project documentation for keybindings; owns the up-arrow / Ctrl-R rebinding and how to opt out.
Establishes: By default Atuin binds both the up arrow and Ctrl-R to its search. Each can be disabled independently by passing --disable-up-arrow or --disable-ctrl-r to `atuin init`, or both disabled at once via `export ATUIN_NOBIND="true"` before init.
Paraphrase:  Default behavior rebinds up-arrow and Ctrl-R to Atuin's search UI. Users who want to keep native up-arrow (a common objection, since Atuin's up-arrow opens a full-screen UI rather than recalling the previous line) disable it with `eval "$(atuin init zsh --disable-up-arrow)"`; ATUIN_NOBIND disables both.
Locators:    "Disabling Atuin Key Bindings" section.
Quote:       "eval \"$(atuin init zsh --disable-up-arrow)\"" / "export ATUIN_NOBIND=\"true\""
```

```text
URL:         https://docs.atuin.sh/18.18/guide/sync/
Kind:        primary — project documentation for sync; owns the end-to-end encryption statement and the key/self-hosting facts.
Establishes: History sync is fully end-to-end encrypted; the encryption key is generated at registration, stored locally, retrievable with `atuin key`, must never be shared, and is unrecoverable if lost. Self-hosting is supported by setting sync_address. Auto-sync runs hourly by default in the doc's wording (note: the source default is "5m"; see Contradictions).
Paraphrase:  The sync guide states history is fully end-to-end encrypted so the server cannot snoop, describes the local encryption key and `atuin key`, and documents pointing sync_address at a self-hosted server.
Locators:    Encryption section; key section; self-hosting note.
Quote:       "All of your history is fully end-to-end encrypted, so there are no risks of the server snooping on you."
```

```text
URL:         https://github.com/atuinsh/atuin/releases
Kind:        primary — the project's own release history; owns the maintenance-cadence judgment.
Establishes: Active, frequent releases through August 2026. Latest stable at time of research: 18.19.0 (2026-08-03); 18.18.1 (2026-07-28), 18.18.0 (2026-07-27); an 18.20.0 beta line (beta.3 on 2026-08-07) was in progress. Roughly a stable release every 1–2 weeks with beta iterations between.
Paraphrase:  The release feed shows a steady stream of stable and beta releases across July–August 2026, evidence of an actively maintained project rather than an abandoned one.
Locators:    Releases list, newest first.
Quote:       (dates as listed) "18.19.0 — August 3, 2026" ; "18.18.0 — July 27, 2026".
```

```text
URL:         https://github.com/atuinsh/atuin/blob/main/LICENSE
Kind:        primary — the license file; owns license and original-author facts.
Establishes: Atuin is MIT-licensed, copyright 2021 Ellie Huxtable (the founder/lead maintainer; development now under the atuinsh organization). Repository description "magical shell history"; written in Rust; distributed via the setup.atuin.sh install script and published on crates.io as the `atuin` crate.
Paraphrase:  MIT license, first authored by Ellie Huxtable in 2021, maintained under the atuinsh GitHub organization. Distribution is a Rust binary via the official install script or crates.io.
Locators:    LICENSE header; README badges (crates.io, license).
Quote:       "MIT License / Copyright (c) 2021 Ellie Huxtable"
```

```text
URL:         https://isc.sans.edu/diary/33226
Kind:        secondary — SANS Internet Storm Center diary by Xavier Mertens; reports on Atuin from outside the project. Used only for the adoption counter-case, not for any capability claim.
Establishes: Independent confirmation that Atuin's local SQLite database is a genuine privacy/exposure vector: it silently records far more per-command context than .bash_history, and if sync is on it aggregates commands run on other machines into this host's database.
Paraphrase:  A digital-forensics write-up frames Atuin as "both a gift and a trap" — the rich local database (timestamps, cwd, exit code, duration, session, hostname) is a forensic goldmine, and sync pulls other machines' commands onto the local host, widening the exposure. This corroborates, from an outside party, the source-level fact that the local DB is unencrypted and comprehensive.
Locators:    Article body; "The main DB table is called 'history'" passage.
Quote:       "If sync is enabled, commands executed on other machines under the same account are pulled into this host's database."
Title/author: "Linux Shell Forensic: Let's Dive Into Atuin!", Xavier Mertens, SANS ISC.
```

## Contradictions

- **"End-to-end encrypted" vs. what is actually encrypted.** The README and sync
  guide say history is "fully" encrypted. Read precisely against the source
  (`history.rs`, `record.rs`), the end-to-end encryption protects the sync
  payload only. Two facts qualify the marketing phrasing, both from primary
  source: (1) the local SQLite database is stored **unencrypted** — the
  `history.rs` comment states "Client stores data unencrypted, and only encrypts
  it before sending to the server"; (2) the sync server, while it cannot read
  command text, still receives per-record envelope metadata in the clear (host
  id, per-host record index/count, tag, version, timestamp; see `record.rs`).
  The claim "the server can't see my history" is true for command *content* and
  false for *metadata about how much you run and when*. This is the honest core
  of the commission's "sync-server trust question," and it does not undercut the
  angle — the tool is what it says, with a precisely bounded encryption
  guarantee.

- **Sync cadence: docs say "hourly", source default is "5m".** The sync guide's
  prose describes automatic sync as hourly by default, but the client's config
  default is `sync_frequency = "5m"` (settings.rs line ~1467) with `auto_sync =
  true`. Where they disagree, the source default governs the shipped behavior.
  Flag this if the writer states a number; cite the source default, not the doc
  prose.

- **Ctrl-R "replacement" is also an up-arrow replacement, and some users object
  to the latter.** Atuin rebinds up-arrow to the full-screen search UI, not just
  Ctrl-R. This changes muscle memory for recalling the immediately previous line.
  It is opt-out (`--disable-up-arrow`), which is itself evidence that the default
  is contentious enough to need an escape hatch. Not a contradiction of a
  capability claim, but a real adoption cost the commission asks to be named.

No contradiction was found to the core storage, search, or maintenance claims;
each is confirmed by the source itself.

## Numbers

```text
Figure: 12 context fields captured per command (id, timestamp, duration, exit, command, cwd, session, hostname, author, intent, deleted_at, shell)
Owner:  crates/atuin-client/src/history.rs (`History` struct) + migrations
Scope:  Per history row in the local SQLite `history` table. The commission names five (cwd, exit, duration, session, hostname); the source has these plus timestamp and the newer author/intent/shell/deleted_at fields.
```

```text
Figure: 32 bytes — master encryption key size; one random 32-byte content-encryption key generated per record
Owner:  crates/atuin-common/src/encryption/paseto_v4.rs (`Key([u8;32])`, `encrypt_sync`)
Scope:  Sync encryption. Master key held locally, exportable as a BIP39 mnemonic; each synced record wraps its own random CEK under the master key.
```

```text
Figure: sync_frequency default "5m"; auto_sync default true; daemon.enabled default false
Owner:  crates/atuin-client/src/settings.rs (defaults block)
Scope:  Shipped client defaults. The always-on cost is the SQLite DB + shell hook; the background daemon is opt-in.
```

```text
Figure: Latest stable 18.19.0 (2026-08-03); ~1–2 week stable cadence; MIT license; first authored 2021
Owner:  https://github.com/atuinsh/atuin/releases ; LICENSE
Scope:  Maintenance judgment as of research date 2026-08-10.
```

```text
Figure: 6 supported shells (Bash, Zsh, Fish, Nushell, xonsh, PowerShell)
Owner:  https://docs.atuin.sh/18.18/guide/shell-integration/ (corroborated by README)
Scope:  Shells for which `atuin init` provides an integration.
```

## Source assets

```text
Asset: The demo GIF at the top of the README (demo.gif), showing the interactive search UI with exit code, duration, time, and command columns.
Shows: What the Ctrl-R replacement actually looks like — the full-screen TUI and the context columns the flat history lacks. This is the one visual that carries an argument prose cannot: the reader sees the metadata-rich result rows at a glance.
Crop:  Must retain the result rows showing the exit-code/duration/time columns beside the command. A still frame is enough; omit surrounding README chrome. Note it is an animation, so a representative frame must be chosen.
```

Otherwise: None found. This is a CLI tool; the argument is best carried by a live
shell example (`nb-code`) the writer builds, not by screenshots. The recorded
context fields, the `atuin search --exclude-exit 0 --cwd .` query, and the
before/after of an up-arrow keypress are all clearer as code listings than images.

## Discarded

```text
URL: https://trendoceans.com/atuin-linux/ — third-party install/overview blog; secondary and adds nothing the primary docs do not. Commission forbids third-party summaries for capability claims.
URL: https://kx.cloudingenium.com/en/atuin-shell-history-sync-search-statistics-guide/ — same: derivative walkthrough, no independent claim.
URL: https://jpk.io/dev-tools/atuin-shell-history-review/ — a personal review; opinion only, no primary fact the record needs.
URL: https://clis.dev/cli/atuin — auto-generated CLI reference mirror; the project's own docs.atuin.sh reference is the authoritative source and was used instead.
URL: https://api.github.com/repos/atuinsh/atuin and /releases — GitHub REST API returned 403 through the fetch proxy (rate limit). Data obtained instead from the cloned repository and the human-facing https://github.com/atuinsh/atuin/releases page, which resolve for the reader.
```

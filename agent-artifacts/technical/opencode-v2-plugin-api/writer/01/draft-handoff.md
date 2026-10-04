# Draft handoff: technical/opencode-v2-plugin-api (writer 01)

Original work: the article reads the loader source (external.ts, promise.ts), the 2.0.22 type declarations and eight dated migration reports against each other to show which default exports pass the loader's check, what happens to those that fail, and the smallest diff that carries a v1 plugin across, which no single source (docs, migration guide, issue) states in one place.

Proof: `nb check ... --series technical --repo /home/user/the-nightly-build` (links included) returns BLOCK: 0, WARN: 0, PUBLISHABLE. 2787 words, 20 sources, 12 min read. No warning left on purpose.

Notes for the editor:
- The load-path figure is a PNG (`opencode-v2-plugin-api/load-path.png`) drawn with ImageMagick because the proof rejects data: URIs. It is labeled conceptual and cites the loader source.
- Marked documented or reported, not verified, in the text: hook names prompt/context/compaction/generate/title/retry and permission evaluate (table rows say "Documented only"); subdirectory autoload; the load-error string; the host warning on a skip; transform reload(). "v1 plugin is skipped" is stated as following from the loader schema plus three user reports, and the text says the binary was not run.
- Corrected the commission: the eight issues/PRs are in six repositories, not eight. The text says "eight dated issues and pull requests in six third-party repositories".
- Import path used is @opencode/plugin (+ /effect), never the repo's @opencode-ai/plugin/v2/*. No vendor "GA" claim. v1 vs v2 downloads stated as about 147 to 1.
- The dek says "OpenCode 2's loader" because the loader source was read at commit 907b3bc (2026-10-02), not extracted from the 2.0.22 binary.

Open question: none.

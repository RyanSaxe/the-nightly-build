# writer brief: daily-brief/2026-10-31 (01)

Inputs:
- `../../editorial-direction.md`
- `../../commission.md`
- `../../writing-coach/01/voice-guide.md`
- `../../researcher/01/evidence.md` (the verified candidates, with locators and caveats)
Output: `/home/user/the-nightly-build/.nb-work/daily-brief/2026-10-31/library/daily-brief/2026-10-31.html`
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-10-31/library/daily-brief/2026-10-31.html --series daily-brief --repo /home/user/the-nightly-build`

Work from these inputs. Do not tour the repository or the archive. The markup
contract is under `.nb-work/daily-brief/2026-10-31/.nb-context/`. Where something
is missing, ask me (the orchestrator).

I have selected the six items (template order). Write each from the evidence
record; do not substitute items. The caveats below are decided and binding.

1. **Word of the Day: eggcorn** (noun). Give part of speech, a pronunciation, a
   one-sentence definition (Merriam-Webster owns it), then the documented story
   in three or four sentences: Geoffrey K. Pullum coined it in late September 2003
   on Language Log, in a thread Mark Liberman started, and the word is itself an
   eggcorn for "acorn". Cite M-W for the definition and the OED (Liberman's 30 Sep
   2003 citation) for the story. Base the story only on what the record pins; the
   original 2003 post was not opened.
2. **News — California:** a federal judge's order (Trina Thompson) bars DOJ and
   DHS from threatening California election officials, the Ninth Circuit ruled
   2-1 against DOJ's bid to set aside about 20,000 ballots, and DOJ sent
   grand-jury subpoenas to Los Angeles County officials (29-30 Oct). Do NOT state
   the restraining order's geographic scope (reports disagree). One source: the
   NBC report that covers both the order and the Ninth Circuit ruling.
3. **News — economy:** BEA put third-quarter GDP growth at 3.4% annualized and
   September PCE prices up 3.6% from a year earlier, reported 29 Oct, five days
   before the midterms. Cite BEA's own release. Do NOT place the 2.1%
   annualized-quarterly Q3 PCE figure beside the 3.6% twelve-month figure; they
   measure different things. Use one.
4. **News — veterans:** NPR's new analysis of VA data finds more than 15,000
   veterans now pay at least $150 more a month after the VA ended its VASP
   loan-modification program (30 Oct). This is analysis of existing data, not a
   new policy. Use NPR's framing; do not write that veterans were "steered". Cite
   NPR.
5. **Technology — robots.txt opt-out:** an IETF Internet-Draft submitted by Kevin
   Kelley of Anthropic proposes a shared token websites can put in robots.txt to
   opt out of AI training (30 Oct); Google says it plans to support such a signal
   (targeted 2027). Attribute it as an individual draft with no IETF standing, and
   note a wildcard rule does not count as an opt-out. Cite the IETF draft (and
   Google's post if a second is useful, but one strong source suffices). Report it
   neutrally as a proposal, not an adopted standard.
6. **Technology — Mistral Large 4:** Mistral released Large 4 as open weights on
   29 Oct, about 1 trillion parameters, with hosted-service use needing a separate
   licence. Cite Mistral's page or the Hugging Face model card. Any benchmark
   figures are Mistral's own; attribute them as such or omit them.

Form and geometry:
- Exactly six items in this order; one strong source per item (the word item may
  use two). min_sources 6. Number sources in first-citation order and carry each
  source's kind into `data-nb-kind` per the record.
- STRICT word band 300-700 counting everything but the Sources list. Each news
  and tech item is two or three sentences: what happened, who did it or claims it,
  what follows. Keep it tight; this is the three-minute read.
- Title and dek (spec/headlines.md): title the brief with the single strongest
  item's real headline (subject, verb, surprise first) rather than a bare-date
  roundup line or a reflexive court lead; the California order days before the
  election is a strong lead candidate, but choose by what the day's strongest
  item is. The dek names the one or two items that make this brief unmistakable,
  and is not a comma-triad or a semicolon reversal. Build the six item headlines
  differently from one another.
- Banned terms (merged, STRICT — these BLOCK): em-dash max 4, "leverage" max 1,
  "load-bearing" 0, "mechanism"/"mechanisms" max 1.
- nb-meta: date `2026-10-31` (must equal slug); keep mode `rolling`; `order`
  stays `null`; set `tags` to a short topical set spanning the items (for example
  `["elections","economy","veterans-affairs","ai-policy","open-weights"]`);
  `harness` `claude-code-routine`; `model` the model you ran as. Make the nb-meta
  dek and the rendered dekline identical. `nb stamp` writes the counts.

Iterate the proof with `--no-check-links`, then `nb stamp` and the exact proof
command above with links until `BLOCK: 0`. Write `draft-handoff.md` in
`writer/01/` with the proof result, any warning left on purpose, and any open
question. Report the handoff path and the final word count (it must be within
300-700).

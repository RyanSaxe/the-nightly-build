# Evidence record — tech-news/2026-07-30 (invocation 01)

The evidence supports a five-item brief of developments dated 2026-07-27 to
2026-07-30, each with one primary and one independent secondary that resolves.
The strongest, best-sourced item is Anthropic's Claude Mythos cryptanalysis
(primary announcement plus independent US security reporting that adds an
outside expert and an extra caveat). The two physics/chemistry items rest on
institutional or journal primaries that return HTTP 403 to automated fetchers
(gated, not dead): their domains resolve and their claims were read through
independent secondaries and search retrieval. Evidence is thin on the exact
semiconductor material in the "electron lighthouse" device (secondaries do not
name it), so the article should not name a material. Two candidates were
rejected for staleness (Rice lanthanide-oxygen chemistry, primary dated April 9;
SNU programmable slow-light photonic chip, primary dated June 28) and several
for being current-events/economic (the "Pacing the Frontier" employee letter,
GlobalFoundries award, Chinese-robot import restrictions, funding rounds) or
Nvidia-adjacent.

## Sources

### s1 — Anthropic, "Discovering cryptographic weaknesses with Claude" (PRIMARY)
URL: https://www.anthropic.com/research/discovering-cryptographic-weaknesses
Classification: PRIMARY — the authoring party's own account of its own research.
HTTP 200.
Establishes firsthand:
- Claude Mythos found a nontrivial automorphism (a hidden lattice symmetry) in
  the HAWK post-quantum signature scheme that prior work predicted might exist
  but had not confirmed for this scheme.
- The attack "reduces the 'effective keysize' by a factor of two." For HAWK-256
  the expected attack cost drops from 2^64 to 2^38. It is "a faster exponential
  time attack against HAWK than previously known, and does not run in polynomial
  time." (~60 hours of work; roughly $100,000 in API costs.)
- Separately, Claude developed a fingerprinting algorithm it named the "Möbius
  Bridge" for meet-in-the-middle attacks on 7-round AES (out of the full 10
  rounds), "between 200 and 800 times faster" than the previous best, by
  eliminating one enumeration guess of 2^56 work. "This attack does not break the
  full cipher."
- Verbatim caveat: "Neither of these results has a practical impact on today's
  computer systems; no production software will have to change as a result."
Locator: sections "HAWK," "AES," and the closing impact statement.
Publication date on page: 2026-07-28.

### s2 — CyberScoop, "Anthropic's Claude Mythos finds weaknesses in encryption algorithms" (SECONDARY)
URL: https://cyberscoop.com/anthropic-claude-mythos-encryption-flaws-hawk-aes-pqc/
Classification: SECONDARY — independent US security newsroom (author Greg Otto,
2026-07-28), outside Anthropic. HTTP 200.
Adds firsthand reporting: outside expert Ellen Boehm (Keyfactor) says the work
"proves that the NIST PQC evaluation process is working"; extra caveat that the
7-round AES attack "requires an impossible amount of target data — over 400
octillion messages — and cannot touch the full 10-round encryption protecting
everyday software"; flags the unresolved policy question Anthropic itself raised
about what to do if AI finds flaws in deployed cryptosystems.
Corroborating tertiary read (not cited): The Hacker News (HTTP 200), CSO Online,
Decrypt, The Next Web — all consistent on the τ-cocycle/automorphism framing.

### s3 — MIT News, "Making robots faster by helping them think ahead" (PRIMARY)
URL: https://news.mit.edu/2026/making-robots-faster-helping-them-think-ahead-0728
Classification: PRIMARY — the authoring institution's account of its own
research (VLASH). HTTP 200. Date: 2026-07-28.
Establishes firsthand:
- VLASH lets a vision-language-action (VLA) model predict the robot's future
  state and plan the next action chunk while the current one executes, removing
  the lag between chunks. Quote: "we give the robot awareness of its future
  state."
- Doubles robot speed on tasks such as pick-and-place; accelerates reaction
  speeds by more than 30× by removing inter-chunk lag; "does not add any
  computational overhead to the planning process."
- Demonstrated on pick-and-place, cube sorting, stacking, table tennis, and
  Whack-a-Mole; named use cases include search-and-rescue and emergency response.
- Lead author Song Han (MIT EECS), with collaborators at Nvidia, UC Berkeley,
  UC San Diego, Caltech, and Tsinghua; presented at the IEEE/RSJ International
  Conference on Intelligent Robots and Systems (IROS).
Locator: body paragraphs on the method and the results.

### s4 — Interesting Engineering, "MIT's new model cuts reaction delays by 30 times for faster robot movement" (SECONDARY)
URL: https://interestingengineering.com/ai-robotics/mit-tech-robot-move-2x-faster
Classification: SECONDARY — independent technology newsroom. HTTP 200.
Corroborates the 2× speed and 30× reaction-delay figures and the no-overhead
claim from outside MIT.

### s5 — NASA Science, "NASA's Swift Sees 'Wandering' Mega Black Hole Shredding Star" (PRIMARY)
URL: https://science.nasa.gov/missions/swift/nasas-swift-sees-wandering-mega-black-hole-shredding-star/
Classification: PRIMARY — the mission's own announcement of its result. HTTP 200.
Establishes firsthand:
- A tidal disruption event more than 30,000 light-years from its host galaxy's
  center — "the farthest such event ever observed outside a galactic core" for an
  optically discovered TDE.
- Black hole mass ~1 million times the Sun's; host galaxy ~750 million
  light-years away in the constellation Cetus.
- The flare temporarily radiated with the light of ~10 billion Suns and
  outshone its entire host galaxy in ultraviolet for several months; Swift's
  UVOT measured ~30,000 °C (54,000 °F).
- First flagged in November 2025 by the Zwicky Transient Facility (ZTF) at
  Palomar. Robert Stein: "Out of the half million flashes ZTF detects each night,
  our new artificial intelligence algorithm automatically recognized a flare that
  looked a lot like a tidal disruption event, despite its unusual location in the
  outskirts of a galaxy."
- Paper led by Robert Stein, published 2026-07-28 in The Astrophysical Journal
  Letters.
Locator: opening summary, detection paragraph, and quote block.

### s6 — Universe Today, "A Wandering Black Hole Meets a Wandering Star" (SECONDARY)
URL: https://www.universetoday.com/articles/a-wandering-black-hole-meets-a-wandering-star
Classification: SECONDARY — independent astronomy newsroom. HTTP 200.
Corroborates the off-nuclear offset, the ~1M-solar-mass black hole, and the
AI-flagged ZTF detection from outside NASA.

### s7 — University of Michigan News, "'Electron lighthouse' illuminates new physics" (PRIMARY)
URL: https://news.umich.edu/electron-lighthouse-illuminates-new-physics/
Classification: PRIMARY — the authoring institution's account of its own study.
HTTP 403 to automated fetchers (gated, not dead); domain resolves; claims read
via the independent secondary (s8) and search retrieval.
Establishes firsthand (read via s8 and retrieval):
- Two laser pulses of different infrared "colors" meet in a device and launch a
  current of electrons in a controllable direction through a semiconductor, with
  no applied electric field.
- The direction is set by quantum interference between two absorption pathways
  to the same final state (constructive enhances one direction, destructive
  suppresses others), producing a narrow beam steerable by rotating the light's
  polarization / changing the colors.
- Senior author Steven Cundiff (experimental physicist, U-M); first author Yiming
  Gong. Cundiff: "using light, you can actually sort of squirt the electrons in a
  specific direction without applying an electric field." Published in Physical
  Review Letters (2026). Named applications: quantum sensing, imaging,
  telecommunications, quantum computation.
Caveat for the writer: no secondary names the specific semiconductor material —
do not name one.
Locator: press release body; PRL paper is the underlying record.

### s8 — ScienceAlert, "Physicists Created an 'Electron Lighthouse' That Steers Current With Light" (SECONDARY)
URL: https://www.sciencealert.com/physicists-created-an-electron-lighthouse-that-steers-current-with-light
Classification: SECONDARY — independent science newsroom, cites the peer-reviewed
PRL paper and quotes Cundiff; not written by the university. HTTP 200.
Corroborates: two IR-color beams, polarization-set direction, quantum
interference, no electric field, PRL publication.

### s9 — Science Advances, "Twisted topological light illuminates molecular chirality" (PRIMARY)
URL: https://www.science.org/doi/10.1126/sciadv.aec6549
Classification: PRIMARY — the peer-reviewed paper that owns the claim. HTTP 403
(paywall/gated, not dead); DOI resolves; abstract-level claim read via the
independent secondary (s10) and search retrieval.
Establishes firsthand (read via s10 and retrieval):
- Twisted laser light (carrying orbital angular momentum / topological structure)
  interacts differently with left- and right-handed molecules, distinguishing
  enantiomers by the fragments they produce upon interaction.
- Proposes a faster, simpler, more sensitive route to enantiomer discrimination
  for chemistry and pharmaceuticals.
- Authors from the Tata Institute of Fundamental Research, IIT Bombay, and IIT
  Hyderabad. DOI 10.1126/sciadv.aec6549. Reported publicly 2026-07-27.
Locator: abstract and significance statement.

### s10 — Phys.org, "Twisted laser light distinguishes mirror-image molecules by their fragment counts" (SECONDARY)
URL: https://phys.org/news/2026-07-laser-distinguishes-mirror-image-molecules.html
Classification: SECONDARY — independent science newsroom. HTTP 403 to automated
fetchers (gated, not dead); domain resolves; content read via search retrieval.
Corroborates the fragment-based enantiomer discrimination and the pharma/chemistry
significance from outside the authoring team.

## Contradictions
- No primary/secondary numerical conflict inside any item. Secondaries agree with
  their primaries on every figure used.
- Anthropic vs. its independent secondary: no conflict, but CyberScoop sharpens
  the AES scope (the 7-round result needs >400 octillion messages and cannot
  touch full 10-round AES). The article must carry this limit so the "faster
  attack" claim is not overread.
- Framing risk, not contradiction: coverage sometimes calls the AES result a
  "crack" of AES; the primary is explicit it does not break the full cipher.
  Governs: the primary. Use "reduced-round" language.
- The MIT item lists Nvidia among many academic collaborators; this is a
  multi-institution robotics result, not an Nvidia story, and must not be framed
  as one.

## Numbers
- HAWK: effective key strength halved; HAWK-256 attack cost 2^64 → 2^38; ~60
  hours; ~$100,000 API cost. (s1)
- AES: 7 of 10 rounds; 200–800× faster than previous best; eliminates a 2^56
  enumeration guess; needs >400 octillion messages (s2); does not break full
  cipher. (s1, s2)
- VLASH: ~2× task speed (pick-and-place); >30× faster reaction between action
  chunks; no added planning compute. (s3, s4)
- TDE: >30,000 light-years offset (record for an optical TDE); black hole ~1×10^6
  solar masses; host ~750 million light-years (Cetus); peak ~10 billion Suns; UVOT
  ~30,000 °C; ZTF flagged Nov 2025. (s5, s6)
- Electron lighthouse: two IR laser colors; zero applied electric field; PRL 2026.
  (s7, s8)
- Chirality: enantiomer discrimination by fragment counts under twisted light;
  Science Advances, DOI 10.1126/sciadv.aec6549. (s9, s10)

## Source assets
None used. The Anthropic and NASA pages carry figures, but none is load-bearing
for a wire brief where the numbers in prose carry the argument; adding an image
would be decoration. `None found` that the argument must spend.

## Discarded
- Rice University lanthanide-dioxygen chemistry (JACS 10.1021/jacs.5c22234):
  strong result, but the paper is dated 2026-04-09; the 07-29 coverage is a
  re-feature, not a new development. Stale for a "what moved" brief.
- SNU/University of Seoul programmable slow-light photonic chip (Advanced Science
  10.1002/advs.76378): primary dated ~06-28; stale.
- "Pacing the Frontier" letter (1,100+ AI-lab employees, 07-28): major, but a
  petition to the US government — public-consequence political, owned tonight by
  current-events. Excluded to avoid a double-run.
- GlobalFoundries $300M chip-interconnect award; US restrictions on Chinese
  humanoid robots; Antares $470M Series C; ChipAgents $60M (Nvidia-backed):
  economic/political or Nvidia-adjacent → not this brief.
- OpenAI GPT-5.6 Sol ARC-AGI-3 benchmark counter-claim; Moonshot MoonEP library;
  Thinking Machines "Inkling" (07-15): incremental, adjacent to already-covered
  stories, or stale.
- NASA Psyche Mars flyby (07-28): a milestone in operations, not a result that
  changes technical practice.

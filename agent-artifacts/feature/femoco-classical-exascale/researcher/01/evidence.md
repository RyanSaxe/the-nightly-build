# Evidence record: FeMoco, classical exascale, quantum projections (researcher 01)

The evidence supports a narrower story than the commission's angle. The SC26 abstract does state 105 minutes on 1,280 LineShine nodes against "the best published 8.6-hour single-run projection", and it does say the active space is CAS(113e, 76o). But the full paper could not be opened, so what "ground-state consensus" means, what accuracy it reaches and what the 105 minutes contains are unknown. The 8.6 hours (Low et al., Google Quantum AI, 2025) is a projection for hardware that does not exist, assumes a perfect starting state and excludes the cost of preparing it. The same group's May 2026 preprint gives about 2.5 hours for the same 76-orbital Hamiltonian, so the five-fold gap in the abstract rests on a superseded number. The classical chemical-accuracy estimate for this Hamiltonian was published in January 2026 by Zhai, Chan et al., on ordinary CPU nodes, with an uncertainty of 0.31 to 1.25 kcal/mol that comes from extrapolation and not from a bound. The evidence is thin on the paper's own method, on any quantum-side reaction to the prize result (none found), and on ACM's own release (blocked).

## Sources

URL:         https://sc26.supercomputing.org/proceedings/papers/paper_pages/gb103.html
Kind:        primary. The SC26 proceedings page carries the authors' abstract for the prize paper. Fetched directly and read verbatim.
Establishes: Title, authors, affiliations and the abstract's claims: first exascale classical solution of CAS(113e, 76o); 1.456 EFLOP/s double precision on 20,480 LineShine nodes; 5.626 EFLOP/s mixed precision; "ground-state consensus" on 1,280 nodes in 105 minutes; "approximately one-fifth of the best published 8.6-hour single-run projection". It establishes only what the authors say. The page has no PDF, DOI or accuracy figure.
Paraphrase:  The authors say the FeMoco active space is beyond exact diagonalization and hard for every polynomial-scaling classical method. They tuned one code for LineShine and for China's New-generation Intelligent Supercomputer (CNIS). Peak sustained rate was measured on the 20,480-node run. The ground-state consensus was reached on a smaller run, 1,280 nodes, taking 105 minutes end to end.
Locators:    Abstract, whole page (one paragraph).
Quote:       "reaching sustained performance on 20,480 LineShine nodes of 1.456 EFLOP/s in double precision (58.9% of the machine peak) and 5.626 EFLOP/s in mixed precision. These computational achievements enable the FeMoco ground-state consensus to be reached on 1,280 LineShine nodes within a measured end-to-end wall time of 105 minutes (1.75 h), approximately one-fifth of the best published 8.6-hour single-run projection for fault-tolerant quantum computing on the same active space."
Authors as printed: Honghui Shang (State Key Laboratory of Precision and Intelligent Chemistry, Hefei National Laboratory, University of Science and Technology of China); Zhiyu Xiao (Institute of Physics, Chinese Academy of Sciences); Zhuozhao Xia, Hao Wu, Huan Ma (same USTC laboratory); Yongqing Chen, Bin Li (National High Performance Computer Engineering Technology Research Center); Zhenyu Li (same USTC laboratory); Yutong Lu (Sun Yat-sen University); Jinlong Yang (same USTC laboratory). The commission's "SYSU" is Sun Yat-sen University. The Quantum Insider repost puts Zhenyu Li at Sun Yat-Sen University, which the proceedings page does not.

URL:         https://thequantuminsider.com/2026/11/20/10-member-team-drawn-from-chinese-institutions-wins-2026-gordon-bell-prize/
Kind:        secondary. A republication of ACM's press release with a short "Insider Brief" by Matt Swayne (20 Nov 2026). Read through a summarizing fetch, not verbatim.
Establishes: That ACM named a ten-member team from Chinese institutions the 2026 Gordon Bell Prize winner, presented at SC26 in Chicago, for the first "exascale" classical solution to the FeMoco CAS problem. Repeats the 20,480-node, 1.456 and 5.626 EFLOP/s figures from the abstract.
Paraphrase:  The release says nothing about accuracy, time to solution or a quantum comparison. The 105 minutes and 8.6 hours appear only in the paper abstract.
Locators:    Whole article.
Quote:       None needed.

URL:         https://www.hpcwire.com/off-the-wire/chinese-team-wins-2026-acm-gordon-bell-prize-for-exascale-quantum-chemistry/
Kind:        secondary. HPCwire repost of ACM's release, dated 19 Nov 2026. Direct fetch returned 403 (Cloudflare); content reached through a summarizing fetch only.
Establishes: Same as the Quantum Insider entry. The page names ACM as the origin but does not link ACM's own page.
Paraphrase:  The prize was presented at SC26 in Chicago on 19 November. The release names the paper's ten authors and gives the machine figures.
Locators:    Whole article.
Quote:       None needed.

URL:         https://arxiv.org/abs/2601.04621 (PDF https://arxiv.org/pdf/2601.04621, v2 dated 22 June 2026)
Kind:        primary. Zhai, Li, Zhang, Li, Lee and Chan own the classical calculation, the cost figures and the comparison to 8.6 hours. Preprint, 93 pages, no journal reference listed. Read the PDF text and rendered Fig. 4.
Establishes: A classical estimate of the ground-state energy of the CAS(113e, 76o) model to an uncertainty of about chemical accuracy, by DMRG and coupled cluster with extrapolation. Its own hypothetical cost on Frontier and its own comparison to the 8.6-hour quantum figure.
Paraphrase:  The model is the Li, Li, Dattani, Umrigar, Chan (LLDUC) 113-electron, 76-orbital active space of the resting state (E0), cluster charge -1, S = 3/2. The method runs many broken-symmetry spin starting points through unrestricted-orbital DMRG (UDMRG) and unrestricted coupled cluster (UCC, up to quadruples, UCCSDTQ), then extrapolates. The only strict variational bound is the D = 18,000 UDMRG energy, 8.76 kcal/mol above their estimated ground state. They report two ways to state the answer. The "consensus" is the average of the UCC and UDMRG predicted exact energies: E0 = -22140.4106 ± 0.0005 Hartree (±0.31 kcal/mol). The conservative range is E0 = -22140.4091 ± 0.0020 Hartree (±1.25 kcal/mol). They say there is "no formal theory of these extrapolations". Three spin isomers (BS7-235, BS8-237, possibly BS8-236) are degenerate within this accuracy. The model is "not a quantitative model of FeMo-co electronic structure", since it omits correlation outside 76 orbitals and protein and geometry fluctuations. Prior DMRG on this model "fell far short" of 1 kcal/mol, with a residual error of about 100 mHartree (63 kcal/mol) in the cited earlier work.
Locators:    Abstract and Intro p.1-2; "FeMo-co models" p.2-4; "Classical electronic structure methods" p.5; ground-state estimate p.9-11 (Fig. 3); "Cost of classical methods and quantum advantage" p.11-12 (Fig. 4); Supplementary Sec. 3.1.7 and Tables 17-18 for CPU hours; Sec. 3.1.6 for overlap.
Quote:       "Consensus of estimates from the two methods is thus a stringent consistency test." And: "While we have not run our calculations using a large supercomputer, we follow the analogous procedure to contextualize our costs." The word "consensus" is the same word Shang et al. use. That the Shang paper uses the Zhai protocol is an inference from the shared word and the shared active space. The abstract does not cite Zhai and the full paper was not read.
Affiliations as printed: Garnet Kin-Lic Chan, Division of Chemistry and Chemical Engineering and Marcus Center for Theoretical Chemistry, California Institute of Technology (corresponding author). Huanchen Zhai, Caltech and Flatiron Institute (Initiative for Computational Catalysis). No academic title is printed.

URL:         https://quantumfrontiers.com/2026/03/12/the-femo-cofactor-and-classical-and-quantum-computing/
Kind:        primary for Chan's position. A blog post by Garnet Chan (12 Mar 2026) on the blog of the Institute for Quantum Information and Matter at Caltech, commenting on his own group's preprint. Read raw.
Establishes: Chan's argument, in his own words, and his account of the 54-orbital (RWST) versus 76-orbital (LLDUC) models.
Paraphrase:  The 2017 Reiher et al. model (RWST, 54 orbitals, 108 qubits) was "very easy classically": per Li et al. 2019, a few hours on a laptop, because its ground state had no unpaired electrons. His group built the 76-orbital LLDUC model to keep the open-shell character; it is "still a significant truncation" of the real cofactor and became the common benchmark for quantum resource estimates. On exponential speedup he writes that convincing evidence for the needed conditions "has not yet been found" (citing Lee et al. 2023 and Chan 2024). On the societal-impact claim he says the claim that nitrogenase uses much less energy than Haber-Bosch "is simply false". He calls FeMoco "overrepresented" in quantum chemistry literature because it was an early advantage case, says the resource-estimation work still applies elsewhere, and says he is "excited to see quantum computers applied to this problem", only "not waiting for them to be built first". He grants quantum algorithms "come with theoretical guarantees" that extrapolated classical error estimates lack.
Locators:    Sections "Exponential speedup and societal impact", "Which FeMo-cofactor model?", "Heuristics in the classical solution", "How should one think about past work on quantum algorithms...", "What are some lessons".
Quote:       "there is nothing especially mysterious about FeMo-co's electronic structure". "the choice of computational algorithm and hardware to solve the problem is irrelevant."

URL:         https://arxiv.org/abs/2502.15882 (PDF https://arxiv.org/pdf/2502.15882, v1, 21 Feb 2025)
Kind:        primary. Low et al. (Google Quantum AI and collaborators) own the 8.6-hour figure. Published as Phys. Rev. X 15, 041016 (2025), per the reference line in arXiv:2605.30455. The PRX page returned 403, so this record uses arXiv v1.
Establishes: The assumptions and scope of the 8.6 hours.
Paraphrase:  For the 76-orbital Li et al. Hamiltonian, the phase estimation (PEA) block costs 9.99 x 10^8 Toffoli gates and 1,459 logical qubits (Table I). The target is a phase-estimation standard deviation of 1 mHa within a chemical-accuracy budget of 1.6 mHa. Assuming four CCZ factories, a physical error rate of 0.001, a 1 microsecond surface-code cycle and a 10 microsecond reaction time, they estimate 4.5 million physical qubits running 8.6 hours at code distance 27. The 54-orbital model: 3.2 million qubits, 2.7 hours. The 8.6 hours covers phase estimation only. The authors separately cite state preparation at 7.6 x 10^8 to 1.3 x 10^9 Toffolis for matrix-product-state (MPS) trial states with overlaps of 0.95 to 0.99, and write that the predicted "8 hours of runtime is a substantial overestimate" because magic state cultivation postdates their cost model.
Locators:    Table I (p.3); "physical resources" paragraph near the end of Sec. V (the 8.6 and 2.7 hour statements); Discussion paragraph on state-preparation cost and cultivation. Table II lists a DMRG M = 6000 variational energy for CAS(113e, 76o).
Quote:       "we estimate that the FeMoco76 example will require 4.5 million physical qubits running for 8.6 hours on a set of d = 27 surface code patches."

URL:         https://arxiv.org/abs/2605.30455 (PDF https://arxiv.org/pdf/2605.30455, v1, 28 May 2026)
Kind:        primary. Low, Huggins, Berry, Khattar, White, Rubin and Babbush (Google Quantum AI; Berry at Macquarie University) own the newer estimates. Preprint. Read the text, Fig. 1 and Table XXVII (p.101).
Establishes: A faster published run-time projection for the same FeMoco-76 Hamiltonian, and the same group's statement about classical heuristics.
Paraphrase:  Table XXVII (FeMoco-76o113e) lists a Pareto frontier. Examples (1-shot runtime, qubits): 2,692 thousand qubits, 2.50 hours (2.36 expected); 1,170 thousand qubits, 5.26 hours (minimum volume, 6.16 million qubit-hours); 444 thousand qubits, 23.9 hours; 166.9 thousand qubits, 716 hours (the "within a month" point, "167k" in the text). Same hardware model as before (10^-3 error, 1 microsecond cycle, 10 microsecond reaction time). They write that the 2025 PRX estimates were "previous state-of-the-art minimum-Toffoli resource estimates". They also say they "assume perfect ground state overlap and ignore the cost of preparing a good trial state". For FeMoco-54 the table gives 48 minutes on 2.0 million qubits (Fig. 1 inset).
Locators:    Fig. 1 and inset table p.2; Sec. I paragraph on "chemically accurate ground state phase estimation"; Sec. VI intro (the perfect-overlap statement, near eq. 6.1); Table XXVII p.101. The reading of columns (Volume = qubits x hours) is mine and checks: 2,692k x 2.50 h = 6.73 million qubit-hours, as printed.
Quote:       "quantum methods can provide accuracy guarantees that are missing when comparing heuristic classical methods and extrapolating."

URL:         https://arxiv.org/abs/1605.03590
Kind:        primary. Reiher, Wiebe, Svore, Wecker and Troyer own the original FeMoco quantum resource estimate. This record reads arXiv v2 (25 May 2016). The PNAS version is Proc. Natl. Acad. Sci. 114, 7555 (2017), as cited in arXiv:2601.04621; the PNAS text was not opened.
Establishes: The origin of the benchmark and its first run-time figures.
Paraphrase:  Table I: for structure 1 (spin 0, charge +3, 54 electrons in 54 orbitals) at 0.1 mHa, Trotter-based runtimes of 130 days (serial, 1.1 x 10^15 T gates, 111 logical qubits), 15 days (nesting, 135 logical qubits) and 110 hours (programmable ancilla rotations, 1,982 logical qubits). At 1 mHa, 12 days, 1.4 days and 11 hours. These assume one logical T gate per 10 ns and "that a good trial state for the ground state is available". The paper states that quantitative understanding of such species "remains beyond the capability of classical-computer simulations".
Locators:    Table I (p.5); "Resource requirements" text on p.5-6; Discussion p.6.
Quote:       None needed.

URL:         https://arxiv.org/abs/1809.10307
Kind:        primary. Li, Li, Dattani, Umrigar and Chan (J. Chem. Phys. 150, 024302, 2019). Read the full 3-page arXiv text.
Establishes: That the 54-orbital model of Reiher et al. was classically easy, and the definition of the 113-electron, 76-orbital model.
Paraphrase:  For the 54e/54o model, coupled cluster, DMRG and semistochastic heatbath CI gave accurate S = 0 energies; the lowest DMRG variational and extrapolated SHCI energies agree within 5 mEh, "only modest resources were required". The new CAS(113e, 76o) active space comes from Fe 3d, S 3p, Mo 4d and C 2s2p orbitals plus some ligand orbitals. The paper does not itself say "laptop". That wording is Chan's, in the 2026 blog.
Locators:    Fig. 1 and the paragraph below it (p.1-2); Table I; last paragraphs.
Quote:       None needed.

URL:         https://arxiv.org/abs/2011.03494
Kind:        primary (abstract only read). Lee, Berry, Gidney, Huggins, McClean, Wiebe, Babbush: tensor hypercontraction (THC) resource estimate, Nature Communications 2021 per the arXiv record.
Establishes: A run-time step between Reiher and Low.
Paraphrase:  "FeMoCo can be simulated using about four million physical qubits and under four days of runtime, assuming 1 microsecond cycle times and physical gate error rates no worse than 0.1%." The abstract does not name the active space. Low et al. 2025 cite the same work for 12 days (FeMoco-76) and 2 days (FeMoco-54) "not considering the additional space-time tradeoffs".
Locators:    Abstract; Low et al. 2025 paragraph after the 8.6-hour statement.
Quote:       None needed.

URL:         https://arxiv.org/abs/2409.11748
Kind:        primary (abstract only read). Berry et al. (Google Quantum AI with Chan, Lee and others), trial-state preparation.
Establishes: That preparing the starting state is a counted cost.
Paraphrase:  An MPS of bond dimension 4,000 gives an estimated overlap squared of about 0.9 with a candidate FeMoco ground state, for a total of 7.3 x 10^10 Toffoli gates in their accounting, "neglecting the search over candidates and assuming the accuracy of the extrapolation".
Locators:    Abstract.
Quote:       None needed.

URL:         https://arxiv.org/abs/2511.09124 (HTML v2, 13 Nov 2025)
Kind:        primary for a quantum-side position. Babbush, King, Boixo and others, Google Quantum AI, "The Grand Challenge of Quantum Applications". Predates the Zhai preprint. Read the HTML text.
Establishes: How the quantum-side authors framed FeMoco before the classical results.
Paraphrase:  They write that for systems like FeMoco "no classical method has solved its electronic structure to the accuracy needed for definitive chemical insight" and that "we can efficiently prepare quantum states with a very high overlap on its true ground state", while saying the "theoretical debate over exponential quantum speedup remains unresolved". They treat FeMoco as a problem with "effectively a finite number of distinct calculations", where a classical model might later learn the patterns. Table 4 lists FeMoco (76 orbitals) at 1,500 logical qubits, 10^9 Toffolis, 5 x 10^6 physical qubits, 9 hours.
Locators:    Section on the pragmatic perspective, after the P/Poly discussion (search "no classical method has solved"); Table 4.
Quote:       "no classical method has solved its electronic structure to the accuracy needed for definitive chemical insight"

URL:         https://arxiv.org/abs/2208.02199 and https://arxiv.org/abs/2407.11235
Kind:        primary (abstracts only). Lee et al. (18 authors including Babbush, Preskill and Chan; Nat. Commun. 2023 per Chan's blog) and Chan's 2024 essay.
Establishes: The claim Chan's blog cites on exponential advantage.
Paraphrase:  Lee et al.: "evidence for such an exponential advantage across chemical space has yet to be found" while "quantum computers may still prove useful".
Locators:    Abstracts.
Quote:       None needed.

URL:         https://arxiv.org/abs/2510.04795
Kind:        primary (abstract and results paragraph read). Brower et al., NVIDIA, Legeza and others, mixed-precision DMRG.
Establishes: A source of "chemical accuracy" wording that does not mean accuracy against the true ground state.
Paraphrase:  For CAS(113, 76) they report error profiles with 4 or 6 emulated-FP64 "slices" similar to native FP64 DMRG and conclude this "is adequate to reach chemical accuracy". The comparison is between arithmetic modes of the same DMRG calculation, not against the exact energy.
Locators:    Abstract; the "FeMoco on CAS(54,54) and CAS(113,76)" paragraph (p.4).
Quote:       None needed.

URL:         https://arxiv.org/abs/2407.07411 and https://arxiv.org/abs/2604.06841
Kind:        primary (abstracts only). Menczer et al. (July 2024): DMRG performance on DGX-H100, CAS(113, 76) among benchmarks, 246 teraFLOP/s sustained. Li, Wu, Zhang, Fang, Li (8 Apr 2026): spin-adapted neural-network backflow for CAS(113e, 76o), "competitive with recent spin-adapted DMRG calculations at bond dimension D=10000".
Establishes: Other classical work on this Hamiltonian between Li et al. 2019 and the prize. Neither claims a chemical-accuracy solution in its abstract.
Paraphrase:  As above.
Locators:    Abstracts.
Quote:       None needed.

URL:         https://arxiv.org/abs/2609.27482
Kind:        primary for the machine description (authors include Yutong Lu, who is also a prize-paper author). CerebroSim paper, 23 Sep 2026.
Establishes: LineShine's node architecture, to identify the machine.
Paraphrase:  LineShine, at the National Supercomputing Center in Shenzhen, has 22,680 compute nodes and more than 13 million processor cores. Each node has two chiplet-based LX2 Arm processors, 608 cores and about 120.6 teraFLOP/s peak FP64. No GPUs. A separate arXiv abstract (2610.09766) calls LineShine "currently ranked first on the TOP500 list". The brief says not to revisit rankings, so the record keeps only the identification.
Locators:    Sec. III, "LineShine Supercomputer", and Fig. 2.
Quote:       None needed.

URL:         https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/
Kind:        secondary. Kevin Hartnett, Quanta Magazine, 29 May 2026, on Zhai et al. Read through a summarizing fetch, not verbatim. It does not mention Shang or exascale computing.
Establishes: Named reactions to the Zhai result from outside Chan's group, as reported.
Paraphrase:  Daniel Suess (chemist at MIT who studies nitrogenase) says the work "described the resting state" only. James Whitfield (quantum computing theorist at Dartmouth College) argues solving one instance does not show a method transfers, and that ground-state energy was never where quantum computers were expected to win; he sees their advantage in dynamics. Chan is quoted as saying he doesn't "see why we should wait for a fault-tolerant quantum computer to be built." Exact wording of the Suess and Whitfield quotes should be checked against the page before quotation.
Locators:    Whole article.
Quote:       None recorded verbatim.

## Contradictions

1. The abstract's "best published 8.6-hour single-run projection" against a faster projection for the same Hamiltonian. Low et al. 2025 (PRX 15, 041016) gives 8.6 hours on 4.5 million physical qubits. Low et al., arXiv:2605.30455 (28 May 2026), gives 2.50 hours (2.36 expected) on 2.69 million qubits, and 5.26 hours on 1.17 million, for CAS(113e, 76o) under the same error rate, cycle time and reaction time. So by late May 2026 the best published projection for this active space was about 2.5 hours, not 8.6. Whether the prize paper was finalized before 28 May 2026 is unknown. Against 2.5 hours, 105 minutes is a ratio of about 1.4, not 4.9.
2. Which node count goes with the 105 minutes. The abstract says the ground-state consensus came on 1,280 nodes in 105 minutes and the EFLOP/s figures were measured on 20,480 nodes. Several secondary outlets give only 20,480 nodes. One search-result summary placed the 105 minutes on 1,280 nodes, consistent with the abstract.
3. What "chemical accuracy" claims cover. Zhai et al.: an extrapolated estimate with ±0.31 to ±1.25 kcal/mol and a strict upper bound 8.76 kcal/mol above it. Brower et al.: agreement between arithmetic modes. Low et al.: a phase-estimation standard deviation of 1 mHa given a perfect trial state. These are three different claims. The prize abstract states no accuracy figure.
4. Chan's position against the commission's wording. The commission says Chan argued the advantage case "was overstated". Chan's own words are narrower: no convincing evidence yet for exponential speedup on chemically relevant problems; FeMoco "overrepresented" in the literature; quantum algorithms still carry guarantees and could give polynomial or constant-factor speedups. He says he is excited to see quantum computers applied.
5. Quantum-side wording against Chan's. Babbush et al. (Nov 2025) say no classical method had solved FeMoco's electronic structure to the accuracy needed for definitive chemical insight. Zhai et al. (Jan 2026) claim a solution to about chemical accuracy for the 76-orbital model while saying the model is not a quantitative model of the real cofactor. The two statements can both hold, since "definitive chemical insight" may refer to the real cofactor and not to the model, but the sources do not say so.
6. Whitfield (via Quanta) says ground-state energy was never where quantum advantage was expected. Babbush et al. list FeMoco ground-state estimation as a Stage II quantum-advantage target. Whitfield's words were read through a summary only.
7. The 2017 entry in Low et al.'s Table I (5.0 x 10^13 Toffolis, 111 qubits) is not the number printed in Reiher's Table I (1.0 x 10^14 T gates for 1 mHa serial; 1.1 x 10^15 for 0.1 mHa). The conversion Low et al. used is not stated.
8. The commission calls the prize "an exascale classical computation of the FeMoco active space... solved end to end". ACM's text says "first 'exascale' classical solution". It is not the first classical estimate: Zhai et al. posted theirs on 8 January 2026 and ran it on CPU nodes at the Flatiron Institute.

## Numbers

Figure: 105 minutes (1.75 h), measured end-to-end wall time, ground-state consensus
Owner:  SC26 paper abstract (Shang et al.)
Scope:  CAS(113e, 76o); 1,280 LineShine nodes; what the end-to-end time includes is unknown (integrals, number of spin isomers, I/O)

Figure: 1.456 EFLOP/s sustained double precision (58.9% of peak); 5.626 EFLOP/s mixed precision
Owner:  SC26 paper abstract
Scope:  20,480 LineShine nodes; a different run from the 105-minute one

Figure: Implied peak for 20,480 nodes = 1.456 / 0.589 = 2.47 EFLOP/s. Per node 120.6 TFLOP/s FP64 (CerebroSim paper). 20,480 x 120.6 = 2.470 EFLOP/s, which agrees.
Owner:  Arithmetic from the two primaries
Scope:  Peak FP64, all-CPU nodes

Figure: Derived, not in any paper: 1,280 nodes x 120.6 TFLOP/s = 154 PFLOP/s peak. Over 6,300 s that is at most 9.7 x 10^20 floating-point operations, or 5.7 x 10^20 at the same 58.9% of peak. This assumes the 1,280-node run sustained the 20,480-node efficiency, which the abstract does not say.
Owner:  Arithmetic by the researcher
Scope:  For scale against Zhai's operation counts below. Treat as an upper bound only.

Figure: Zhai et al., classical cost as measured: 2,768,994 CPU core-hours for UDMRG (two sweeps at D = 18,000 plus 12 extrapolation points at D = 5,000 to 16,000; one D = 18,000 sweep took 317,440 core-hours); about 40,000 core-hours for the largest UCCSDTQ calculation (about 400 core-hours per iteration, 100 iterations)
Owner:  arXiv:2601.04621, p.11 and Supplementary Tables 17-18
Scope:  LLDUC model; AMD EPYC 9474F 96-core nodes with 1.5 TB memory, Flatiron Institute; spin isomers BS7-C and BS8-E

Figure: Zhai et al., hypothetical ideal Frontier time (operation count divided by 1.102 EFLOP/s combined CPU and GPU): UCCSDTQ in a 54-orbital, 69-electron subspace 1.90 s; UDMRG extrapolation (D = 18,000) 46.3 s; full-space UCCSDTQ composite 21.0 s; UDMRG at D of about 393,000 (variational to about 1 kcal/mol of the extrapolated energy, two sweeps) 22.9 hours.
Owner:  arXiv:2601.04621, p.11-12 and Fig. 4
Scope:  "theoretical ideal cost", no memory limits, "do not account for important practical factors". Derived by the researcher from these: 46.3 s x 1.102 x 10^18 = 5.1 x 10^19 operations; 22.9 h x 1.102 x 10^18 = 9.1 x 10^22 operations.

Figure: Zhai et al. energy for the LLDUC model, E0 = -22140.4106 ± 0.0005 Hartree (consensus, ±0.31 kcal/mol); -22140.4091 ± 0.0020 Hartree (conservative, ±1.25 kcal/mol); strict variational UDMRG (D = 18,000) is 8.76 kcal/mol above the estimate. 1 kcal/mol = 1.6 mHartree.
Owner:  arXiv:2601.04621, p.9-11
Scope:  Spin isomers BS8-E and BS7-C; extrapolation, no formal error theory

Figure: Overlap of the dominant broken-symmetry determinant with the D = 18,000 UDMRG state: 0.4738 (BS7-C) and 0.4468 (BS8-E). Zhai et al. say this should be read as overlap with the manifold of eigenstates within 1 kcal/mol of the ground state.
Owner:  arXiv:2601.04621, Supplementary Sec. 3.1.6, quoted on p.12
Scope:  The 8.6-hour figure assumes O(1) overlap with the initial state, per Zhai et al.

Figure: 8.6 hours; 4.5 million physical qubits; code distance 27; 9.99 x 10^8 Toffolis; 1,459 logical qubits
Owner:  arXiv:2502.15882 (PRX 15, 041016)
Scope:  CAS(113e, 76o); phase estimation only; 10^-3 physical error rate, 1 microsecond cycle, 10 microsecond reaction time, four CCZ factories; perfect trial state; no trial-state preparation

Figure: 2.50 hours 1-shot (2.36 expected) on 2,692 thousand qubits; 5.26 h on 1,170 thousand; 23.9 h on 444 thousand; 716 h on 166.9 thousand
Owner:  arXiv:2605.30455, Table XXVII (FeMoco-76o113e)
Scope:  Same hardware model as above; "assume perfect ground state overlap and ignore the cost of preparing a good trial state"; preprint

Timeline, quantum resource estimates for FeMoco (year; active space; method; hardware assumption; result):

```text
Year  Active space   Method                         Assumed hardware              Result                         Owner
2016  54e/54o        Trotter, 0.1 mHa target        10 ns logical T gate          130 d serial, 15 d nesting,    arXiv:1605.03590 (PNAS 2017)
      (RWST)         (structure 1)                                                110 h parallel rotations
2016  54e/54o        Trotter, 1 mHa target          same                          12 d, 1.4 d, 11 h              same
2019  54e/54o;       Single-factorization           not stated in the table       9.5e10 and 1.2e11 Toffolis     arXiv:2502.15882 Table I
      76o            qubitization                                                 (3,320 / 3,628 logical qubits)
2020  54e/54o;       Double factorization           not stated in the table       2.3e10 and 5.3e10 Toffolis     same
      76o                                                                         (3,600 / 6,404)
2020  54e/54o;       Tensor hypercontraction (THC)  surface code, 1 us, 0.1%       5.3e9 and 3.2e10 Toffolis;     same; arXiv:2011.03494 abstract
      76o                                                                         about 4 million physical qubits,
                                                                                  under 4 days (abstract)
2024  54o            Symmetry-compressed DF         not stated                    2.6e9 Toffolis (1,994)         arXiv:2502.15882 Table I
2025  76o            Symmetry-compressed THC        not stated                    4.3e9 Toffolis (1,512)         same
2025  76o            Spectrum amplification +       surface code, 1 us, 1e-3,     9.99e8 Toffolis; 4.5 million   arXiv:2502.15882 (PRX 15, 041016)
                     DFTHC                          10 us reaction                physical qubits, 8.6 h
2025  54o            same                           same                          3.2 million qubits, 2.7 h      same
2026  76o            DFTHC + denser surface code,   same error rate and cycle     2.69 million qubits, 2.50 h;   arXiv:2605.30455
                     space-time optimization        times                         1.17 million qubits, 5.26 h
2026  54o            same                           same                          2.0 million qubits, 48 min;    same
                                                                                  1.1 million qubits, 1.1 h
```

Timeline, classical work on the 113e/76o Hamiltonian and its predecessor (year; active space; method; hardware; result):

```text
Year   Active space  Method                          Hardware                      Result                                Owner
2018   54e/54o       CC, DMRG, SHCI                  "modest resources"            DMRG and SHCI agree within 5 mEh;     arXiv:1809.10307 (JCP 2019)
(19)                                                 (Chan: a laptop, hours)       model judged easy; 76-orbital model
                                                                                   introduced
2024   113e/76o      Spin-adapted DMRG (benchmark)   one NVIDIA DGX-H100 node      246 TFLOP/s sustained; no            arXiv:2407.07411
                                                                                   solution claimed in abstract
2025   113e/76o      Mixed-precision DMRG            NVIDIA Blackwell, emulated    "chemical accuracy" relative to      arXiv:2510.04795
       (Oct)                                         FP64                          FP64 DMRG, not the exact energy
2026   113e/76o      UDMRG + UCC with extrapolation  AMD EPYC 96-core nodes;        E0 = -22140.4106 +/- 0.0005 Ha        arXiv:2601.04621
       (Jan)                                         about 2.8 million core-hours  (+/-0.31 kcal/mol); conservative
                                                                                   +/-1.25 kcal/mol
2026   113e/76o      Spin-adapted neural-network     not in abstract               competitive with DMRG at D = 10,000   arXiv:2604.06841
       (Apr)         backflow
2026   113e/76o      Not stated in accessible text   20,480 LineShine nodes        1.456 EFLOP/s DP; "ground-state       SC26 gb103 abstract
       (Nov)                                         (rate); 1,280 nodes (result)  consensus" in 105 min
```

Time and resource comparison (what each side's figure covers):

```text
Item                        Classical, Shang et al. (SC26)        Classical, Zhai et al. (Jan 2026)       Quantum, Low et al. 2025       Quantum, Low et al. 2026
Time                        105 min measured                      2.77M core-hours measured;             8.6 h projected                2.50 h projected
                                                                  46.3 s ideal on Frontier (hypothetical)
Machine                     1,280 of 22,680 LineShine nodes       96-core EPYC nodes                      4.5M physical qubits (does     2.69M physical qubits (does
                            (all-CPU Arm)                                                                 not exist)                     not exist)
Active space                CAS(113e, 76o)                        CAS(113e, 76o) (LLDUC)                  CAS(113e, 76o)                 CAS(113e, 76o)
Accuracy                    not stated in accessible text         +/-0.31 to +/-1.25 kcal/mol,            std dev 1 mHa target, within   same
                                                                  extrapolated                            1.6 mHa budget
Starting state              not stated                            broken-symmetry determinants            perfect overlap assumed;       perfect overlap assumed;
                                                                  (overlap 0.45 to 0.47)                  preparation excluded           preparation excluded
Status                      peer-reviewed conference paper        preprint v2                             PRX 2025                       preprint
```

## Limits

- The full prize paper was not opened. The SC26 page has no PDF or DOI link, and the SC26 table of contents (IEEE Computer Society, pages 39-50 per a search snippet) did not expose the paper. What method it runs, what "ground-state consensus" means, what energy and uncertainty it reaches and against what reference could not be established. That it uses the Zhai UCC and UDMRG consensus is an inference from the shared word and active space.
- The 105-minute run's contents are unknown: whether it covers all 35 spin isomers or one, whether the time includes integrals and I/O, and whether it reaches 1 kcal/mol. The abstract gives no accuracy figure.
- A like-for-like time comparison cannot be made from what was read. The Hamiltonian matches, and Shang's abstract says "on the same active space". Everything else differs: measured versus projected, extrapolated estimate versus phase estimation with a perfect-overlap assumption and no trial-state cost, and an existing machine versus a hypothetical one.
- ACM's own release or award page was not opened (403 from Cloudflare on awards.acm.org and acm.org, for both direct and browser-style requests). The Quantum Insider and HPCwire reposts, both read through summarizing fetches, are the stand-in. Their texts say ACM does not give accuracy or a quantum comparison.
- Low et al. 2025 was read as arXiv v1. The published PRX version (journals.aps.org, 403) may differ.
- No quantum-side reaction to the Shang result was found in several searches. The quantum-side positions here (Babbush et al. Nov 2025; Low et al. May 2026) predate it. Whitfield and Suess are quoted in a Quanta article about Zhai et al., read only through a summary, so their exact words need checking against the page.
- Chan's academic title is not printed in the sources read. Use the affiliation as printed in arXiv:2601.04621.
- The 2.5-hour quantum figure is a preprint and has not been checked against a refereed version. Its Table XXVII column headings were read from a rendered page and checked arithmetically (qubits x hours = volume), not against a text description.
- Other FeMoco-76 resource estimates that surfaced in searches (arXiv:2411.04270, with runtimes in years) were not opened and are not used.
- Not checked: anything about CNIS beyond its name, and the claim reported in a secondary op-ed that the team identifies Fe6 as the most stable candidate for nitrogen binding.

## Source assets

Asset: Fig. 4 in arXiv:2601.04621, p.12. A horizontal bar chart on a log time axis (10^-1 to 10^6 seconds) of hypothetical Frontier wall time for four classical calculations, labeled 1.90 s, 46.3 s, 21.0 s and 22.9 hours.
Shows:  How far apart the cheap extrapolation workload and the 1 kcal/mol variational workload are on the same machine, and that these are operation counts divided by peak rate, not runs.
Crop:   Keep the axis label, the four bar labels with their method names and the "(extrapolation ~1 kcal/mol error)" notes. Keep the caption's word "Hypothetical". Do not present the bars as measurements.

Asset: Table I in arXiv:2502.15882, p.3. A year-by-year table of FeMoco-54 and FeMoco-76 logical qubits and Toffoli counts from 2017 (5.0 x 10^13) to 2025 (3.41 x 10^8 and 9.99 x 10^8).
Shows:  The seven-orders-of-magnitude fall in quantum cost for the benchmark, with the specific innovation behind each step. A timeline can be redrawn from these rows.
Crop:   Keep the year, innovation and both active-space column groups, including the footnote that Toffoli counts use σPEA = 1 mHa.

Asset: Fig. 1 and its inset table in arXiv:2605.30455, p.2. Pareto curves of expected runtime (hours, log scale) against physical qubits (log scale) for FeMoco-54, FeMoco-76 and other molecules, with the 2025 estimates marked "Prior art". The inset gives FeMoco-54 rows from 8.6 million qubit-hours down to 1.3.
Shows:  That a quantum run-time projection is a curve over hardware size and not a single number, and that the 8.6-hour point sits on the slow side of a curve that has since moved.
Crop:   Keep both axes, the FeMoco-76o113e curve and the "Prior art" markers. The FeMoco-76 numbers in Table XXVII (p.101) are text-only. Redraw them from the Numbers section if a chart is wanted.

Asset: Fig. 1F and Fig. 3 in arXiv:2601.04621 (p.3 and p.10). Per the captions: DMRG energy against bond dimension for three orbital choices, with the estimated ground-state energy as reference; and the extrapolation of UDMRG and UCC energies to the exact answer for BS7-235 and BS8-237. Only the captions and the p.12 Fig. 4 page image were read; the figures themselves were not inspected.
Shows:  Why the classical answer is an extrapolated estimate with an error bar and not a converged variational number.
Crop:   Keep the reference line and the extrapolation fit, if the figures hold up when viewed.

Asset: Chan's blog has no figures taken for use. Babbush et al. (arXiv:2511.09124) plot FeMoco Toffoli counts by publication year in a "right plot" of a resource-reduction figure; not opened as an image.
Shows:  Not established.
Crop:   Not established.

## Discarded

https://www.eurasiareview.com/23112026-seven-iron-atoms-and-the-real-test-of-quantum-advantage-oped/: opinion piece by Burak Oktenli (bio lists an MBA and an MPS in Applied Intelligence from Georgetown; no chemistry background) dated 23 Nov 2026. It cites the 2025 PRX study for 8.6 hours and the SC26 paper for 105 minutes, and says the comparison is of an observed run against a projection. Repeats what the primaries establish. Its Fe6 claim for the prize paper could not be checked against the paper.
https://mlq.ai/news/chinese-team-wins-the-2026-gordon-bell-prize-for-an-exascale-simulation-of-a-chemistry-problem-pitched-for-quantum-computers/: repost of the ACM release with a note that ACM gives no accuracy figure and no quantum comparison. Adds nothing beyond the release.
https://casrai.org/news/acm-gordon-bell-prize-2026-femoco-exascale-chinese-team: aggregator summary of HPCwire, Quantum Insider and MLQ, no firsthand material, no quotes.
https://gazewire.com/technology-innovation/quantum-and-enterprise/chinese-research-team-wins-2026-acm-gordon-bell-prize: AI-synthesized rewrite of the Quantum Insider piece. Its "impact analysis" is the site's own interpretation.
https://www.hpcwire.com/2026/11/20/gordon-bell-prize-goes-to-chinese-team-for-exascale-femoco-solution/: 403 on every attempt; content unseen.
https://awards.acm.org/bell and https://www.acm.org/articles/bulletins/2026/november/gordon-bell-prizes-2026: 403 (Cloudflare) on every attempt; content unseen.
https://journals.aps.org/prx/abstract/10.1103/pb2g-j9cw: 403; not read.
https://arxiv.org/abs/2411.04270: appeared in a search with FeMoco-76 estimates measured in years, which does not bear on the 2025 to 2026 comparison. Not opened.

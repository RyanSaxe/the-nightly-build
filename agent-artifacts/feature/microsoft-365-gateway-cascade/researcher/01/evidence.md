# Evidence: feature/microsoft-365-gateway-cascade (researcher 01)

## Provenance verdict

The final PIR text is very probably the document Microsoft issued. No copy of it on a Microsoft-controlled address could be found, so the article must cite a third-party copy and say what that copy is. Microsoft publishes PIRs only inside the Microsoft 365 admin center (Service health, History), which needs an administrator sign-in. Every public copy of the final traces to one origin. The Dutch consultancy site 365Fanatic re-saved the admin-center document in Word on 21 November 2026: PDF metadata reads "Microsoft® Word voor Microsoft 365", created 2026-11-21 07:53:23 UTC, 15 pages. TechBag reports that origin independently. The tianyin.github.io mirror named in the brief is byte-identical to 365Fanatic's file (SHA-256 d77e84e6…e1b2 for both, and for the scout's `source-copies/final.pdf`). Its server reports Last-Modified 24 November, so it is a later copy of the same file and not a second confirmation. The best copy to cite is the origin: https://www.365fanatic.com/wp-content/uploads/2026/11/postincidentreport-mo1550821.pdf. Its authenticity rests on four checks. (1) Microsoft's @MSFT365Status posts during the incident match final-PIR timeline entries on the same events and times: 7:20 PM load diagnosis, 11:55 PM rejoined servers failing again, and the 48-hour mail window. (2) Charles Lamanna, a Microsoft EVP, posted on X an "abridged version" of the preliminary root cause that matches the preliminary copy almost word for word. The final repeats the preliminary's Actions Taken table nearly verbatim, so that continuity covers most of the final's timeline. (3) GeekWire (Todd Bishop), TechBag and a Reuters-sourced aggregator quote or summarize final-only wording consistent with this file ("not caused by AI tooling", "about two hours", 13 next steps), but GeekWire and TechBag link the 365Fanatic copy, so they confirm what the copy says and not independently that Microsoft wrote it. (4) Tony Redmond (office365itpros.com) wrote on 22 November that "the final PIR is now online". The preliminary copy at next.ink is a "Microsoft: Print To PDF" export of "PostIncidentReport.docx" by author "Vincent Hermann", the Next journalist whose 16 November article links it. Its root-cause text is corroborated word for word by Lamanna's post, so it counts as an authentic copy. One artifact in the final copy needs handling: the "Completed actions" table appears twice (a three-row version on p.13 and a six-row version without a heading on p.14). This may come from the re-save or may sit in Microsoft's original. The union is seven distinct items.

## Summary

The final PIR (Microsoft's own account) supports the commission's mechanism in every part except two figures in its framing. The PIR names four co-occurring factors: a lock-contention defect from a July update that hit only newer, higher-core SKUs; about 14% of gateway capacity out for a routine deployment; a Teams failover onto the Exchange gateway at 1:07 AM UTC; and the North American daily peak. Broad failures began at about 4:00 PM UTC on 12 November. Intra-region redistribution spread them across North America within two hours, and cross-region redistribution reached every region within about two hours of 4:00 PM. Recovery stalled because rejoining servers were "immediately overwhelmed by queuing client traffic", and the only repair item written against that finding (gradual ramp-up and admission control) has no date. Two framing points in the commission do not hold. The PIR puts worldwide spread at about two hours after broad failure, not about four. And the PIR's executive summary attributes the long recovery to three other factors: finding a months-old change, the double restart, and fleet-wide deployment time. The rejoin loop appears in the body section "Why recovery took longer", not in that summary. The evidence is thin in three places. All capacity and spread figures are Microsoft's, with no independent measurement. Figure 1 has no y-axis scale. And the PIR never says whether servers rejoining after the defect was reverted were re-overwhelmed, which is the observation that would make the loop metastable in the Bronson et al. sense rather than a symptom of a defect still present.

## Sources

```text
URL:         https://www.365fanatic.com/wp-content/uploads/2026/11/postincidentreport-mo1550821.pdf
             (byte-identical copy: https://tianyin.github.io/misc/pir_microsoft_365_11-12-2026.pdf)
Kind:        primary. Microsoft authored it and owns every claim in it about its own systems. The file is a third-party
             re-save (365Fanatic, Word, 2026-11-21) of the admin-center document; see Provenance verdict.
Establishes: Microsoft's final account: four causal factors, spread mechanism, recovery account, UTC timeline,
             completed actions, 13 next steps with categories and due quarters. Firsthand for Microsoft's statements;
             every capacity figure is Microsoft-reported and unaudited.
Paraphrase:  See the Numbers and Timeline sections below; locators are to PDF pages 1-15.
Locators:    p.1 title and report date (20 Nov 2026); p.2 incident IDs, Executive Summary (incl. three recovery
             factors, "not caused by AI tooling"); pp.2-5 User Impact (p.3 consumer mailboxes inactive >30 days
             expired); p.5 Incident Start/End list; p.6 Factor 1 (defect, newer SKUs, July, load testing), Factor 2
             (14%), Factor 3 (Teams failover, 1:07 AM, ~16 hours); p.7 Factor 4 (peak, ~4:00 PM), Figure 1, "How the
             disruption spread" begins; p.8 cascade across NA, ">80%", cross-region "within about two hours",
             Mitigation, "Why recovery took longer", five-step fix, group recovery strategy; p.9 24->48 h retry window,
             Actions Taken begins (12:25 AM-5:03 PM Nov 12); p.10 5:32-8:30 PM; p.11 9:00 PM-1:15 AM Nov 13;
             p.12 1:53 AM-11:35 AM Nov 13; p.13 1:00 PM Nov 13-4:15 AM Nov 14 and first "Completed actions" table;
             p.14 second completed table, Next Steps rows 1-5; p.15 Next Steps rows 6-13.
Quote:       "Recovery took longer than usual because as gateway servers returned to service, they were immediately
             overwhelmed by queuing client traffic and became unresponsive again." (p.8)
             "Within about two hours of the broad failures that began in North America, servers in every region were
             affected globally." (p.8)
             "This change was not caused by AI tooling." (p.2)
```

```text
URL:         https://next.ink/wp-content/uploads/2026/11/PostIncidentReport.pdf
Kind:        primary. Microsoft authored it. The file is a "Microsoft: Print To PDF" export (author field "Vincent
             Hermann", 2026-11-16 15:39 UTC) of PostIncidentReport.docx, linked from Next's 16 Nov article.
Establishes: Microsoft's preliminary account dated 15 November 2026 (announced by @MSFT365Status 16 Nov 05:48 UTC).
             Root-cause text corroborated near-verbatim by Lamanna's X post.
Paraphrase:  Three main factors: (1) the latent lock-contention defect from "a fix that was prepared specifically
             for Microsoft 365 networking gateway servers", first deployed in July; (2) a load surge from Teams
             failing over to the "primary" gateway "approximately fifteen hours before the outage"; (3) nearly 14% of
             capacity out "due to an unrelated issue from the previous day". The cascade reached >80% of servers
             unresponsive in under two hours; the regional "bulkheads" failed "due to a separate issue". Recovery was
             slow because returning servers were overwhelmed by waiting traffic; the fix was applied to groups of
             servers ("e.g. 50%+ of a region"). Incident end given as 13 Nov 4:10 PM UTC only. Six repair rows, five
             completed and one promising the comprehensive list on 11/20/2026.
Locators:    p.1 report date; p.2 Important Note (final within five business days), Incident Start/End; p.3 Root
             Cause (three factors, fifteen hours, unrelated issue, 80%, bulkheads/separate issue); p.4 failing out of
             the gateway ("scale reasons"), Recovery took longer, 50%+, Actions Taken begins; pp.4-6 timeline;
             p.7 Mitigation / Repair Items.
Quote:       "In this case, due to a separate issue, the normal bulkheads between these different partitions did not
             stop the cascading failure." (p.3) Quoted because the final drops this explanation.
```

```text
URL:         https://x.com/clamanna/status/2122209697226948729
Kind:        primary for the fact that a Microsoft executive published the preliminary root cause. Charles Lamanna,
             profile title "EVP of Copilot, Agents, and Platform at Microsoft". Posted 16 Nov 2026 06:06 UTC. Read via
             the fxtwitter API because x.com returned 402 to the fetch tool; the address above is the post itself.
Establishes: Authenticity of the preliminary copy's root-cause section (near-verbatim match, with "Windows" removed
             from two phrases) and Microsoft's apology.
Paraphrase:  "an abridged version" of the root cause, three factors, identical to preliminary p.3-4 text.
Locators:    single post.
Quote:       "More details on the root cause can be found in the Microsoft 365 Admin center, and an abridged version
             can be found below."
```

```text
URL:         https://x.com/MSFT365Status/status/2120938282204688468 (12 Nov 17:54 UTC)
             https://x.com/MSFT365Status/status/2120957934607700161 (12 Nov 19:12 UTC)
             https://x.com/MSFT365Status/status/2120962673911181437 (12 Nov 19:31 UTC)
             https://x.com/MSFT365Status/status/2120967496303858112 (12 Nov 19:50 UTC)
             https://x.com/MSFT365Status/status/2120995209261514827 (12 Nov 21:40 UTC)
             https://x.com/MSFT365Status/status/2121016338181161457 (12 Nov 23:04 UTC)
             https://x.com/MSFT365Status/status/2121031935010951521 (13 Nov 00:06 UTC)
             https://x.com/MSFT365Status/status/2121172248241348867 (13 Nov 09:24 UTC)
             https://x.com/MSFT365Status/status/2122205066157257160 (16 Nov 05:48 UTC)
Kind:        primary. Microsoft's official incident account ("The official @Microsoft account for updates on certain
             @Microsoft365 service incidents"). Contemporaneous. Read via the fxtwitter API (x.com returned 402).
Establishes: Contemporaneous Microsoft statements that match PIR timeline entries, which independently corroborates
             the PIR copies. Most relevant: 19:31 "the elevated load isn't driven by an increase in traffic, but by a
             number of servers being unexpectedly unavailable" (cf. PIR 7:20 PM); 23:04 "users may experience a gradual
             recovery as their clients reconnect"; 00:06 "The servers we returned to service can become unresponsive
             again once they receive traffic" (cf. PIR 11:55 PM); 09:24 "extended email timeout to 48 hours";
             16 Nov preliminary PIR released in the admin center.
Paraphrase:  as quoted.
Locators:    individual posts, times as listed.
Quote:       00:06 UTC 13 Nov: "The servers we returned to service can become unresponsive again once they receive
             traffic; we're analyzing diagnostic data to determine what's triggering the behavior." Contemporaneous
             evidence of the rejoin loop.
```

```text
URL:         https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf
Kind:        primary for the definition of metastable failure (the authors own the framework). Bronson, Aghayev,
             Charapko, Zhu, "Metastable Failures in Distributed Systems", HotOS '21, doi 10.1145/3458336.3465286.
Establishes: The definition only. Says nothing about Microsoft.
Paraphrase:  In a metastable failure a trigger pushes a system into a bad state that persists after the trigger is
             removed, held there by a sustaining effect (often work amplification). Leaving it needs a strong
             corrective push such as a reboot or a large load reduction.
Locators:    §1 Introduction, p.221 (first page) paragraph beginning "Metastable failures occur in open systems",
             continuing on p.222 "a feedback loop sustains the failure".
Quote:       "Metastable failures occur in open systems with an uncontrolled source of load where a trigger causes the
             system to enter a bad state that persists even when the trigger is removed." (p.221)
             "When one of many potential triggers causes the system to enter the metastable state, a feedback loop
             sustains the failure, causing the system to remain in the failure state until a big enough corrective
             action is applied." (p.222)
```

```text
URL:         https://www.usenix.org/system/files/osdi22-huang-lexiang.pdf
             (landing page https://www.usenix.org/conference/osdi22/presentation/huang-lexiang)
Kind:        primary for the formal definition of the sustaining effect. Huang, Magnusson, Bangalore Muralikrishna,
             Estyak, Isaacs, Aghayev, Zhu, Charapko, "Metastable Failures in the Wild", OSDI '22.
Establishes: The definition only.
Paraphrase:  A sustaining effect is a feedback loop that keeps load at or above capacity after the trigger is gone.
             The amplification can raise load or lower capacity.
Locators:    §3.3 "Sustaining Effect Loop", Definition 3, proceedings p.78.
Quote:       "Definition 3 (Sustaining effect). A sustaining effect is a feedback loop that keeps the system in an
             overloaded state such that Lsys(t) ≥ Csys(t) even after the trigger is removed."
```

```text
URL:         https://www.365fanatic.com/m365-outage-12-november-2026-final-report/
Kind:        secondary. 365Fanatic, a Dutch Microsoft 365 consultancy, summarizing; it says "Microsoft's report is
             authoritative for the exact text". Last updated 21 Nov 2026.
Establishes: Only that this site published the final PDF copy, captioned as 15 pages, credited to Microsoft, and
             pointed admins to the admin center. Does not say how it obtained the document.
Paraphrase:  Summary of four factors, five recovery steps, seven completed items, 13 next steps by quarter.
Locators:    whole page; PDF link in body.
```

```text
URL:         https://www.thetechbag.com/blog/microsoft-365-final-report-teams-traffic-newer-servers
Kind:        secondary. TechBag, 21 Nov 2026.
Establishes: That the public final copy is 365Fanatic's 21 Nov Word re-save of the admin-center report, which matches
             the PDF metadata. Its preliminary-vs-final comparison agrees with this record's own reading.
Paraphrase:  The final has four factors, not three. The 14% is now routine deployment, not an unrelated issue. The
             "separate issue" bulkhead explanation is gone. 13 next steps, nine dated, four due by end-2026.
Locators:    whole article, "what changed" section.
```

```text
URL:         https://www.geekwire.com/2026/microsofts-final-outlook-outage-report-details-testing-gaps-and-safeguards-that-backfired/
Kind:        secondary. Todd Bishop, GeekWire co-founder and editor, 21 Nov 2026.
Establishes: That press quoted final-only wording matching the copy: "Within about two hours…", "can cascade failures
             to other regions", the AI-tooling sentence. Links the 365Fanatic PDF, so this is not independent
             authentication.
Paraphrase:  Reports the final's changes from the preliminary; calls the rejoin pattern a "thundering herd" (the
             reporter's term, not Microsoft's); notes the ramp-up fix has no date.
Locators:    body; the "separate issue" comparison paragraph.
```

## Contradictions

- **Worldwide spread time.** The commission says the service went down worldwide "within about four hours". The final PIR says broad NA failures began at about 4:00 PM UTC, a significant portion of the NA fleet failed "in less than two hours", and "within about two hours of the broad failures that began in North America, servers in every region were affected globally" (p.7-8). That puts global spread at about 6:00 PM UTC, about two hours, not four. Measured from the Teams failover (1:07 AM) it is about 17 hours. No reading of the PIR gives four.
- **Why recovery took a day.** The commission leads on the rejoin loop. The final's Executive Summary (p.2) names three different recovery factors: identifying a defect introduced months earlier, restarting each server twice (before and after the fix), and deploying the update across many servers. The rejoin loop appears in the body, as the first sentence of "Why recovery took longer" (p.8), and in Next Steps row 8 (p.15). The writer should present both, not only the loop.
- **Is the loop metastable in the literature's sense?** Bronson et al. require a bad state that "persists even when the trigger is removed" (p.221). In the PIR, rejoined servers were re-overwhelmed (11:55 PM Nov 12) while the defect was still deployed. The revert began at 7:20 AM Nov 13 and stability on patched capacity was confirmed at 8:00 AM (p.12). The PIR never reports a patched server being re-overwhelmed, and its recovery method took capacity units out of rotation, patched them and returned whole groups (p.8-9). The evidence fits a sustaining effect: re-failure persisted through US evening and night hours (11:55 PM-5:00 AM UTC) when the NA peak had passed. It does not separate the loop from the defect. Calling it metastable is the article's inference and must be labeled as such.
- **Preliminary vs final on the 14%.** Preliminary p.3: out "due to an unrelated issue from the previous day", on track to return through routine maintenance. Final p.6: out "as part of routine operations when we deploy the latest version of the service on these servers". Executive Summary p.2: "planned maintenance". Microsoft changed its explanation. The commission's "out for maintenance" follows the final.
- **Preliminary vs final on cross-region spread.** Preliminary p.3: bulkheads failed "due to a separate issue". Final p.8: when a region exhausts healthy capacity, "the traffic management system detects this condition and redirects the traffic to other regions", which is the designed behavior, and Next Steps row 1 says "Traffic distribution design can cascade failures to other regions". The separate issue is not mentioned or explained in the final.
- **Teams failover lead time.** Preliminary p.3 "approximately fifteen hours before the outage"; final p.6 "~16 hours". From 1:07 AM to the 4:00 PM broad failures is 14 h 53 min; to the 4:20 PM incident start it is 15 h 13 min. The final's "~16" is loose.
- **Scope of the Teams shift.** Final Factor 3 (p.6) describes a routing issue "on its networking gateway in the US East region". Next Steps row 4 (p.14) states "A routing issue in one region moved all Teams traffic worldwide to the primary network gateway". So one region's fault moved global Teams traffic. Only the final says this, and only in the table.
- **What the July change was.** Preliminary: "a fix that was prepared specifically for Microsoft 365 networking gateway servers". Final: "an update that was enabled on Microsoft 365 networking gateway servers" (p.6), and "connection handling change" (p.13). Neither says what it fixed. Lamanna, per Reuters as relayed by news.sulat.com (not opened at Reuters), told an internal review the component had "roughly ten years' worth of acceptable failures". Unverified; not usable.
- **Onset per Figure 1 vs "broad failures ~4:00 PM".** Figure 1 (p.7) shows NA unhealthy servers as a small fraction from about 4:10 to 5:05 PM UTC, rising steeply only after about 5:20 PM. That is visually at odds with "broad failures … began at approximately 4:00 PM UTC" (p.7). It is consistent with the 5:03 PM and 5:32 PM timeline entries. The chart has no y-axis scale, so its fractions are visual estimates only.
- **Next.ink headline says August.** Next's 16 Nov headline says the fault started with "un correctif déployé en août". Both PIRs say deployment started in July. Next appears to have counted back "more than three months". Use July.
- **Status account vs root cause.** Expert Insights reports that @MSFT365Status said on 12 Nov it had "not identified any recent change correlated with the start of impact". That is consistent with the PIR's own statement that change auditing took longer because the change was months old (p.8). Not a contradiction of the PIR.
- **Duration.** Impact window 4:20 PM 12 Nov to 4:10 PM 13 Nov = 23 h 50 min (both PIRs). Resolution declared 4:15 AM 14 Nov = 35 h 55 min after start (final p.5). Some coverage (FourWeekMBA) calls it a "36-hour outage". Say which span is meant.
- **Repair list and the loop.** The commission says the loop is addressed "only with an undated item for admission control". Against the finding "Servers were re-overwhelmed on return to service" there is exactly one row, TBD (p.15). Related items carry dates: row 7 "[Recovery] Improve recovery procedures for fleet-wide failures" CY27Q1 (addresses slow fix distribution, not rejoin), and the completed "temporary guardrails to avoid automatic traffic distribution" (p.14). Row 9 (retry/back-off with other services) is also TBD. The commission's claim holds narrowly.

## Numbers

```text
Figure: ~14% ("Nearly 14%") of networking-gateway server capacity out of service
Owner:  final PIR p.6 (Factor 2); preliminary p.3
Scope:  global gateway server capacity, at the time of the incident; cause differs between reports (see Contradictions)
```
```text
Figure: >80% of servers unresponsive "at the lowest point"
Owner:  final PIR p.8; preliminary p.3 ("more than 80% of servers")
Scope:  final ties it to the North American fleet ("a significant portion of the North American server fleet. At the
        lowest point, more than 80% of servers were unresponsive"); preliminary reads as fleet-wide. Time of the
        trough not given.
```
```text
Figure: < 2 hours for the defect to spread across a significant portion of the NA fleet
Owner:  final PIR p.8
Scope:  from broad NA failures (~4:00 PM UTC 12 Nov)
```
```text
Figure: ~2 hours from broad NA failures until servers in every region were affected
Owner:  final PIR p.8
Scope:  from ~4:00 PM UTC 12 Nov
```
```text
Figure: ~16 hours healthy after the Teams shift (final); ~15 hours before the outage (preliminary)
Owner:  final PIR p.6; preliminary p.3
Scope:  from 1:07 AM UTC 12 Nov
```
```text
Figure: July 2026 start of deployment; "saturated globally over several weeks"; "more than three months" deployed
        worldwide without impact
Owner:  final PIR p.6; preliminary p.3
Scope:  deployment of the defective change to gateway servers
```
```text
Figure: 2 independent, heterogeneous network gateway systems; "thousands of 'capacity units'"
Owner:  final PIR p.6, p.7
Scope:  Microsoft 365 networking gateway architecture
```
```text
Figure: 5 steps per server to apply the fix (out of service; restart from failed state; patch; restart again; back in
        service)
Owner:  final PIR p.8
Scope:  each gateway server
```
```text
Figure: "50%+ of a region" per recovery batch
Owner:  preliminary p.4 only; final p.8 says "large groups of 'capacity units'" without a figure
Scope:  recovery batches
```
```text
Figure: mail retry window extended from 24 to 48 hours before NDR
Owner:  final PIR p.9 (also p.3); @MSFT365Status 13 Nov 09:24 UTC
Scope:  Exchange Online delivery retries
```
```text
Figure: consumer mailboxes inactive > 30 days: some delayed messages expired, senders got NDRs
Owner:  final PIR p.3 (new in final)
Scope:  consumer mailboxes; no count given. Enterprise: "no enterprise messages that were permanently lost"
```
```text
Figure: first customer notification "about 20 minutes after broad impact"
Owner:  final PIR p.15 (Next Steps row 13 finding)
Scope:  ~4:00 PM broad impact to 4:20 PM SHD post
```
```text
Figure: impact 23 h 50 min (4:20 PM 12 Nov to 4:10 PM 13 Nov UTC); resolved declared 4:15 AM 14 Nov (35 h 55 min)
Owner:  final PIR p.5; preliminary p.2 (end 4:10 PM only)
Scope:  incident window
```
```text
Figure: 13 next steps: 4 due CY26 Q4, 5 due CY27 Q1, 4 TBD; 7 distinct completed actions
Owner:  final PIR pp.13-15
Scope:  repair list as of 20 Nov 2026
```

### Timeline (UTC), final PIR Actions Taken unless noted

Use for the timeline visual. "P" = also in the preliminary with the same wording; "F" = new in the final.

```text
12 Nov 12:25 AM  Teams users in US East begin timing out on the alternative gateway (F, p.9)
12 Nov  1:07 AM  Automated failover moves Teams traffic onto gateway front ends shared with Exchange Online (P, p.9;
                 also Factor 3 p.6)
1:07 AM-4:00 PM  Load rises gradually; isolated server failures in some regions; automated mitigations (P, p.9)
~4:00 PM         Broad failures in North America begin as US traffic nears daily peak (F narrative, p.7)
 4:03 PM         Anomaly monitor sees rise in connectivity issues (P, p.9)
 4:17 PM         Automation starts redirecting traffic to alternate healthy endpoints (P, p.9)
 4:20 PM         High-priority alert; SHD post EX1550543. Official incident start (P, p.9; p.5)
 4:25 PM         Impact confirmed across Outlook, OWA, EAS, REST APIs (P, p.9)
 4:33 PM         First support case; DownDetector reports accumulate (P, p.9)
 5:03 PM         Further increase in connectivity issues (P, p.9)
 5:32 PM         Automated redirection continues; degradation across multiple regions (P, p.10)
 5:45 PM         Errors located on access-request infrastructure; network logs collected (P, p.10)
 ~6:00 PM        (inferred from p.8: every region affected within ~2 h of 4:00 PM)
 6:00 PM         Progressive restarts and traffic redirection (P, p.10)
 6:27 PM         SHD post MO1550821 (Teams, Copilot, Defender) (P, p.10)
 6:33 PM         Failovers triggered to even out traffic (P, p.10)
 7:00 PM         All deployments and config changes paused (P, p.10)
 7:20 PM         Load traced to unavailable servers, not more traffic (P, p.10; @MSFT365Status 19:31)
 8:00 PM         Targeted change to bypass components failing health checks (P, p.10)
 8:30 PM         Many servers found unresponsive; restarts begin (P, p.10)
 9:00 PM         Alternative health check lets a subset return; auto detect-and-restart prepared (P, p.11)
10:00 PM         Actions confirmed ineffective; regional traffic isolation evaluated (P, p.11)
11:00 PM         Some servers returned; limited recovery; protective traffic measures in one location (P, p.11)
11:55 PM         Returned servers healthy at first, then unresponsive again on receiving traffic (P, p.11;
                 @MSFT365Status 00:06 13 Nov)
13 Nov 12:30 AM  Connection negotiation identified; competing processes block connection handling (P, p.11)
 1:00 AM         Connection-establishing process found overwhelmed (P, p.11)
 1:15 AM         Pressure-reduction measures (monitoring, load); partial success (P, p.11)
 1:53 AM         Some automated traffic redirection by anomaly monitors disabled (P, p.12)
 2:10 AM         Capacity improvements where possible (P, p.12)
 3:00 AM         Changes not applying as expected; new workstreams (P, p.12)
 4:00 AM         Protocol adjustments, redistribution, traffic blocking; partial, unsustained recovery (P, p.12)
 5:00 AM         Machines stuck in bad states block sync; VMs scaled up (P, p.12)
 7:20 AM         Mitigation applied: update reverting the defective change, to a portion of capacity (P, p.12)
 8:00 AM         Stability confirmed on patched capacity; rollout prioritized to regions entering peak (P, p.12)
10:00 AM         Service begins to stabilize; capacity not yet normal (P, p.12)
11:00 AM         APAC recovery actions complete (P, p.12; p.5)
11:35 AM         Europe availability healthy (P, p.12; p.5)
 1:00 PM         Recovery sustained in all regions; mail queues shrink (P, p.13)
 2:17 PM         Global OWA availability back to expected levels; stable by 2:44 PM (P, p.13; p.5)
 3:05 PM         Eligible traffic moved to alternative connection paths (P, p.13)
 3:54 PM         Most major access methods at normal traffic (P, p.13; p.5)
 4:10 PM         No active customer impact; extended monitoring and mail backlog. Impact end (P, p.13; p.5)
14 Nov  4:15 AM  Final customer updates; incident declared resolved (P, p.13; F as an end-time entry, p.5)
```

### Causal factors, preliminary vs final

```text
Preliminary (15 Nov, p.3): three factors
  1 latent lock-contention defect from a July "fix prepared specifically for" gateway servers; worse on more cores;
    load testing "tended to focus on weaker hardware with fewer cores"
  2 load surge from Teams failover ~15 h earlier
  3 ~14% capacity out "due to an unrelated issue from the previous day"
  peak: "This occurred during the peak window of traffic in the United States" (not a numbered factor)
  cross-region: bulkheads failed "due to a separate issue"
Final (20 Nov, pp.2, 6-8): four factors
  1 connection-processing defect: lock contention in an internal Windows process exhausts CPU and memory; from "an
    update that was enabled on" gateway servers; hit newer high-core SKUs, "but not the older generation SKUs"; load
    tests "used older SKU hardware with fewer cores"
  2 reduced capacity: ~14% out "as part of routine operations when we deploy the latest version of the service"
  3 Teams failover: US East routing issue -> automatic failover at 1:07 AM; services healthy ~16 h after
  4 peak load: first NA failures near start of US East business day; broad failures ~4:00 PM
  spread: intra-region redistribution between capacity units, then cross-region redirection when a region exhausts
    healthy capacity (designed behavior); no "separate issue"
```

### Repair items (final, pp.13-15)

Completed (union of the two tables, pp.13-14): revert update for the connection-handling change; Windows image permanently updated with the fix; email delivery window extended; additional capacity added; monitoring for traffic-redirection patterns and connection-handling health; "temporary guardrails to avoid automatic traffic distribution and avoid cascading impact"; servers returned from maintenance.

```text
#  Category                         Finding (abridged)                                Action (abridged)                              Due
1  Blast radius                     traffic distribution can cascade across regions   fix traffic distribution                       CY26 Q4
2  Blast radius                     regional failure zones too large                  smaller fault zones                            TBD
3  Blast radius                     Teams failover helped expose the defect           partition gateway into per-workload pools      CY27 Q1
4  Failover design                  one region's routing issue moved all Teams        Teams fails over only for the affected region  CY26 Q4
                                    traffic worldwide
5  Failover drills, Blast radius    failover testing did not find the defect          scoped failover tests at peak + other changes  TBD
6  Diagnosis                        change auditing slow to find the Windows change   diagnostics and change auditing for Windows    CY27 Q1
7  Recovery                         fleet-wide distribution of the fix too slow       recovery procedures for fleet-wide failures    CY27 Q1
8  Recovery                         servers re-overwhelmed on return to service       gradual ramp-up and admission control on       TBD
                                                                                      rejoin; per-protocol/workload/region traffic
                                                                                      controls; retry and back-off in the service
9  Blast radius                     service retries may spread issues                 retry/back-off with other services             TBD
10 Testing                          tests missed hardware + traffic mix               load tests on newest high-core HW at peak      CY27 Q1
11 Capacity Design                  gateways could not absorb defect at peak          more headroom                                  CY27 Q1
12 Capacity Design                  maintenance capacity loss risky with other        detect extended capacity loss                  CY26 Q4
                                    factors
13 Customer communications          first notice ~20 min after broad impact           faster detection and automated notification    CY26 Q4
```

### What the final adds to or changes from the preliminary

- Adds an Executive Summary (p.2) with three recovery-extending factors, the no-cyberattack statement and "This change was not caused by AI tooling."
- Raises three factors to four, making peak load its own factor; states that the defect hit only newer, higher-core SKUs (p.6).
- Changes the 14% from "unrelated issue from the previous day" to routine deployment / planned maintenance.
- Changes the July change from "a fix prepared specifically for" gateway servers to "an update that was enabled on" them.
- Drops the "separate issue" bulkhead explanation; describes two-stage spread (intra-region capacity units, then cross-region) as designed redistribution.
- Adds the 12:25 AM US East Teams timeouts, the US East routing issue as the failover cause, and (Next Steps) that it moved all Teams traffic worldwide.
- Adds Figure 1 (NA server health, ~4:10-5:55 PM UTC).
- Adds the five-step per-server fix and the group recovery strategy; drops "50%+ of a region".
- Adds the staged end-time list (APAC 11:00 AM to resolved 4:15 AM 14 Nov); the preliminary gave only 4:10 PM.
- Adds consumer-mailbox NDRs (inactive >30 days) and the 24->48 h detail; changes "delayed for many users" to "most users".
- Drops "Teams chats and meetings functioning without issue for most of the outage" and the "scale reasons" Exchange could not fail out (preliminary p.4).
- Adds "permanently updated the Windows image", "Return servers from maintenance", and "temporary" to the guardrails item.
- Adds the 13-item Next Steps table, which the preliminary deferred to 20 Nov.

## Limits

- No Microsoft-hosted public copy of either PIR exists to compare against; the admin-center original could not be opened (sign-in required). Authenticity of final-only passages rests on the copy plus press consistent with it, all traceable to one 365Fanatic re-save.
- Cannot tell whether the duplicated "Completed actions" table (pp.13-14) is in Microsoft's original or was introduced by the re-save.
- Figure 1 has no y-axis values; no server counts, fleet size, core counts, SKU names or per-region figures appear anywhere in either PIR.
- The PIR gives no time for the ">80% unresponsive" trough and no per-region failure times beyond the end-of-incident list.
- Not established whether servers re-failed after receiving the revert, so the metastable label for the recovery loop is inference (see Contradictions).
- The PIR does not say what the July change was meant to fix, or what Windows process held the lock.
- No independent measurement of the outage (e.g., third-party monitoring) was gathered; the brief did not ask for it and the PIR is the account.
- The Reuters "Code Red" memo reporting (load shedding, traffic partitioning, faster recovery workstreams) was seen only via an aggregator; Reuters itself was not opened.

## Source assets

```text
Asset: Figure 1, "The trend of machine health overview" stacked bars, final PIR p.7 (embedded PNG, 1363x691)
Shows: NA gateway servers by state (Healthy, Unhealthy, Not In Service, No Health Indicator Data) at ~5-minute
       intervals from ~4:10 to ~5:55 PM UTC 12 Nov: a small unhealthy band until ~5:05 PM, then a steep rise in
       unhealthy and no-data servers; by the last bar roughly half the servers are not healthy (visual estimate).
Crop:  keep the legend, all bars and the time axis; keep the PIR caption text (times UTC, NA only). There is no y-axis
       scale to retain, so the caption must say proportions are not labeled.
```
```text
Asset: Next Steps table, final PIR pp.14-15
Shows: the 13 findings, category tags and due quarters, including the TBD admission-control row.
Crop:  a crop splits across two pages; better rebuilt as an HTML table or chart from this record.
```
```text
Asset: Bronson et al. Figure 1 (stable / vulnerable / metastable state diagram), HotOS '21 p.221
Shows: the lifecycle the literature uses, with trigger and sustaining-effect transitions.
Crop:  usable only if the article draws on the literature's frame; the brief limits literature citations to the
       defining passage, so drawing the loop in the article's own SVG is preferable.
```
Preliminary PIR (next.ink): None found (text only).
@MSFT365Status and Lamanna posts: None found.

## Discarded

```text
https://next.ink/267845/panne-microsoft-365-tout-est-une-partie-dun-correctif-deploye-en-aout/: paywalled article;
  only headline and dek visible; used only to identify the preliminary PDF's origin and the "August" headline error
https://expertinsights.com/news/microsoft-365-outage-post-incident-report: preliminary-era paraphrase, no PIR quotes
https://office365itpros.com/2026/11/16/exchange-online-outage-nov26/: preliminary-era paraphrase; useful only for the
  author's 22 Nov comment that the final PIR was online
https://ghacks.net/2026/11/24/microsofts-final-outage-report-blames-a-july-bug-and-confirms-some-emails-never-arrived: 403 (gated); final-report coverage adds nothing the PIR copy lacks
https://news.sulat.com/2026/11/25/microsoft-code-red/: aggregator relaying Reuters on internal memos; outside the
  commission and not verifiable at the primary
https://www.365fanatic.com/wp-content/uploads/2026/11/postincidentreport.pdf: former preliminary copy, now redirects
  (302) to an HTML page; next.ink copy used instead
https://fourweekmba.com/ai-microsoft-365-root-cause-latent-bug-behind-36-hour-outage/: search-result headline only
  ("36-hour"), used for the duration contradiction; not read further
```

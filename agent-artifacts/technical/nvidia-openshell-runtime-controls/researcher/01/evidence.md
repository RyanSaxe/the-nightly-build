# Evidence record: NVIDIA OpenShell 0.1.0

The evidence supports a walkthrough centered on a real separation of authority in the tagged 0.1.0 code: the Gateway provisions and supplies policy, a Supervisor outside the workload evaluates outbound requests and handles provider credentials, and the sandbox applies operating-system controls to local processes and files. A concrete read-only API example is source-backed and can show how a request is mediated. The evidence is thinner on operational security outcomes: NVIDIA describes adoption and broad safety claims, but I found no independent performance or adversarial evaluation of 0.1.0, and the available Gateway log buffer is not a durable audit store. The `v0.1.0` GitHub release is dated September 25, 2026; NVIDIA’s general-availability announcement and blog are dated September 28. These are separate events.

The source implementation was inspected at tag `v0.1.0`, commit `496ebba293f5cc2bb2753444dddd534f0b4aeb6a`. The evidence below is pinned to that release unless explicitly identified as current third-party integration documentation.

## Sources

### 1. NVIDIA OpenShell v0.1.0 release

URL:         https://github.com/NVIDIA/OpenShell/releases
Kind:        primary; NVIDIA’s release record owns the tag and release metadata.
Establishes: The `v0.1.0` tag and commit, its September 25 release timestamp, and its release contents. The page separately shows later `v0.1.1`/`v0.1.2` tags dated September 26/28, so do not collapse the tag date into NVIDIA’s September 28 GA announcement.
Paraphrase: GitHub lists OpenShell v0.1.0 at lines 400–441, associates it with commit `496ebba`, and records the release time at lines 423–429. The entry includes an explicit-version install command and a release change list.
Locators:   [Release entry](https://github.com/NVIDIA/OpenShell/releases), lines 400–457; tag commit `496ebba` at lines 423–429.
Quote:      None.

### 2. NVIDIA OpenShell v0.1.0 Architecture documentation

URL:         https://docs.nvidia.com/openshell/v0.1.0/about/architecture
Kind:        primary; NVIDIA documents the product architecture.
Establishes: The documented Gateway / compute driver / Supervisor / sandbox roles, the outer egress fence, policy decision path, workload startup order, runtime placements, authentication, and failure handling.
Paraphrase: Sections “What Each Piece Does” and “Inside the Sandbox Boundary” (lines 156–186) state that Gateway owns sandbox state and policy; the driver creates the boundary; `openshell-sandbox` owns agent processes and forwards DNS/TCP; and the Supervisor checks policy and opens approved upstream connections. “How a network request travels” (193–201) gives the five-step path. Runtime table (202–211) names Docker, Podman, Kubernetes, and VM boundaries. Authentication and agent visibility (214–245) keep gateway/provider credentials on the trusted side and say the sandbox freezes the agent if its Supervisor disconnects. These are vendor-stated architecture and intended behavior, not independent proof of all boundary properties.
Locators:   [Architecture](https://docs.nvidia.com/openshell/v0.1.0/about/architecture), lines 156–211 and 214–245.
Quote:      None.

### 3. NVIDIA OpenShell v0.1.0 Sandbox Policies

URL:         https://docs.nvidia.com/openshell/v0.1.0/how-it-works/policies/overview
Kind:        primary; NVIDIA specifies policy fields and precedence.
Establishes: Filesystem, process, network and middleware policy categories; enforcement points and policy selection/composition.
Paraphrase: “What a Policy Controls” (lines 154–168) maps `filesystem_policy` to Landlock at startup, `process` to container creation, and `network_policies` / `network_middlewares` to the sandbox proxy at runtime. The page says unmatched outbound traffic is denied. “Where the Active Policy Comes From” (169–184) orders global, saved, image, and restrictive default policies. A global policy replaces the sandbox policy and suppresses provider-contributed rules while active; it does not merely narrow each sandbox policy. Provider rules can contribute to the effective policy (176–181).
Locators:   [Sandbox Policies](https://docs.nvidia.com/openshell/v0.1.0/how-it-works/policies/overview), sections “What a Policy Controls,” “Where the Active Policy Comes From,” “Base and Effective Policies,” and “Global Policy,” lines 154–184.
Quote:      None.

### 4. NVIDIA OpenShell v0.1.0 Network Rules

URL:         https://docs.nvidia.com/openshell/v0.1.0/how-it-works/policies/network-rules
Kind:        primary; NVIDIA documents the request policy and supported examples.
Establishes: Destination/binary matching, optional HTTP-level inspection, `enforce` versus `audit`, credential scoping, and a read-only API policy example.
Paraphrase: “How Network Rules Work” (163–224) describes default-deny outbound checks and a second request-inspection stage for protocols such as REST. “Enforcement” (225–240) distinguishes blocking from audit-only behavior and explains overlapping rules. “Network Access and Credentials” and “Allow Read-Only API Access” (242–278) state that allowing a destination does not itself permit provider credential release; the preset allows `GET`, `HEAD`, and `OPTIONS`, and enforced violations receive `policy_denied`. The same page cautions that a read-only HTTP-method preset does not guarantee an upstream `GET` has no side effects (278). For a narrower illustration, “Allow Specific Methods and Paths” shows explicit method/path rules at lines 279–317.
Locators:   [Network Rules](https://docs.nvidia.com/openshell/v0.1.0/how-it-works/policies/network-rules), lines 163–240, 242–278, 279–317.
Quote:      None.

### 5. NVIDIA OpenShell v0.1.0 first network-policy tutorial

URL:         https://docs.nvidia.com/openshell/v0.1.0/tutorials/first-network-policy
Kind:        primary; NVIDIA’s versioned tutorial is the source of its example commands and expected results.
Establishes: A reproducible vendor-described example in which an initially blocked `curl` request is allowed by a read-only REST policy, while a `POST` is blocked; policy update is live and logs expose denials.
Paraphrase: “Apply a Read-Only GitHub API Policy” (214–251) provides the `api.github.com:443:read-only:rest:enforce` rule bound to `/usr/bin/curl`, says TLS is terminated for HTTP inspection, and describes live policy update. “Check the Deny Log” (202–211) describes a denied connection log. “Try a Write” is linked in the table of contents at line 142. This is a documented demonstration, not evidence that I ran it or that it was independently tested.
Locators:   [Tutorial](https://docs.nvidia.com/openshell/v0.1.0/tutorials/first-network-policy), sections “Check the Deny Log” and “Apply a Read-Only GitHub API Policy,” lines 202–251; contents lists write attempt at line 142.
Quote:      None.

### 6. NVIDIA OpenShell v0.1.0 installation and runtime requirements

URL:         https://docs.nvidia.com/openshell/v0.1.0/about/installation
Kind:        primary; NVIDIA states package and runtime prerequisites.
Establishes: Docker, Podman, and MicroVM host requirements, Linux package minimum, and that the runtime can be used on Linux/macOS hosts without BlueField hardware.
Paraphrase: “Supported Runtimes” (199–207) lists Docker Desktop/Engine 28.0+, Podman 5.x on Linux with cgroups v2 and an active user socket, and Hypervisor.framework on macOS or KVM on Linux for MicroVM. Linux packages require glibc 2.28+ (217–220). This page does not by itself state the full kernel feature requirements; see the pinned source and Landlock documentation below.
Locators:   [Installation](https://docs.nvidia.com/openshell/v0.1.0/about/installation), “Supported Runtimes,” lines 199–207; “Linux,” lines 217–220.
Quote:      None.

### 7. NVIDIA OpenShell v0.1.0 source: sandbox architecture

URL:         https://github.com/NVIDIA/OpenShell/blob/v0.1.0/architecture/sandbox.md
Kind:        primary; tag-pinned source repository documentation, inspected at commit `496ebba293f5cc2bb2753444dddd534f0b4aeb6a`.
Establishes: The detailed implementation contract behind the announced architecture, including no-capability workload identity, startup admission, Linux controls, outer fences, and limitations of network mediation.
Paraphrase: “Runtime Model” (9–21) separates the Supervisor from sandbox and agent child, with a non-root identity and zero Linux capabilities. “Startup Flow” (81–110) says the driver builds/evidences an outer fence, the sandbox installs seccomp and Landlock before launch, and the Supervisor validates the boundary before sending a launch permit. “Isolation Layers” (154–184) distinguishes Landlock filesystem policy, seccomp-mediated supported INET sockets, outer fence and policy proxy. “Network and Inference” (225–244) explains seccomp user notification and its role in handing external `connect` decisions to the Supervisor. The document states the mandatory self-protection baseline requires Landlock ABI v3 at lines 186–193. These are implementation documentation at the pinned release; source code below independently confirms the key mechanisms.
Locators:   [Pinned sandbox architecture](https://github.com/NVIDIA/OpenShell/blob/v0.1.0/architecture/sandbox.md), “Runtime Model,” lines 9–21; “Startup Flow,” 81–110; “Isolation Layers,” 154–184; “Network and Inference,” 225–244.
Quote:      None.

### 8. NVIDIA OpenShell v0.1.0 source: security policy

URL:         https://github.com/NVIDIA/OpenShell/blob/v0.1.0/architecture/security-policy.md
Kind:        primary; tag-pinned source repository documentation, inspected at the same release commit.
Establishes: Enforcement order and policy domains; credential binding; security limits of the prover and network request inspection.
Paraphrase: “Policy Areas” and “Network Decisions” (13–22, 58–71) say policy is enforced by kernel controls, process setup and a local proxy, while the Gateway stores/delivers policy and does not decide each egress request. Traffic is fenced, attributed to a binary, checked against destination and binary rules, and then optionally inspected at L7. “TLS and L7 Inspection” (95–116) describes TLS termination and method/path inspection; uninspected protocols remain a distinct limitation. “Credentialed Endpoints” (125–169) describes endpoint-bound credential provenance and rejects credentialed L4-only or `tls: skip` policy absent an explicit escape hatch. “What the proposal prover decides” (440–468) scopes the formal checks and explicitly says credential scope in v1 is sandbox-coarse, not a credential’s read/write permission model. The prover checks modeled grants; it does not prove runtime behavior or a running machine’s actual kernel state (412–420).
Locators:   [Pinned security policy](https://github.com/NVIDIA/OpenShell/blob/v0.1.0/architecture/security-policy.md), lines 13–22, 58–71, 95–116, 125–169, 412–468.
Quote:      None.

### 9. NVIDIA OpenShell v0.1.0 source: Landlock implementation

URL:         https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-sandbox/src/sandbox/linux/landlock.rs
Kind:        primary; release-tagged implementation source.
Establishes: The tagged Linux code probes Landlock availability and constructs filesystem restrictions; it distinguishes required runtime baseline from optional policy compatibility behavior.
Paraphrase: `probe_availability` (51–87) probes the kernel and distinguishes missing, disabled, or blocked Landlock. The mandatory baseline creates a hard-requirement ABI v3 ruleset (129–165). Optional user filesystem rules read `best_effort` versus hard-requirement configuration (224–270); the code can emit a high-severity finding that filesystem restrictions are absent in best-effort mode. The writer should not describe all filesystem rules as fail-closed without explaining this compatibility setting. The special mandatory `/.openshell` baseline still requires ABI v3.
Locators:   [Pinned Landlock source](https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-sandbox/src/sandbox/linux/landlock.rs), `probe_availability`, lines 51–87; baseline, 129–165; optional policy behavior, 224–270.
Quote:      None.

### 10. NVIDIA OpenShell v0.1.0 source: seccomp implementation

URL:         https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-sandbox/src/sandbox/linux/seccomp.rs
Kind:        primary; release-tagged implementation source.
Establishes: Seccomp is not described accurately as a blanket syscall allowlist: the code documents a default-allow filter with targeted blocks and installs `no_new_privs` before applying it.
Paraphrase: File header (4–33) enumerates socket-domain blocks, unconditional and conditional syscall blocks, and the `NETLINK_ROUTE` allowance needed by common runtimes; `apply` (71–85) creates the main filter and compatibility filter. This is combined with Landlock, unprivileged execution, the Supervisor, and the outer network fence. Avoid saying “seccomp blocks all dangerous system calls” or treating seccomp alone as the entire boundary.
Locators:   [Pinned seccomp source](https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-sandbox/src/sandbox/linux/seccomp.rs), module description and `apply`, lines 4–85.
Quote:      None.

### 11. NVIDIA OpenShell v0.1.0 source: OPA network authorization

URL:         https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-supervisor-network/src/opa.rs
Kind:        primary; release-tagged implementation source.
Establishes: The Supervisor-side evaluator loads policy and returns an allow/deny result, reason and matched policy name; a failed-closed engine denies.
Paraphrase: `evaluate_network` (506–558) evaluates the `allow_network` Rego rule, returns false when the engine is in fail-closed state, and retrieves denial reason and matched policy. `authorize_egress` begins at 577 and carries one policy generation into authorization. The nearby Rego bundle’s default is deny (source entry 12).
Locators:   [Pinned OPA engine](https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-supervisor-network/src/opa.rs), `evaluate_network`, lines 506–558; `authorize_egress`, 560–590.
Quote:      None.

### 12. NVIDIA OpenShell v0.1.0 source: default-deny Rego policy

URL:         https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-supervisor-network/data/sandbox-policy.rego
Kind:        primary; release-tagged policy implementation.
Establishes: The evaluator’s network default and selector logic at the code level.
Paraphrase: `default allow_network = false` appears at line 6. Lines 18–20 permit only when a matching network policy succeeds. Lines 71–99 identify matching policy names and define endpoint-plus-binary matching; exact host/port matching is shown at 107–125. Together with the OPA engine and proxy, this is the policy decision behind the read-only walkthrough.
Locators:   [Pinned Rego policy](https://github.com/NVIDIA/OpenShell/blob/v0.1.0/crates/openshell-supervisor-network/data/sandbox-policy.rego), lines 4–20, 71–125.
Quote:      `default allow_network = false` (line 6); this exact line is the useful implementation string.

### 13. Linux kernel Landlock documentation

URL:         https://cdn.kernel.org/doc/html/latest/userspace-api/landlock.html
Kind:        primary; Linux kernel project documentation for the underlying LSM.
Establishes: Landlock’s scope and ABI-version constraints; it is a stackable restriction on ambient process rights and file hierarchies, not an all-purpose agent policy engine.
Paraphrase: The introduction and “Landlock rules” (11–32) describe layering filesystem restrictions onto existing controls. ABI caveats (838–850) say truncation cannot be denied before ABI v3 and network port controls are ABI v4. OpenShell’s mandatory v3 baseline therefore matters, but the article should not infer that Landlock itself enforces host/path/API semantics outside its documented scope.
Locators:   [Landlock userspace API](https://cdn.kernel.org/doc/html/latest/userspace-api/landlock.html), lines 11–32 and “File truncation (ABI < 3)” / “TCP bind and connect (ABI < 4),” lines 838–850.
Quote:      None.

### 14. Linux seccomp user-notification manual

URL:         https://man7.org/linux/man-pages/man2/seccomp_unotify.2.html
Kind:        primary; Linux man-pages project documentation for the kernel interface.
Establishes: Seccomp user notification delegates a blocked syscall to a user-space process, but the interface is explicitly not intended by itself as a security-policy mechanism.
Paraphrase: “Overview” (44–63) describes delegation; “NOTES” (586–590) expressly warns against using the notification mechanism alone to implement security policy. OpenShell’s design layers it with Landlock, reduced privilege, and the outer egress fence, which should be named when discussing the mediated `connect` path.
Locators:   [seccomp_unotify(2)](https://man7.org/linux/man-pages/man2/seccomp_unotify.2.html), “Overview,” lines 44–63; “NOTES,” 584–590.
Quote:      None.

### 15. NVIDIA OpenShell v0.1.0 logs and retention

URL:         https://docs.nvidia.com/openshell/v0.1.0/observability/accessing-logs
Kind:        primary; NVIDIA describes log event formats, transport and retention.
Establishes: OCSF examples can record allowed/denied network activity and policy changes; the Gateway’s recent-log buffer is bounded and volatile, and the streaming API reports gaps.
Paraphrase: “CLI” (151–164) shows `NET:OPEN`, `HTTP:GET`, and policy-mutation examples. “Gateway Log Storage” (169–173) says the sandbox pushes logs over gRPC, the Gateway keeps a bounded buffer that is not persisted and is lost at restart, and durable storage requires local files or exporting OCSF JSON to an external aggregator. “Loss Awareness and Resume” (174–185) describes explicit loss warnings and terminal `OUT_OF_RANGE` when a cursor has fallen out of the buffer. Do not call the default Gateway buffer an immutable or complete audit log.
Locators:   [Accessing Logs](https://docs.nvidia.com/openshell/v0.1.0/observability/accessing-logs), “CLI,” lines 151–164; “Gateway Log Storage,” 169–173; “Loss Awareness and Resume,” 174–185.
Quote:      None.

### 16. OpenClaw OpenShell integration documentation

URL:         https://docs.openclaw.ai/gateway/openshell
Kind:        primary for OpenClaw’s own integration; independent of NVIDIA’s authoring and marketing.
Establishes: OpenClaw documents and maintains an OpenShell-managed sandbox backend: it delegates lifecycle to the CLI, executes commands over SSH, and has local/remote and workspace-sync options. This establishes an actual third-party integration surface, not the scale or production use of that integration.
Paraphrase: “OpenShell” (652–660) describes lifecycle delegation, transport and prerequisites. Configuration examples and lifecycle management (751–788) show selectable provider, workspace, policy and runtime settings. OpenClaw requires a supported OpenShell runtime and active Gateway. The docs accept OpenShell v0.0.88 or newer, confirming compatibility predates 0.1.0; they do not report adoption metrics.
Locators:   [OpenClaw OpenShell backend](https://docs.openclaw.ai/gateway/openshell), overview and prerequisites, lines 652–660; configuration/lifecycle, 751–788.
Quote:      None.

### 17. NVIDIA OpenShell 0.1.0 general-availability announcement

URL:         https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/
Kind:        primary; NVIDIA announcement and product walkthrough.
Establishes: NVIDIA announced 0.1.0 GA on September 28 and describes its intended model, sample read-only request, broader Open Agent Safety Platform, and named organizations.
Paraphrase: The article is dated September 28 (lines 10–16). “How organizations are adopting OpenShell” (46–51) claims Cadence uses it for chip design, Slack is building an on-demand agent platform on it, and Gecko Robotics uses it for robot-agent governance; these statements are NVIDIA’s, not independent deployment verification. The walkthrough (75–121) gives the public GitHub API GET/POST example and explicitly labels it a demo. “Access services without exposing credentials” (122–134) describes provider credential substitution outside the workload, while line 129 notes that upstream service permissions still apply. The announced Open Agent Safety Platform is described as broader than OpenShell at line 41.
Locators:   [NVIDIA technical blog](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/), date/byline, lines 10–16; adoption claims, 46–51; architecture/demo, 63–121; credentials and platform boundary, 122–134.
Quote:      None.

### 18. Associated Press reporting on OpenShell and Sentry

URL:         https://apnews.com/article/nvidia-ai-security-openshell-sentry-a4cfc84ed00353ff8f2dad4bed7b429e
Kind:        secondary; independent reporting that attributes product claims to NVIDIA and includes an outside expert’s caution.
Establishes: OpenShell is one component of the broader announced platform; Sentry is a distinct hardware layer; the product cannot prevent model dishonesty or mistakes, and operators define permissions. AP reports a computer-science professor’s view that rules can block useful work and says case studies are needed.
Paraphrase: “The platform includes a sandbox” and “It promises to stop…” (1812–1847) distinguish OpenShell from Sentry and attribute runtime-boundary claims to NVIDIA. Lines 1845–1847 state limits. Somesh Jha, identified as a University of Wisconsin computer-science professor, says performance tradeoffs require case studies (1858–1859). This supports a limit on what an architecture/demo establishes, not a measured defect in OpenShell.
Locators:   [AP report](https://apnews.com/article/nvidia-ai-security-openshell-sentry-a4cfc84ed00353ff8f2dad4bed7b429e), lines 1812–1847 and 1858–1859.
Quote:      None.

### 19. Reuters report on the September 28 launch

URL:         https://www.reuters.com/legal/litigation/nvidia-releases-ai-safety-software-it-says-could-have-stopped-hugging-face-hack-2026-09-28/
Kind:        secondary; independent launch reporting with attributed statements from NVIDIA.
Establishes: The software launch occurred September 28; NVIDIA’s claim that it could have stopped the Hugging Face incident is an attributed vendor counterfactual, not an independent test result. Reuters distinguishes OpenShell from Sentry.
Paraphrase: The article date/byline appears at lines 151–155. Lines 172–179 report the release and partner launch; lines 184–188 attribute the claimed Hugging Face prevention and Sentry behavior to NVIDIA spokespeople. No independent evaluation is reported in this article.
Locators:   [Reuters](https://www.reuters.com/legal/litigation/nvidia-releases-ai-safety-software-it-says-could-have-stopped-hugging-face-hack-2026-09-28/), lines 151–179 and 184–190.
Quote:      None.

## Contradictions

- **Release date language:** The commission calls September 28 the date OpenShell 0.1.0 was made generally available. NVIDIA’s blog and Reuters use September 28 for the announcement/launch, while GitHub records the signed `v0.1.0` release on September 25. State both facts with their labels; do not describe the tag as first published on September 28.
- **“Traces all actions” / “audit trail”:** AP reports NVIDIA’s “traces all actions” description (1834); NVIDIA’s product blog says OCSF audit trail (74). The versioned log docs enumerate network, process, filesystem, configuration and API activity, but the Gateway only retains a bounded, non-persistent recent buffer and can report event loss (Accessing Logs 169–185). The product can emit useful structured event records, but the evidence does not establish a complete, tamper-proof, durable record of every agent action. Require operators to ship durable logs and qualify coverage.
- **Seccomp boundary:** A broad account that “the kernel decides every network request” would be inaccurate. Linux’s seccomp user-notification facility delegates a syscall to a user-space supervisor and explicitly is not meant to implement security policy on its own. OpenShell pairs notification with policy evaluation and a separate outer network fence; explain all three.
- **Filesystem failure mode:** “All file policy fails closed” is too broad. The mandatory private-path self-protection baseline requires Landlock ABI v3, but user-configured filesystem rules have a `best_effort` compatibility mode that can let the sandbox start without those rules and emit a finding. The writer should distinguish these layers and recommend checking runtime evidence or using hard requirement for the relevant policy.
- **Hardware scope:** NVIDIA and press coverage present OpenShell alongside the broader Open Agent Safety Platform and Sentry on BlueField-4. The tagged 0.1.0 release and installation docs describe a software runtime with Docker, Podman and MicroVM backends and Linux/macOS host virtualization requirements. Sentry is a separate platform component; do not imply that BlueField-4 is required to run OpenShell 0.1.0.
- **Read-only semantics:** An enforced `read-only` preset blocks HTTP methods outside GET/HEAD/OPTIONS, but NVIDIA explicitly cautions that method filtering cannot guarantee an upstream GET has no side effects. Describe it as method-level control, not proof of a semantically read-only API or credential-level read permission.

## Numbers

Figure: `v0.1.0` release timestamp: September 25, 2026 (GitHub release record).
Owner:  NVIDIA OpenShell GitHub Releases, release entry for v0.1.0.
Scope: The tag’s published release timestamp, not the September 28 NVIDIA GA announcement.

Figure: GA announcement date: September 28, 2026.
Owner:  NVIDIA developer blog; independently corroborated as the launch date by Reuters.
Scope: Announcement/public launch date, distinct from the GitHub tag timestamp.

Figure: Docker Desktop / Engine 28.0 or later; Podman 5.x and cgroups v2; glibc 2.28 or newer for Linux packages.
Owner:  NVIDIA OpenShell v0.1.0 Installation docs.
Scope: Host/runtime and package prerequisites; these are not evidence of security efficacy.

Figure: Mandatory Landlock ABI v3; upstream Linux 6.2 provides ABI v3.
Owner:  OpenShell v0.1.0 source `architecture/sandbox.md` for the mandatory ABI; Linux kernel Landlock documentation for ABI semantics. ABI-to-upstream-kernel mapping should be verified against the release documentation before including the Linux version in article prose.
Scope: Mandatory `/.openshell` self-protection baseline, even if optional filesystem rules use `best_effort`.

## Limits

- No independent adversarial evaluation, penetration test, false-positive/negative rate, or security outcome study of OpenShell 0.1.0 was found. Do not infer these from a vendor demo or source architecture.
- The named Cadence, Slack and Gecko Robotics implementation claims come from NVIDIA. OpenClaw’s own maintained backend documentation independently establishes a concrete integration, but does not verify those organizations’ deployment depth or broad adoption.
- The example can show that a file path is configured read-only and that an enforced REST rule allows selected methods and denies another. It cannot show that an upstream GET is side-effect-free, that the API token itself is read-only, or that an agent cannot influence data through an allowed read endpoint.
- Kernel Landlock and seccomp behavior does not by itself establish containment against host compromise, kernel/runtime vulnerabilities, operator mistakes, or a malicious/overbroad policy. Present the controls as reducing specified authority under the configured boundary, not as proving safe agent behavior.
- Credential isolation is policy- and protocol-dependent. 0.1.0’s source notes that credentialed L4-only or TLS-skipped endpoints are rejected unless an explicit escape hatch is enabled; do not claim credentials are kept outside the workload for every arbitrary protocol.
- OpenShell does not establish model honesty, correctness, benign intent, or whether a policy grants enough authority to complete a task. AP reports NVIDIA’s claim and an outside expert’s call for case studies.
- Log retention defaults do not constitute durable audit preservation. The Gateway buffer is bounded and volatile; source-level summary aggregation can omit individual event detail. A durable audit story depends on configured export and external retention.
- The versioned docs and source establish local Docker/Podman/VM paths and Kubernetes support. No evidence located here establishes production scale, comparative security, or commercial adoption volume.

## Illustrative request trace (not executed)

This is an example for the writer to explain, not a test I ran. Replace the sample repository and verify the actual executable path inside the chosen image. The explicit GET rule is narrower than the documented `read-only` preset, which also permits HEAD and OPTIONS.

```yaml
version: 1
filesystem_policy:
  include_workdir: false
  read_only:
    - /workspace/project
  read_write: []
network_policies:
  github_issues:
    endpoints:
      - host: api.github.com
        port: 443
        protocol: rest
        enforcement: enforce
        rules:
          - allow:
              method: GET
              path: /repos/acme/widget/issues
    binaries:
      - path: /usr/bin/curl
```

1. The Gateway stores/delivers the sandbox policy and the compute driver constructs the workload boundary. A global policy or attached provider can affect the effective policy, so inspect the effective policy before drawing conclusions.
2. The agent reads `/workspace/project/README.md`. Landlock applies the configured read-only path rights at sandbox startup. A write to that path is denied by the kernel policy; other paths not granted by the effective policy are inaccessible, subject to OpenShell’s runtime baseline paths.
3. The agent invokes `/usr/bin/curl` for `GET https://api.github.com/repos/acme/widget/issues?per_page=5`. The sandbox mediates DNS/TCP through the protected Supervisor channel, and the outer fence blocks direct workload egress. The Supervisor checks the calling binary and destination against policy, then its REST inspection checks the method/path before opening/relaying the upstream request. This public endpoint example needs no API key.
4. A `POST` to that same endpoint has no matching allow rule, so enforced REST policy denies it before upstream forwarding. The client receives `policy_denied`. Network/HTTP OCSF events can record the connection/request decision; the operator should export logs if durable retention is required.

The component allocation and policy syntax come from the versioned architecture, policy overview, and network-rule tutorial (Sources 2–5); the code path is confirmed by the tag-pinned sandbox/OPA/Rego sources (Sources 7–12). The log/retention qualification is from Source 15. Do not present the expected trace as observed output or claim that GET is semantically side-effect-free.

## Source assets

Asset: NVIDIA OpenShell v0.1.0 Architecture page, Figure 1 (architecture overview at the top of the page).
Shows: Gateway/control-plane responsibilities, separate Supervisor and sandbox workload, and the protected channel / network boundary.
Crop: Keep component labels and arrows showing which side owns policy and which side runs the agent; omit unrelated page chrome.

Asset: NVIDIA technical blog, Figure 1 and Figure 2 (lines 71–72 and 125–126).
Shows: The vendor’s agent-fleet and credential-substitution illustrations. Figure 2 specifically depicts a placeholder crossing from workload to Supervisor, with the real credential substituted outside it.
Crop: Keep the full request path and the labeled boundary; attribute the figure to NVIDIA and pair it with source/code limits.

Asset: GitHub release page, v0.1.0 entry (lines 423–457).
Shows: Tag, commit and release date; useful as a compact chronology graphic only if the September 25 tag and September 28 announcement are separately labeled.
Crop: Retain the v0.1.0 label, commit hash, date and nearby later release dates if used to clarify chronology.

Asset: NVIDIA OpenShell v0.1.0 Sandbox Policies page.
Shows: None found beyond the policy-category table; use the table as a simple text/HTML table if helpful.
Crop: Not applicable.

Asset: NVIDIA OpenShell v0.1.0 Network Rules page.
Shows: None found; its YAML and method/path examples are more useful as a code listing than as an image.
Crop: Not applicable.

Asset: NVIDIA OpenShell v0.1.0 installation page.
Shows: None found; runtime requirements are a table.
Crop: Not applicable.

Asset: Tagged source files `architecture/sandbox.md`, `architecture/security-policy.md`, `crates/openshell-sandbox/src/sandbox/linux/landlock.rs`, `.../seccomp.rs`, `crates/openshell-supervisor-network/src/opa.rs`, and `.../data/sandbox-policy.rego`.
Shows: None found; these are source text/code.
Crop: Not applicable.

Asset: Linux kernel Landlock docs and Linux seccomp_unotify manual.
Shows: None found; technical documentation is textual.
Crop: Not applicable.

Asset: OpenClaw OpenShell integration docs.
Shows: None found; integration configuration and lifecycle examples are code/text.
Crop: Not applicable.

Asset: AP and Reuters reports.
Shows: None found.
Crop: Not applicable.

## Discarded

URL: https://github.com/NVIDIA/OpenShell/blob/main/architecture/sandbox.md — The rolling `main` documentation contains newer design and implementation changes. I used the tag-pinned v0.1.0 source for release claims; do not cite `main` as evidence of the 0.1.0 implementation.

URL: https://github.com/NVIDIA/OpenShell/tree/v0.1.0 — Browser search could not open the GitHub tag tree due robots restrictions. The tag itself was resolved and source files were inspected locally at commit `496ebba293f5cc2bb2753444dddd534f0b4aeb6a`; cite direct, tag-pinned file URLs above, not this tree URL.

URL: https://www.npmjs.com/package/%40openclaw/openshell-sandbox?activeTab=dependencies — Search result suggested a package listing, but the page returned HTTP 403 on open. Not used for package metadata or adoption claims; OpenClaw’s own documentation was opened instead.

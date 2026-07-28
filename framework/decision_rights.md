# Data Governance Decision Rights Framework

## 1. Purpose

This document defines how Data Governance decisions are allocated across HelvetiaCare Insurance Group.

The framework ensures that:

- Decisions are made by the appropriate authority
- Accountability is clearly assigned
- Operational matters are resolved efficiently
- Material risks receive appropriate oversight
- Cross-domain conflicts are escalated consistently
- Decisions remain documented and auditable

The framework supports the Enterprise Data Governance Charter and Operating Model.

---

## 2. Decision Rights Principles

### 2.1 Decisions remain with the business

Business Data Owners retain accountability for the meaning, quality, permitted use and risk profile of data within their domains.

Technology teams implement approved requirements but do not determine business accountability.

### 2.2 Decisions are made at the lowest appropriate level

Operational matters should be resolved within the relevant data domain where:

- The decision affects one domain
- Enterprise standards remain satisfied
- Risk remains within delegated authority
- No cross-domain conflict exists

### 2.3 Material matters require broader oversight

Decisions must be escalated where they:

- Affect multiple data domains
- Create material customer, financial or regulatory risk
- Require an exception to enterprise standards
- Exceed delegated authority
- Require significant investment
- Create unresolved ownership or definition conflicts

### 2.4 Accountability cannot be delegated away

Activities may be assigned to Data Stewards, Data Custodians or delivery teams, but the Data Owner remains accountable for approved domain decisions.

### 2.5 Decisions must be traceable

Material decisions must include:

- Decision identifier
- Date
- Decision-maker
- Participants
- Data domain
- Decision requested
- Alternatives considered
- Decision rationale
- Conditions or limitations
- Required actions
- Review or expiry date
- Supporting evidence

---

## 3. Decision Roles

### Chief Data Officer

The Chief Data Officer:

- Sponsors enterprise Data Governance
- Chairs or appoints the chair of the Data Governance Council
- Resolves matters within delegated executive authority
- Escalates material enterprise risks
- Approves governance priorities and implementation direction
- Ensures alignment with the Data and AI strategy

### Data Governance Council

The Data Governance Council:

- Approves enterprise governance standards
- Resolves cross-domain matters
- Confirms enterprise ownership decisions
- Approves material governance exceptions
- Prioritises major remediation initiatives
- Reviews governance performance
- Escalates matters beyond its authority

### Data Owner

The Data Owner:

- Approves domain business definitions
- Approves critical data elements
- Sets data-quality expectations
- Approves domain remediation priorities
- Accepts residual risk within delegated authority
- Approves domain-specific governance decisions
- Escalates material or cross-domain matters

### Data Steward

The Data Steward:

- Prepares decision proposals
- Maintains governance records
- Coordinates stakeholder review
- Assesses operational data issues
- Recommends remediation actions
- Escalates matters to the Data Owner
- Records approved decisions and evidence

### Data Custodian

The Data Custodian:

- Assesses technical feasibility
- Implements approved technical controls
- Provides system and control evidence
- Identifies technical risks and dependencies
- Escalates implementation constraints
- Does not approve business meaning or data usage

### Control and Advisory Functions

Control and advisory functions:

- Provide specialist advice
- Review matters within their mandates
- Challenge material risk decisions
- Recommend conditions or controls
- Escalate concerns independently where required

---

## 4. Decision Categories

The following categories define the main Data Governance decisions.

### 4.1 Data ownership decisions

These decisions determine:

- Which domain owns a data asset
- Which senior role acts as Data Owner
- Which Data Steward supports the domain
- How shared data responsibilities are divided
- Which domain leads cross-domain coordination

### 4.2 Business-definition decisions

These decisions determine:

- Approved business terminology
- Standard definitions
- Permitted synonyms
- Definition ownership
- Definition status
- Definition retirement or replacement

### 4.3 Critical data-element decisions

These decisions determine:

- Which data elements are considered critical
- Why they are critical
- Which quality rules apply
- Which controls are required
- Which owner and steward are assigned

### 4.4 Data-quality decisions

These decisions determine:

- Relevant quality dimensions
- Measurement methods
- Quality thresholds
- Monitoring frequency
- Remediation priorities
- Acceptance of temporary quality limitations

### 4.5 Data-classification decisions

These decisions determine:

- Data sensitivity
- Required protection level
- Access restrictions
- Handling requirements
- Sharing conditions
- Retention and disposal expectations

### 4.6 Data-access decisions

These decisions determine:

- Whether access is justified
- Which role or team requires access
- Which data may be accessed
- The permitted purpose
- Duration of access
- Review frequency
- Additional controls

### 4.7 Data-issue decisions

These decisions determine:

- Issue severity
- Business impact
- Responsible remediation owner
- Target resolution date
- Escalation level
- Closure criteria
- Residual risk acceptance

### 4.8 Governance-exception decisions

These decisions determine:

- Whether a temporary exception is justified
- Which requirement is affected
- Which risks arise
- Which compensating controls are required
- Who approves the exception
- When the exception expires
- How the exception will be remediated

### 4.9 AI data-readiness decisions

These decisions determine:

- Whether data is sufficiently governed for an AI use case
- Whether quality is adequate for the intended purpose
- Whether sensitive data usage is permitted
- Whether ownership and lineage are clear
- Whether additional controls are required
- Whether the use case may proceed

---

## 5. Decision Authority Matrix

| Decision | Recommend | Approve | Consulted | Informed |
|---|---|---|---|---|
| Assign a Data Owner | Chief Data Office | Data Governance Council | Business leadership, Human Resources | Relevant domain stakeholders |
| Assign a Data Steward | Data Owner | Data Owner | Chief Data Office, business management | Relevant domain stakeholders |
| Approve a domain business definition | Data Steward | Data Owner | Subject-matter experts, Architecture | Data consumers |
| Resolve a cross-domain definition conflict | Relevant Data Stewards | Data Governance Council | Data Owners, Architecture, Compliance | Affected data consumers |
| Identify a critical data element | Data Steward | Data Owner | Data Custodian, Risk, Compliance | Domain Governance Forum |
| Approve a data-quality rule | Data Steward | Data Owner | Data Custodian, business experts | Data consumers |
| Change an enterprise quality threshold | Chief Data Office | Data Governance Council | Data Owners, Risk, Compliance | Affected domains |
| Classify a data asset | Data Steward | Data Owner | Data Protection, Information Security | Data Custodian |
| Approve standard data access | Line manager or process owner | Data Owner or delegated authority | Data Protection, Information Security when required | Data Custodian |
| Approve privileged or sensitive access | Business sponsor | Data Owner | Information Security, Data Protection | Data Custodian |
| Assign issue severity | Data Steward | Data Owner for high-severity issues | Data Custodian, control functions | Domain Governance Forum |
| Approve remediation action | Data Steward | Data Owner | Data Custodian, delivery teams | Chief Data Office |
| Close a material data issue | Data Steward | Data Owner | Control functions where required | Data Governance Council |
| Accept residual domain risk | Data Owner | Data Owner within delegated authority | Risk, Compliance, Data Protection | Chief Data Office |
| Accept material enterprise risk | Data Governance Council | Executive Management | Risk, Compliance, Legal | Affected stakeholders |
| Approve a governance exception | Data Steward or process owner | Data Owner for low-risk exceptions | Relevant control functions | Chief Data Office |
| Approve a material governance exception | Data Owner | Data Governance Council | Risk, Compliance, Security, Data Protection | Executive Management where required |
| Approve AI data readiness | AI use-case owner | Data Owner | Data and AI Centre of Excellence, Data Protection, Security | Data Governance Council |
| Approve an enterprise governance standard | Chief Data Office | Data Governance Council | Data Owners, control functions, Architecture | Enterprise stakeholders |

---

## 6. Delegated Authority

Data Owners may delegate specific operational approvals where:

- The delegation is documented
- The delegate has sufficient expertise
- The scope is clearly defined
- Material risk acceptance remains with the Data Owner
- The delegation has a review date
- Evidence of decisions is retained

The following decisions must not be delegated below the Data Owner:

- Approval of critical data elements
- Acceptance of material domain risk
- Approval of material business definitions
- Approval of significant governance exceptions
- Closure of high-severity issues
- Approval of domain quality thresholds with material impact

---

## 7. Decision Thresholds

### Operational decision

An operational decision:

- Affects one process or system
- Has limited business impact
- Remains within approved standards
- Does not involve sensitive risk acceptance
- Can be resolved by the Data Steward or delegated authority

### Domain decision

A domain decision:

- Affects one enterprise data domain
- Requires Data Owner approval
- May affect several systems or processes
- Remains within enterprise standards
- Does not create material cross-domain risk

### Enterprise decision

An enterprise decision:

- Affects multiple domains
- Changes an enterprise standard
- Requires cross-functional prioritisation
- Creates material governance implications
- Requires Data Governance Council approval

### Executive decision

An executive decision:

- Exceeds Council authority
- Requires significant funding
- Creates material regulatory or customer impact
- Requires enterprise-level risk acceptance
- Could affect organisational strategy or reputation

---

## 8. Decision Escalation Triggers

A matter must be escalated when:

- No accountable owner can be identified
- Two Data Owners claim or reject ownership
- Business definitions conflict across domains
- A quality issue exceeds approved thresholds
- A high-severity issue is overdue
- A required control cannot be implemented
- A governance exception exceeds local authority
- Sensitive data is proposed for a new purpose
- A material AI use case lacks sufficient data governance
- Regulatory, customer or financial reporting may be affected
- The decision requires significant funding or resources

---

## 9. Decision-Making Process

Each material Data Governance decision follows the process below.

### Step 1 — Initiate

The requester identifies:

- Decision required
- Relevant data domain
- Business context
- Required timeline
- Affected stakeholders

### Step 2 — Assess

The Data Steward coordinates assessment of:

- Business impact
- Data impact
- Risk
- Regulatory implications
- Technical feasibility
- Dependencies
- Available options

### Step 3 — Consult

Relevant stakeholders review the proposal.

These may include:

- Data Owner
- Data Custodian
- Data Protection
- Compliance
- Information Security
- Risk Management
- Data Architecture
- Business subject-matter experts
- Data and AI Centre of Excellence

### Step 4 — Recommend

The responsible role documents:

- Recommended decision
- Alternatives considered
- Supporting rationale
- Risks
- Required controls
- Proposed actions

### Step 5 — Approve

The designated authority:

- Approves
- Rejects
- Requests further analysis
- Approves subject to conditions
- Escalates the matter

### Step 6 — Record

The decision is entered into the governance decision log.

### Step 7 — Implement

Assigned owners implement the approved actions.

### Step 8 — Verify

The Data Steward confirms that:

- Actions were completed
- Conditions were satisfied
- Required evidence exists
- Remaining risks are documented

### Step 9 — Close or review

The decision is closed or scheduled for periodic review.

---

## 10. Decision Record Template

Each material decision must contain the following information:

| Field | Description |
|---|---|
| Decision ID | Unique identifier |
| Decision title | Concise description |
| Date raised | Date the decision was requested |
| Decision deadline | Required decision date |
| Data domain | Relevant domain or domains |
| Requester | Person or role raising the matter |
| Decision authority | Role or governance body responsible |
| Decision requested | Clear statement of the required decision |
| Business context | Reason the decision is required |
| Options considered | Available alternatives |
| Risk assessment | Main risks associated with each option |
| Consultation | Stakeholders consulted |
| Recommendation | Proposed outcome |
| Final decision | Approved decision |
| Decision rationale | Reason for the decision |
| Conditions | Requirements attached to approval |
| Actions | Follow-up actions |
| Action owners | Accountable persons or roles |
| Target dates | Completion deadlines |
| Review date | Date the decision must be reconsidered |
| Evidence | Supporting documents or records |
| Status | Open, approved, rejected, implemented or closed |

---

## 11. Decision Statuses

Governance decisions use the following statuses:

- Draft
- Under assessment
- Consultation in progress
- Awaiting approval
- Approved
- Approved with conditions
- Rejected
- Escalated
- Implementation in progress
- Implemented
- Closed
- Superseded
- Expired

---

## 12. Decision Review

A governance decision must be reviewed when:

- Its review date is reached
- An associated exception expires
- Business circumstances materially change
- New regulatory requirements apply
- A control proves ineffective
- A material incident occurs
- The underlying data use changes
- A new system or process replaces the existing arrangement

The review outcome must be documented.

---

## 13. Decision Evidence and Auditability

Decision evidence must be:

- Complete
- Accurate
- Dated
- Attributable to an authorised decision-maker
- Protected from unauthorised alteration
- Retained according to applicable requirements
- Accessible for governance review and audit

Material verbal decisions must be documented after the meeting or discussion in which they were made.

---

## 14. Performance Indicators

The effectiveness of decision-making may be measured through:

- Percentage of decisions completed within target
- Number of overdue decisions
- Number of decisions escalated
- Number of decisions returned for insufficient evidence
- Average decision cycle time
- Number of expired exceptions
- Number of decisions without assigned actions
- Percentage of actions completed within target
- Number of repeated issues following previous decisions

---

## 15. Document Control

| Field | Value |
|---|---|
| Document owner | Chief Data Office |
| Approval body | Data Governance Council |
| Version | 1.0 |
| Status | Illustrative portfolio version |
| Review frequency | Annual |
| Next review | To be determined |

---

This document forms part of a fictional portfolio project and does not represent the decision framework of a real insurance organisation.
# Enterprise Data Governance Operating Model

## 1. Purpose

This document defines how Data Governance is organised and operated across HelvetiaCare Insurance Group.

The operating model establishes:

- Governance bodies
- Roles and responsibilities
- Reporting relationships
- Decision and escalation paths
- Domain-level governance
- Interaction with control and technology functions
- Governance meeting cadence
- Required governance outputs

The objective is to ensure that governance responsibilities are embedded in business operations rather than managed solely as a central policy function.

---

## 2. Operating Model Design

HelvetiaCare uses a federated Data Governance model.

Under this model:

- The Chief Data Office defines the enterprise framework.
- Business functions retain accountability for their data.
- Data Stewards coordinate governance within each domain.
- Data Custodians implement technical controls.
- Control functions provide independent advice and challenge.
- The Data Governance Council resolves enterprise and cross-domain matters.
- The Data and AI Centre of Excellence supports implementation, tooling and responsible innovation.

This model combines central consistency with decentralised business ownership.

---

## 3. Governance Structure

The governance structure contains five levels.

### Level 1 — Executive Sponsorship

The Chief Data Officer acts as executive sponsor for enterprise Data Governance.

The Chief Data Officer:

- Sets the strategic direction
- Promotes executive support
- Ensures alignment with Data and AI strategy
- Secures resources
- Escalates material risks
- Sponsors governance maturity improvements

The Chief Data Officer reports material governance matters to executive management.

### Level 2 — Data Governance Council

The Data Governance Council is the principal enterprise decision body.

The Council includes representatives from:

- Chief Data Office
- Customer domain
- Policy domain
- Claims domain
- Healthcare Provider domain
- Finance domain
- Data Architecture
- Data and AI Centre of Excellence
- Data Protection
- Compliance
- Information Security
- Risk Management
- Technology
- Internal Control functions

The Council is chaired by the Chief Data Officer or an appointed delegate.

### Level 3 — Data Domain Governance

Each enterprise data domain has:

- One accountable Data Owner
- At least one operational Data Steward
- Relevant Data Custodians
- Domain subject-matter experts
- Representatives from dependent business functions

Domain governance is responsible for the practical application of enterprise standards.

### Level 4 — Control and Enablement Functions

Specialist functions support governance implementation and provide challenge.

These include:

- Data Protection
- Compliance
- Information Security
- Enterprise Architecture
- Data Architecture
- Risk Management
- Internal Audit
- Legal
- Data and AI Centre of Excellence

These functions advise on requirements within their area of expertise.

They do not replace the accountability of Data Owners.

### Level 5 — Delivery and Operations

Business and technology teams apply governance requirements in daily work.

This includes:

- Business operations
- Product teams
- Application teams
- Data engineering teams
- Analytics teams
- Artificial intelligence teams
- External service providers
- Agile Release Train stakeholders

These teams create, process, transform and use governed data.

---

## 4. Governance Structure Diagram

```mermaid
flowchart TD
    A[Executive Management] --> B[Chief Data Officer]

    B --> C[Data Governance Council]
    B --> D[Data and AI Centre of Excellence]

    C --> E[Customer Data Owner]
    C --> F[Policy Data Owner]
    C --> G[Claims Data Owner]
    C --> H[Provider Data Owner]
    C --> I[Finance Data Owner]

    E --> E1[Customer Data Steward]
    F --> F1[Policy Data Steward]
    G --> G1[Claims Data Steward]
    H --> H1[Provider Data Steward]
    I --> I1[Finance Data Steward]

    E1 --> J[Data Custodians and Delivery Teams]
    F1 --> J
    G1 --> J
    H1 --> J
    I1 --> J

    K[Data Protection] --> C
    L[Compliance] --> C
    M[Information Security] --> C
    N[Data Architecture] --> C
    O[Risk Management] --> C

    D --> J

## 5. Core Governance Bodies

### 5.1 Data Governance Council

#### Mandate

The Data Governance Council ensures consistent enterprise governance and resolves matters that cannot be addressed within a single data domain.

#### Responsibilities

The Data Governance Council:

- Approves enterprise Data Governance policies and standards
- Confirms Data Owner appointments
- Reviews governance KPIs and performance indicators
- Reviews Data Governance maturity-assessment results
- Resolves cross-domain definition and ownership conflicts
- Prioritises material remediation initiatives
- Approves high-risk governance exceptions
- Reviews overdue high-severity data issues
- Sponsors governance education and adoption
- Escalates material risks to executive management

#### Meeting cadence

The Data Governance Council meets monthly.

Additional meetings may be scheduled when urgent decisions, material incidents or significant cross-domain issues require attention.

#### Required outputs

Each meeting produces:

- Approved governance decisions
- Assigned actions and accountable owners
- Escalation records
- Exception decisions
- Updated remediation priorities
- Meeting minutes
- Evidence for the governance audit trail

---

### 5.2 Domain Governance Forums

Each enterprise data domain maintains a Domain Governance Forum.

#### Participants

A Domain Governance Forum normally includes:

- Data Owner
- Data Steward
- Relevant Data Custodians
- Business subject-matter experts
- Data Architecture representative
- Technology representative
- Control-function representatives when required

#### Responsibilities

Each Domain Governance Forum:

- Reviews domain data-quality performance
- Approves or recommends business definitions
- Reviews critical data elements
- Monitors open data issues
- Coordinates remediation activities
- Reviews access and appropriate-use concerns
- Assesses proposed business or system changes
- Prepares matters for escalation to the Data Governance Council

#### Meeting cadence

Domain Governance Forums meet at least monthly.

Domains with higher risk, greater operational activity or significant remediation programmes may meet more frequently.

#### Required outputs

Each forum produces:

- Updated domain issue register
- Data-quality review results
- Approved or proposed business definitions
- Remediation decisions
- Escalation requests
- Assigned actions
- Meeting records

---

### 5.3 Data Steward Community

The Data Steward Community promotes consistency and knowledge sharing across enterprise data domains.

#### Responsibilities

The Data Steward Community:

- Shares Data Governance good practices
- Aligns stewardship processes
- Reviews metadata conventions
- Discusses recurring data-quality issues
- Coordinates cross-domain definitions
- Identifies training and coaching requirements
- Proposes improvements to governance processes and tooling
- Supports consistent application of enterprise standards

#### Meeting cadence

The Data Steward Community meets every six weeks.

#### Required outputs

The community produces:

- Stewardship guidance
- Proposed process improvements
- Metadata recommendations
- Training requirements
- Cross-domain coordination actions

---

### 5.4 Data and AI Centre of Excellence

The Data and AI Centre of Excellence supports the practical implementation of Data Governance, analytics and responsible artificial intelligence.

#### Responsibilities

The Data and AI Centre of Excellence provides:

- Governance methods and templates
- Data-quality tooling
- Metadata and data-catalogue support
- Workflow automation
- AI data-readiness assessments
- Training and coaching
- Analytics and AI governance support
- Technical implementation guidance
- Reusable control patterns
- Support for governance reporting and measurement

The Data and AI Centre of Excellence does not assume ownership of business data.

Business accountability remains with the relevant Data Owners.

---

### 5.5 Control and Advisory Functions

Control and advisory functions provide specialist expertise, review and challenge.

These functions include:

- Data Protection
- Compliance
- Information Security
- Risk Management
- Legal
- Enterprise Architecture
- Data Architecture
- Internal Control
- Internal Audit

#### Responsibilities

Control and advisory functions:

- Interpret requirements within their areas of expertise
- Review proposed governance controls
- Challenge material risk assessments
- Support incident and issue assessment
- Participate in exception reviews
- Advise on regulatory and control implications
- Escalate matters within their mandates

These functions do not replace the accountability of Data Owners.

---

## 6. Role Interaction Model

### 6.1 Data Owner

The Data Owner is a senior business representative accountable for data within an assigned domain.

The Data Owner is accountable for:

- Business meaning
- Data criticality
- Data-quality expectations
- Permitted data usage
- Risk acceptance
- Remediation sponsorship
- Domain-level governance performance
- Approval of critical data elements
- Approval of material business definitions
- Escalation of unresolved domain risks

The Data Owner approves material decisions affecting the assigned data domain.

---

### 6.2 Data Steward

The Data Steward coordinates the operational implementation of Data Governance within an assigned domain.

The Data Steward is responsible for:

- Maintaining business definitions
- Coordinating metadata
- Monitoring data-quality indicators
- Recording and assessing data issues
- Coordinating remediation activities
- Preparing governance reporting
- Supporting business and technology change initiatives
- Facilitating Domain Governance Forums
- Escalating overdue or material risks
- Maintaining governance evidence

The Data Steward is the primary operational coordination point for the domain.

---

### 6.3 Data Custodian

The Data Custodian implements and operates technical controls for systems, platforms and data assets.

The Data Custodian is responsible for:

- Technical data storage
- Data processing
- System configuration
- Access-control implementation
- Automated validation controls
- Technical metadata
- Data integration
- Backup and recovery
- Data transfer controls
- Control-execution evidence
- Technical remediation activities

The Data Custodian implements approved business and governance requirements.

The Data Custodian does not determine the business meaning or permitted business use of data.

---

### 6.4 Control Functions

Control functions are responsible for:

- Providing specialist advice
- Reviewing proposed controls
- Challenging material risk decisions
- Supporting incident assessment
- Participating in exception reviews
- Monitoring compliance within their mandates
- Escalating material concerns

Control functions provide independent challenge but do not assume business ownership of data.

---

### 6.5 Data Consumers

Data consumers include employees, analysts, reporting teams, automation teams and AI teams that use enterprise data.

Data consumers are responsible for:

- Using approved data sources
- Understanding relevant data limitations
- Applying access and usage requirements
- Reporting identified data issues
- Avoiding unauthorised reuse or disclosure
- Following governance requirements for analytics and AI
- Retaining appropriate evidence of material data usage
- Using data only for approved business purposes

---

## 7. Decision Flow

Governance decisions must be made at the lowest appropriate level of authority.

### 7.1 Domain-level decisions

A matter remains at domain level when:

- It affects only one data domain
- It does not create material enterprise risk
- It remains consistent with approved enterprise standards
- The Data Owner possesses sufficient authority
- It does not create a conflict with another domain
- It does not require a material governance exception

Examples include:

- Approval of a domain-specific business definition
- Approval of a domain data-quality rule
- Assignment of a remediation action
- Confirmation of a critical data element
- Acceptance of a low-risk temporary issue

---

### 7.2 Data Governance Council decisions

A matter must be escalated to the Data Governance Council when:

- It affects multiple data domains
- Data ownership is disputed
- Business definitions conflict
- A material governance exception is requested
- The matter exceeds the Data Owner's delegated authority
- The matter creates significant regulatory, customer or financial risk
- Enterprise prioritisation or investment is required
- A high-severity issue remains unresolved
- An enterprise standard requires interpretation

Examples include:

- Resolving conflicting definitions between Customer and Policy data
- Approving a temporary exception to an enterprise standard
- Prioritising a cross-domain remediation programme
- Deciding ownership of shared enterprise data
- Approving an enterprise Data Governance KPI

---

### 7.3 Executive-level decisions

A matter must be escalated to executive management when:

- Risk exceeds the authority of the Data Governance Council
- Significant investment is required
- The issue affects enterprise strategy
- Regulatory notification may be required
- A material risk remains unresolved
- The matter could significantly affect customers or financial reporting
- Enterprise risk acceptance is required

---

## 8. Escalation Path

The following workflow illustrates the standard escalation path for a Data Governance issue.

```mermaid
flowchart TD
    A[Issue Identified] --> B[Data Steward Assessment]

    B --> C{Can the issue be resolved operationally?}

    C -->|Yes| D[Assign Remediation Action]
    D --> E[Validate Resolution]
    E --> F[Close Issue and Retain Evidence]

    C -->|No| G[Escalate to Data Owner]

    G --> H{Is domain-level authority sufficient?}

    H -->|Yes| I[Approve Remediation or Risk Decision]
    I --> E

    H -->|No| J[Escalate to Data Governance Council]

    J --> K{Is Council authority sufficient?}

    K -->|Yes| L[Record Council Decision]
    L --> E

    K -->|No| M[Escalate to Executive Management]
    M --> N[Record Executive Decision]
    N --> E
```

### Escalation evidence

Each escalation must record:

- Issue identifier
- Affected data domain
- Description of the issue
- Business and control impact
- Severity
- Current owner
- Reason for escalation
- Decision requested
- Decision taken
- Decision-maker
- Required actions
- Target completion date
- Supporting evidence

---

## 9. Governance Cadence

| Governance activity | Frequency | Primary owner |
|---|---|---|
| Data Governance Council | Monthly | Chief Data Officer |
| Domain Governance Forum | Monthly | Data Owner |
| Data Steward Community | Every six weeks | Chief Data Office |
| Governance KPI review | Monthly | Data Steward |
| High-severity issue review | Monthly or more frequently when required | Data Owner |
| Critical data-element review | Quarterly | Data Owner |
| Data-quality rule review | Quarterly | Data Steward |
| Data-access review | Quarterly or risk-based | Data Owner and Data Custodian |
| Governance exception review | Quarterly | Chief Data Office |
| Governance maturity assessment | Annual | Chief Data Office |
| Charter and standards review | Annual | Data Governance Council |
| AI data-readiness assessment | Before use-case approval | Data and AI Centre of Excellence |

---

## 10. Core Governance Processes

The operating model supports the following processes:

1. Data-domain onboarding
2. Data Owner and Data Steward appointment
3. Business-term approval
4. Critical data-element identification
5. Data classification
6. Data-quality rule approval
7. Data issue management
8. Governance exception management
9. Data-access review
10. AI use-case data assessment
11. Governance KPI reporting
12. Governance maturity assessment
13. Policy and standard review

Each governance process must define:

- Process trigger
- Scope
- Participants
- Responsible role
- Accountable decision-maker
- Decision authority
- Required evidence
- Target timeline
- Escalation route
- Audit record
- Closure criteria

---

## 11. Governance Information Flow

Governance information flows from operational teams to enterprise decision-makers.

```text
Operational data and control results
                ↓
          Data Custodian
                ↓
           Data Steward
                ↓
            Data Owner
                ↓
      Data Governance Council
                ↓
       Executive Management
```

### Information flowing upwards

Information flowing from operational teams towards governance bodies includes:

- Data-quality results
- Open data issues
- Remediation progress
- Governance exceptions
- Risk assessments
- KPI performance
- Maturity gaps
- Control failures
- Access-review results
- AI data-readiness findings

### Information flowing downwards

Information flowing from governance bodies towards operational teams includes:

- Approved standards
- Governance decisions
- Remediation priorities
- Risk tolerances
- Required controls
- Governance targets
- Approved business definitions
- Exception conditions
- Implementation guidance

---

## 12. Governance Deliverables

The operating model produces and maintains the following core artefacts:

- Data Governance Charter
- Governance principles
- Data-domain register
- Data ownership register
- Data Steward register
- Business glossary
- Critical data-element inventory
- Data classification records
- Data-quality rules
- Governance standards
- RACI matrix
- Data issue register
- Governance exception register
- Governance KPI dashboard
- Governance maturity assessment
- Meeting records
- Decision records
- Governance audit trail

Each artefact must have:

- A named owner
- A defined purpose
- Version control
- Review frequency
- Approval status
- Retention requirements where applicable

---

## 13. Success Criteria

The operating model is considered effective when:

- All enterprise data domains have approved ownership
- Critical data elements have assigned Data Stewards
- Governance decisions are made within defined timelines
- Business definitions are consistently used
- Data-quality requirements are measurable
- High-severity issues are escalated promptly
- Remediation actions have accountable owners
- Governance requirements are integrated into delivery processes
- Exceptions are documented, approved and time-limited
- Data and AI initiatives complete appropriate governance assessments
- Governance performance is reported regularly
- Governance maturity improves over time

---

## 14. Operating Model Boundaries

The operating model does not:

- Transfer business accountability to technology teams
- Replace Data Protection, Compliance or Information Security responsibilities
- Require every decision to be made centrally
- Eliminate the need for professional judgement
- Treat governance as a documentation-only activity
- Permit undocumented risk acceptance
- Guarantee that all data issues can be prevented
- Replace project, operational or technology governance
- Authorise data usage without an approved business purpose

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

This document forms part of a fictional portfolio project and does not represent the operating model of a real insurance organisation.
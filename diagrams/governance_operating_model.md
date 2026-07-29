# Enterprise Data Governance Operating Model

This diagram shows how HelvetiaCare Insurance Group translates enterprise data-governance policy into accountable domain-level execution, operational controls and executive oversight.

```mermaid
flowchart TB
    BOARD["Executive Committee<br/>Sets strategic direction and risk appetite"]

    COUNCIL["Data Governance Council<br/>Approves standards, priorities and escalations"]

    OFFICE["Data Governance Office<br/>Coordinates the operating model<br/>Maintains standards and reporting"]

    OWNERS["Data Owners<br/>Accountable for domain outcomes<br/>Approve access, quality and remediation decisions"]

    STEWARDS["Data Stewards<br/>Maintain definitions, controls and issue records<br/>Monitor data quality"]

    CUSTODIANS["Data Custodians<br/>Implement technical controls<br/>Operate platforms and data pipelines"]

    DOMAINS["Governed Data Domains<br/>Customer | Policy | Claims<br/>Healthcare Provider | Finance"]

    GLOSSARY["Business Glossary<br/>Definitions, ownership and criticality"]

    QUALITY["Data Quality Register<br/>Rules, thresholds and monitoring"]

    ISSUES["Governance Issues Register<br/>Root cause, remediation and escalation"]

    ACCESS["Access Exceptions Register<br/>Risk assessment and compensating controls"]

    AI["AI Use Case Register<br/>Readiness, risk tier and human oversight"]

    STANDARDS["Governance Standards<br/>Metadata | Quality | Classification<br/>Access | Issue Management | AI Readiness"]

    WORKFLOWS["Operational Workflows<br/>Glossary approval | Issue management<br/>Access exception | AI assessment"]

    REPORTING["Executive Governance Portal<br/>KPIs, exceptions, risks and decisions"]

    BOARD --> COUNCIL
    COUNCIL --> OFFICE

    OFFICE --> OWNERS
    OFFICE --> STANDARDS
    OFFICE --> WORKFLOWS

    OWNERS --> STEWARDS
    STEWARDS --> CUSTODIANS

    OWNERS --> DOMAINS
    STEWARDS --> DOMAINS
    CUSTODIANS --> DOMAINS

    DOMAINS --> GLOSSARY
    DOMAINS --> QUALITY
    DOMAINS --> ISSUES
    DOMAINS --> ACCESS
    DOMAINS --> AI

    STANDARDS --> GLOSSARY
    STANDARDS --> QUALITY
    STANDARDS --> ISSUES
    STANDARDS --> ACCESS
    STANDARDS --> AI

    WORKFLOWS --> GLOSSARY
    WORKFLOWS --> ISSUES
    WORKFLOWS --> ACCESS
    WORKFLOWS --> AI

    GLOSSARY --> REPORTING
    QUALITY --> REPORTING
    ISSUES --> REPORTING
    ACCESS --> REPORTING
    AI --> REPORTING

    REPORTING --> COUNCIL
```

## Accountability model

| Governance layer | Primary responsibility |
|---|---|
| Executive Committee | Sets strategic direction and enterprise risk appetite |
| Data Governance Council | Approves standards, resolves escalations and prioritises remediation |
| Data Governance Office | Coordinates the framework, reporting and governance processes |
| Data Owners | Remain accountable for data outcomes and material decisions |
| Data Stewards | Maintain definitions, controls, quality rules and issue records |
| Data Custodians | Implement and operate technical data controls |
| Governed domains | Apply governance requirements to business data assets |

> This operating model is fictional and uses synthetic portfolio data only.
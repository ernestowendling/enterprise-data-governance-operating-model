# Governance Portal Architecture

The portal separates governance content, validation controls and presentation logic. Source registers remain human-readable, while automated tests prevent malformed or inconsistent records from reaching the dashboard.

```mermaid
flowchart LR
    subgraph SOURCES["Governance Source Layer"]
        YAML["Domain Definitions<br/>5 YAML files"]
        CSV["Governance Registers<br/>Glossary | Quality | Issues<br/>Access | AI Use Cases"]
        MD["Controlled Documents<br/>Standards | Workflows<br/>Framework | Roles"]
    end

    subgraph CONTROLS["Validation and Control Layer"]
        SCHEMA["Schema Validation<br/>Required columns and fields"]
        STRUCTURE["CSV Structure Validation<br/>Exact field counts"]
        VALUES["Controlled-Value Validation<br/>Status, severity, domains and roles"]
        LINKS["Referential Validation<br/>Rules, issues and domain relationships"]
        TESTS["Pytest Control Suite<br/>Automated quality gate"]
    end

    subgraph APPLICATION["Application Layer"]
        LOADER["Cached File Loaders<br/>Pandas | PyYAML | pathlib"]
        FILTERS["Filtering and Search<br/>Domain, status, risk and text"]
        METRICS["Governance Metrics<br/>Coverage, open issues and readiness"]
        DETAILS["Record Drill-Down<br/>Ownership, controls and remediation"]
        DOCUMENTS["Markdown Renderer<br/>Standards and workflows"]
    end

    subgraph PORTAL["Streamlit Governance Portal"]
        OVERVIEW["Executive Overview"]
        DOMAINS["Data Domains"]
        GLOSSARY["Business Glossary"]
        QUALITY["Data Quality"]
        ISSUES["Governance Issues"]
        ACCESS["Access Exceptions"]
        AI["AI Use Cases"]
        LIBRARY["Standards & Workflows"]
    end

    subgraph USERS["Governance Stakeholders"]
        COUNCIL["Data Governance Council"]
        OWNERS["Data Owners"]
        STEWARDS["Data Stewards"]
        CUSTODIANS["Data Custodians"]
        AUDIT["Risk, Compliance and Audit"]
    end

    YAML --> SCHEMA
    CSV --> STRUCTURE
    CSV --> SCHEMA
    MD --> SCHEMA

    SCHEMA --> VALUES
    STRUCTURE --> VALUES
    VALUES --> LINKS
    LINKS --> TESTS

    TESTS -->|Pass| LOADER
    TESTS -->|Fail| BLOCK["Deployment Blocked<br/>Correction Required"]

    LOADER --> FILTERS
    LOADER --> METRICS
    LOADER --> DETAILS
    LOADER --> DOCUMENTS

    METRICS --> OVERVIEW
    DETAILS --> DOMAINS
    FILTERS --> GLOSSARY
    FILTERS --> QUALITY
    FILTERS --> ISSUES
    FILTERS --> ACCESS
    FILTERS --> AI
    DOCUMENTS --> LIBRARY

    OVERVIEW --> COUNCIL
    DOMAINS --> OWNERS
    GLOSSARY --> STEWARDS
    QUALITY --> STEWARDS
    ISSUES --> COUNCIL
    ACCESS --> OWNERS
    AI --> AUDIT
    LIBRARY --> CUSTODIANS
```

## Architectural principles

| Principle | Implementation |
|---|---|
| Separation of concerns | Governance definitions, validation rules and presentation logic are maintained separately |
| Human-readable governance assets | YAML, CSV and Markdown files can be reviewed without specialist software |
| Automated quality gate | Pytest validates structures, controlled values and relationships before release |
| No silent schema failure | Raw CSV rows are checked for missing or surplus fields |
| Traceable accountability | Registers connect decisions to Data Owners, Data Stewards and Data Custodians |
| Controlled AI readiness | AI use cases include risk tier, data readiness, human oversight and approval status |
| Synthetic portfolio environment | No real customer, patient, employee or insurer information is used |

> This architecture is an illustrative portfolio implementation for the fictional HelvetiaCare Insurance Group.
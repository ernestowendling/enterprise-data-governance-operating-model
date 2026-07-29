from pathlib import Path

import pandas as pd
import streamlit as st
import yaml

st.set_page_config(
    page_title="Enterprise Data Governance",
    page_icon="◆",
    layout="wide",
)


PROJECT_ROOT = Path(__file__).resolve().parent

DOMAINS_DIRECTORY = PROJECT_ROOT / "domains"
STANDARDS_DIRECTORY = PROJECT_ROOT / "standards"
WORKFLOWS_DIRECTORY = PROJECT_ROOT / "workflows"

GLOSSARY_FILE = PROJECT_ROOT / "glossary" / "business_glossary.csv"

DATA_QUALITY_RULES_FILE = PROJECT_ROOT / "data" / "data_quality_rules.csv"

GOVERNANCE_ISSUES_FILE = PROJECT_ROOT / "data" / "governance_issues.csv"

ACCESS_EXCEPTIONS_FILE = PROJECT_ROOT / "data" / "access_exceptions.csv"

AI_USE_CASES_FILE = PROJECT_ROOT / "data" / "ai_use_cases.csv"


@st.cache_data
def load_csv(file_path: Path) -> pd.DataFrame:
    """Load a governed CSV register."""

    if not file_path.exists():
        raise FileNotFoundError(f"Required file does not exist: {file_path}")

    return pd.read_csv(
        file_path,
        dtype=str,
    ).fillna("")


@st.cache_data
def load_domain_records() -> list[dict]:
    """Load all governed data-domain definitions."""

    if not DOMAINS_DIRECTORY.exists():
        raise FileNotFoundError("The domains directory does not exist.")

    domain_records = []

    for domain_file in sorted(DOMAINS_DIRECTORY.glob("*.yaml")):
        with domain_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            domain_record = yaml.safe_load(file)

        if not isinstance(domain_record, dict):
            raise ValueError(
                f"{domain_file.name} does not contain " "a valid YAML mapping."
            )

        domain_record["_source_file"] = domain_file.name
        domain_records.append(domain_record)

    return domain_records


def count_markdown_files(directory: Path) -> int:
    """Count Markdown governance artefacts."""

    if not directory.exists():
        return 0

    return len(list(directory.glob("*.md")))


def build_domain_coverage(
    glossary: pd.DataFrame,
    quality_rules: pd.DataFrame,
    issues: pd.DataFrame,
    access_exceptions: pd.DataFrame,
    ai_use_cases: pd.DataFrame,
) -> pd.DataFrame:
    """Build a domain-level governance coverage summary."""

    operational_domains = [
        "Customer",
        "Policy",
        "Claims",
        "Healthcare Provider",
        "Finance",
    ]

    rows = []

    for domain in operational_domains:
        glossary_count = int((glossary["data_domain"] == domain).sum())

        quality_rule_count = int((quality_rules["data_domain"] == domain).sum())

        issue_count = int(
            (
                (issues["primary_domain"] == domain)
                | (issues["additional_domains"] == domain)
            ).sum()
        )

        access_exception_count = int((access_exceptions["data_domain"] == domain).sum())

        ai_use_case_count = int(
            (
                (ai_use_cases["primary_domain"] == domain)
                | (ai_use_cases["additional_domains"] == domain)
            ).sum()
        )

        rows.append(
            {
                "Data Domain": domain,
                "Glossary Terms": glossary_count,
                "Quality Rules": quality_rule_count,
                "Governance Issues": issue_count,
                "Access Exceptions": access_exception_count,
                "AI Use Cases": ai_use_case_count,
            }
        )

    return pd.DataFrame(rows)


def get_domain_value(
    domain_record: dict,
    *possible_keys: str,
    default=None,
):
    """Return the first available domain field."""

    for key in possible_keys:
        if key in domain_record:
            return domain_record[key]

    return default


def convert_items_to_dataframe(
    items,
    default_column: str,
) -> pd.DataFrame:
    """Convert YAML list content into a displayable table."""

    if items is None:
        return pd.DataFrame()

    if not isinstance(items, list):
        items = [items]

    if not items:
        return pd.DataFrame()

    if all(isinstance(item, dict) for item in items):
        return pd.DataFrame(items).fillna("")

    return pd.DataFrame({default_column: [str(item) for item in items]})


def render_domain_table(
    title: str,
    items,
    default_column: str,
) -> None:
    """Render one structured domain-information table."""

    st.subheader(title)

    dataframe = convert_items_to_dataframe(
        items,
        default_column,
    )

    if dataframe.empty:
        st.caption("No information has been recorded.")
        return

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True,
    )


def render_domain_explorer() -> None:
    """Render the governed data-domain explorer."""

    domain_records = load_domain_records()

    if not domain_records:
        st.warning("No governed data domains were found.")
        return

    domain_lookup = {
        str(
            get_domain_value(
                record,
                "name",
                "domain_name",
                default=record["_source_file"],
            )
        ): record
        for record in domain_records
    }

    st.title("Data Domain Explorer")

    st.caption(
        "Review domain accountability, critical data "
        "elements, systems, risks, controls and KPIs."
    )

    selected_domain_name = st.selectbox(
        "Select a governed data domain",
        options=sorted(domain_lookup),
    )

    selected_domain = domain_lookup[selected_domain_name]

    domain_id = get_domain_value(
        selected_domain,
        "id",
        "domain_id",
        default="Not recorded",
    )

    description = get_domain_value(
        selected_domain,
        "description",
        default="No description recorded.",
    )

    data_owner = get_domain_value(
        selected_domain,
        "data_owner",
        "owner",
        default="Not assigned",
    )

    data_steward = get_domain_value(
        selected_domain,
        "data_steward",
        "steward",
        default="Not assigned",
    )

    business_purposes = get_domain_value(
        selected_domain,
        "business_purposes",
        "business_purpose",
        default=[],
    )

    data_custodians = get_domain_value(
        selected_domain,
        "data_custodians",
        "custodians",
        default=[],
    )

    systems = get_domain_value(
        selected_domain,
        "systems",
        "key_systems",
        default=[],
    )

    critical_data_elements = get_domain_value(
        selected_domain,
        "critical_data_elements",
        default=[],
    )

    risks = get_domain_value(
        selected_domain,
        "risks",
        "principal_risks",
        default=[],
    )

    controls = get_domain_value(
        selected_domain,
        "controls",
        "governance_controls",
        default=[],
    )

    kpis = get_domain_value(
        selected_domain,
        "kpis",
        "governance_kpis",
        default=[],
    )

    related_standards = get_domain_value(
        selected_domain,
        "related_standards",
        default=[],
    )

    st.divider()

    st.subheader(selected_domain_name)

    st.write(description)

    identity_columns = st.columns(3)

    identity_columns[0].metric(
        "Domain ID",
        str(domain_id),
    )

    identity_columns[1].metric(
        "Data Owner",
        str(data_owner),
    )

    identity_columns[2].metric(
        "Data Steward",
        str(data_steward),
    )

    coverage_columns = st.columns(4)

    coverage_columns[0].metric(
        "Critical Data Elements",
        len(
            critical_data_elements
            if isinstance(
                critical_data_elements,
                list,
            )
            else [critical_data_elements]
        ),
    )

    coverage_columns[1].metric(
        "Systems",
        len(systems if isinstance(systems, list) else [systems]),
    )

    coverage_columns[2].metric(
        "Governance Controls",
        len(controls if isinstance(controls, list) else [controls]),
    )

    coverage_columns[3].metric(
        "Governance KPIs",
        len(kpis if isinstance(kpis, list) else [kpis]),
    )

    st.caption("Source definition: " f"{selected_domain['_source_file']}")

    st.divider()

    left_column, right_column = st.columns(2)

    with left_column:
        render_domain_table(
            "Business Purposes",
            business_purposes,
            "Business Purpose",
        )

        render_domain_table(
            "Data Custodians",
            data_custodians,
            "Data Custodian",
        )

        render_domain_table(
            "Key Systems",
            systems,
            "System",
        )

        render_domain_table(
            "Related Standards",
            related_standards,
            "Standard",
        )

    with right_column:
        render_domain_table(
            "Critical Data Elements",
            critical_data_elements,
            "Critical Data Element",
        )

        render_domain_table(
            "Principal Risks",
            risks,
            "Risk",
        )

        render_domain_table(
            "Governance Controls",
            controls,
            "Control",
        )

        render_domain_table(
            "Governance KPIs",
            kpis,
            "KPI",
        )

    st.info(
        "All domain definitions shown in this application "
        "are fictional and created for portfolio purposes."
    )


def render_glossary_explorer() -> None:
    """Render the governed Business Glossary."""

    glossary = load_csv(GLOSSARY_FILE)

    st.title("Business Glossary")

    st.caption(
        "Explore approved business definitions, "
        "ownership, authoritative sources, "
        "classification and criticality."
    )

    st.divider()

    filter_columns = st.columns(4)

    domain_options = [
        "All",
        *sorted(glossary["data_domain"].dropna().unique().tolist()),
    ]

    sensitivity_options = [
        "All",
        *sorted(glossary["sensitivity"].dropna().unique().tolist()),
    ]

    status_options = [
        "All",
        *sorted(glossary["status"].dropna().unique().tolist()),
    ]

    criticality_options = [
        "All",
        "Yes",
        "No",
    ]

    selected_domain = filter_columns[0].selectbox(
        "Data domain",
        options=domain_options,
    )

    selected_sensitivity = filter_columns[1].selectbox(
        "Sensitivity",
        options=sensitivity_options,
    )

    selected_status = filter_columns[2].selectbox(
        "Status",
        options=status_options,
    )

    selected_criticality = filter_columns[3].selectbox(
        "Critical data element",
        options=criticality_options,
    )

    search_text = st.text_input(
        "Search business terms and definitions",
        placeholder=("Enter a term, definition, owner " "or authoritative source"),
    )

    filtered_glossary = glossary.copy()

    if selected_domain != "All":
        filtered_glossary = filtered_glossary[
            filtered_glossary["data_domain"] == selected_domain
        ]

    if selected_sensitivity != "All":
        filtered_glossary = filtered_glossary[
            filtered_glossary["sensitivity"] == selected_sensitivity
        ]

    if selected_status != "All":
        filtered_glossary = filtered_glossary[
            filtered_glossary["status"] == selected_status
        ]

    if selected_criticality != "All":
        filtered_glossary = filtered_glossary[
            filtered_glossary["critical_data_element"] == selected_criticality
        ]

    if search_text.strip():
        search_value = search_text.strip().casefold()

        searchable_columns = [
            "business_term",
            "definition",
            "data_owner",
            "data_steward",
            "authoritative_source",
            "related_terms",
        ]

        search_mask = pd.Series(
            False,
            index=filtered_glossary.index,
        )

        for column in searchable_columns:
            search_mask = search_mask | filtered_glossary[
                column
            ].str.casefold().str.contains(
                search_value,
                regex=False,
                na=False,
            )

        filtered_glossary = filtered_glossary[search_mask]

    filtered_glossary = filtered_glossary.sort_values(
        by=[
            "data_domain",
            "business_term",
        ]
    ).reset_index(drop=True)

    st.divider()

    metric_columns = st.columns(4)

    metric_columns[0].metric(
        "Displayed Terms",
        len(filtered_glossary),
    )

    metric_columns[1].metric(
        "Represented Domains",
        filtered_glossary["data_domain"].nunique(),
    )

    metric_columns[2].metric(
        "Critical Data Elements",
        int((filtered_glossary["critical_data_element"] == "Yes").sum()),
    )

    metric_columns[3].metric(
        "Approved Terms",
        int((filtered_glossary["status"] == "Approved").sum()),
    )

    st.subheader("Glossary Register")

    display_columns = [
        "term_id",
        "business_term",
        "definition",
        "data_domain",
        "data_owner",
        "sensitivity",
        "critical_data_element",
        "status",
    ]

    st.dataframe(
        filtered_glossary[display_columns],
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("Business Term Detail")

    if filtered_glossary.empty:
        st.warning("No glossary terms match the selected filters.")

        return

    selected_term = st.selectbox(
        "Select a business term",
        options=filtered_glossary["business_term"].tolist(),
    )

    selected_record = filtered_glossary[
        filtered_glossary["business_term"] == selected_term
    ].iloc[0]

    st.markdown(f"### {selected_record['business_term']}")

    st.write(selected_record["definition"])

    detail_columns = st.columns(3)

    with detail_columns[0]:
        st.markdown("**Governance**")

        st.write(f"**Term ID:** " f"{selected_record['term_id']}")

        st.write(f"**Data domain:** " f"{selected_record['data_domain']}")

        st.write(f"**Status:** " f"{selected_record['status']}")

        st.write(
            f"**Critical data element:** " f"{selected_record['critical_data_element']}"
        )

    with detail_columns[1]:
        st.markdown("**Accountability**")

        st.write(f"**Data Owner:** " f"{selected_record['data_owner']}")

        st.write(f"**Data Steward:** " f"{selected_record['data_steward']}")

        st.write(
            f"**Authoritative source:** " f"{selected_record['authoritative_source']}"
        )

    with detail_columns[2]:
        st.markdown("**Control Metadata**")

        st.write(f"**Sensitivity:** " f"{selected_record['sensitivity']}")

        st.write(f"**Quality dimension:** " f"{selected_record['quality_dimension']}")

        st.write(f"**Related terms:** " f"{selected_record['related_terms']}")

    st.info(
        "All glossary terms and organisational roles "
        "shown here are fictional and created for "
        "portfolio purposes."
    )


def render_data_quality_register() -> None:
    """Render the governed Data Quality Rules Register."""

    quality_rules = load_csv(DATA_QUALITY_RULES_FILE)

    st.title("Data Quality Register")

    st.caption(
        "Review governed data-quality controls, "
        "thresholds, ownership and failure severity."
    )

    st.divider()

    filter_columns = st.columns(4)

    domain_options = [
        "All",
        *sorted(quality_rules["data_domain"].dropna().unique().tolist()),
    ]

    dimension_options = [
        "All",
        *sorted(quality_rules["quality_dimension"].dropna().unique().tolist()),
    ]

    severity_options = [
        "All",
        *sorted(quality_rules["failure_severity"].dropna().unique().tolist()),
    ]

    status_options = [
        "All",
        *sorted(quality_rules["status"].dropna().unique().tolist()),
    ]

    selected_domain = filter_columns[0].selectbox(
        "Data domain",
        options=domain_options,
        key="dq_domain_filter",
    )

    selected_dimension = filter_columns[1].selectbox(
        "Quality dimension",
        options=dimension_options,
        key="dq_dimension_filter",
    )

    selected_severity = filter_columns[2].selectbox(
        "Failure severity",
        options=severity_options,
        key="dq_severity_filter",
    )

    selected_status = filter_columns[3].selectbox(
        "Status",
        options=status_options,
        key="dq_status_filter",
    )

    search_text = st.text_input(
        "Search quality rules",
        placeholder=("Enter a rule, business term, owner " "or control logic"),
        key="dq_search",
    )

    filtered_rules = quality_rules.copy()

    if selected_domain != "All":
        filtered_rules = filtered_rules[
            filtered_rules["data_domain"] == selected_domain
        ]

    if selected_dimension != "All":
        filtered_rules = filtered_rules[
            filtered_rules["quality_dimension"] == selected_dimension
        ]

    if selected_severity != "All":
        filtered_rules = filtered_rules[
            filtered_rules["failure_severity"] == selected_severity
        ]

    if selected_status != "All":
        filtered_rules = filtered_rules[filtered_rules["status"] == selected_status]

    if search_text.strip():
        search_value = search_text.strip().casefold()

        searchable_columns = [
            "rule_id",
            "rule_name",
            "business_term",
            "rule_logic",
            "data_owner",
            "data_steward",
            "data_custodian",
        ]

        search_mask = pd.Series(
            False,
            index=filtered_rules.index,
        )

        for column in searchable_columns:
            search_mask = search_mask | filtered_rules[
                column
            ].str.casefold().str.contains(
                search_value,
                regex=False,
                na=False,
            )

        filtered_rules = filtered_rules[search_mask]

    filtered_rules = filtered_rules.sort_values(
        by=[
            "data_domain",
            "rule_id",
        ]
    ).reset_index(drop=True)

    st.divider()

    metric_columns = st.columns(4)

    metric_columns[0].metric(
        "Displayed Rules",
        len(filtered_rules),
    )

    metric_columns[1].metric(
        "Represented Domains",
        filtered_rules["data_domain"].nunique(),
    )

    metric_columns[2].metric(
        "Active Rules",
        int((filtered_rules["status"] == "Active").sum()),
    )

    metric_columns[3].metric(
        "Critical Failures",
        int((filtered_rules["failure_severity"] == "Critical").sum()),
    )

    st.subheader("Quality Rules")

    display_columns = [
        "rule_id",
        "rule_name",
        "data_domain",
        "business_term",
        "quality_dimension",
        "target_percentage",
        "failure_severity",
        "status",
    ]

    st.dataframe(
        filtered_rules[display_columns],
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("Quality Rule Detail")

    if filtered_rules.empty:
        st.warning("No data-quality rules match " "the selected filters.")
        return

    selected_rule_id = st.selectbox(
        "Select a quality rule",
        options=filtered_rules["rule_id"].tolist(),
        key="dq_rule_selector",
    )

    selected_rule = filtered_rules[filtered_rules["rule_id"] == selected_rule_id].iloc[
        0
    ]

    st.markdown(f"### {selected_rule['rule_name']}")

    st.write(selected_rule["rule_logic"])

    detail_columns = st.columns(3)

    with detail_columns[0]:
        st.markdown("**Rule Definition**")

        st.write(f"**Rule ID:** " f"{selected_rule['rule_id']}")

        st.write(f"**Data domain:** " f"{selected_rule['data_domain']}")

        st.write(f"**Business term:** " f"{selected_rule['business_term']}")

        st.write(f"**Quality dimension:** " f"{selected_rule['quality_dimension']}")

        st.write(f"**Frequency:** " f"{selected_rule['frequency']}")

    with detail_columns[1]:
        st.markdown("**Thresholds**")

        st.write(f"**Target:** " f"{selected_rule['target_percentage']}%")

        st.write(
            f"**Warning threshold:** "
            f"{selected_rule['warning_threshold_percentage']}%"
        )

        st.write(
            f"**Critical threshold:** "
            f"{selected_rule['critical_threshold_percentage']}%"
        )

        st.write(f"**Failure severity:** " f"{selected_rule['failure_severity']}")

        st.write(f"**Status:** " f"{selected_rule['status']}")

    with detail_columns[2]:
        st.markdown("**Accountability**")

        st.write(f"**Data Owner:** " f"{selected_rule['data_owner']}")

        st.write(f"**Data Steward:** " f"{selected_rule['data_steward']}")

        st.write(f"**Data Custodian:** " f"{selected_rule['data_custodian']}")

    st.info(
        "The quality rules and thresholds shown here " "use synthetic portfolio data."
    )


def render_governance_issues() -> None:
    """Render the Governance Issues Register."""

    governance_issues = load_csv(GOVERNANCE_ISSUES_FILE)

    st.title("Governance Issues")

    st.caption(
        "Review data-governance incidents, "
        "ownership, remediation plans and deadlines."
    )

    st.divider()

    filter_columns = st.columns(4)

    domain_options = [
        "All",
        *sorted(governance_issues["primary_domain"].dropna().unique().tolist()),
    ]

    category_options = [
        "All",
        *sorted(governance_issues["issue_category"].dropna().unique().tolist()),
    ]

    severity_options = [
        "All",
        *sorted(governance_issues["severity"].dropna().unique().tolist()),
    ]

    status_options = [
        "All",
        *sorted(governance_issues["status"].dropna().unique().tolist()),
    ]

    selected_domain = filter_columns[0].selectbox(
        "Primary domain",
        options=domain_options,
        key="issue_domain_filter",
    )

    selected_category = filter_columns[1].selectbox(
        "Issue category",
        options=category_options,
        key="issue_category_filter",
    )

    selected_severity = filter_columns[2].selectbox(
        "Severity",
        options=severity_options,
        key="issue_severity_filter",
    )

    selected_status = filter_columns[3].selectbox(
        "Status",
        options=status_options,
        key="issue_status_filter",
    )

    search_text = st.text_input(
        "Search governance issues",
        placeholder=(
            "Enter an issue, data element, owner, " "root cause or remediation action"
        ),
        key="issue_search",
    )

    filtered_issues = governance_issues.copy()

    if selected_domain != "All":
        filtered_issues = filtered_issues[
            filtered_issues["primary_domain"] == selected_domain
        ]

    if selected_category != "All":
        filtered_issues = filtered_issues[
            filtered_issues["issue_category"] == selected_category
        ]

    if selected_severity != "All":
        filtered_issues = filtered_issues[
            filtered_issues["severity"] == selected_severity
        ]

    if selected_status != "All":
        filtered_issues = filtered_issues[filtered_issues["status"] == selected_status]

    if search_text.strip():
        search_value = search_text.strip().casefold()

        searchable_columns = [
            "issue_id",
            "issue_title",
            "affected_data_element",
            "data_owner",
            "data_steward",
            "remediation_owner",
            "root_cause",
            "containment_action",
            "remediation_plan",
            "related_rule_id",
        ]

        search_mask = pd.Series(
            False,
            index=filtered_issues.index,
        )

        for column in searchable_columns:
            search_mask = search_mask | filtered_issues[
                column
            ].str.casefold().str.contains(
                search_value,
                regex=False,
                na=False,
            )

        filtered_issues = filtered_issues[search_mask]

    severity_order = {
        "Critical": 0,
        "High": 1,
        "Medium": 2,
        "Low": 3,
    }

    filtered_issues["_severity_order"] = (
        filtered_issues["severity"].map(severity_order).fillna(4)
    )

    filtered_issues = (
        filtered_issues.sort_values(
            by=[
                "_severity_order",
                "target_date",
                "issue_id",
            ]
        )
        .drop(columns="_severity_order")
        .reset_index(drop=True)
    )

    open_statuses = [
        "Closed",
        "Cancelled",
    ]

    st.divider()

    metric_columns = st.columns(4)

    metric_columns[0].metric(
        "Displayed Issues",
        len(filtered_issues),
    )

    metric_columns[1].metric(
        "Open Issues",
        int((~filtered_issues["status"].isin(open_statuses)).sum()),
    )

    metric_columns[2].metric(
        "Critical or High",
        int(
            filtered_issues["severity"]
            .isin(
                [
                    "Critical",
                    "High",
                ]
            )
            .sum()
        ),
    )

    metric_columns[3].metric(
        "Cross-Domain Issues",
        int((filtered_issues["additional_domains"].str.strip() != "").sum()),
    )

    st.subheader("Issue Register")

    display_columns = [
        "issue_id",
        "issue_title",
        "primary_domain",
        "issue_category",
        "severity",
        "remediation_owner",
        "target_date",
        "status",
    ]

    st.dataframe(
        filtered_issues[display_columns],
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("Issue Detail")

    if filtered_issues.empty:
        st.warning("No governance issues match " "the selected filters.")
        return

    selected_issue_id = st.selectbox(
        "Select a governance issue",
        options=filtered_issues["issue_id"].tolist(),
        key="issue_selector",
    )

    selected_issue = filtered_issues[
        filtered_issues["issue_id"] == selected_issue_id
    ].iloc[0]

    st.markdown(f"### {selected_issue['issue_title']}")

    summary_columns = st.columns(4)

    summary_columns[0].metric(
        "Issue ID",
        selected_issue["issue_id"],
    )

    summary_columns[1].metric(
        "Severity",
        selected_issue["severity"],
    )

    summary_columns[2].metric(
        "Status",
        selected_issue["status"],
    )

    summary_columns[3].metric(
        "Target Date",
        selected_issue["target_date"],
    )

    detail_columns = st.columns(3)

    with detail_columns[0]:
        st.markdown("**Issue Context**")

        st.write(f"**Category:** " f"{selected_issue['issue_category']}")

        st.write(f"**Primary domain:** " f"{selected_issue['primary_domain']}")

        st.write(f"**Additional domains:** " f"{selected_issue['additional_domains']}")

        st.write(
            f"**Affected data element:** " f"{selected_issue['affected_data_element']}"
        )

        st.write(
            f"**Critical data element:** " f"{selected_issue['critical_data_element']}"
        )

        st.write(
            f"**Data classification:** " f"{selected_issue['data_classification']}"
        )

        st.write(f"**Issue source:** " f"{selected_issue['issue_source']}")

    with detail_columns[1]:
        st.markdown("**Accountability**")

        st.write(f"**Data Owner:** " f"{selected_issue['data_owner']}")

        st.write(f"**Data Steward:** " f"{selected_issue['data_steward']}")

        st.write(f"**Remediation Owner:** " f"{selected_issue['remediation_owner']}")

        st.write(f"**Date identified:** " f"{selected_issue['date_identified']}")

        st.write(f"**Last review:** " f"{selected_issue['last_review_date']}")

        st.write(f"**Next review:** " f"{selected_issue['next_review_date']}")

        st.write(f"**Related quality rule:** " f"{selected_issue['related_rule_id']}")

    with detail_columns[2]:
        st.markdown("**Remediation**")

        st.write("**Root cause**")

        st.write(selected_issue["root_cause"])

        st.write("**Containment action**")

        st.write(selected_issue["containment_action"])

        st.write("**Remediation plan**")

        st.write(selected_issue["remediation_plan"])

    st.info(
        "All governance issues shown here are "
        "fictional and use synthetic portfolio data."
    )


def render_access_exceptions() -> None:
    """Render the Access Exceptions Register."""

    access_exceptions = load_csv(ACCESS_EXCEPTIONS_FILE)

    st.title("Access Exceptions")

    st.caption(
        "Review temporary access deviations, "
        "risk assessments, compensating controls "
        "and expiry dates."
    )

    st.divider()

    filter_columns = st.columns(4)

    domain_options = [
        "All",
        *sorted(access_exceptions["data_domain"].dropna().unique().tolist()),
    ]

    risk_options = [
        "All",
        *sorted(access_exceptions["risk_level"].dropna().unique().tolist()),
    ]

    status_options = [
        "All",
        *sorted(access_exceptions["status"].dropna().unique().tolist()),
    ]

    external_options = [
        "All",
        "Yes",
        "No",
    ]

    selected_domain = filter_columns[0].selectbox(
        "Data domain",
        options=domain_options,
        key="access_domain_filter",
    )

    selected_risk = filter_columns[1].selectbox(
        "Risk level",
        options=risk_options,
        key="access_risk_filter",
    )

    selected_status = filter_columns[2].selectbox(
        "Status",
        options=status_options,
        key="access_status_filter",
    )

    selected_external = filter_columns[3].selectbox(
        "External access",
        options=external_options,
        key="access_external_filter",
    )

    search_text = st.text_input(
        "Search access exceptions",
        placeholder=(
            "Enter an exception, account, system, " "owner or business purpose"
        ),
        key="access_search",
    )

    filtered_exceptions = access_exceptions.copy()

    if selected_domain != "All":
        filtered_exceptions = filtered_exceptions[
            filtered_exceptions["data_domain"] == selected_domain
        ]

    if selected_risk != "All":
        filtered_exceptions = filtered_exceptions[
            filtered_exceptions["risk_level"] == selected_risk
        ]

    if selected_status != "All":
        filtered_exceptions = filtered_exceptions[
            filtered_exceptions["status"] == selected_status
        ]

    if selected_external != "All":
        filtered_exceptions = filtered_exceptions[
            filtered_exceptions["external_access"] == selected_external
        ]

    if search_text.strip():
        search_value = search_text.strip().casefold()

        searchable_columns = [
            "exception_id",
            "exception_title",
            "user_or_account",
            "line_manager_or_sponsor",
            "system_or_platform",
            "business_purpose",
            "standard_access_gap",
            "compensating_controls",
            "permanent_remediation",
            "data_owner",
            "data_steward",
            "data_custodian",
        ]

        search_mask = pd.Series(
            False,
            index=filtered_exceptions.index,
        )

        for column in searchable_columns:
            search_mask = search_mask | filtered_exceptions[
                column
            ].str.casefold().str.contains(
                search_value,
                regex=False,
                na=False,
            )

        filtered_exceptions = filtered_exceptions[search_mask]

    risk_order = {
        "High": 0,
        "Medium": 1,
        "Low": 2,
    }

    filtered_exceptions["_risk_order"] = (
        filtered_exceptions["risk_level"].map(risk_order).fillna(3)
    )

    filtered_exceptions["_expiry_sort"] = pd.to_datetime(
        filtered_exceptions["expiry_date"],
        errors="coerce",
    )

    filtered_exceptions = (
        filtered_exceptions.sort_values(
            by=[
                "_risk_order",
                "_expiry_sort",
                "exception_id",
            ],
            na_position="last",
        )
        .drop(
            columns=[
                "_risk_order",
                "_expiry_sort",
            ]
        )
        .reset_index(drop=True)
    )

    inactive_statuses = [
        "Closed",
        "Rejected",
        "Cancelled",
    ]

    st.divider()

    metric_columns = st.columns(4)

    metric_columns[0].metric(
        "Displayed Exceptions",
        len(filtered_exceptions),
    )

    metric_columns[1].metric(
        "Active Exceptions",
        int((~filtered_exceptions["status"].isin(inactive_statuses)).sum()),
    )

    metric_columns[2].metric(
        "High-Risk Exceptions",
        int((filtered_exceptions["risk_level"] == "High").sum()),
    )

    metric_columns[3].metric(
        "External Access",
        int((filtered_exceptions["external_access"] == "Yes").sum()),
    )

    st.subheader("Exception Register")

    display_columns = [
        "exception_id",
        "exception_title",
        "user_or_account",
        "data_domain",
        "system_or_platform",
        "risk_level",
        "expiry_date",
        "status",
    ]

    st.dataframe(
        filtered_exceptions[display_columns],
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("Exception Detail")

    if filtered_exceptions.empty:
        st.warning("No access exceptions match " "the selected filters.")
        return

    selected_exception_id = st.selectbox(
        "Select an access exception",
        options=filtered_exceptions["exception_id"].tolist(),
        key="access_exception_selector",
    )

    selected_exception = filtered_exceptions[
        filtered_exceptions["exception_id"] == selected_exception_id
    ].iloc[0]

    st.markdown(f"### {selected_exception['exception_title']}")

    summary_columns = st.columns(4)

    summary_columns[0].metric(
        "Exception ID",
        selected_exception["exception_id"],
    )

    summary_columns[1].metric(
        "Risk Level",
        selected_exception["risk_level"],
    )

    summary_columns[2].metric(
        "Status",
        selected_exception["status"],
    )

    summary_columns[3].metric(
        "Expiry Date",
        selected_exception["expiry_date"],
    )

    detail_columns = st.columns(3)

    with detail_columns[0]:
        st.markdown("**Access Request**")

        st.write(f"**User or account:** " f"{selected_exception['user_or_account']}")

        st.write(
            f"**Recipient type:** " f"{selected_exception['access_recipient_type']}"
        )

        st.write(
            f"**Manager or sponsor:** "
            f"{selected_exception['line_manager_or_sponsor']}"
        )

        st.write(f"**Data domain:** " f"{selected_exception['data_domain']}")

        st.write(
            f"**System or platform:** " f"{selected_exception['system_or_platform']}"
        )

        st.write(f"**Access level:** " f"{selected_exception['access_level']}")

        st.write(
            f"**Data classification:** " f"{selected_exception['data_classification']}"
        )

    with detail_columns[1]:
        st.markdown("**Risk Assessment**")

        st.write(f"**External access:** " f"{selected_exception['external_access']}")

        st.write(
            f"**Segregation conflict:** "
            f"{selected_exception['segregation_conflict']}"
        )

        st.write(
            f"**Production data outside production:** "
            f"{selected_exception['production_data_outside_production']}"
        )

        st.write(f"**Start date:** " f"{selected_exception['start_date']}")

        st.write(f"**Expiry date:** " f"{selected_exception['expiry_date']}")

        st.write(f"**Renewal count:** " f"{selected_exception['renewal_count']}")

        st.write(f"**Next review:** " f"{selected_exception['next_review_date']}")

    with detail_columns[2]:
        st.markdown("**Controls and Remediation**")

        st.write("**Business purpose**")

        st.write(selected_exception["business_purpose"])

        st.write("**Standard access gap**")

        st.write(selected_exception["standard_access_gap"])

        st.write("**Compensating controls**")

        st.write(selected_exception["compensating_controls"])

        st.write("**Permanent remediation**")

        st.write(selected_exception["permanent_remediation"])

    st.divider()

    accountability_columns = st.columns(3)

    accountability_columns[0].write(
        f"**Data Owner:** " f"{selected_exception['data_owner']}"
    )

    accountability_columns[1].write(
        f"**Data Steward:** " f"{selected_exception['data_steward']}"
    )

    accountability_columns[2].write(
        f"**Data Custodian:** " f"{selected_exception['data_custodian']}"
    )

    st.info(
        "All access exceptions shown here are "
        "fictional and use synthetic portfolio data."
    )


def render_ai_use_cases() -> None:
    """Render the governed AI Use Case Register."""

    ai_use_cases = load_csv(AI_USE_CASES_FILE)

    st.title("AI Use Cases")

    st.caption(
        "Review AI initiatives, data readiness, "
        "risk classification, human oversight "
        "and approval decisions."
    )

    st.divider()

    filter_columns = st.columns(4)

    risk_options = [
        "All",
        *sorted(ai_use_cases["ai_risk_tier"].dropna().unique().tolist()),
    ]

    domain_options = [
        "All",
        *sorted(ai_use_cases["primary_domain"].dropna().unique().tolist()),
    ]

    decision_options = [
        "All",
        *sorted(ai_use_cases["approval_decision"].dropna().unique().tolist()),
    ]

    status_options = [
        "All",
        *sorted(ai_use_cases["status"].dropna().unique().tolist()),
    ]

    selected_risk = filter_columns[0].selectbox(
        "AI risk tier",
        options=risk_options,
        key="ai_risk_filter",
    )

    selected_domain = filter_columns[1].selectbox(
        "Primary domain",
        options=domain_options,
        key="ai_domain_filter",
    )

    selected_decision = filter_columns[2].selectbox(
        "Approval decision",
        options=decision_options,
        key="ai_decision_filter",
    )

    selected_status = filter_columns[3].selectbox(
        "Status",
        options=status_options,
        key="ai_status_filter",
    )

    search_text = st.text_input(
        "Search AI use cases",
        placeholder=(
            "Enter a use case, business purpose, "
            "owner, data source or oversight control"
        ),
        key="ai_search",
    )

    filtered_use_cases = ai_use_cases.copy()

    if selected_risk != "All":
        filtered_use_cases = filtered_use_cases[
            filtered_use_cases["ai_risk_tier"] == selected_risk
        ]

    if selected_domain != "All":
        filtered_use_cases = filtered_use_cases[
            filtered_use_cases["primary_domain"] == selected_domain
        ]

    if selected_decision != "All":
        filtered_use_cases = filtered_use_cases[
            filtered_use_cases["approval_decision"] == selected_decision
        ]

    if selected_status != "All":
        filtered_use_cases = filtered_use_cases[
            filtered_use_cases["status"] == selected_status
        ]

    if search_text.strip():
        search_value = search_text.strip().casefold()

        searchable_columns = [
            "use_case_id",
            "use_case_name",
            "business_purpose",
            "business_owner",
            "intended_users",
            "data_sources",
            "data_owner",
            "data_steward",
            "data_custodian",
            "human_oversight",
            "related_issue_id",
        ]

        search_mask = pd.Series(
            False,
            index=filtered_use_cases.index,
        )

        for column in searchable_columns:
            search_mask = search_mask | filtered_use_cases[
                column
            ].str.casefold().str.contains(
                search_value,
                regex=False,
                na=False,
            )

        filtered_use_cases = filtered_use_cases[search_mask]

    risk_order = {
        "High": 0,
        "Medium": 1,
        "Low": 2,
    }

    filtered_use_cases["_risk_order"] = (
        filtered_use_cases["ai_risk_tier"].map(risk_order).fillna(3)
    )

    filtered_use_cases["_readiness_sort"] = pd.to_numeric(
        filtered_use_cases["readiness_score"],
        errors="coerce",
    )

    filtered_use_cases = (
        filtered_use_cases.sort_values(
            by=[
                "_risk_order",
                "_readiness_sort",
                "use_case_id",
            ],
            ascending=[
                True,
                False,
                True,
            ],
            na_position="last",
        )
        .drop(
            columns=[
                "_risk_order",
                "_readiness_sort",
            ]
        )
        .reset_index(drop=True)
    )

    decision_text = filtered_use_cases["approval_decision"].str.casefold()

    ready_or_conditional = decision_text.str.contains(
        "approved",
        regex=False,
        na=False,
    ) | decision_text.str.contains(
        "condition",
        regex=False,
        na=False,
    )

    st.divider()

    metric_columns = st.columns(4)

    metric_columns[0].metric(
        "Displayed Use Cases",
        len(filtered_use_cases),
    )

    metric_columns[1].metric(
        "Ready or Conditional",
        int(ready_or_conditional.sum()),
    )

    metric_columns[2].metric(
        "High-Risk Use Cases",
        int((filtered_use_cases["ai_risk_tier"] == "High").sum()),
    )

    metric_columns[3].metric(
        "External Processing",
        int((filtered_use_cases["external_processing"] == "Yes").sum()),
    )

    st.subheader("AI Portfolio")

    display_columns = [
        "use_case_id",
        "use_case_name",
        "business_owner",
        "primary_domain",
        "ai_risk_tier",
        "readiness_score",
        "approval_decision",
        "status",
    ]

    st.dataframe(
        filtered_use_cases[display_columns],
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("AI Use Case Detail")

    if filtered_use_cases.empty:
        st.warning("No AI use cases match " "the selected filters.")
        return

    selected_use_case_id = st.selectbox(
        "Select an AI use case",
        options=filtered_use_cases["use_case_id"].tolist(),
        key="ai_use_case_selector",
    )

    selected_use_case = filtered_use_cases[
        filtered_use_cases["use_case_id"] == selected_use_case_id
    ].iloc[0]

    st.markdown(f"### {selected_use_case['use_case_name']}")

    st.write(selected_use_case["business_purpose"])

    summary_columns = st.columns(4)

    summary_columns[0].metric(
        "Use Case ID",
        selected_use_case["use_case_id"],
    )

    summary_columns[1].metric(
        "Risk Tier",
        selected_use_case["ai_risk_tier"],
    )

    summary_columns[2].metric(
        "Readiness Score",
        selected_use_case["readiness_score"],
    )

    summary_columns[3].metric(
        "Decision",
        selected_use_case["approval_decision"],
    )

    detail_columns = st.columns(3)

    with detail_columns[0]:
        st.markdown("**Use Case Context**")

        st.write(f"**Business Owner:** " f"{selected_use_case['business_owner']}")

        st.write(f"**Primary domain:** " f"{selected_use_case['primary_domain']}")

        st.write(
            f"**Additional domains:** " f"{selected_use_case['additional_domains']}"
        )

        st.write(
            f"**Degree of automation:** " f"{selected_use_case['degree_of_automation']}"
        )

        st.write(f"**Intended users:** " f"{selected_use_case['intended_users']}")

        st.write(f"**Status:** " f"{selected_use_case['status']}")

    with detail_columns[1]:
        st.markdown("**Data Assessment**")

        st.write(
            f"**Data classification:** " f"{selected_use_case['data_classification']}"
        )

        st.write(f"**Personal data:** " f"{selected_use_case['personal_data']}")

        st.write(
            f"**Sensitive personal data:** "
            f"{selected_use_case['sensitive_personal_data']}"
        )

        st.write(f"**Restricted data:** " f"{selected_use_case['restricted_data']}")

        st.write(
            f"**External processing:** " f"{selected_use_case['external_processing']}"
        )

        st.write(f"**Dataset version:** " f"{selected_use_case['dataset_version']}")

        st.write(f"**Lineage status:** " f"{selected_use_case['lineage_status']}")

        st.write(
            f"**Data quality status:** " f"{selected_use_case['data_quality_status']}"
        )

    with detail_columns[2]:
        st.markdown("**Governance Controls**")

        st.write(f"**Human oversight:** " f"{selected_use_case['human_oversight']}")

        st.write(
            f"**Monitoring frequency:** " f"{selected_use_case['monitoring_frequency']}"
        )

        st.write(f"**Approval date:** " f"{selected_use_case['approval_date']}")

        st.write(f"**Next review:** " f"{selected_use_case['next_review_date']}")

        st.write(f"**Related issue:** " f"{selected_use_case['related_issue_id']}")

    st.divider()

    st.markdown("**Data Sources**")

    st.write(selected_use_case["data_sources"])

    accountability_columns = st.columns(3)

    accountability_columns[0].write(
        f"**Data Owner:** " f"{selected_use_case['data_owner']}"
    )

    accountability_columns[1].write(
        f"**Data Steward:** " f"{selected_use_case['data_steward']}"
    )

    accountability_columns[2].write(
        f"**Data Custodian:** " f"{selected_use_case['data_custodian']}"
    )

    st.info(
        "All AI use cases, systems and organisational "
        "roles shown here are fictional and use "
        "synthetic portfolio data."
    )


def format_document_title(file_path: Path) -> str:
    """Convert a Markdown filename into a readable title."""

    return file_path.stem.replace("_", " ").replace("-", " ").title()


@st.cache_data
def load_markdown_documents(
    directory: Path,
) -> dict[str, dict[str, str]]:
    """Load Markdown governance documents."""

    documents = {}

    for file_path in sorted(directory.glob("*.md")):
        title = format_document_title(file_path)

        documents[title] = {
            "filename": file_path.name,
            "content": file_path.read_text(encoding="utf-8"),
        }

    return documents


def render_document_library(
    documents: dict[str, dict[str, str]],
    selector_label: str,
    selector_key: str,
) -> None:
    """Render one selectable Markdown document library."""

    if not documents:
        st.warning("No governance documents were found.")
        return

    selected_title = st.selectbox(
        selector_label,
        options=list(documents),
        key=selector_key,
    )

    selected_document = documents[selected_title]

    st.caption("Source file: " f"{selected_document['filename']}")

    st.divider()

    st.markdown(selected_document["content"])


def render_standards_and_workflows() -> None:
    """Render governance standards and workflows."""

    standards = load_markdown_documents(STANDARDS_DIRECTORY)

    workflows = load_markdown_documents(WORKFLOWS_DIRECTORY)

    st.title("Standards & Workflows")

    st.caption(
        "Review the policies and operational procedures "
        "supporting the enterprise data-governance model."
    )

    st.divider()

    metric_columns = st.columns(3)

    metric_columns[0].metric(
        "Governance Standards",
        len(standards),
    )

    metric_columns[1].metric(
        "Governance Workflows",
        len(workflows),
    )

    metric_columns[2].metric(
        "Controlled Documents",
        len(standards) + len(workflows),
    )

    st.divider()

    standards_tab, workflows_tab = st.tabs(
        [
            "Governance Standards",
            "Operational Workflows",
        ]
    )

    with standards_tab:
        st.subheader("Governance Standards")

        st.write(
            "The standards define mandatory controls, "
            "accountability requirements and minimum "
            "governance expectations."
        )

        render_document_library(
            documents=standards,
            selector_label="Select a governance standard",
            selector_key="standard_document_selector",
        )

    with workflows_tab:
        st.subheader("Operational Workflows")

        st.write(
            "The workflows translate governance policy "
            "into repeatable decision, review and "
            "approval procedures."
        )

        render_document_library(
            documents=workflows,
            selector_label="Select an operational workflow",
            selector_key="workflow_document_selector",
        )

    st.info(
        "All organisations, roles, controls and operating "
        "procedures shown here are fictional and created "
        "for portfolio purposes."
    )


def render_overview() -> None:
    """Render the executive governance overview."""

    glossary = load_csv(GLOSSARY_FILE)
    quality_rules = load_csv(DATA_QUALITY_RULES_FILE)
    issues = load_csv(GOVERNANCE_ISSUES_FILE)
    access_exceptions = load_csv(ACCESS_EXCEPTIONS_FILE)
    ai_use_cases = load_csv(AI_USE_CASES_FILE)
    domain_records = load_domain_records()

    open_issues = issues[
        ~issues["status"].isin(
            {
                "Closed",
                "Cancelled",
            }
        )
    ].copy()

    active_access_exceptions = access_exceptions[
        ~access_exceptions["status"].isin(
            {
                "Closed",
                "Rejected",
                "Cancelled",
            }
        )
    ].copy()

    approved_ai_use_cases = ai_use_cases[
        ai_use_cases["status"].isin(
            {
                "Ready",
                "Conditionally Ready",
            }
        )
    ].copy()

    active_quality_rules = quality_rules[quality_rules["status"] == "Active"].copy()

    standards_count = count_markdown_files(STANDARDS_DIRECTORY)

    workflows_count = count_markdown_files(WORKFLOWS_DIRECTORY)

    st.title("Enterprise Data Governance Operating Model")

    st.caption(
        "Fictional Swiss insurance governance portfolio "
        "covering data ownership, quality, metadata, "
        "access, issue management and AI readiness."
    )

    st.divider()

    metric_row_one = st.columns(4)

    metric_row_one[0].metric(
        "Governed Domains",
        len(domain_records),
    )

    metric_row_one[1].metric(
        "Business Glossary Terms",
        len(glossary),
    )

    metric_row_one[2].metric(
        "Active Quality Rules",
        len(active_quality_rules),
    )

    metric_row_one[3].metric(
        "Open Governance Issues",
        len(open_issues),
    )

    metric_row_two = st.columns(4)

    metric_row_two[0].metric(
        "Active Access Exceptions",
        len(active_access_exceptions),
    )

    metric_row_two[1].metric(
        "Ready or Conditional AI Use Cases",
        (f"{len(approved_ai_use_cases)}" f" / {len(ai_use_cases)}"),
    )

    metric_row_two[2].metric(
        "Governance Standards",
        standards_count,
    )

    metric_row_two[3].metric(
        "Operational Workflows",
        workflows_count,
    )

    st.divider()

    st.subheader("Governance Coverage by Data Domain")

    domain_coverage = build_domain_coverage(
        glossary=glossary,
        quality_rules=quality_rules,
        issues=issues,
        access_exceptions=access_exceptions,
        ai_use_cases=ai_use_cases,
    )

    st.dataframe(
        domain_coverage,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    chart_column_one, chart_column_two = st.columns(2)

    with chart_column_one:
        st.subheader("Open Issues by Severity")

        severity_order = [
            "High",
            "Medium",
            "Low",
        ]

        severity_counts = (
            open_issues["severity"]
            .value_counts()
            .reindex(
                severity_order,
                fill_value=0,
            )
            .rename("Open Issues")
        )

        st.bar_chart(severity_counts)

    with chart_column_two:
        st.subheader("AI Use Cases by Status")

        ai_status_counts = ai_use_cases["status"].value_counts().rename("AI Use Cases")

        st.bar_chart(ai_status_counts)

    st.divider()

    st.subheader("Priority Governance Issues")

    priority_issues = open_issues[open_issues["severity"] == "High"][
        [
            "issue_id",
            "issue_title",
            "primary_domain",
            "status",
            "data_owner",
            "target_date",
        ]
    ].sort_values(by="target_date")

    st.dataframe(
        priority_issues,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("AI Governance Portfolio")

    ai_portfolio = ai_use_cases[
        [
            "use_case_id",
            "use_case_name",
            "ai_risk_tier",
            "primary_domain",
            "data_classification",
            "readiness_score",
            "status",
            "next_review_date",
        ]
    ].copy()

    ai_portfolio["readiness_score"] = pd.to_numeric(
        ai_portfolio["readiness_score"],
        errors="coerce",
    )

    ai_portfolio = ai_portfolio.sort_values(
        by="readiness_score",
        ascending=False,
    )

    st.dataframe(
        ai_portfolio,
        use_container_width=True,
        hide_index=True,
    )

    st.info(
        "All data, organisations, roles, systems and "
        "issues presented in this application are "
        "fictional and created for portfolio purposes."
    )


with st.sidebar:
    st.header("Governance Portal")

    selected_page = st.radio(
        "Navigate",
        options=[
            "Executive Overview",
            "Data Domains",
            "Business Glossary",
            "Data Quality",
            "Governance Issues",
            "Access Exceptions",
            "AI Use Cases",
            "Standards & Workflows",
        ],
    )

    st.divider()

    st.caption("HelvetiaCare Insurance Group")

    st.caption("Illustrative portfolio environment")


try:
    if selected_page == "Executive Overview":
        render_overview()

    elif selected_page == "Data Domains":
        render_domain_explorer()

    elif selected_page == "Business Glossary":
        render_glossary_explorer()

    elif selected_page == "Data Quality":
        render_data_quality_register()

    elif selected_page == "Governance Issues":
        render_governance_issues()

    elif selected_page == "Access Exceptions":
        render_access_exceptions()

    elif selected_page == "AI Use Cases":
        render_ai_use_cases()

    elif selected_page == "Standards & Workflows":
        render_standards_and_workflows()

except (
    FileNotFoundError,
    ValueError,
    KeyError,
    TypeError,
    pd.errors.ParserError,
    yaml.YAMLError,
) as error:
    st.error("The governance dashboard could not be loaded.")

    st.exception(error)

import csv
from datetime import date
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOMAINS_DIRECTORY = PROJECT_ROOT / "domains"
FRAMEWORK_DIRECTORY = PROJECT_ROOT / "framework"
STANDARDS_DIRECTORY = PROJECT_ROOT / "standards"
WORKFLOWS_DIRECTORY = PROJECT_ROOT / "workflows"
RACI_FILE = PROJECT_ROOT / "roles" / "raci_matrix.csv"

GLOSSARY_FILE = PROJECT_ROOT / "glossary" / "business_glossary.csv"

DATA_QUALITY_RULES_FILE = PROJECT_ROOT / "data" / "data_quality_rules.csv"

GOVERNANCE_ISSUES_FILE = PROJECT_ROOT / "data" / "governance_issues.csv"

ACCESS_EXCEPTIONS_FILE = PROJECT_ROOT / "data" / "access_exceptions.csv"

AI_USE_CASES_FILE = PROJECT_ROOT / "data" / "ai_use_cases.csv"

EXPECTED_DOMAIN_FILES = {
    "customer_domain.yaml",
    "policy_domain.yaml",
    "claims_domain.yaml",
    "provider_domain.yaml",
    "finance_domain.yaml",
}

REQUIRED_DOMAIN_FIELDS = {
    "id",
    "name",
    "description",
    "business_purpose",
    "data_owner",
    "data_steward",
    "data_custodians",
    "key_systems",
    "critical_data_elements",
    "primary_risks",
    "governance_controls",
    "governance_kpis",
    "related_standards",
}

EXPECTED_RACI_COLUMNS = {
    "activity",
    "chief_data_officer",
    "data_governance_council",
    "data_owner",
    "data_steward",
    "data_custodian",
    "data_protection",
    "compliance",
    "information_security",
    "data_architecture",
    "data_ai_centre_of_excellence",
    "business_subject_matter_experts",
}

VALID_RACI_CODES = {"R", "A", "C", "I"}

EXPECTED_GLOSSARY_COLUMNS = {
    "term_id",
    "business_term",
    "definition",
    "data_domain",
    "data_owner",
    "data_steward",
    "authoritative_source",
    "sensitivity",
    "critical_data_element",
    "status",
    "quality_dimension",
    "related_terms",
}

VALID_GLOSSARY_DOMAINS = {
    "Customer",
    "Policy",
    "Claims",
    "Healthcare Provider",
    "Finance",
    "Enterprise",
}

REQUIRED_OPERATIONAL_DOMAINS = {
    "Customer",
    "Policy",
    "Claims",
    "Healthcare Provider",
    "Finance",
}

VALID_GLOSSARY_STATUSES = {
    "Draft",
    "Approved",
    "Retired",
}

VALID_SENSITIVITY_VALUES = {
    "Internal",
    "Confidential",
    "Personal",
    "Sensitive Personal",
    "Restricted",
}

VALID_CRITICAL_ELEMENT_VALUES = {
    "Yes",
    "No",
}

VALID_QUALITY_DIMENSIONS = {
    "Accuracy",
    "Completeness",
    "Consistency",
    "Referential Integrity",
    "Timeliness",
    "Uniqueness",
    "Validity",
}

EXPECTED_DATA_QUALITY_RULE_COLUMNS = {
    "rule_id",
    "rule_name",
    "data_domain",
    "business_term",
    "quality_dimension",
    "rule_logic",
    "target_percentage",
    "warning_threshold_percentage",
    "critical_threshold_percentage",
    "frequency",
    "data_owner",
    "data_steward",
    "data_custodian",
    "failure_severity",
    "status",
}

EXPECTED_DATA_QUALITY_RULE_DOMAINS = {
    "Customer",
    "Policy",
    "Claims",
    "Healthcare Provider",
    "Finance",
}

VALID_DATA_QUALITY_RULE_PREFIXES = {
    "CUSTOMER",
    "POLICY",
    "CLAIMS",
    "PROVIDER",
    "FINANCE",
}

VALID_DATA_QUALITY_FREQUENCIES = {
    "Real-time",
    "Event-driven",
    "Daily",
    "Weekly",
    "Monthly",
    "Quarterly",
    "Annual",
}

VALID_FAILURE_SEVERITIES = {
    "Low",
    "Medium",
    "High",
}

VALID_DATA_QUALITY_RULE_STATUSES = {
    "Draft",
    "Active",
    "Suspended",
    "Retired",
}

EXPECTED_GOVERNANCE_ISSUE_COLUMNS = {
    "issue_id",
    "issue_title",
    "issue_category",
    "primary_domain",
    "additional_domains",
    "date_identified",
    "issue_source",
    "affected_data_element",
    "critical_data_element",
    "data_classification",
    "severity",
    "data_owner",
    "data_steward",
    "remediation_owner",
    "root_cause",
    "containment_action",
    "remediation_plan",
    "target_date",
    "status",
    "related_rule_id",
    "last_review_date",
    "next_review_date",
    "closure_date",
}

VALID_ISSUE_DOMAINS = {
    "Customer",
    "Policy",
    "Claims",
    "Healthcare Provider",
    "Finance",
    "Enterprise",
}

VALID_ISSUE_CATEGORIES = {
    "Ownership and Accountability",
    "Business Definition and Metadata",
    "Data Quality",
    "Data Classification and Handling",
    "Data Access",
    "Data Lifecycle",
    "Data Lineage and Integration",
    "Reporting and Analytics",
    "Artificial Intelligence",
    "Third-Party Data",
    "Governance Process and Evidence",
}

VALID_ISSUE_SEVERITIES = {
    "Low",
    "Medium",
    "High",
}

VALID_ISSUE_STATUSES = {
    "Identified",
    "Under Assessment",
    "Remediation Agreed",
    "In Progress",
    "Blocked",
    "Awaiting Validation",
    "Awaiting Closure Approval",
    "Closed",
    "Risk Accepted",
    "Cancelled",
    "Reopened",
}

VALID_ROOT_CAUSES = {
    "Ownership gap",
    "Stewardship gap",
    "Definition ambiguity",
    "Incomplete metadata",
    "Process design",
    "Manual input error",
    "Training gap",
    "System configuration",
    "Software defect",
    "Interface failure",
    "Transformation logic",
    "Reference-data failure",
    "Access-control failure",
    "Control design weakness",
    "Control execution failure",
    "Change-management failure",
    "Third-party failure",
    "Legacy-data limitation",
    "Resource constraint",
    "Unapproved workaround",
    "Unknown",
}

EXPECTED_ACCESS_EXCEPTION_COLUMNS = {
    "exception_id",
    "exception_title",
    "request_date",
    "user_or_account",
    "access_recipient_type",
    "line_manager_or_sponsor",
    "data_domain",
    "system_or_platform",
    "data_classification",
    "access_level",
    "business_purpose",
    "standard_access_gap",
    "start_date",
    "expiry_date",
    "risk_level",
    "segregation_conflict",
    "external_access",
    "production_data_outside_production",
    "compensating_controls",
    "permanent_remediation",
    "data_owner",
    "data_steward",
    "data_custodian",
    "status",
    "renewal_count",
    "last_review_date",
    "next_review_date",
    "revocation_date",
    "closure_date",
}

VALID_ACCESS_RECIPIENT_TYPES = {
    "Employee",
    "Contractor",
    "Service Account",
}

VALID_ACCESS_LEVELS = {
    "Read",
    "Create",
    "Amend",
    "Approve",
    "Export",
    "Administer",
}

VALID_ACCESS_RISK_LEVELS = {
    "Low",
    "Medium",
    "High",
}

VALID_ACCESS_EXCEPTION_BOOLEAN_VALUES = {
    "Yes",
    "No",
}

VALID_ACCESS_EXCEPTION_STATUSES = {
    "Draft",
    "Submitted",
    "Information Required",
    "Under Assessment",
    "Specialist Review",
    "Awaiting Approval",
    "Approved",
    "Approved with Conditions",
    "Rejected",
    "Implemented",
    "Active",
    "Renewal Under Review",
    "Expired",
    "Revocation Pending",
    "Closed",
    "Cancelled",
}

ACCESS_STATUSES_REQUIRING_REVIEW = {
    "Specialist Review",
    "Approved",
    "Approved with Conditions",
    "Implemented",
    "Active",
    "Renewal Under Review",
    "Expired",
    "Revocation Pending",
}

EXPECTED_AI_USE_CASE_COLUMNS = {
    "use_case_id",
    "use_case_name",
    "business_purpose",
    "business_owner",
    "ai_risk_tier",
    "primary_domain",
    "additional_domains",
    "degree_of_automation",
    "intended_users",
    "data_classification",
    "personal_data",
    "sensitive_personal_data",
    "restricted_data",
    "external_processing",
    "data_sources",
    "dataset_version",
    "data_owner",
    "data_steward",
    "data_custodian",
    "lineage_status",
    "data_quality_status",
    "human_oversight",
    "monitoring_frequency",
    "readiness_score",
    "approval_decision",
    "status",
    "approval_date",
    "next_review_date",
    "related_issue_id",
}

VALID_AI_RISK_TIERS = {
    "Tier 1",
    "Tier 2",
    "Tier 3",
}

VALID_AUTOMATION_LEVELS = {
    "Advisory",
    "Partially Automated",
    "Automated",
}

VALID_AI_BOOLEAN_VALUES = {
    "Yes",
    "No",
}

VALID_LINEAGE_STATUSES = {
    "Complete",
    "Partial",
    "Missing",
}

VALID_AI_DATA_QUALITY_STATUSES = {
    "Green",
    "Amber",
    "Red",
}

VALID_AI_MONITORING_FREQUENCIES = {
    "Real-time",
    "Daily",
    "Weekly",
    "Monthly",
    "Quarterly",
    "Annual",
}

VALID_AI_APPROVAL_DECISIONS = {
    "Ready",
    "Conditionally Ready",
    "Not Ready",
}

VALID_AI_USE_CASE_STATUSES = {
    "Draft",
    "Under Triage",
    "Under Assessment",
    "Information Required",
    "Specialist Review",
    "Remediation Required",
    "Awaiting Approval",
    "Ready",
    "Conditionally Ready",
    "Not Ready",
    "Suspended",
    "Retired",
}

EXPECTED_STANDARD_FILES = {
    "metadata_standard.md",
    "data_quality_standard.md",
    "data_classification_standard.md",
    "data_access_standard.md",
    "data_issue_management_standard.md",
    "ai_data_readiness_standard.md",
}

REQUIRED_STANDARD_SECTIONS = {
    "## 1. Purpose",
    "## 2. Scope",
    "Document Control",
}

EXPECTED_WORKFLOW_FILES = {
    "access_exception.md",
    "ai_use_case_assessment.md",
    "data_issue_management.md",
    "glossary_approval.md",
}

REQUIRED_WORKFLOW_SECTIONS = {
    "## 1. Purpose",
    "## 2. Scope",
    "Document Control",
}


def load_yaml_file(file_path: Path) -> dict:
    """Load a YAML file and return its contents."""

    with file_path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    assert content is not None, f"{file_path.name} is empty."
    assert isinstance(content, dict), f"{file_path.name} must contain a YAML mapping."

    return content


def get_domain_files() -> list[Path]:
    """Return all YAML data-domain files."""

    return sorted(DOMAINS_DIRECTORY.glob("*_domain.yaml"))


def load_raci_rows() -> tuple[list[str], list[dict[str, str]]]:
    """Load the RACI matrix and return its columns and rows."""

    assert RACI_FILE.exists(), "The RACI matrix does not exist."

    with RACI_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        assert reader.fieldnames is not None, "The RACI matrix has no header."

        columns = [column.strip() for column in reader.fieldnames]

        rows = []

        for raw_row in reader:
            cleaned_row = {
                key.strip(): value.strip()
                for key, value in raw_row.items()
                if key is not None
            }

            rows.append(cleaned_row)

    return columns, rows


def load_glossary_rows() -> tuple[
    list[str],
    list[dict[str, str]],
]:
    """Load the business glossary and return its columns and rows."""

    assert GLOSSARY_FILE.exists(), "The business glossary does not exist."

    with GLOSSARY_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        assert reader.fieldnames is not None, "The business glossary has no header."

        columns = [column.strip() for column in reader.fieldnames]

        rows = []

        for raw_row in reader:
            cleaned_row = {
                key.strip(): value.strip()
                for key, value in raw_row.items()
                if key is not None
            }

            rows.append(cleaned_row)

    return columns, rows


def load_data_quality_rule_rows() -> tuple[
    list[str],
    list[dict[str, str]],
]:
    """Load the Data Quality Rules Register."""

    assert (
        DATA_QUALITY_RULES_FILE.exists()
    ), "The Data Quality Rules Register does not exist."

    with DATA_QUALITY_RULES_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        assert (
            reader.fieldnames is not None
        ), "The Data Quality Rules Register has no header."

        columns = [column.strip() for column in reader.fieldnames]

        rows = []

        for raw_row in reader:
            cleaned_row = {
                key.strip(): value.strip()
                for key, value in raw_row.items()
                if key is not None
            }

            rows.append(cleaned_row)

    return columns, rows


def load_governance_issue_rows() -> tuple[
    list[str],
    list[dict[str, str]],
]:
    """Load the Governance Issues Register."""

    assert (
        GOVERNANCE_ISSUES_FILE.exists()
    ), "The Governance Issues Register does not exist."

    with GOVERNANCE_ISSUES_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        assert (
            reader.fieldnames is not None
        ), "The Governance Issues Register has no header."

        columns = [column.strip() for column in reader.fieldnames]

        rows = []

        for raw_row in reader:
            cleaned_row = {
                key.strip(): value.strip()
                for key, value in raw_row.items()
                if key is not None
            }

            rows.append(cleaned_row)

    return columns, rows


def load_access_exception_rows() -> tuple[
    list[str],
    list[dict[str, str]],
]:
    """Load the Data Access Exceptions Register."""

    assert (
        ACCESS_EXCEPTIONS_FILE.exists()
    ), "The Data Access Exceptions Register does not exist."

    with ACCESS_EXCEPTIONS_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        assert reader.fieldnames is not None, (
            "The Data Access Exceptions Register " "has no header."
        )

        columns = [column.strip() for column in reader.fieldnames]

        rows = []

        for raw_row in reader:
            cleaned_row = {
                key.strip(): value.strip()
                for key, value in raw_row.items()
                if key is not None
            }

            rows.append(cleaned_row)

    return columns, rows


def load_ai_use_case_rows() -> tuple[
    list[str],
    list[dict[str, str]],
]:
    """Load the AI Use Cases Register."""

    assert AI_USE_CASES_FILE.exists(), "The AI Use Cases Register does not exist."

    with AI_USE_CASES_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        assert reader.fieldnames is not None, "The AI Use Cases Register has no header."

        columns = [column.strip() for column in reader.fieldnames]

        rows = []

        for raw_row in reader:
            cleaned_row = {
                key.strip(): value.strip()
                for key, value in raw_row.items()
                if key is not None
            }

            rows.append(cleaned_row)

    return columns, rows


def test_expected_domain_files_exist() -> None:
    """Verify that the five expected domain files exist."""

    actual_files = {file.name for file in get_domain_files()}

    assert actual_files == EXPECTED_DOMAIN_FILES


@pytest.mark.parametrize(
    "domain_file",
    get_domain_files(),
)
def test_domain_file_has_root_domain_key(
    domain_file: Path,
) -> None:
    """Verify that each YAML file has a domain root key."""

    content = load_yaml_file(domain_file)

    assert "domain" in content
    assert isinstance(content["domain"], dict)


@pytest.mark.parametrize(
    "domain_file",
    get_domain_files(),
)
def test_domain_contains_required_fields(
    domain_file: Path,
) -> None:
    """Verify that each domain contains all required fields."""

    content = load_yaml_file(domain_file)
    domain = content["domain"]

    missing_fields = REQUIRED_DOMAIN_FIELDS - set(domain.keys())

    assert not missing_fields, (
        f"{domain_file.name} is missing required fields: " f"{sorted(missing_fields)}"
    )


@pytest.mark.parametrize(
    "domain_file",
    get_domain_files(),
)
def test_domain_has_valid_owner_and_steward(
    domain_file: Path,
) -> None:
    """Verify that ownership and stewardship are documented."""

    content = load_yaml_file(domain_file)
    domain = content["domain"]

    assert domain["data_owner"].get("role")
    assert domain["data_owner"].get("accountability")

    assert domain["data_steward"].get("role")
    assert domain["data_steward"].get("responsibility")


@pytest.mark.parametrize(
    "domain_file",
    get_domain_files(),
)
def test_domain_has_critical_data_elements(
    domain_file: Path,
) -> None:
    """Verify that each domain has complete critical elements."""

    content = load_yaml_file(domain_file)

    critical_elements = content["domain"]["critical_data_elements"]

    assert isinstance(critical_elements, list)
    assert len(critical_elements) >= 5

    required_element_fields = {
        "name",
        "definition",
        "classification",
        "quality_dimension",
        "quality_rule",
    }

    for element in critical_elements:
        missing_fields = required_element_fields - set(element.keys())

        assert not missing_fields, (
            f"{domain_file.name}: critical element "
            f"'{element.get('name', 'Unknown')}' "
            f"is missing {sorted(missing_fields)}"
        )


@pytest.mark.parametrize(
    "domain_file",
    get_domain_files(),
)
def test_domain_has_governance_kpis(
    domain_file: Path,
) -> None:
    """Verify that each domain has measurable governance KPIs."""

    content = load_yaml_file(domain_file)
    kpis = content["domain"]["governance_kpis"]

    assert isinstance(kpis, list)
    assert len(kpis) >= 4

    for kpi in kpis:
        assert kpi.get("name")
        assert kpi.get("target")


def test_raci_matrix_is_not_empty() -> None:
    """Verify that the RACI matrix contains activities."""

    _, rows = load_raci_rows()

    assert rows, "The RACI matrix contains no activities."
    assert len(rows) >= 40, "The RACI matrix should contain at least 40 activities."


def test_raci_matrix_has_expected_columns() -> None:
    """Verify that all required governance roles are present."""

    columns, _ = load_raci_rows()

    assert set(columns) == EXPECTED_RACI_COLUMNS


def test_raci_activities_are_unique() -> None:
    """Verify that no governance activity is duplicated."""

    _, rows = load_raci_rows()

    activities = [row["activity"] for row in rows]

    assert len(activities) == len(
        set(activities)
    ), "The RACI matrix contains duplicate activities."


def test_raci_activities_are_not_blank() -> None:
    """Verify that every row has an activity description."""

    _, rows = load_raci_rows()

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        assert row["activity"], f"RACI row {row_number} has no activity."


def test_raci_codes_are_valid() -> None:
    """Verify that all role assignments use R, A, C or I."""

    columns, rows = load_raci_rows()
    role_columns = [column for column in columns if column != "activity"]

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        for role in role_columns:
            code = row.get(role, "")

            assert code in VALID_RACI_CODES, (
                f"Invalid RACI code '{code}' in row " f"{row_number}, role '{role}'."
            )


def test_each_activity_has_one_accountable_role() -> None:
    """Verify that each activity has exactly one accountable role."""

    columns, rows = load_raci_rows()
    role_columns = [column for column in columns if column != "activity"]

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        accountable_roles = [role for role in role_columns if row.get(role) == "A"]

        assert len(accountable_roles) == 1, (
            f"RACI row {row_number} "
            f"('{row['activity']}') must have exactly "
            f"one accountable role. Found: "
            f"{accountable_roles}"
        )


def test_each_activity_has_responsible_role() -> None:
    """Verify that each activity has at least one responsible role."""

    columns, rows = load_raci_rows()
    role_columns = [column for column in columns if column != "activity"]

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        responsible_roles = [role for role in role_columns if row.get(role) == "R"]

        assert responsible_roles, (
            f"RACI row {row_number} "
            f"('{row['activity']}') has no "
            f"responsible role."
        )


def test_framework_documents_are_not_empty() -> None:
    """Verify that the core framework documents contain content."""

    expected_documents = {
        "organisation_context.md",
        "data_governance_charter.md",
        "governance_principles.md",
        "operating_model.md",
        "decision_rights.md",
        "governance_council_terms.md",
    }

    for document_name in expected_documents:
        document_path = FRAMEWORK_DIRECTORY / document_name

        assert document_path.exists(), f"{document_name} does not exist."

        content = document_path.read_text(
            encoding="utf-8",
        ).strip()

        assert content, f"{document_name} is empty."

        assert len(content) >= 500, (
            f"{document_name} does not contain " f"enough substantive content."
        )


def test_glossary_is_not_empty() -> None:
    """Verify that the glossary contains substantive content."""

    _, rows = load_glossary_rows()

    assert rows, "The business glossary contains no terms."

    assert len(rows) >= 40, "The business glossary should contain " "at least 40 terms."


def test_glossary_has_expected_columns() -> None:
    """Verify that all required metadata columns exist."""

    columns, _ = load_glossary_rows()

    assert set(columns) == EXPECTED_GLOSSARY_COLUMNS


def test_glossary_term_ids_are_unique() -> None:
    """Verify that glossary identifiers are unique."""

    _, rows = load_glossary_rows()

    term_ids = [row["term_id"] for row in rows]

    assert len(term_ids) == len(
        set(term_ids)
    ), "The glossary contains duplicate term identifiers."


def test_glossary_business_terms_are_unique() -> None:
    """Verify that approved business terms are unique."""

    _, rows = load_glossary_rows()

    business_terms = [row["business_term"].casefold() for row in rows]

    assert len(business_terms) == len(
        set(business_terms)
    ), "The glossary contains duplicate business terms."


def test_glossary_term_ids_are_sequential() -> None:
    """Verify that glossary identifiers follow BUS-001 format."""

    _, rows = load_glossary_rows()

    actual_ids = [row["term_id"] for row in rows]

    expected_ids = [
        f"BUS-{number:03d}"
        for number in range(
            1,
            len(rows) + 1,
        )
    ]

    assert actual_ids == expected_ids, (
        "Glossary identifiers must be sequential " "and use the BUS-001 format."
    )


def test_glossary_required_metadata_is_complete() -> None:
    """Verify that required glossary metadata is populated."""

    _, rows = load_glossary_rows()

    required_fields = {
        "term_id",
        "business_term",
        "definition",
        "data_domain",
        "data_owner",
        "data_steward",
        "authoritative_source",
        "sensitivity",
        "critical_data_element",
        "status",
        "quality_dimension",
    }

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        missing_fields = [field for field in required_fields if not row.get(field)]

        assert not missing_fields, (
            f"Glossary row {row_number} "
            f"('{row.get('business_term', 'Unknown')}') "
            f"is missing required metadata: "
            f"{sorted(missing_fields)}"
        )


def test_glossary_domains_are_valid_and_covered() -> None:
    """Verify valid domains and coverage of all five domains."""

    _, rows = load_glossary_rows()

    actual_domains = {row["data_domain"] for row in rows}

    invalid_domains = actual_domains - VALID_GLOSSARY_DOMAINS

    assert not invalid_domains, (
        "The glossary contains invalid data domains: " f"{sorted(invalid_domains)}"
    )

    missing_domains = REQUIRED_OPERATIONAL_DOMAINS - actual_domains

    assert not missing_domains, (
        "The glossary does not cover these required "
        f"data domains: {sorted(missing_domains)}"
    )


def test_glossary_statuses_are_valid() -> None:
    """Verify that glossary statuses use approved values."""

    _, rows = load_glossary_rows()

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        status = row["status"]

        assert status in VALID_GLOSSARY_STATUSES, (
            f"Invalid glossary status '{status}' " f"in row {row_number}."
        )


def test_glossary_sensitivity_values_are_valid() -> None:
    """Verify that sensitivity values are standardised."""

    _, rows = load_glossary_rows()

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        sensitivity = row["sensitivity"]

        assert sensitivity in VALID_SENSITIVITY_VALUES, (
            f"Invalid sensitivity value " f"'{sensitivity}' in row {row_number}."
        )


def test_glossary_critical_element_values_are_valid() -> None:
    """Verify that critical-element indicators use Yes or No."""

    _, rows = load_glossary_rows()

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        value = row["critical_data_element"]

        assert value in VALID_CRITICAL_ELEMENT_VALUES, (
            f"Invalid critical-data-element value " f"'{value}' in row {row_number}."
        )


def test_glossary_quality_dimensions_are_valid() -> None:
    """Verify that quality dimensions use approved terminology."""

    _, rows = load_glossary_rows()

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        quality_dimension = row["quality_dimension"]

        assert quality_dimension in VALID_QUALITY_DIMENSIONS, (
            f"Invalid quality dimension "
            f"'{quality_dimension}' "
            f"in row {row_number}."
        )


def test_expected_governance_standards_exist() -> None:
    """Verify that all required governance standards exist."""

    actual_files = {file.name for file in STANDARDS_DIRECTORY.glob("*.md")}

    missing_files = EXPECTED_STANDARD_FILES - actual_files

    assert not missing_files, (
        "The following governance standards are missing: " f"{sorted(missing_files)}"
    )


@pytest.mark.parametrize(
    "standard_name",
    sorted(EXPECTED_STANDARD_FILES),
)
def test_governance_standard_is_substantive(
    standard_name: str,
) -> None:
    """Verify that each standard contains substantive content."""

    standard_path = STANDARDS_DIRECTORY / standard_name

    assert standard_path.exists(), f"{standard_name} does not exist."

    content = standard_path.read_text(
        encoding="utf-8",
    ).strip()

    assert content, f"{standard_name} is empty."

    assert len(content) >= 2_000, (
        f"{standard_name} does not contain " "enough substantive content."
    )


@pytest.mark.parametrize(
    "standard_name",
    sorted(EXPECTED_STANDARD_FILES),
)
def test_governance_standard_has_required_sections(
    standard_name: str,
) -> None:
    """Verify that each standard includes core sections."""

    standard_path = STANDARDS_DIRECTORY / standard_name

    content = standard_path.read_text(
        encoding="utf-8",
    )

    missing_sections = {
        section for section in REQUIRED_STANDARD_SECTIONS if section not in content
    }

    assert not missing_sections, (
        f"{standard_name} is missing required sections: " f"{sorted(missing_sections)}"
    )


def test_governance_standards_have_unique_titles() -> None:
    """Verify that each standard has a unique H1 title."""

    titles = []

    for standard_name in sorted(EXPECTED_STANDARD_FILES):
        standard_path = STANDARDS_DIRECTORY / standard_name

        lines = standard_path.read_text(
            encoding="utf-8",
        ).splitlines()

        title = next(
            (line.strip() for line in lines if line.startswith("# ")),
            "",
        )

        assert title, f"{standard_name} has no H1 title."

        titles.append(title)

    assert len(titles) == len(set(titles)), (
        "Two or more governance standards " "have the same title."
    )


def test_governance_standards_include_disclaimer() -> None:
    """Verify that standards identify the fictional context."""

    required_phrase = "fictional portfolio project"

    for standard_name in sorted(EXPECTED_STANDARD_FILES):
        standard_path = STANDARDS_DIRECTORY / standard_name

        content = standard_path.read_text(
            encoding="utf-8",
        ).lower()

        assert required_phrase in content, (
            f"{standard_name} does not include " "the portfolio disclaimer."
        )


def test_exact_governance_workflows_exist() -> None:
    """Verify that the four required workflow files exist."""

    actual_files = {file.name for file in WORKFLOWS_DIRECTORY.glob("*.md")}

    missing_files = EXPECTED_WORKFLOW_FILES - actual_files

    unexpected_files = actual_files - EXPECTED_WORKFLOW_FILES

    assert not missing_files, (
        "The following governance workflows are missing: " f"{sorted(missing_files)}"
    )

    assert not unexpected_files, (
        "Unexpected workflow files were found: " f"{sorted(unexpected_files)}"
    )


@pytest.mark.parametrize(
    "workflow_name",
    sorted(EXPECTED_WORKFLOW_FILES),
)
def test_governance_workflow_is_substantive(
    workflow_name: str,
) -> None:
    """Verify that each workflow contains substantive content."""

    workflow_path = WORKFLOWS_DIRECTORY / workflow_name

    assert workflow_path.exists(), f"{workflow_name} does not exist."

    content = workflow_path.read_text(
        encoding="utf-8",
    ).strip()

    assert content, f"{workflow_name} is empty."

    assert len(content) >= 2_000, (
        f"{workflow_name} does not contain " "enough substantive content."
    )


@pytest.mark.parametrize(
    "workflow_name",
    sorted(EXPECTED_WORKFLOW_FILES),
)
def test_governance_workflow_has_required_sections(
    workflow_name: str,
) -> None:
    """Verify that each workflow includes its core sections."""

    workflow_path = WORKFLOWS_DIRECTORY / workflow_name

    content = workflow_path.read_text(
        encoding="utf-8",
    )

    missing_sections = {
        section for section in REQUIRED_WORKFLOW_SECTIONS if section not in content
    }

    assert not missing_sections, (
        f"{workflow_name} is missing required sections: " f"{sorted(missing_sections)}"
    )


def test_governance_workflows_have_unique_titles() -> None:
    """Verify that every workflow has a unique H1 title."""

    titles = []

    for workflow_name in sorted(EXPECTED_WORKFLOW_FILES):
        workflow_path = WORKFLOWS_DIRECTORY / workflow_name

        lines = workflow_path.read_text(
            encoding="utf-8",
        ).splitlines()

        title = next(
            (line.strip() for line in lines if line.startswith("# ")),
            "",
        )

        assert title, f"{workflow_name} has no H1 title."

        titles.append(title)

    assert len(titles) == len(set(titles)), (
        "Two or more governance workflows " "have the same title."
    )


def test_governance_workflows_include_disclaimer() -> None:
    """Verify that workflows identify the fictional context."""

    required_phrase = "fictional portfolio project"

    for workflow_name in sorted(EXPECTED_WORKFLOW_FILES):
        workflow_path = WORKFLOWS_DIRECTORY / workflow_name

        content = workflow_path.read_text(
            encoding="utf-8",
        ).lower()

        assert required_phrase in content, (
            f"{workflow_name} does not include " "the portfolio disclaimer."
        )


def test_data_quality_rules_have_expected_columns() -> None:
    """Verify the structure of the rules register."""

    columns, _ = load_data_quality_rule_rows()

    assert set(columns) == EXPECTED_DATA_QUALITY_RULE_COLUMNS


def test_data_quality_rules_contain_twenty_rules() -> None:
    """Verify that the register contains twenty rules."""

    _, rows = load_data_quality_rule_rows()

    assert len(rows) == 20, (
        "The Data Quality Rules Register must " "contain exactly 20 rules."
    )


def test_data_quality_rule_ids_are_unique_and_valid() -> None:
    """Verify that rule identifiers are unique and well formed."""

    _, rows = load_data_quality_rule_rows()

    rule_ids = [row["rule_id"] for row in rows]

    assert len(rule_ids) == len(
        set(rule_ids)
    ), "The register contains duplicate rule identifiers."

    for rule_id in rule_ids:
        parts = rule_id.split("-")

        assert len(parts) == 3, f"Invalid rule identifier: {rule_id}"

        assert parts[0] == "DQ", f"Rule identifier must begin with DQ: {rule_id}"

        assert (
            parts[1] in VALID_DATA_QUALITY_RULE_PREFIXES
        ), f"Invalid domain prefix in rule identifier: {rule_id}"

        assert (
            len(parts[2]) == 3 and parts[2].isdigit()
        ), f"Invalid numeric suffix in rule identifier: {rule_id}"


def test_data_quality_rules_have_complete_metadata() -> None:
    """Verify that every rule has complete mandatory metadata."""

    _, rows = load_data_quality_rule_rows()

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        empty_fields = [
            column
            for column in EXPECTED_DATA_QUALITY_RULE_COLUMNS
            if not row.get(column)
        ]

        assert not empty_fields, (
            f"Data Quality Rule row {row_number} "
            f"is missing values in: {sorted(empty_fields)}"
        )


def test_data_quality_rules_use_controlled_values() -> None:
    """Verify domains and controlled values."""

    _, rows = load_data_quality_rule_rows()

    for row in rows:
        assert row["data_domain"] in EXPECTED_DATA_QUALITY_RULE_DOMAINS

        assert row["quality_dimension"] in VALID_QUALITY_DIMENSIONS

        assert row["frequency"] in VALID_DATA_QUALITY_FREQUENCIES

        assert row["failure_severity"] in VALID_FAILURE_SEVERITIES

        assert row["status"] in VALID_DATA_QUALITY_RULE_STATUSES


def test_data_quality_rule_thresholds_are_valid() -> None:
    """Verify percentage bounds and threshold ordering."""

    _, rows = load_data_quality_rule_rows()

    for row in rows:
        target = float(row["target_percentage"])
        warning = float(row["warning_threshold_percentage"])
        critical = float(row["critical_threshold_percentage"])

        assert 0 <= critical <= 100
        assert 0 <= warning <= 100
        assert 0 <= target <= 100

        assert (
            target >= warning >= critical
        ), f"{row['rule_id']} has invalid threshold ordering."


def test_each_domain_has_exactly_four_quality_rules() -> None:
    """Verify balanced rule coverage across all domains."""

    _, rows = load_data_quality_rule_rows()

    domain_counts = {domain: 0 for domain in EXPECTED_DATA_QUALITY_RULE_DOMAINS}

    for row in rows:
        domain_counts[row["data_domain"]] += 1

    assert set(domain_counts) == (EXPECTED_DATA_QUALITY_RULE_DOMAINS)

    for domain, count in domain_counts.items():
        assert count == 4, (
            f"{domain} must contain exactly four "
            f"Data Quality Rules, but contains {count}."
        )


def test_data_quality_rules_reference_glossary_terms() -> None:
    """Verify that every governed term exists in the glossary."""

    _, rule_rows = load_data_quality_rule_rows()
    _, glossary_rows = load_glossary_rows()

    glossary_terms = {row["business_term"].casefold() for row in glossary_rows}

    missing_terms = {
        row["business_term"]
        for row in rule_rows
        if row["business_term"].casefold() not in glossary_terms
    }

    assert not missing_terms, (
        "The following Data Quality Rule terms are "
        "missing from the business glossary: "
        f"{sorted(missing_terms)}"
    )


def test_governance_issues_have_expected_columns() -> None:
    """Verify the structure of the issues register."""

    columns, _ = load_governance_issue_rows()

    assert len(columns) == len(set(columns)), (
        "The Governance Issues Register has " "duplicate column names."
    )

    assert set(columns) == EXPECTED_GOVERNANCE_ISSUE_COLUMNS


def test_governance_issues_contain_ten_issues() -> None:
    """Verify that the register contains ten issues."""

    _, rows = load_governance_issue_rows()

    assert len(rows) == 10, (
        "The Governance Issues Register must " "contain exactly 10 issues."
    )


def test_governance_issue_ids_are_unique_and_sequential() -> None:
    """Verify unique sequential issue identifiers."""

    _, rows = load_governance_issue_rows()

    actual_ids = [row["issue_id"] for row in rows]

    expected_ids = [
        f"ISSUE-2026-{number:03d}"
        for number in range(
            1,
            len(rows) + 1,
        )
    ]

    assert len(actual_ids) == len(
        set(actual_ids)
    ), "The register contains duplicate Issue IDs."

    assert actual_ids == expected_ids, (
        "Issue IDs must be sequential and use " "the ISSUE-2026-001 format."
    )


def test_governance_issues_have_complete_metadata() -> None:
    """Verify that mandatory issue metadata is populated."""

    _, rows = load_governance_issue_rows()

    optional_fields = {
        "additional_domains",
        "related_rule_id",
        "next_review_date",
        "closure_date",
    }

    required_fields = EXPECTED_GOVERNANCE_ISSUE_COLUMNS - optional_fields

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        empty_fields = [field for field in required_fields if not row.get(field)]

        assert not empty_fields, (
            f"Governance issue row {row_number} "
            f"is missing values in: {sorted(empty_fields)}"
        )


def test_governance_issues_use_controlled_values() -> None:
    """Verify controlled issue metadata values."""

    _, rows = load_governance_issue_rows()

    for row in rows:
        assert (
            row["primary_domain"] in VALID_ISSUE_DOMAINS
        ), f"{row['issue_id']} has an invalid primary domain."

        additional_domain = row["additional_domains"]

        if additional_domain:
            assert additional_domain in VALID_ISSUE_DOMAINS, (
                f"{row['issue_id']} has an invalid " "additional domain."
            )

            assert additional_domain != row["primary_domain"], (
                f"{row['issue_id']} repeats its primary domain "
                "as an additional domain."
            )

        assert (
            row["issue_category"] in VALID_ISSUE_CATEGORIES
        ), f"{row['issue_id']} has an invalid issue category."

        assert (
            row["severity"] in VALID_ISSUE_SEVERITIES
        ), f"{row['issue_id']} has an invalid severity."

        assert (
            row["status"] in VALID_ISSUE_STATUSES
        ), f"{row['issue_id']} has an invalid status."

        assert (
            row["root_cause"] in VALID_ROOT_CAUSES
        ), f"{row['issue_id']} has an invalid root cause."

        assert row["critical_data_element"] in VALID_CRITICAL_ELEMENT_VALUES, (
            f"{row['issue_id']} has an invalid " "critical-data-element value."
        )

        assert row["data_classification"] in VALID_SENSITIVITY_VALUES, (
            f"{row['issue_id']} has an invalid " "data classification."
        )


def test_governance_issue_dates_are_valid() -> None:
    """Verify ISO dates and logical date ordering."""

    _, rows = load_governance_issue_rows()

    date_fields = {
        "date_identified",
        "target_date",
        "last_review_date",
        "next_review_date",
        "closure_date",
    }

    for row in rows:
        parsed_dates = {}

        for field in date_fields:
            value = row[field]

            if value:
                try:
                    parsed_dates[field] = date.fromisoformat(value)
                except ValueError as error:
                    raise AssertionError(
                        f"{row['issue_id']} has an invalid " f"{field}: {value}"
                    ) from error

        identified = parsed_dates["date_identified"]
        target = parsed_dates["target_date"]
        last_review = parsed_dates["last_review_date"]

        assert target >= identified, (
            f"{row['issue_id']} has a target date " "before its identification date."
        )

        assert last_review >= identified, (
            f"{row['issue_id']} has a last review date "
            "before its identification date."
        )

        if "next_review_date" in parsed_dates:
            assert parsed_dates["next_review_date"] >= last_review, (
                f"{row['issue_id']} has a next review date "
                "before its last review date."
            )

        if "closure_date" in parsed_dates:
            assert parsed_dates["closure_date"] >= identified, (
                f"{row['issue_id']} has a closure date "
                "before its identification date."
            )


def test_governance_issue_closure_fields_match_status() -> None:
    """Verify that closure and review dates match issue status."""

    _, rows = load_governance_issue_rows()

    for row in rows:
        if row["status"] == "Closed":
            assert row["closure_date"], (
                f"{row['issue_id']} is Closed but " "has no closure date."
            )

            assert not row["next_review_date"], (
                f"{row['issue_id']} is Closed but " "still has a next review date."
            )
        else:
            assert not row["closure_date"], (
                f"{row['issue_id']} is not Closed but " "has a closure date."
            )

            assert row["next_review_date"], (
                f"{row['issue_id']} is open but " "has no next review date."
            )


def test_governance_issues_reference_valid_quality_rules() -> None:
    """Verify related Data Quality Rule references."""

    _, issue_rows = load_governance_issue_rows()
    _, rule_rows = load_data_quality_rule_rows()

    valid_rule_ids = {row["rule_id"] for row in rule_rows}

    invalid_references = {
        row["related_rule_id"]
        for row in issue_rows
        if row["related_rule_id"] and row["related_rule_id"] not in valid_rule_ids
    }

    assert not invalid_references, (
        "The following related Data Quality Rules "
        f"do not exist: {sorted(invalid_references)}"
    )


def test_governance_issue_elements_exist_in_glossary() -> None:
    """Verify that affected data elements are governed terms."""

    _, issue_rows = load_governance_issue_rows()
    _, glossary_rows = load_glossary_rows()

    glossary_terms = {row["business_term"].casefold() for row in glossary_rows}

    missing_terms = {
        row["affected_data_element"]
        for row in issue_rows
        if row["affected_data_element"].casefold() not in glossary_terms
    }

    assert not missing_terms, (
        "The following affected data elements are "
        "missing from the business glossary: "
        f"{sorted(missing_terms)}"
    )


def test_governance_issues_cover_all_operational_domains() -> None:
    """Verify issue coverage across all operational domains."""

    _, rows = load_governance_issue_rows()

    represented_domains = {row["primary_domain"] for row in rows}

    represented_domains.update(
        row["additional_domains"] for row in rows if row["additional_domains"]
    )

    missing_domains = REQUIRED_OPERATIONAL_DOMAINS - represented_domains

    assert not missing_domains, (
        "The issues register does not cover these "
        f"operational domains: {sorted(missing_domains)}"
    )


def test_access_exceptions_have_expected_columns() -> None:
    """Verify the structure of the exceptions register."""

    columns, _ = load_access_exception_rows()

    assert len(columns) == len(set(columns)), (
        "The Access Exceptions Register has " "duplicate column names."
    )

    assert set(columns) == EXPECTED_ACCESS_EXCEPTION_COLUMNS


def test_access_exceptions_contain_eight_records() -> None:
    """Verify that the register contains eight exceptions."""

    _, rows = load_access_exception_rows()

    assert len(rows) == 8, (
        "The Access Exceptions Register must " "contain exactly 8 exceptions."
    )


def test_access_exception_ids_are_unique_and_sequential() -> None:
    """Verify unique sequential exception identifiers."""

    _, rows = load_access_exception_rows()

    actual_ids = [row["exception_id"] for row in rows]

    expected_ids = [
        f"ACCESS-EXC-2026-{number:03d}"
        for number in range(
            1,
            len(rows) + 1,
        )
    ]

    assert len(actual_ids) == len(
        set(actual_ids)
    ), "The register contains duplicate Exception IDs."

    assert actual_ids == expected_ids, (
        "Exception IDs must be sequential and use " "the ACCESS-EXC-2026-001 format."
    )


def test_access_exceptions_have_complete_metadata() -> None:
    """Verify that mandatory exception metadata is populated."""

    _, rows = load_access_exception_rows()

    optional_fields = {
        "next_review_date",
        "revocation_date",
        "closure_date",
    }

    required_fields = EXPECTED_ACCESS_EXCEPTION_COLUMNS - optional_fields

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        empty_fields = [field for field in required_fields if not row.get(field)]

        assert not empty_fields, (
            f"Access exception row {row_number} "
            f"is missing values in: {sorted(empty_fields)}"
        )


def test_access_exceptions_use_controlled_values() -> None:
    """Verify controlled exception metadata values."""

    _, rows = load_access_exception_rows()

    for row in rows:
        exception_id = row["exception_id"]

        assert row["access_recipient_type"] in VALID_ACCESS_RECIPIENT_TYPES, (
            f"{exception_id} has an invalid " "access-recipient type."
        )

        assert (
            row["data_domain"] in REQUIRED_OPERATIONAL_DOMAINS
        ), f"{exception_id} has an invalid data domain."

        assert row["data_classification"] in VALID_SENSITIVITY_VALUES, (
            f"{exception_id} has an invalid " "data classification."
        )

        assert (
            row["access_level"] in VALID_ACCESS_LEVELS
        ), f"{exception_id} has an invalid access level."

        assert (
            row["risk_level"] in VALID_ACCESS_RISK_LEVELS
        ), f"{exception_id} has an invalid risk level."

        assert (
            row["status"] in VALID_ACCESS_EXCEPTION_STATUSES
        ), f"{exception_id} has an invalid status."

        boolean_fields = {
            "segregation_conflict",
            "external_access",
            "production_data_outside_production",
        }

        for field in boolean_fields:
            assert row[field] in VALID_ACCESS_EXCEPTION_BOOLEAN_VALUES, (
                f"{exception_id} has an invalid " f"{field} value."
            )


def test_access_exception_dates_are_valid() -> None:
    """Verify ISO dates and logical date ordering."""

    _, rows = load_access_exception_rows()

    date_fields = {
        "request_date",
        "start_date",
        "expiry_date",
        "last_review_date",
        "next_review_date",
        "revocation_date",
        "closure_date",
    }

    for row in rows:
        parsed_dates = {}

        for field in date_fields:
            value = row[field]

            if value:
                try:
                    parsed_dates[field] = date.fromisoformat(value)
                except ValueError as error:
                    raise AssertionError(
                        f"{row['exception_id']} has an " f"invalid {field}: {value}"
                    ) from error

        request_date = parsed_dates["request_date"]
        start_date = parsed_dates["start_date"]
        expiry_date = parsed_dates["expiry_date"]
        last_review_date = parsed_dates["last_review_date"]

        assert start_date >= request_date, (
            f"{row['exception_id']} starts before " "the request date."
        )

        assert expiry_date >= start_date, (
            f"{row['exception_id']} expires before " "the start date."
        )

        assert last_review_date >= request_date, (
            f"{row['exception_id']} has a last review " "before the request date."
        )

        if "next_review_date" in parsed_dates:
            assert parsed_dates["next_review_date"] >= last_review_date, (
                f"{row['exception_id']} has a next review " "before the last review."
            )

        if "revocation_date" in parsed_dates:
            assert parsed_dates["revocation_date"] >= start_date, (
                f"{row['exception_id']} was revoked " "before access started."
            )

        if "closure_date" in parsed_dates:
            assert parsed_dates["closure_date"] >= request_date, (
                f"{row['exception_id']} was closed " "before it was requested."
            )

            if "revocation_date" in parsed_dates:
                assert (
                    parsed_dates["closure_date"] >= parsed_dates["revocation_date"]
                ), (f"{row['exception_id']} was closed " "before access was revoked.")


def test_access_exception_dates_match_status() -> None:
    """Verify lifecycle dates against exception status."""

    _, rows = load_access_exception_rows()

    for row in rows:
        exception_id = row["exception_id"]
        status = row["status"]

        if status == "Closed":
            assert row["revocation_date"], (
                f"{exception_id} is Closed but has " "no revocation date."
            )

            assert row["closure_date"], (
                f"{exception_id} is Closed but has " "no closure date."
            )

            assert not row["next_review_date"], (
                f"{exception_id} is Closed but still " "has a next review date."
            )

        else:
            assert not row["closure_date"], (
                f"{exception_id} is not Closed but " "has a closure date."
            )

        if status == "Rejected":
            assert not row["next_review_date"], (
                f"{exception_id} is Rejected but has " "a next review date."
            )

            assert not row["revocation_date"], (
                f"{exception_id} is Rejected but has " "a revocation date."
            )

        if status in ACCESS_STATUSES_REQUIRING_REVIEW:
            assert row["next_review_date"], (
                f"{exception_id} requires ongoing review "
                "but has no next review date."
            )


def test_access_exception_renewal_counts_are_valid() -> None:
    """Verify renewal counts and renewal status."""

    _, rows = load_access_exception_rows()

    for row in rows:
        value = row["renewal_count"]

        try:
            renewal_count = int(value)
        except ValueError as error:
            raise AssertionError(
                f"{row['exception_id']} has an invalid " f"renewal count: {value}"
            ) from error

        assert renewal_count >= 0, (
            f"{row['exception_id']} has a negative " "renewal count."
        )

        if row["status"] == "Renewal Under Review":
            assert renewal_count >= 1, (
                f"{row['exception_id']} is under renewal "
                "review but has no prior renewal."
            )


def test_high_risk_access_exceptions_have_controls() -> None:
    """Verify controls for high-risk exceptions."""

    _, rows = load_access_exception_rows()

    for row in rows:
        exception_id = row["exception_id"]

        if row["risk_level"] == "High" and row["status"] != "Rejected":
            assert row["compensating_controls"].casefold() != "none proposed", (
                f"{exception_id} is High risk but has " "no compensating controls."
            )

        if row["segregation_conflict"] == "Yes":
            assert row["risk_level"] == "High", (
                f"{exception_id} has a segregation " "conflict but is not High risk."
            )

        if row["production_data_outside_production"] == "Yes":
            assert row["risk_level"] == "High", (
                f"{exception_id} uses production data "
                "outside production but is not High risk."
            )


def test_access_exceptions_cover_all_operational_domains() -> None:
    """Verify coverage across all operational domains."""

    _, rows = load_access_exception_rows()

    represented_domains = {row["data_domain"] for row in rows}

    missing_domains = REQUIRED_OPERATIONAL_DOMAINS - represented_domains

    assert not missing_domains, (
        "The Access Exceptions Register does not cover "
        f"these domains: {sorted(missing_domains)}"
    )


def test_ai_use_cases_have_expected_columns() -> None:
    """Verify the structure of the AI Use Cases Register."""

    columns, _ = load_ai_use_case_rows()

    assert len(columns) == len(set(columns)), (
        "The AI Use Cases Register has " "duplicate column names."
    )

    assert set(columns) == EXPECTED_AI_USE_CASE_COLUMNS


def test_ai_use_cases_contain_six_records() -> None:
    """Verify that the register contains six use cases."""

    _, rows = load_ai_use_case_rows()

    assert len(rows) == 6, (
        "The AI Use Cases Register must " "contain exactly 6 use cases."
    )


def test_ai_use_case_ids_are_unique_and_sequential() -> None:
    """Verify identifiers and unique use-case metadata."""

    _, rows = load_ai_use_case_rows()

    actual_ids = [row["use_case_id"] for row in rows]

    expected_ids = [
        f"AI-UC-2026-{number:03d}"
        for number in range(
            1,
            len(rows) + 1,
        )
    ]

    use_case_names = [row["use_case_name"].casefold() for row in rows]

    dataset_versions = [row["dataset_version"] for row in rows]

    assert len(actual_ids) == len(
        set(actual_ids)
    ), "The register contains duplicate AI Use Case IDs."

    assert actual_ids == expected_ids, (
        "AI Use Case IDs must be sequential and use " "the AI-UC-2026-001 format."
    )

    assert len(use_case_names) == len(
        set(use_case_names)
    ), "The register contains duplicate use-case names."

    assert len(dataset_versions) == len(
        set(dataset_versions)
    ), "The register contains duplicate dataset versions."


def test_ai_use_cases_have_complete_metadata() -> None:
    """Verify that mandatory use-case metadata is populated."""

    _, rows = load_ai_use_case_rows()

    optional_fields = {
        "additional_domains",
        "approval_date",
        "related_issue_id",
    }

    required_fields = EXPECTED_AI_USE_CASE_COLUMNS - optional_fields

    for row_number, row in enumerate(
        rows,
        start=2,
    ):
        empty_fields = [field for field in required_fields if not row.get(field)]

        assert not empty_fields, (
            f"AI use-case row {row_number} "
            f"is missing values in: {sorted(empty_fields)}"
        )


def test_ai_use_cases_use_controlled_values() -> None:
    """Verify controlled AI use-case metadata values."""

    _, rows = load_ai_use_case_rows()

    for row in rows:
        use_case_id = row["use_case_id"]

        assert (
            row["ai_risk_tier"] in VALID_AI_RISK_TIERS
        ), f"{use_case_id} has an invalid AI risk tier."

        assert (
            row["primary_domain"] in REQUIRED_OPERATIONAL_DOMAINS
        ), f"{use_case_id} has an invalid primary domain."

        additional_domain = row["additional_domains"]

        if additional_domain:
            assert additional_domain in REQUIRED_OPERATIONAL_DOMAINS, (
                f"{use_case_id} has an invalid " "additional domain."
            )

            assert additional_domain != row["primary_domain"], (
                f"{use_case_id} repeats its primary " "domain as an additional domain."
            )

        assert row["degree_of_automation"] in VALID_AUTOMATION_LEVELS, (
            f"{use_case_id} has an invalid " "degree of automation."
        )

        assert row["data_classification"] in VALID_SENSITIVITY_VALUES, (
            f"{use_case_id} has an invalid " "data classification."
        )

        boolean_fields = {
            "personal_data",
            "sensitive_personal_data",
            "restricted_data",
            "external_processing",
        }

        for field in boolean_fields:
            assert row[field] in VALID_AI_BOOLEAN_VALUES, (
                f"{use_case_id} has an invalid " f"{field} value."
            )

        assert row["lineage_status"] in VALID_LINEAGE_STATUSES, (
            f"{use_case_id} has an invalid " "lineage status."
        )

        assert row["data_quality_status"] in VALID_AI_DATA_QUALITY_STATUSES, (
            f"{use_case_id} has an invalid " "data-quality status."
        )

        assert row["monitoring_frequency"] in VALID_AI_MONITORING_FREQUENCIES, (
            f"{use_case_id} has an invalid " "monitoring frequency."
        )

        assert row["approval_decision"] in VALID_AI_APPROVAL_DECISIONS, (
            f"{use_case_id} has an invalid " "approval decision."
        )

        assert (
            row["status"] in VALID_AI_USE_CASE_STATUSES
        ), f"{use_case_id} has an invalid status."


def test_ai_use_case_dates_are_valid() -> None:
    """Verify ISO dates and review-date ordering."""

    _, rows = load_ai_use_case_rows()

    for row in rows:
        use_case_id = row["use_case_id"]

        try:
            next_review_date = date.fromisoformat(row["next_review_date"])
        except ValueError as error:
            raise AssertionError(
                f"{use_case_id} has an invalid "
                f"next review date: "
                f"{row['next_review_date']}"
            ) from error

        approval_date_value = row["approval_date"]

        if approval_date_value:
            try:
                approval_date = date.fromisoformat(approval_date_value)
            except ValueError as error:
                raise AssertionError(
                    f"{use_case_id} has an invalid "
                    f"approval date: {approval_date_value}"
                ) from error

            assert next_review_date >= approval_date, (
                f"{use_case_id} has a next review date " "before its approval date."
            )


def test_ai_use_case_decisions_match_statuses() -> None:
    """Verify approval decisions and lifecycle statuses."""

    _, rows = load_ai_use_case_rows()

    for row in rows:
        use_case_id = row["use_case_id"]
        decision = row["approval_decision"]
        status = row["status"]

        if status == "Ready":
            assert decision == "Ready", (
                f"{use_case_id} is Ready but has " f"decision '{decision}'."
            )

            assert row["approval_date"], (
                f"{use_case_id} is Ready but has " "no approval date."
            )

        if status == "Conditionally Ready":
            assert decision == "Conditionally Ready", (
                f"{use_case_id} is Conditionally Ready "
                f"but has decision '{decision}'."
            )

            assert row["approval_date"], (
                f"{use_case_id} is Conditionally Ready " "but has no approval date."
            )

        if status == "Not Ready":
            assert decision == "Not Ready", (
                f"{use_case_id} is Not Ready but has " f"decision '{decision}'."
            )

            assert not row["approval_date"], (
                f"{use_case_id} is Not Ready but has " "an approval date."
            )

        if status == "Suspended":
            assert decision == "Not Ready", (
                f"{use_case_id} is Suspended but does " "not have a Not Ready decision."
            )

            assert row["approval_date"], (
                f"{use_case_id} is Suspended but has " "no previous approval date."
            )


def test_ai_readiness_scores_match_decisions() -> None:
    """Verify readiness-score ranges and quality outcomes."""

    _, rows = load_ai_use_case_rows()

    for row in rows:
        use_case_id = row["use_case_id"]

        try:
            score = float(row["readiness_score"])
        except ValueError as error:
            raise AssertionError(
                f"{use_case_id} has an invalid "
                f"readiness score: {row['readiness_score']}"
            ) from error

        assert 0 <= score <= 100, (
            f"{use_case_id} has a readiness score " "outside the 0 to 100 range."
        )

        decision = row["approval_decision"]
        quality_status = row["data_quality_status"]

        if decision == "Ready":
            assert score >= 85, f"{use_case_id} is Ready but its " "score is below 85."

            assert quality_status != "Red", (
                f"{use_case_id} is Ready despite " "a Red data-quality status."
            )

        elif decision == "Conditionally Ready":
            assert 70 <= score < 85, (
                f"{use_case_id} is Conditionally Ready "
                "but its score is outside 70 to 84.99."
            )

            assert quality_status != "Red", (
                f"{use_case_id} is Conditionally Ready "
                "despite a Red data-quality status."
            )

        elif decision == "Not Ready":
            assert score < 70, (
                f"{use_case_id} is Not Ready but its " "score is not below 70."
            )

            assert quality_status == "Red", (
                f"{use_case_id} is Not Ready but does "
                "not have a Red data-quality status."
            )


def test_ai_data_classification_matches_flags() -> None:
    """Verify classification and personal-data indicators."""

    _, rows = load_ai_use_case_rows()

    for row in rows:
        use_case_id = row["use_case_id"]
        classification = row["data_classification"]

        if row["sensitive_personal_data"] == "Yes":
            assert row["personal_data"] == "Yes", (
                f"{use_case_id} uses Sensitive Personal "
                "data but personal_data is not Yes."
            )

        if classification == "Sensitive Personal":
            assert row["personal_data"] == "Yes", (
                f"{use_case_id} is classified as "
                "Sensitive Personal but personal_data "
                "is not Yes."
            )

            assert row["sensitive_personal_data"] == "Yes", (
                f"{use_case_id} is classified as "
                "Sensitive Personal but the sensitive "
                "data flag is not Yes."
            )

        if classification == "Restricted":
            assert row["restricted_data"] == "Yes", (
                f"{use_case_id} is Restricted but " "restricted_data is not Yes."
            )

        if row["restricted_data"] == "Yes":
            assert classification == "Restricted", (
                f"{use_case_id} has restricted_data Yes "
                "but is not classified as Restricted."
            )

        if row["ai_risk_tier"] == "Tier 1":
            assert row["sensitive_personal_data"] == "No", (
                f"{use_case_id} is Tier 1 but uses " "Sensitive Personal data."
            )

            assert row["restricted_data"] == "No", (
                f"{use_case_id} is Tier 1 but uses " "Restricted data."
            )


def test_ai_use_cases_reference_valid_issues() -> None:
    """Verify linked Governance Issue references."""

    _, use_case_rows = load_ai_use_case_rows()
    _, issue_rows = load_governance_issue_rows()

    valid_issue_ids = {row["issue_id"] for row in issue_rows}

    invalid_references = {
        row["related_issue_id"]
        for row in use_case_rows
        if row["related_issue_id"] and row["related_issue_id"] not in valid_issue_ids
    }

    assert not invalid_references, (
        "The following related Governance Issues "
        f"do not exist: {sorted(invalid_references)}"
    )


def test_ai_use_cases_cover_all_operational_domains() -> None:
    """Verify AI use-case coverage across all domains."""

    _, rows = load_ai_use_case_rows()

    represented_domains = {row["primary_domain"] for row in rows}

    represented_domains.update(
        row["additional_domains"] for row in rows if row["additional_domains"]
    )

    missing_domains = REQUIRED_OPERATIONAL_DOMAINS - represented_domains

    assert not missing_domains, (
        "The AI Use Cases Register does not cover "
        f"these domains: {sorted(missing_domains)}"
    )


@pytest.mark.parametrize(
    (
        "register_name",
        "file_path",
        "expected_columns",
    ),
    [
        (
            "Business Glossary",
            GLOSSARY_FILE,
            EXPECTED_GLOSSARY_COLUMNS,
        ),
        (
            "Data Quality Rules Register",
            DATA_QUALITY_RULES_FILE,
            EXPECTED_DATA_QUALITY_RULE_COLUMNS,
        ),
        (
            "Governance Issues Register",
            GOVERNANCE_ISSUES_FILE,
            EXPECTED_GOVERNANCE_ISSUE_COLUMNS,
        ),
        (
            "Access Exceptions Register",
            ACCESS_EXCEPTIONS_FILE,
            EXPECTED_ACCESS_EXCEPTION_COLUMNS,
        ),
        (
            "AI Use Cases Register",
            AI_USE_CASES_FILE,
            EXPECTED_AI_USE_CASE_COLUMNS,
        ),
    ],
    ids=[
        "business_glossary",
        "data_quality_rules",
        "governance_issues",
        "access_exceptions",
        "ai_use_cases",
    ],
)
def test_csv_register_rows_have_exact_field_count(
    register_name: str,
    file_path: Path,
    expected_columns: set[str],
) -> None:
    """Reject CSV rows with missing or surplus fields."""

    assert file_path.exists(), f"{register_name} does not exist: {file_path}"

    with file_path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        rows = list(csv.reader(file))

    assert rows, f"{register_name} is empty."

    header = rows[0]

    assert len(header) == len(expected_columns), (
        f"{register_name} header contains "
        f"{len(header)} fields instead of "
        f"{len(expected_columns)}."
    )

    assert len(header) == len(set(header)), (
        f"{register_name} contains duplicate " "column names."
    )

    assert set(header) == expected_columns, (
        f"{register_name} does not contain " "the expected columns."
    )

    for line_number, row in enumerate(
        rows[1:],
        start=2,
    ):
        assert len(row) == len(header), (
            f"{register_name}, line {line_number}, "
            f"contains {len(row)} fields instead of "
            f"{len(header)}."
        )

import csv
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

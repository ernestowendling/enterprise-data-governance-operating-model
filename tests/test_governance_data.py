import csv
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOMAINS_DIRECTORY = PROJECT_ROOT / "domains"
FRAMEWORK_DIRECTORY = PROJECT_ROOT / "framework"
RACI_FILE = PROJECT_ROOT / "roles" / "raci_matrix.csv"

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

from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOMAINS_DIRECTORY = PROJECT_ROOT / "domains"

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


def load_yaml_file(file_path: Path) -> dict:
    """Load a YAML file and return its contents."""

    with file_path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    assert content is not None, f"{file_path.name} is empty."
    assert isinstance(content, dict), f"{file_path.name} must contain a YAML mapping."

    return content


def get_domain_files() -> list[Path]:
    """Return all YAML domain files."""

    return sorted(DOMAINS_DIRECTORY.glob("*_domain.yaml"))


def test_expected_domain_files_exist() -> None:
    actual_files = {file.name for file in get_domain_files()}

    assert actual_files == EXPECTED_DOMAIN_FILES


@pytest.mark.parametrize("domain_file", get_domain_files())
def test_domain_file_has_root_domain_key(domain_file: Path) -> None:
    content = load_yaml_file(domain_file)

    assert "domain" in content
    assert isinstance(content["domain"], dict)


@pytest.mark.parametrize("domain_file", get_domain_files())
def test_domain_contains_required_fields(domain_file: Path) -> None:
    content = load_yaml_file(domain_file)
    domain = content["domain"]

    missing_fields = REQUIRED_DOMAIN_FIELDS - set(domain.keys())

    assert not missing_fields, (
        f"{domain_file.name} is missing required fields: " f"{sorted(missing_fields)}"
    )


@pytest.mark.parametrize("domain_file", get_domain_files())
def test_domain_has_valid_owner_and_steward(domain_file: Path) -> None:
    content = load_yaml_file(domain_file)
    domain = content["domain"]

    assert domain["data_owner"].get("role")
    assert domain["data_owner"].get("accountability")

    assert domain["data_steward"].get("role")
    assert domain["data_steward"].get("responsibility")


@pytest.mark.parametrize("domain_file", get_domain_files())
def test_domain_has_critical_data_elements(domain_file: Path) -> None:
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
            f"'{element.get('name', 'Unknown')}' is missing "
            f"{sorted(missing_fields)}"
        )


@pytest.mark.parametrize("domain_file", get_domain_files())
def test_domain_has_governance_kpis(domain_file: Path) -> None:
    content = load_yaml_file(domain_file)
    kpis = content["domain"]["governance_kpis"]

    assert isinstance(kpis, list)
    assert len(kpis) >= 4

    for kpi in kpis:
        assert kpi.get("name")
        assert kpi.get("target")

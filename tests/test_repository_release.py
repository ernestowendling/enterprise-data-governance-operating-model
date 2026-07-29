"""Release-readiness tests for the public portfolio repository."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

README_FILE = PROJECT_ROOT / "README.md"
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"

EXPECTED_SCREENSHOTS = {
    PROJECT_ROOT / "docs" / "screenshots" / "executive-overview.png",
    PROJECT_ROOT / "docs" / "screenshots" / "governance-issues.png",
    PROJECT_ROOT / "docs" / "screenshots" / "ai-use-cases.png",
}

EXPECTED_DIAGRAMS = {
    PROJECT_ROOT / "diagrams" / "governance_operating_model.md",
    PROJECT_ROOT / "diagrams" / "governance_portal_architecture.md",
}

EXPECTED_DEPENDENCIES = {
    "streamlit",
    "pandas",
    "pyyaml",
    "pytest",
}


def normalise_requirement(
    requirement: str,
) -> str:
    """Return the package name from a requirement line."""

    package_name = requirement.split(";", maxsplit=1)[0].split("[", maxsplit=1)[0]

    for separator in (
        "==",
        ">=",
        "<=",
        "~=",
        "!=",
        ">",
        "<",
    ):
        package_name = package_name.split(
            separator,
            maxsplit=1,
        )[0]

    return package_name.strip().casefold()


def test_readme_exists_and_is_not_empty() -> None:
    """The public repository must include a substantial README."""

    assert README_FILE.exists(), f"README not found: {README_FILE}"

    readme_text = README_FILE.read_text(
        encoding="utf-8",
    )

    assert len(readme_text.strip()) >= 2_000, "README.md is unexpectedly short."


def test_demonstration_screenshots_exist() -> None:
    """Every screenshot referenced by the portfolio must exist."""

    missing_screenshots = {
        str(path.relative_to(PROJECT_ROOT))
        for path in EXPECTED_SCREENSHOTS
        if not path.exists()
    }

    assert not missing_screenshots, (
        "Missing demonstration screenshots: " f"{sorted(missing_screenshots)}"
    )

    empty_screenshots = {
        str(path.relative_to(PROJECT_ROOT))
        for path in EXPECTED_SCREENSHOTS
        if path.exists() and path.stat().st_size == 0
    }

    assert not empty_screenshots, (
        "Empty demonstration screenshots: " f"{sorted(empty_screenshots)}"
    )


def test_readme_references_every_screenshot() -> None:
    """The README must display every demonstration screenshot."""

    readme_text = README_FILE.read_text(
        encoding="utf-8",
    )

    missing_references = {
        path.relative_to(PROJECT_ROOT).as_posix()
        for path in EXPECTED_SCREENSHOTS
        if path.relative_to(PROJECT_ROOT).as_posix() not in readme_text
    }

    assert not missing_references, (
        "README screenshot references are missing: " f"{sorted(missing_references)}"
    )


def test_governance_diagrams_exist_and_use_mermaid() -> None:
    """Both documented diagrams must exist and contain Mermaid."""

    missing_diagrams = {
        str(path.relative_to(PROJECT_ROOT))
        for path in EXPECTED_DIAGRAMS
        if not path.exists()
    }

    assert not missing_diagrams, (
        "Missing governance diagrams: " f"{sorted(missing_diagrams)}"
    )

    invalid_diagrams = {
        str(path.relative_to(PROJECT_ROOT))
        for path in EXPECTED_DIAGRAMS
        if "```mermaid"
        not in path.read_text(
            encoding="utf-8",
        )
    }

    assert not invalid_diagrams, (
        "Diagram files without Mermaid content: " f"{sorted(invalid_diagrams)}"
    )


def test_required_dependencies_are_declared() -> None:
    """The installation file must declare core dependencies."""

    assert (
        REQUIREMENTS_FILE.exists()
    ), f"Requirements file not found: {REQUIREMENTS_FILE}"

    declared_dependencies = {
        normalise_requirement(line)
        for line in REQUIREMENTS_FILE.read_text(
            encoding="utf-8",
        ).splitlines()
        if line.strip() and not line.strip().startswith("#")
    }

    missing_dependencies = EXPECTED_DEPENDENCIES - declared_dependencies

    assert not missing_dependencies, (
        "Missing required dependencies: " f"{sorted(missing_dependencies)}"
    )

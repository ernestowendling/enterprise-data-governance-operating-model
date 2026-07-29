"""Smoke tests for the Streamlit governance portal."""

from __future__ import annotations

import ast
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_FILE = PROJECT_ROOT / "app.py"

EXPECTED_RENDER_FUNCTIONS = {
    "render_overview",
    "render_domain_explorer",
    "render_glossary_explorer",
    "render_data_quality_register",
    "render_governance_issues",
    "render_access_exceptions",
    "render_ai_use_cases",
    "render_standards_and_workflows",
}

EXPECTED_NAVIGATION_LABELS = {
    "Executive Overview",
    "Data Domains",
    "Business Glossary",
    "Data Quality",
    "Governance Issues",
    "Access Exceptions",
    "AI Use Cases",
    "Standards & Workflows",
}

EXPECTED_DATA_SOURCES = {
    "GLOSSARY_FILE",
    "DATA_QUALITY_RULES_FILE",
    "GOVERNANCE_ISSUES_FILE",
    "ACCESS_EXCEPTIONS_FILE",
    "AI_USE_CASES_FILE",
    "STANDARDS_DIRECTORY",
    "WORKFLOWS_DIRECTORY",
}


def read_app_source() -> str:
    """Read the Streamlit application source."""

    return APP_FILE.read_text(
        encoding="utf-8",
    )


def parse_app() -> ast.Module:
    """Parse the application into a Python syntax tree."""

    return ast.parse(
        read_app_source(),
        filename=str(APP_FILE),
    )


def test_app_file_exists() -> None:
    """The Streamlit entry point must exist."""

    assert APP_FILE.exists(), f"Streamlit application not found: {APP_FILE}"


def test_app_compiles_successfully() -> None:
    """The application must contain valid Python syntax."""

    source = read_app_source()

    compile(
        source,
        str(APP_FILE),
        "exec",
    )


def test_all_portal_render_functions_are_defined() -> None:
    """Every expected portal page must have a render function."""

    syntax_tree = parse_app()

    defined_functions = {
        node.name
        for node in ast.walk(syntax_tree)
        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            ),
        )
    }

    missing_functions = EXPECTED_RENDER_FUNCTIONS - defined_functions

    assert not missing_functions, (
        "Missing portal render functions: " f"{sorted(missing_functions)}"
    )


def test_all_navigation_labels_are_present() -> None:
    """Every expected portal page must appear in navigation."""

    source = read_app_source()

    missing_labels = {
        label
        for label in EXPECTED_NAVIGATION_LABELS
        if f'"{label}"' not in source and f"'{label}'" not in source
    }

    assert not missing_labels, "Missing navigation labels: " f"{sorted(missing_labels)}"


def test_all_governance_data_sources_are_referenced() -> None:
    """The application must reference every governed source."""

    source = read_app_source()

    missing_sources = {
        source_name
        for source_name in EXPECTED_DATA_SOURCES
        if source_name not in source
    }

    assert not missing_sources, (
        "Missing governance data sources: " f"{sorted(missing_sources)}"
    )

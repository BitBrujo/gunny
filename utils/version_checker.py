"""
CrewAI version detection and compatibility checking.

This module provides utilities to detect the installed CrewAI version
and check compatibility with Gunny's tested versions.
"""

import importlib.metadata
from typing import Tuple, Optional


def get_crewai_version() -> Optional[str]:
    """
    Get the installed CrewAI version.

    Returns:
        Version string (e.g., "0.4.0") or None if CrewAI is not installed
    """
    try:
        version = importlib.metadata.version('crewai')
        return version
    except importlib.metadata.PackageNotFoundError:
        return None
    except Exception:
        # Handle any other unexpected errors gracefully
        return None


def parse_version(version_str: str) -> Tuple[int, ...]:
    """
    Parse a version string into a tuple of integers for comparison.

    Args:
        version_str: Version string (e.g., "0.4.0" or "0.86.0")

    Returns:
        Tuple of integers (e.g., (0, 4, 0))
    """
    try:
        # Remove any pre-release/build metadata (e.g., "0.4.0-beta" -> "0.4.0")
        clean_version = version_str.split('-')[0].split('+')[0]
        return tuple(int(x) for x in clean_version.split('.'))
    except (ValueError, AttributeError):
        return (0, 0, 0)


def check_version_compatibility(
    installed_version: str,
    tested_versions: list[str],
    latest_tested: str
) -> Tuple[bool, str]:
    """
    Check if the installed CrewAI version is tested/compatible.

    Args:
        installed_version: The installed CrewAI version string
        tested_versions: List of tested version strings
        latest_tested: The latest tested version string

    Returns:
        Tuple of (is_compatible, warning_message)
        - is_compatible: True if version is tested or within safe range
        - warning_message: Message to display to user (empty if compatible)
    """
    if not installed_version:
        return True, ""  # No warning if CrewAI not installed

    # Check if exact version match
    if installed_version in tested_versions:
        return True, ""

    # Parse versions for comparison
    installed = parse_version(installed_version)
    latest = parse_version(latest_tested)

    # Check if installed is newer than latest tested
    if installed > latest:
        msg = (
            f"⚠️ **CrewAI v{installed_version} Detected (Untested)**\n\n"
            f"Gunny has been tested with CrewAI up to v{latest_tested}. "
            f"Your version may have new features or breaking changes. "
            f"Generated projects may require adjustments. "
            f"See MAINTAINABILITY.md for sync procedures."
        )
        return False, msg

    # Check if installed is much older
    if installed < parse_version(tested_versions[0]):
        msg = (
            f"⚠️ **CrewAI v{installed_version} Detected (Outdated)**\n\n"
            f"This version is older than Gunny's tested range "
            f"({tested_versions[0]} - {latest_tested}). "
            f"Consider upgrading CrewAI for best compatibility."
        )
        return False, msg

    # Version is within range but not explicitly tested
    # Show info but don't warn
    return True, ""


def get_version_info(tested_versions: list[str], latest_tested: str) -> Tuple[Optional[str], bool, str]:
    """
    Get comprehensive version information for display.

    Args:
        tested_versions: List of tested version strings
        latest_tested: The latest tested version string

    Returns:
        Tuple of (version, is_compatible, message)
        - version: Installed version string or None
        - is_compatible: Whether version is compatible
        - message: Message to display (warning or info)
    """
    version = get_crewai_version()

    if version is None:
        # CrewAI not installed - this is fine for Gunny
        return None, True, ""

    is_compatible, warning_msg = check_version_compatibility(
        version, tested_versions, latest_tested
    )

    if warning_msg:
        return version, is_compatible, warning_msg

    # Version is compatible - show info message
    info_msg = f"✅ **CrewAI v{version}** - Tested & Compatible"
    return version, is_compatible, info_msg

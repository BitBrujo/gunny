#!/usr/bin/env python3
"""
Simple CrewAI Update Checker for Gunny

Run this script to check if there's a new version of CrewAI available
and whether Gunny has been tested with it.

Usage:
    python check_updates.py
"""

import sys
import json
from urllib import request, error
from utils.constants import TESTED_CREWAI_VERSIONS, LATEST_TESTED_VERSION


def get_latest_crewai_version():
    """Fetch the latest CrewAI version from PyPI."""
    try:
        with request.urlopen('https://pypi.org/pypi/crewai/json', timeout=5) as response:
            data = json.loads(response.read().decode())
            return data['info']['version']
    except (error.URLError, error.HTTPError, KeyError, json.JSONDecodeError) as e:
        print(f"❌ Error fetching CrewAI version from PyPI: {e}")
        return None


def check_local_crewai():
    """Check if CrewAI is installed locally and get its version."""
    try:
        import crewai
        return crewai.__version__
    except ImportError:
        return None
    except AttributeError:
        return "unknown"


def main():
    print("=" * 60)
    print("🔍 Gunny - CrewAI Update Checker")
    print("=" * 60)
    print()

    # Check local installation
    local_version = check_local_crewai()
    if local_version:
        print(f"📦 Your CrewAI version: {local_version}")
    else:
        print("📦 CrewAI not installed locally (optional for Gunny)")
    print()

    # Check latest version
    print("🌐 Checking PyPI for latest CrewAI version...")
    latest_version = get_latest_crewai_version()

    if not latest_version:
        print("\n⚠️  Could not fetch latest version. Check your internet connection.")
        sys.exit(1)

    print(f"📦 Latest CrewAI version: {latest_version}")
    print()

    # Check Gunny compatibility
    print("=" * 60)
    print("🧪 Gunny Compatibility Status")
    print("=" * 60)
    print()
    print(f"✅ Gunny's latest tested version: {LATEST_TESTED_VERSION}")
    print(f"✅ All tested versions: {', '.join(TESTED_CREWAI_VERSIONS)}")
    print()

    # Determine status
    if latest_version in TESTED_CREWAI_VERSIONS:
        print("✅ COMPATIBLE: Gunny has been tested with this CrewAI version!")
        print()
        print("🎉 You're all set! No updates needed.")
    elif latest_version > LATEST_TESTED_VERSION:
        print(f"⚠️  NEW VERSION AVAILABLE: CrewAI {latest_version}")
        print()
        print("📋 Next Steps:")
        print("   1. Test Gunny with the new CrewAI version:")
        print("      pip install crewai==" + latest_version)
        print("      python run.sh  # or: uv run streamlit run app.py")
        print()
        print("   2. Generate a test project and verify it works:")
        print("      - Create a project in Gunny UI")
        print("      - Download and extract the ZIP")
        print("      - Run: crewai install && crewai run")
        print()
        print("   3. If tests pass, update Gunny:")
        print("      - Add '" + latest_version + "' to TESTED_CREWAI_VERSIONS in utils/constants.py")
        print("      - Update LATEST_TESTED_VERSION to '" + latest_version + "'")
        print()
        print("   4. Check CrewAI release notes for new tools/features:")
        print(f"      https://github.com/crewAIInc/crewAI/releases/tag/{latest_version}")
    else:
        print(f"ℹ️  You're using a version older than Gunny's latest tested ({LATEST_TESTED_VERSION})")
        print()
        print("Consider upgrading to the latest tested version:")
        print(f"   pip install crewai=={LATEST_TESTED_VERSION}")

    print()
    print("=" * 60)
    print("📚 For more info, see MAINTAINABILITY.md")
    print("=" * 60)


if __name__ == "__main__":
    main()

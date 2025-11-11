# MAINTAINABILITY.md

**Keeping Gunny in Sync with CrewAI**

This document describes a simple process for keeping Gunny up-to-date with CrewAI evolution.

---

## Quick Update Process

### Step 1: Check for Updates

Run the update checker script:

```bash
python check_updates.py
```

This will:
- Check PyPI for the latest CrewAI version
- Compare it with Gunny's tested versions
- Show compatibility status
- Provide next steps if update needed

### Step 2: Test New Version (if available)

If a new CrewAI version is detected:

```bash
# Install the new version
pip install crewai==X.Y.Z

# Run Gunny
uv run streamlit run app.py
# or: python run.sh

# Generate a test project in the UI
# Download and extract the ZIP

# Test the generated project
cd test_project/
crewai install
crewai run
```

### Step 3: Update Gunny Constants (if tests pass)

Edit `utils/constants.py`:

```python
# Add new version to the list
TESTED_CREWAI_VERSIONS = [
    "0.86.0",
    "1.4.1",
    "X.Y.Z",  # Add new version here
]

# Update latest tested version
LATEST_TESTED_VERSION = "X.Y.Z"
```

### Step 4: Check for New Tools/Features

Visit the CrewAI release notes:
```
https://github.com/crewAIInc/crewAI/releases/tag/X.Y.Z
```

Look for:
- **New tools** → Add to `TOOLS_CATALOG` in `utils/constants.py`
- **New agent parameters** → Add to UI and defaults
- **New LLM providers** → Add to `LLM_PROVIDERS`

---

## What Gets Updated

### 1. Tools Catalog
**File**: `utils/constants.py:6-647`
- 94+ CrewAI tools organized by category
- Each tool has: name, description, auth requirements, env vars

**To add a new tool**:
```python
TOOLS_CATALOG = {
    "Category Name": [
        {
            "name": "ToolName",
            "description": "2-3 sentence description",
            "requires_auth": True,  # or False
            "env_vars": ["API_KEY_NAME"],  # or []
            "auth_note": "Get key from provider.com"  # optional
        },
    ],
}
```

### 2. Version Tracking
**File**: `utils/constants.py:770-780`
- `TESTED_CREWAI_VERSIONS`: List of versions Gunny has been tested with
- `LATEST_TESTED_VERSION`: Most recent tested version

### 3. Default Configurations
**File**: `utils/constants.py`
- `DEFAULT_AGENT_CONFIG` (line ~724): Agent defaults
- `DEFAULT_TASK_CONFIG` (line ~746): Task defaults
- `DEFAULT_CREW_CONFIG` (line ~756): Crew defaults

### 4. LLM Providers
**File**: `utils/constants.py:671-678`
- Maps provider names to model options
- Used in agent LLM configuration

### 5. Code Generation
**File**: `generators/python_generator.py`
- Uses CrewAI decorators: `@agent`, `@task`, `@crew`
- Generates tool stubs with usage examples
- Imports from `crewai` package

---

## Troubleshooting

### "Could not fetch latest version from PyPI"
**Cause**: Network issue or PyPI down
**Fix**: Check internet connection, try again later

### "CrewAI not installed locally"
**Note**: This is normal - CrewAI is optional for running Gunny
**Action**: No action needed unless you want to test generated projects locally

### Generated project fails with "unknown parameter"
**Cause**: Gunny uses a parameter that doesn't exist in older CrewAI
**Fix**:
1. Check which parameter is causing the issue
2. Update `utils/constants.py` defaults to remove it
3. Update UI forms in `ui/components.py` to hide it for older versions

### New CrewAI tool not appearing in Gunny
**Cause**: Tool not yet added to `TOOLS_CATALOG`
**Fix**:
1. Find tool documentation in CrewAI docs
2. Add to appropriate category in `TOOLS_CATALOG`
3. Include auth requirements and env vars
4. Test in UI → Tools tab

### Tool stub generation missing auth info
**Cause**: Tool missing `env_vars` or `auth_note` in catalog
**Fix**:
1. Check CrewAI tool documentation for auth requirements
2. Update tool entry in `TOOLS_CATALOG`:
   ```python
   "requires_auth": True,
   "env_vars": ["API_KEY_NAME"],
   "auth_note": "Get API key from provider.com/api"
   ```
3. Regenerate project to test

---

## Version Compatibility

### Tested Versions
Gunny has been tested with these CrewAI versions:
- ✅ 0.86.0
- ✅ 1.4.1

### Compatibility Notes
- **Older versions (<0.86.0)**: May work but untested
- **Newer versions (>1.4.1)**: Check with `python check_updates.py`
- **Breaking changes**: Usually announced in CrewAI release notes

### Version Checker Display
The Streamlit sidebar shows:
- ✅ Green: Using a tested version
- ⚠️ Yellow: Using untested version (newer or older)
- (No message): CrewAI not installed (normal for Gunny-only use)

---

## Key Files Reference

| Purpose | File | Lines |
|---------|------|-------|
| Tools catalog | `utils/constants.py` | 6-647 |
| Version constants | `utils/constants.py` | 770-780 |
| Agent defaults | `utils/constants.py` | 724-743 |
| Task defaults | `utils/constants.py` | 746-753 |
| Crew defaults | `utils/constants.py` | 756-766 |
| LLM providers | `utils/constants.py` | 671-678 |
| Agent generation | `generators/python_generator.py` | 6-282 |
| Tool stub generation | `generators/python_generator.py` | 347-509 |
| YAML generation | `generators/yaml_generator.py` | All |
| UI components | `ui/components.py` | All |
| Validation | `utils/validators.py` | All |
| Version checker | `utils/version_checker.py` | All |

---

## Additional Documentation

- **`README.md`**: User guide and installation
- **`CLAUDE.md`**: Development guide for AI assistants
- **`TEST_REPORT_1.4.1.md`**: Testing results for CrewAI 1.4.1

---

## Summary

**The simple maintenance workflow:**

```bash
# 1. Check for updates
python check_updates.py

# 2. If new version available:
pip install crewai==X.Y.Z

# 3. Test in Gunny UI + test generated project

# 4. If tests pass, update constants:
# - Add to TESTED_CREWAI_VERSIONS
# - Update LATEST_TESTED_VERSION

# 5. Check release notes for new tools/features
# - Add new tools to TOOLS_CATALOG if needed
```

That's it! One simple command replaces complex manual procedures.

# GitHub Actions Setup Guide

## Overview

This repository is now configured with GitHub Actions to automatically run Playwright tests on every push and pull request.

## What Was Set Up

### 1. Dependencies File (`requirements.txt`)
All Python dependencies are now listed in `requirements.txt`:
- playwright>=1.40.0
- pytest>=7.4.0
- pytest-html>=4.1.0

### 2. GitHub Actions Workflow (`.github/workflows/playwright-tests.yml`)
The workflow automatically:
- Runs on push/PR to main/master branches
- Can be manually triggered via the Actions tab
- Sets up Python 3.11
- Installs dependencies
- Installs Playwright browsers
- Runs all tests in headless mode
- Uploads test reports and screenshots as artifacts

### 3. Configuration Updates (`config.py`)
- Now supports `HEADLESS_MODE` environment variable
- Automatically runs in headless mode in CI/CD environments
- Maintains backward compatibility for local development

### 4. Git Ignore (`.gitignore`)
Excludes unnecessary files from the repository:
- Python cache files
- Test reports
- Screenshots
- Virtual environments
- IDE files

## How to Use

### Automatic Execution
Tests run automatically when you:
- Push code to main/master branch
- Create a pull request to main/master branch

### Manual Execution
1. Go to the repository on GitHub
2. Click on the **Actions** tab
3. Select **Playwright Python Tests** workflow
4. Click **Run workflow** button
5. Select the branch and click **Run workflow**

### View Results
After a workflow run completes:
1. Go to the **Actions** tab
2. Click on the specific workflow run
3. Review the test results in the Summary
4. Download artifacts:
   - **test-report**: HTML test report
   - **screenshots**: Screenshots from failed tests (if any)

## Workflow Status Badge

The README now includes a workflow status badge that shows:
- ✅ Green: All tests passing
- ❌ Red: Tests failing
- 🟡 Yellow: Tests running

## Local Development

For local development, the configuration remains unchanged:
- Tests run with `HEADLESS_MODE = False` by default
- Use `HEADLESS_MODE=true pytest tests/` to test CI behavior locally

## Troubleshooting

### Workflow Not Running
- Check that the workflow file is in `.github/workflows/` directory
- Ensure you're pushing to main or master branch
- Check branch protection rules

### Tests Failing in CI but Passing Locally
- Ensure headless mode works locally: `HEADLESS_MODE=true pytest tests/`
- Check for timing issues (add waits if needed)
- Review CI logs for specific errors

### Artifacts Not Available
- Artifacts are retained for 30 days
- Check that the workflow completed (artifacts upload even on failure)
- Ensure you have permissions to access the repository

## Next Steps

You can now:
1. ✅ Run tests automatically on every code change
2. ✅ View test results in the Actions tab
3. ✅ Download HTML reports and screenshots
4. ✅ Add more tests that will run automatically
5. ✅ Integrate with branch protection rules to require passing tests before merge

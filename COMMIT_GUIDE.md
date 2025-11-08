# Commit and PR Guide

This document explains how to use the commit message and PR description for this restructuring.

## Files Created

1. **COMMIT_MESSAGE.txt** - Ready-to-use commit message
2. **PR_DESCRIPTION.md** - Complete PR description for GitHub
3. **COMMIT_GUIDE.md** - This file (usage instructions)

## Option 1: Create Commit and PR via Command Line

### Step 1: Stage All Changes

```bash
# Stage all new and modified files
git add .

# Or stage specific categories
git add src/ tests/ data/ setup.py Makefile MANIFEST.in README.md MAKEFILE.md
```

### Step 2: Create Commit

```bash
# Use the commit message file directly
git commit -F COMMIT_MESSAGE.txt

# Or copy the message (if you want to edit it)
cat COMMIT_MESSAGE.txt
# Then paste into: git commit -m "paste here"
```

### Step 3: Push to Branch

```bash
# Create and push to feature branch
git checkout -b feat/restructure-project-package
git push -u origin feat/restructure-project-package
```

### Step 4: Create PR

**Using GitHub CLI (gh):**
```bash
# Create PR with body from file
gh pr create --title "Restructure project into proper Python package with comprehensive tooling" \
             --body-file PR_DESCRIPTION.md \
             --base develop
```

**Using GitHub Web UI:**
1. Go to https://github.com/yourusername/Job-Rejection-Analysis/pulls
2. Click "New pull request"
3. Select base: `develop` and compare: `feat/restructure-project-package`
4. Copy contents of `PR_DESCRIPTION.md` into the description field
5. Click "Create pull request"

## Option 2: Use Make Target (Simpler!)

I can add a Make target to automate this:

```bash
# Add this commit and push
make commit-restructure

# Then create PR manually or with gh
```

## Commit Message Breakdown

The commit message follows Conventional Commits format:

```
feat: <type of change>

<detailed description>

Key Changes:
- <bullet points of main changes>

<additional sections>

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

**Structure:**
- **Type**: `feat` (new feature/capability)
- **Scope**: Project restructuring
- **Body**: Detailed explanation of all changes
- **Footer**: Credits to Claude Code

## PR Description Sections

The PR description includes:

1. **Summary** - Quick overview of what changed
2. **Motivation** - Why this change was needed
3. **Changes** - Detailed breakdown:
   - Project Structure
   - Package Configuration
   - Development Tools
   - Code Organization
   - Documentation
   - New Features
4. **Migration Guide** - Before/after examples for:
   - Users
   - Developers
   - Code importers
5. **Breaking Changes** - What might break existing workflows
6. **Testing** - Verification steps and results
7. **Checklist** - PR completion checklist
8. **Files Changed** - Summary of added/modified/moved files
9. **Reviewer Notes** - Guidance for code reviewers

## Quick Commands Reference

### Full Workflow

```bash
# 1. Review changes
git status

# 2. Stage everything
git add .

# 3. Commit with prepared message
git commit -F COMMIT_MESSAGE.txt

# 4. Create feature branch and push
git checkout -b feat/restructure-project-package
git push -u origin feat/restructure-project-package

# 5. Create PR
gh pr create --title "Restructure project into proper Python package with comprehensive tooling" \
             --body-file PR_DESCRIPTION.md \
             --base develop
```

### If You Need to Amend

```bash
# If you need to add more changes
git add <files>
git commit --amend --no-edit

# Force push (only if branch not yet reviewed!)
git push -f origin feat/restructure-project-package
```

## Customization

### Customize Commit Message

If you want to personalize the commit message:

1. Copy COMMIT_MESSAGE.txt to a new file
2. Edit as needed
3. Commit with: `git commit -F your-custom-message.txt`

### Customize PR Description

If you want to add/modify PR description:

1. Copy PR_DESCRIPTION.md to a new file
2. Edit sections as needed
3. Use the modified file: `gh pr create --body-file your-custom-pr.md`

## GitHub PR Template

If you want to set this as a template for future PRs:

```bash
# Copy to .github directory
mkdir -p .github
cp PR_DESCRIPTION.md .github/pull_request_template.md

# Now all new PRs will use this template
```

## Verification Before Committing

Run these checks before creating the commit:

```bash
# 1. Make sure code is formatted
make format

# 2. Run all checks
make check-all

# 3. Clean up any generated files
make clean

# 4. Verify package installation works
make verify

# 5. Check git status
git status
```

## After PR is Merged

1. **Delete feature branch:**
   ```bash
   git checkout develop
   git pull origin develop
   git branch -d feat/restructure-project-package
   git push origin --delete feat/restructure-project-package
   ```

2. **Tag the release (optional):**
   ```bash
   git tag -a v0.1.0 -m "Version 0.1.0: Package restructure"
   git push origin v0.1.0
   ```

3. **Build and publish (if ready):**
   ```bash
   make build
   make upload-test  # Test on TestPyPI first
   make upload       # Then publish to PyPI
   ```

## Tips

- ✅ **Review the diff**: `git diff --staged` before committing
- ✅ **Keep branch up to date**: Rebase on develop if needed
- ✅ **Squash if needed**: Consider squashing commits before merge
- ✅ **Update CHANGELOG**: Add entry for this version
- ✅ **Test in clean environment**: Use fresh virtualenv to verify

## Troubleshooting

**Issue: Commit message too long**
- Some git tools have line length limits
- Break long lines at 72 characters if needed

**Issue: PR description formatting off**
- GitHub Markdown may render slightly differently
- Preview the PR description before submitting

**Issue: Conflicts with develop branch**
```bash
git checkout develop
git pull origin develop
git checkout feat/restructure-project-package
git rebase develop
# Resolve conflicts if any
git push -f origin feat/restructure-project-package
```

## Example Complete Workflow

```bash
# Starting from develop branch
cd Job-Rejection-Analysis

# Create feature branch
git checkout -b feat/restructure-project-package

# Stage all changes (already done by Claude)
git add .

# Verify what's staged
git status

# Run final checks
make format
make check-all
make clean

# Commit with prepared message
git commit -F COMMIT_MESSAGE.txt

# Push to remote
git push -u origin feat/restructure-project-package

# Create PR (using gh CLI)
gh pr create \
  --title "Restructure project into proper Python package with comprehensive tooling" \
  --body-file PR_DESCRIPTION.md \
  --base develop \
  --label "enhancement" \
  --label "breaking-change"

# Get the PR URL
gh pr view --web
```

## Need Help?

- Run `make help` to see available targets
- Check `MAKEFILE.md` for detailed documentation
- Review `README.md` for updated usage instructions
- See `CONTRIBUTING.md` for contribution guidelines

---

**Ready to commit?** Run:
```bash
git add . && git commit -F COMMIT_MESSAGE.txt
```

**Ready for PR?** Run:
```bash
gh pr create --title "Restructure project into proper Python package with comprehensive tooling" --body-file PR_DESCRIPTION.md --base develop
```

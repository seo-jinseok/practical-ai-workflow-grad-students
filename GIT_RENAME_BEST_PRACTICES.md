# Git Rename Best Practices

This document outlines best practices for preserving Git history when renaming files and folders, based on lessons learned from the v13.0 refactor.

## Why Rename Detection Matters

Preserving Git history through renames is crucial for:
- **Attribution tracking**: `git blame` shows original authors
- **History continuity**: `git log --follow` traces changes across renames
- **Educational value**: Students can see evolution of documents
- **Code review**: Understanding context of changes

## The Problem

When renaming files, Git may fail to detect renames if:
1. Rename detection is not enabled in Git config
2. Multiple operations are combined (folder + file renames)
3. Content changes are mixed with renames
4. Staging is not done properly

## Solution: Step-by-Step Rename Process

### 1. Enable Rename Detection Globally

```bash
git config diff.renames true
git config diff.renameLimit 999999
```

### 2. Create .gitattributes File

Add to repository root:

```gitattributes
# Git Attributes for Better Rename Detection
*.md diff=markdown
*.md merge=union
* text=auto

# Binary files
*.png binary
*.svg binary
```

### 3. Perform Sequential Renames

**DO**: Rename files one at a time or in logical groups
```bash
# Root files first
git mv "old_name_Part1.md" "new_name_Part1.md"
git mv "old_name_Part2.md" "new_name_Part2.md"
git add -A

# Folder rename
git mv old_folder new_folder
git add -A

# Files inside renamed folder
git mv new_folder/old_file.md new_folder/new_file.md
git add -A
```

**DON'T**: Mix content changes with renames
```bash
# BAD: This combines rename + edit
git mv old.md new.md
echo "new content" >> new.md
git add -A
```

### 4. Commit with Proper Message

```bash
git commit -m "refactor: Rename files (preserve history)"
```

The `diff.renames=true` config ensures rename detection is automatic.

### 5. Verify Rename Detection

After committing, verify renames are detected:

```bash
# Should show R100 (renamed with 100% similarity)
git diff --name-status HEAD~1

# Should show "rename from ... to ..." 
git show --stat HEAD

# Should trace back through rename
git log --follow -- new_file.md

# Should show original file name in attribution
git blame -C new_file.md
```

## Case Study: v13.0 Refactor

### Challenge
Remove "v13.0" from filenames while preserving history:
- 3 root markdown files
- 1 folder (v13.0_resources → resources)
- 3 README files inside folder
- 100+ files inside folder structure

### Issue
Initial attempts failed because:
1. Existing `resources` folder conflicted with rename target
2. Folder rename interference with file tracking
3. Default Git config didn't enable rename detection

### Solution Applied
1. Removed conflicting `resources` folder
2. Enabled `diff.renames=true` globally
3. Sequential renames: root files → folder → internal files
4. Explicit staging with `git add -A` after each group
5. Single commit for all renames
6. Separate commit for reference updates

### Result
✅ All 116 files show 100% rename similarity  
✅ `git log --follow` traces full history  
✅ `git blame` shows original authors  
✅ History preserved for educational value

### Verification Performed (2025-11-14)

Comprehensive verification at commit `db7b71dc`:

**1. Rename Detection Status**
```bash
$ git show --find-renames=100% --name-status bdcfeff | grep "^R" | head -3
R100    Practical_AI_Workflow_for_Grad_Students v13.0_Part1.md    Practical_AI_Workflow_for_Grad_Students_Part1.md
R100    Practical_AI_Workflow_for_Grad_Students v13.0_Part2.md    Practical_AI_Workflow_for_Grad_Students_Part2.md
R100    Practical_AI_Workflow_for_Grad_Students v13.0_Part3.md    Practical_AI_Workflow_for_Grad_Students_Part3.md
```
✅ **All renames detected with R100 (100% similarity)**

**2. History Chain Continuity**
```bash
$ git log --follow --oneline -- Practical_AI_Workflow_for_Grad_Students_Part1.md
9610536 refactor: Update internal references to renamed files
bdcfeff refactor: Remove v13.0 version references from filenames...
b4e9375 Update documentation and images for Practical AI Workflow v13.0
1a39cfe Generate all Part 1 mockup screenshots and replace placeholders
c45fdf3 Complete Part 1 document and update instruction files
d24ae56 Initial commit: v13.0 release for students
```
✅ **Full history traced back to original v13.0 filename commits**

**3. Blame Attribution**
```bash
$ git blame -C -L 1,10 Practical_AI_Workflow_for_Grad_Students_Part1.md | head -3
^d24ae56 Practical_AI_Workflow_for_Grad_Students v13.0_Part1.md (Jinseok Seo 2025-11-12 11:30:04 +0900  1)
^d24ae56 Practical_AI_Workflow_for_Grad_Students v13.0_Part1.md (Jinseok Seo 2025-11-12 11:30:04 +0900  2)
^d24ae56 Practical_AI_Workflow_for_Grad_Students v13.0_Part1.md (Jinseok Seo 2025-11-12 11:30:04 +0900  3)
```
✅ **Original filename and author preserved in blame output**

**4. Folder Rename Detection**
```bash
$ git show --stat bdcfeff | grep "v13.0_resources => resources" | wc -l
113
```
✅ **All 113+ files in folder structure tracked through rename**

**5. Internal README Renames**
```bash
$ git log --follow --oneline -- resources/README_Part1.md
9610536 refactor: Update internal references to renamed files
bdcfeff refactor: Remove v13.0 version references...
d24ae56 Initial commit: v13.0 release for students
```
✅ **Internal file renames also preserve history chain**

**Configuration Used:**
- `diff.renames = true` (enabled)
- `diff.renameLimit = 999999` (high threshold)
- `.gitattributes` with markdown diff hints

**Conclusion**: The rename refactor successfully preserved Git history for all 116 files with 100% similarity detection. All verification tests pass.

## Common Pitfalls

### ❌ Pitfall 1: Folder Conflicts
```bash
# If 'new_folder' already exists from previous refactor
git mv old_folder new_folder  # Creates new_folder/old_folder!
```

**Solution**: Remove conflicting folder first
```bash
rm -rf new_folder
git mv old_folder new_folder
```

### ❌ Pitfall 2: Missing Staging
```bash
git mv file1.md new1.md
git mv file2.md new2.md
git commit  # May not detect both renames
```

**Solution**: Stage explicitly
```bash
git mv file1.md new1.md
git mv file2.md new2.md
git add -A
git commit
```

### ❌ Pitfall 3: Mixed Changes
```bash
git mv old.md new.md
sed -i 's/old/new/g' new.md  # Content change!
git commit  # May lose rename detection
```

**Solution**: Separate commits
```bash
git mv old.md new.md
git commit -m "refactor: Rename file"
sed -i 's/old/new/g' new.md
git commit -m "refactor: Update references"
```

## Testing Rename Detection

After any rename operation, run these checks:

```bash
# 1. Name-only status (should show R or R100)
git diff --name-status HEAD~1

# 2. Full stat (should show "rename from...to...")
git show --stat HEAD

# 3. Follow history (should trace through rename)
git log --follow --oneline -- new_name.md

# 4. Blame with copy detection
git blame -C new_name.md | head -5
```

Expected output indicators:
- `R` or `R100` in diff output
- `rename from...to...` in stat output
- Original filename in blame output
- Continuous history in log --follow

## Resources

- Git rename detection: https://git-scm.com/docs/git-diff#Documentation/git-diff.txt---find-renamesltcountgt
- Git attributes: https://git-scm.com/docs/gitattributes
- This repository's refactor: commit `bdcfeff`

## Maintenance

When this file is updated:
1. Test recommendations on a feature branch
2. Verify with the testing checklist above
3. Update examples if Git behavior changes
4. Cross-reference with `.gitattributes` file

---

**Last Updated**: 2025-11-14  
**Last Verified**: 2025-11-14 (commit db7b71dc)  
**Verified On**: Git 2.x  
**Related Files**: `.gitattributes`, `GIT_HISTORY_CLEANUP_GUIDE.md`, `VERIFICATION_CHECKLIST.md`

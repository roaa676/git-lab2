# Lab 2 – Git Workflow Report

**Repository:** https://github.com/roaa676/git-lab2
**Pull Request:** https://github.com/roaa676/git-lab2/pull/1
**Hosting platform:** GitHub

The project is a small Python calculator (`src/calculator.py`) with tests (`tests/test_calculator.py`), used to practice the Git workflow below.

---

## 1. Create two new branches

```bash
git switch -c feature/math-ops
git switch main
git switch -c feature/docs
```

| Branch | Purpose |
|---|---|
| `feature/math-ops` | Adds multiply/divide operations and unit tests |
| `feature/docs` | Adds usage documentation and links it from the README |

## 2. Make different commits on both branches, then merge them

**Commits on `feature/math-ops`:**
- [`94018d1`](https://github.com/roaa676/git-lab2/commit/94018d174561e5fae02f2c326b77464f1d710e01) Add multiply and divide operations
- [`d93445c`](https://github.com/roaa676/git-lab2/commit/d93445cfe86e8b62cfaf9bb64056d5799068b609) Add unit tests for calculator operations

**Commits on `feature/docs`:**
- [`230e561`](https://github.com/roaa676/git-lab2/commit/230e56189ca0c7c6282ebc13d7f68730910c3048) Add usage documentation
- [`371df8a`](https://github.com/roaa676/git-lab2/commit/371df8af2f356efc35bd7c35d4c0aa975db17e5a) Link usage docs from README

**Merge both into `main`:**

```bash
git switch main
git merge --no-ff feature/math-ops
git merge --no-ff feature/docs
```

- [`a3363dc`](https://github.com/roaa676/git-lab2/commit/a3363dcc2317cc5fa061de203537b6bbd2f5169b) Merge branch 'feature/math-ops' into main
- [`a2fc40d`](https://github.com/roaa676/git-lab2/commit/a2fc40d753f447b6b54e63c496ddc98e8bf35e35) Merge branch 'feature/docs' into main

## 3. Use Git stash to temporarily save changes, then restore them

I modified `README.md` and `docs/usage.md`, then:

```bash
git status --short
#  M README.md
#  M docs/usage.md

git stash push -m "WIP: README wording and multiply/divide docs"
# Saved working directory and index state On main: WIP: README wording and multiply/divide docs

git stash list
# stash@{0}: On main: WIP: README wording and multiply/divide docs

git status --short
# (empty – working tree is clean)

git stash pop
# changes restored, stash dropped

git commit -am "Document multiply/divide and update README wording"
```

Result: [`513401b`](https://github.com/roaa676/git-lab2/commit/513401b6e6fbd7cb32e50c26bbf6b7d7133a7d2b) Document multiply/divide and update README wording

> Note: stashes are stored locally only, so they don't appear on GitHub. The commands and output above show the stash workflow.

## 4. Create a meaningful commit on one branch and cherry-pick it into another

A bug fix was committed on `feature/math-ops`: dividing by zero now raises a clear `ValueError`.

```bash
git switch feature/math-ops
git commit -am "Fix: raise ValueError on division by zero"   # d40856f

git switch main
git cherry-pick -x d40856f
```

- Original on `feature/math-ops`: [`d40856f`](https://github.com/roaa676/git-lab2/commit/d40856f6505c25c7f3223f975e1ac0764e1a0471)
- Cherry-picked onto `main`: [`3ff2810`](https://github.com/roaa676/git-lab2/commit/3ff28103a81af9170ebbaacb7d590bf4c85ce718), whose message includes `(cherry picked from commit d40856f…)`

## 5. Revert an existing commit using git revert

A debug print was added and then reverted. The original commit stays in the history:

```bash
git commit -am "Add debug print on module load"   # ed65fa7
git revert ed65fa7
```

- Original: [`ed65fa7`](https://github.com/roaa676/git-lab2/commit/ed65fa709ef72e425efe47a48102648034919925) Add debug print on module load
- Revert: [`3e0931b`](https://github.com/roaa676/git-lab2/commit/3e0931b2237d19240b7316121b578ac9aa8f7b81) Revert "Add debug print on module load"

## 6. Push the repository and branches to GitHub

```bash
git remote add origin https://github.com/roaa676/git-lab2.git
git push -u origin main feature/math-ops feature/docs feature/power-operation
```

All branches: https://github.com/roaa676/git-lab2/branches

## 7. Create a pull request for a new feature

New feature branch `feature/power-operation`:
- [`531e294`](https://github.com/roaa676/git-lab2/commit/531e2945858702b474f886417e7f353c5db2ebdf) Add power operation
- [`3ed5e29`](https://github.com/roaa676/git-lab2/commit/3ed5e2937886b2d8640ead5274c8b0a764c951b6) Add tests for power operation

Pull request: [#1 Add power operation](https://github.com/roaa676/git-lab2/pull/1) (`feature/power-operation` → `main`)

## 8. Review and merge the pull request

- I reviewed the changed files and submitted a review comment. GitHub doesn't let a PR author approve their own PR, so the review was submitted as a **Comment**.
- I merged the PR into `main`: [`aeeec89`](https://github.com/roaa676/git-lab2/commit/aeeec896e428707e551efd020cbe68d2f15a119d) Merge pull request #1 from roaa676/feature/power-operation

---

## Final history

```
git log --oneline --graph --all
```

```
*   aeeec89 Merge pull request #1 from roaa676/feature/power-operation
|\
| * 3ed5e29 Add tests for power operation
| * 531e294 Add power operation
|/
* 3e0931b Revert "Add debug print on module load"
* ed65fa7 Add debug print on module load
* 3ff2810 Fix: raise ValueError on division by zero
* 513401b Document multiply/divide and update README wording
*   a2fc40d Merge branch 'feature/docs' into main
|\
| * 371df8a Link usage docs from README
| * 230e561 Add usage documentation
* |   a3363dc Merge branch 'feature/math-ops' into main
|\ \
| |/
|/|
| | * d40856f Fix: raise ValueError on division by zero   (feature/math-ops)
| |/
| * d93445c Add unit tests for calculator operations
| * 94018d1 Add multiply and divide operations
|/
* 1ded549 Initial commit: calculator with add and subtract
```

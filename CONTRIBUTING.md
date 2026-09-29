# Contributing to weatherkit

Thanks for your interest in improving weatherkit! This document explains how
to set up the project, what conventions we follow, and the checks every pull
request must pass.

## Project setup

```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
pip install -r requirements-docs.txt   # only needed for docs work
```

## Branch naming

Branch off `main` and name branches by type, mirroring
[Conventional Commits](https://www.conventionalcommits.org/):

| Type | Example |
|---|---|
| Docs work | `docs/improvement` |
| Bug fix | `fix/heat-index-rounding` |
| Feature | `feature/wind-chill` |
| Chore / tooling | `chore/ci-cache` |

## Commit style

Use [Conventional Commits](https://www.conventionalcommits.org/): short,
imperative subjects such as:

- `docs: add installation guide`
- `fix: reject humidity outside 0-100 in heat_index_c`
- `chore: pin mkdocs-material to 9.5.x`

## Style guide

- **Python**: standard library only at runtime; type hints on public
  functions; Google-style docstrings on every public name (CI enforces at
  least 80% coverage via `interrogate`).
- **Docs**: Markdown files live in `docs/` and follow the
  [Diátaxis](https://diataxis.fr/) structure (tutorials, how-to, reference,
  explanation). Keep one topic per page.
- **Prose**: English, present tense, no line-length limit (MD013 is off).

## How to run the checks

Run all of these locally before opening a pull request — CI runs the same
ones:

```bash
codespell                                    # spelling
interrogate -v .                             # docstring coverage >= 80%
markdownlint-cli2 "**/*.md"                  # markdown style
lychee --no-progress './**/*.md'             # dead-link check (needs lychee)
mkdocs build --strict                        # docs must build without warnings
```

Tool configuration lives in `.markdownlint.yaml`, `.codespellrc`,
`lychee.toml`, and the `[tool.interrogate]` section of `pyproject.toml`.

## Opening a pull request

1. Push your branch and open a PR against `main`.
2. Fill in the PR template's documentation checklist.
3. Wait for all status checks to go green; a red `docs / checks` job means
   one of the commands above failed — the logs name the exact file and line.

Questions about docs structure? Open an issue with the **docs improvement**
template first so we can agree on the approach before you write pages of
Markdown.

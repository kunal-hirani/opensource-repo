# Description

What does this pull request change, and why? Link any related issues,
e.g. `Fixes #42`.

## Type of change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Documentation improvement
- [ ] Tooling / CI change

## Documentation checklist

Every PR that touches `docs/`, docstrings, or the README must confirm:

- [ ] `mkdocs build --strict` passes locally with no warnings
- [ ] `markdownlint-cli2 "**/*.md"` passes
- [ ] `codespell` passes
- [ ] Any new or changed public function has a Google-style docstring
      (`interrogate -v .` stays at or above 80%)
- [ ] Links in changed Markdown files resolve (`lychee` passes in CI)
- [ ] Screenshots or rendered previews attached when the change is visual

## Verification

Describe how you tested the change, e.g.:

```bash
mkdocs serve   # checked pages X, Y, Z in the browser
```

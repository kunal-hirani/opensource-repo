# Changelog

All notable changes to weatherkit are documented in this file. The format is
based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this
project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Continuous documentation pipeline: MkDocs Material site, generated API
  reference, markdown/spelling/link/style checks in CI, and GitHub Pages
  deployment.
- Community health files: `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, issue and pull-request templates, and `CODEOWNERS`.

### Changed

- Every public function now has a Google-style docstring (interrogate
  coverage 0% to 100%); `k_to_c` and `heat_index_c` gained input validation.

## [0.2.0] - 2026-09-29

### Added

- `classify()` for human-friendly temperature bands.
- Type hints on all public functions.

## [0.1.0] - 2026-09-20

### Added

- `c_to_f`, `f_to_c`, `k_to_c`, and `heat_index_c` conversion helpers.

[Unreleased]: https://github.com/<your-username>/<repo>/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/<your-username>/<repo>/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/<your-username>/<repo>/releases/tag/v0.1.0

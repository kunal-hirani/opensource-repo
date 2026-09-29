# weatherkit

![Licence](https://img.shields.io/badge/licence-MIT-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Docs](https://img.shields.io/badge/docs-mkdocs%20material-3f51b5)

Tiny, dependency-free helpers for temperature conversion, heat index, and
friendly temperature classification. The package exists as a compact,
well-documented example: every public function carries a Google-style
docstring, the API reference is generated from those docstrings, and all
quality checks run in CI on every pull request.

## Features

- Convert between Celsius, Fahrenheit, and Kelvin
- Rothfusz heat index ("feels like" temperature)
- Human-friendly temperature bands (`freezing` to `boiling`)
- Zero runtime dependencies, pure standard library

## Installation

```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

## Usage

```python
from weatherkit import c_to_f, heat_index_c, classify

c_to_f(20)                # 68.0
round(heat_index_c(30, 70), 1)   # 35.0
classify(20)              # 'mild'
```

## Documentation

Full documentation, including a generated API reference, is published with
MkDocs Material at the project's GitHub Pages URL (linked from the repository
home page badge). Build it locally with:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for setup,
branch naming, and the checks every pull request must pass. By participating
you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Licence

Distributed under the [MIT License](LICENSE).

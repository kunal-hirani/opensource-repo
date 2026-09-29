# Installation

weatherkit has **no runtime dependencies** — it only needs Python 3.9 or
newer. These commands were tested on Windows, macOS, and Linux.

## 1. Get the code

```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
```

## 2. Create a virtual environment

Creating an isolated environment keeps the package (and the documentation
toolchain) from touching your system Python.

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows"

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

## 3. Install the package

```bash
pip install -e .
```

The `-e` flag installs it *editable*, so your changes take effect immediately.

## 4. Verify

```bash
python -c "from weatherkit import c_to_f; print(c_to_f(20))"
```

You should see:

```text
68.0
```

## Installing the documentation toolchain (optional)

To build this documentation site locally:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `python: command not found` | Install Python 3.10+, or retry with `python3` / `py` |
| `mkdocs: command not found` | Activate the virtual environment, then re-run `pip install -r requirements-docs.txt` |
| `pip install -e .` fails | Update pip: `python -m pip install --upgrade pip` |

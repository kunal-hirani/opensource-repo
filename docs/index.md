# weatherkit Documentation

Welcome to the documentation for **weatherkit**, a tiny, dependency-free
Python package for temperature conversion, heat index, and classification.

This site follows the [Diátaxis](https://diataxis.fr/) framework, so there is
a page for every way you might want to use the docs:

| Section | What it is for |
|---|---|
| [Getting Started](getting-started/installation.md) | Install the package on your machine |
| [Tutorials](tutorials/first-steps.md) | A guided, runnable first example |
| [How-to Guides](how-to/convert-temperatures.md) | Recipes for specific tasks |
| [Reference](reference/api.md) | The complete, auto-generated API reference |
| [Explanation](explanation/design.md) | Why the package is designed the way it is |

## Quick example

```python
from weatherkit import c_to_f, classify

c_to_f(20)      # 68.0
classify(30)    # 'hot'
```

## Where to go next

- New to the package? Start with the [installation guide](getting-started/installation.md),
  then follow [First steps](tutorials/first-steps.md).
- Looking for one function's signature or return value? Jump straight to the
  [API reference](reference/api.md).
- Curious how the heat index formula works? Read [Design notes](explanation/design.md).

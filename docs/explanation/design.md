# Design notes

Why weatherkit looks the way it does. This page explains the reasoning
behind the package's scope, formula choice, and error handling.

## Scope: one module, no dependencies

weatherkit deliberately ships as a single importable module with zero runtime
dependencies. The goal is a documentation *and* packaging example that stays
readable end to end: every design decision is visible in one file,
`weatherkit/__init__.py`.

Keeping the surface small also keeps the generated API reference
([`weatherkit`](../reference/api.md)) complete without pagination or grouping tricks.

## The heat index formula

The heat index uses the Rothfusz regression, the same multi-parameter
equation the US National Weather Service uses for warm conditions. The
implementation converts the input to Fahrenheit, applies the regression, and
converts the result back to Celsius.

Two simplifications are worth knowing:

1. **No dry adjustment.** The NWS applies a small correction for low
   humidity / high temperature pairs; weatherkit skips it for clarity.
2. **No wet-bulb fallback.** For temperatures below roughly 27 degrees
   Celsius the regression is not physically meaningful, so treat those
   results as approximations.

Because the formula is long, it lives in one function,
[`heat_index_c`](../reference/api.md#weatherkit.heat_index_c), with the coefficients laid
out one per line so they can be checked against the published regression.

## Validation philosophy

Functions validate only what physics or arithmetic cannot survive:

- `k_to_c` rejects negative Kelvin - absolute zero is a hard floor.
- `heat_index_c` rejects humidity outside 0-100% - the regression is
  undefined elsewhere.
- Plain conversions (`c_to_f`, `f_to_c`) accept any float and perform no
  checks, because the arithmetic is defined for every value.

This keeps the library predictable: an exception means *the input was
physically impossible*, not *the library is being fussy*.

## Why Google-style docstrings

The package documents itself with Google-style docstrings because:

1. **Tooling synergy** - mkdocstrings renders them without extra plugins, and
   interrogate only checks *presence*, so the style stays free.
2. **Readability** - the `Args / Returns / Raises / Example` sections stay
   legible in plain source, without reStructuredText markup.
3. **Doctest-ready** - the `Example` sections are runnable with Python's
   `doctest` module, doubling as executable documentation.

## Versioning

weatherkit follows [Semantic Versioning](https://semver.org/); every
user-visible change is recorded in `CHANGELOG.md` at the repository root.

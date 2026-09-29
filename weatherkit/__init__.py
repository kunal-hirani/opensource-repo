"""weatherkit - tiny temperature conversion and heat-index helpers.

The package is intentionally small so that the documentation exercises stay
focused on tooling: every public name is documented with a Google-style
docstring, and the MkDocs API reference is generated from them with
mkdocstrings.

Example:
    >>> from weatherkit import c_to_f, classify
    >>> c_to_f(20)
    68.0
    >>> classify(30)
    'hot'
"""

FREEZING_C: float = 0.0
"""Freezing point of water in degrees Celsius."""

BOILING_C: float = 100.0
"""Boiling point of water in degrees Celsius at standard pressure."""


def c_to_f(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        The equivalent temperature in degrees Fahrenheit.

    Example:
        >>> from weatherkit import c_to_f
        >>> c_to_f(20)
        68.0
    """
    return celsius * 9.0 / 5.0 + 32.0


def f_to_c(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in degrees Fahrenheit.

    Returns:
        The equivalent temperature in degrees Celsius.

    Example:
        >>> from weatherkit import f_to_c
        >>> f_to_c(68)
        20.0
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0


def k_to_c(kelvin: float) -> float:
    """Convert a temperature from Kelvin to Celsius.

    Args:
        kelvin: Temperature in Kelvin. Must not be negative.

    Returns:
        The equivalent temperature in degrees Celsius.

    Raises:
        ValueError: If ``kelvin`` is below absolute zero (0 K).

    Example:
        >>> from weatherkit import k_to_c
        >>> round(k_to_c(300), 2)
        26.85
    """
    if kelvin < 0.0:
        raise ValueError("kelvin cannot be below absolute zero (0 K)")
    return kelvin - 273.15


def heat_index_c(temp_c: float, humidity_pct: float) -> float:
    """Compute the heat index ("feels like" temperature) in Celsius.

    Uses the Rothfusz regression on the Fahrenheit heat index, then converts
    the result back to Celsius. The formula is intended for warm conditions
    (roughly 27 degrees Celsius and above).

    Args:
        temp_c: Air temperature in degrees Celsius.
        humidity_pct: Relative humidity as a percentage (0-100).

    Returns:
        The heat index in degrees Celsius.

    Raises:
        ValueError: If ``humidity_pct`` is not between 0 and 100.

    Example:
        >>> from weatherkit import heat_index_c
        >>> round(heat_index_c(30, 70), 1)
        35.0
    """
    if not 0.0 <= humidity_pct <= 100.0:
        raise ValueError("humidity_pct must be between 0 and 100")

    temp_f = c_to_f(temp_c)
    hi_f = (
        -42.379
        + 2.04901523 * temp_f
        + 10.14333127 * humidity_pct
        - 0.22475541 * temp_f * humidity_pct
        - 0.00683783 * temp_f * temp_f
        - 0.05481717 * humidity_pct * humidity_pct
        + 0.00122874 * temp_f * temp_f * humidity_pct
        + 0.00085282 * temp_f * humidity_pct * humidity_pct
        - 0.00000199 * temp_f * temp_f * humidity_pct * humidity_pct
    )
    return f_to_c(hi_f)


def classify(temp_c: float) -> str:
    """Classify a temperature into a human-friendly band.

    Args:
        temp_c: Temperature in degrees Celsius.

    Returns:
        One of ``"freezing"`` (at or below 0), ``"cold"`` (below 15),
        ``"mild"`` (below 25), ``"hot"`` (below 100), or ``"boiling"``
        (at or above 100).

    Example:
        >>> from weatherkit import classify
        >>> classify(-5)
        'freezing'
        >>> classify(20)
        'mild'
    """
    if temp_c <= FREEZING_C:
        return "freezing"
    if temp_c >= BOILING_C:
        return "boiling"
    if temp_c < 15.0:
        return "cold"
    if temp_c < 25.0:
        return "mild"
    return "hot"

# How to convert between temperature scales

weatherkit covers the three scales you are most likely to meet. Pick the
recipe that matches your task.

## Convert Celsius to Fahrenheit

```python
from weatherkit import c_to_f

c_to_f(20)    # 68.0
c_to_f(-40)   # -40.0  (the scales cross here)
```

## Convert Fahrenheit to Celsius

```python
from weatherkit import f_to_c

f_to_c(98.6)    # 37.0
round(f_to_c(72), 1)   # 22.2
```

## Convert Kelvin to Celsius

```python
from weatherkit import k_to_c

k_to_c(273.15)    # 0.0
k_to_c(300)       # 26.850000000000023  -> round() it
```

!!! warning

    `k_to_c` raises `ValueError` for negative Kelvin values, because nothing
    is colder than absolute zero.

## Chain conversions

Each function returns a plain `float`, so conversions compose:

```python
from weatherkit import c_to_f, f_to_c

f_to_c(c_to_f(23))    # 23.0 (within floating-point error)
```

## Display friendly text

Pair a conversion with [`classify`](../reference/api.md#weatherkit.classify)
to present the result to users:

```python
from weatherkit import classify

f"Room is {classify(21)}"   # 'Room is mild'
```

For full parameter and return details, see the
[API reference](../reference/api.md).

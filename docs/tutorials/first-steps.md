# First steps: a 5-minute weatherkit tutorial

This tutorial walks you through your first use of weatherkit: converting a
temperature, computing a heat index, and classifying the result. It should
take about five minutes.

!!! prerequisite

    Complete the [installation guide](../getting-started/installation.md)
    first. You need an activated virtual environment with weatherkit
    installed.

## Step 1: Open a Python shell

From the project root, with your virtual environment active:

```bash
python
```

## Step 2: Convert a temperature

weatherkit ships conversion functions for the three common temperature scales:

```python
>>> from weatherkit import c_to_f, f_to_c, k_to_c
>>> c_to_f(20)
68.0
>>> f_to_c(68)
20.0
>>> round(k_to_c(300), 2)
26.85
```

If a conversion returns an exact value, you get a clean float; otherwise use
`round()` to keep the display tidy.

## Step 3: Compute a "feels like" temperature

The heat index combines air temperature and relative humidity into an
apparent temperature:

```python
>>> from weatherkit import heat_index_c
>>> round(heat_index_c(30, 70), 1)
35.0
```

At 30 degrees Celsius and 70% relative humidity, it feels like 35 degrees.
Humidity must be given as a percentage between 0 and 100; anything else
raises a `ValueError`.

## Step 4: Classify a temperature

For quick human-readable summaries, `classify()` maps a temperature to a
band:

```python
>>> from weatherkit import classify
>>> [classify(t) for t in (-5, 10, 20, 30, 105)]
['freezing', 'cold', 'mild', 'hot', 'boiling']
```

## Step 5: Put it together

Here is the whole flow in one script — save it as `demo.py` and run it:

```python
from weatherkit import c_to_f, heat_index_c, classify

for temp_c, humidity in [(28, 60), (30, 70), (32, 80)]:
    feels = round(heat_index_c(temp_c, humidity), 1)
    print(f"{temp_c}C at {humidity}% humidity: feels like {feels}C ({classify(feels)})")
```

Expected output:

```text
28C at 60% humidity: feels like 29.5C (hot)
30C at 70% humidity: feels like 35.0C (hot)
32C at 80% humidity: feels like 44.4C (hot)
```

!!! note

    The heat index is only physically meaningful in warm conditions (about 27
    degrees Celsius and above) - see [Design notes](../explanation/design.md),
    which is why the script uses warm temperatures.

## What's next

- Browse the full [API reference](../reference/api.md) for every function's
  signature, parameters, and doctest.
- Read the [design notes](../explanation/design.md) to see why the package
  is shaped this way.

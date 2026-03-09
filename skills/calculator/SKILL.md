---
name: calculator
description: Math calculations and unit conversions. Use when the user wants to perform arithmetic, evaluate a mathematical expression, convert units (length, weight, temperature, area, volume, speed, currency), or compute percentages, powers, roots, or trigonometric functions.
license: MIT
compatibility: Requires bc (Linux/macOS) or Python (cross-platform) or PowerShell (Windows) for expression evaluation. Use run_command to evaluate expressions.
metadata:
  version: "1.0"
---

# Calculator

Perform math calculations and unit conversions using natural language.

## When to Use

- User asks to calculate, compute, evaluate, or solve a math expression
- User asks to convert between units (e.g. miles → km, °C → °F, kg → lbs)
- User asks for percentage, tip, discount, or tax calculations
- User asks for powers, roots, logarithms, or trigonometric values

## Arithmetic Operations

Supported operations:

| Operation | Example prompt |
|---|---|
| Addition / Subtraction | "What is 1024 + 768?" |
| Multiplication / Division | "Divide 144 by 12" |
| Powers | "What is 2 to the power of 10?" |
| Square roots | "Square root of 256" |
| Modulo | "What is 17 mod 5?" |
| Percentages | "What is 15% of $47.50?" |
| Order of operations | "Evaluate (3 + 4) * 2 - 1" |

## Unit Conversions

### Length
| From | To | Example |
|---|---|---|
| Miles | Kilometers | "Convert 100 miles to km" |
| Feet | Meters | "How many meters in 6 feet?" |
| Inches | Centimeters | "Convert 5 inches to cm" |

### Weight / Mass
| From | To | Example |
|---|---|---|
| Pounds | Kilograms | "Convert 180 lbs to kg" |
| Ounces | Grams | "How many grams in 2.5 oz?" |

### Temperature
| From | To | Example |
|---|---|---|
| Celsius | Fahrenheit | "Convert 37°C to Fahrenheit" |
| Fahrenheit | Celsius | "What is 98.6°F in Celsius?" |
| Kelvin | Celsius | "Convert 300K to Celsius" |

### Area
- Square feet ↔ square meters
- Acres ↔ hectares

### Volume
- Liters ↔ gallons
- Milliliters ↔ fluid ounces
- Cups ↔ milliliters

### Speed
- mph ↔ km/h
- knots ↔ mph

### Digital Storage
- Bytes, KB, MB, GB, TB conversions

### Currency
Use web search to look up live exchange rates, then perform the conversion.

## Scientific Functions

| Function | Example prompt |
|---|---|
| Sine / Cosine / Tangent | "What is sin(45°)?" |
| Logarithm (base 10) | "log(1000)" |
| Natural logarithm | "ln(e²)" |
| Factorial | "What is 10 factorial?" |
| Constants | "What is π to 10 decimal places?" |

## Execution (How to run in Akasha)

This skill has no dedicated binary. To evaluate numeric expressions, use **run_command** with one of the following:

- **Linux/macOS** : `run_command bc -l` with the expression on stdin, or `run_command bc -l -e "2+2"` (expression as argument). For more complex expressions (e.g. sqrt, sin), use Python.
- **Cross-platform (Python)** : `run_command python -c "print(eval('2+2'))"` for safe arithmetic. For sqrt, sin, etc., use `run_command python -c "import math; print(math.sqrt(256))"`.
- **Windows (PowerShell)** : `run_command powershell -Command "[math]::Sqrt(256)"` or similar for expressions.

For **unit conversions**, you can either (1) use the conversion factors in the tables above and compute via run_command (e.g. Python one-liner), or (2) for currency, use **web_search** to get the exchange rate, then compute. Do not invoke a non-existent `calculator` command; always use run_command with bc, python, or powershell.

## Behavior Guidelines

- Always show the formula or conversion factor used so the user can verify.
- Round to a sensible number of significant figures unless the user specifies precision.
- For currency conversions, state the exchange rate source and timestamp.
- If the expression is ambiguous, ask the user to clarify before computing.
- Chain conversions when necessary (e.g., inches → cm → mm).

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the calculator skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/calculator
```

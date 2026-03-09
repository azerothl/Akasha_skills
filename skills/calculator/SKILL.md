---
name: calculator
description: Math calculations and unit conversions. Use when the user wants to perform arithmetic, evaluate a mathematical expression, convert units (length, weight, temperature, area, volume, speed, currency), or compute percentages, powers, roots, or trigonometric functions.
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

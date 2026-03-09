---
name: date-time
description: Date and time calculations, timezones, and formatting. Use when the user asks for "in 3 days", "deadline next Friday", "what time in Tokyo", or "days until date". Uses run_command (date, Python datetime).
license: MIT
compatibility: Uses date (Linux/macOS) or PowerShell Get-Date (Windows), or Python datetime for cross-platform calculations.
metadata:
  version: "1.0"
---

# Date & Time

Compute relative dates (e.g. J+7, "next Monday"), differences between dates, timezone conversions, and formatted output using run_command with date, PowerShell, or Python.

## When to Use

- User asks for a date N days or weeks from now, or "next Friday", "last day of month"
- User wants the number of days between two dates or until a deadline
- User asks for the current time in another timezone or to convert between timezones
- User needs a date/time in a specific format (ISO, locale, etc.)

## Tools to Use

- **run_command** : Use `date` (Linux/macOS), `Get-Date` (PowerShell), or `python -c "from datetime import ..."` for calculations and formatting. Ensure the command is in allowed_commands.

## Execution (How to run in Akasha)

- **Current date/time** : `run_command date` (Linux/macOS) or `run_command powershell -Command Get-Date` (Windows).
- **Relative date** (e.g. in 3 days): Linux/macOS `date -d "+3 days" +%Y-%m-%d` or Python: `run_command python -c "from datetime import datetime, timedelta; print((datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'))"`.
- **Next weekday** (e.g. next Monday): Use Python with datetime and weekday arithmetic.
- **Days between dates** : Python: `(date2 - date1).days`.
- **Timezone** : `run_command TZ=Asia/Tokyo date` or Python with zoneinfo (Python 3.9+): `from zoneinfo import ZoneInfo; from datetime import datetime; print(datetime.now(ZoneInfo('Asia/Tokyo')))`.
- **Format** : Use `date +%Y-%m-%dT%H:%M:%S` or Python strftime.

Prefer Python for cross-platform and complex logic (e.g. "last Friday of the month"); use date or PowerShell for simple queries when available.

## Behavior Guidelines

- Always state the timezone when showing a time (e.g. "2025-03-09 14:00 UTC" or "Europe/Paris").
- For "today" or "now", clarify the user's timezone if they did not specify; default to UTC or the system timezone and say which one.
- Use ISO 8601 for machine-readable output when the user does not specify a format.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the date-time skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/date-time
```

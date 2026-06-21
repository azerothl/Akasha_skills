---
name: home-assistant
description: Control and query a Home Assistant installation (lights, climate, sensors, scripts). Use when the user asks about smart home, domotics, room states, or automations via Home Assistant.
license: MIT
compatibility: Home Assistant reachable on LAN; Akasha connector AKASHA_HOMEASSISTANT_ENABLED=1, HA_BASE_URL in connectors.env, ha_access_token in vault; plugin homeassistant installed.
metadata:
  version: "1.0"
---

# Home Assistant (domotique)

Piloter la maison via le plugin **homeassistant** et le connecteur Akasha (pas de stack radio dans Akasha).

## When to Use

- Allumer/éteindre lumières, volets, prises
- Lire température, capteurs, présence
- Lancer scénarios / scripts HA
- Répondre « quelle est la température du salon ? »

## Setup (once)

1. Install Home Assistant and integrate devices (Zigbee/Z-Wave/Matter in HA).
2. Akasha **Settings → Connectors** : enable Home Assistant, **Detect** URL, set vault token.
3. `akasha plugin install …/plugins/homeassistant` then `akasha plugin reload`.
4. Optional events: run `akasha-homeassistant-sidecar` (see plugin README).

## Tools to Use

- **ha_list_entities** [domain] — find entity_id (never guess)
- **ha_get_state** entity_id — read before acting
- **ha_call_service** domain service entity_id [json] — actions (light.turn_on, …)
- **ha_run_script** script_id — run HA scripts

Requires `plugin.call` or named `ha_*` tools in tool profile.

## Safety

- Always **ha_get_state** or **ha_list_entities** before changing state.
- **lock**, **alarm_control_panel**, **cover**, **valve** : require user confirmation; use HITL / `confirm:true` only when user explicitly approved.
- Do not store tokens in chat; connector injects credentials.

## Entity map (customize)

Fill your home (helps routing):

| Room | Lights | Climate | Sensors |
|------|--------|---------|---------|
| Salon | light.salon | climate.salon | sensor.salon_temp |
| Chambre | light.chambre | — | binary_sensor.chambre_motion |

## Installation

Install the home-assistant skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/home-assistant

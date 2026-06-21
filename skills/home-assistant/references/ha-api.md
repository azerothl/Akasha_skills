# Home Assistant REST API (rappels)

Base URL : `{HA_BASE_URL}` (ex. `http://127.0.0.1:8123`)

Auth : `Authorization: Bearer {token}`

| Endpoint | Method | Usage |
|----------|--------|--------|
| `/api/` | GET | Health (discovery probe) |
| `/api/states` | GET | All entities |
| `/api/states/{entity_id}` | GET | One entity |
| `/api/services/{domain}/{service}` | POST | Call service (JSON body) |

Entity id format : `{domain}.{name}` — e.g. `light.salon`, `binary_sensor.porte`.

Common services :

- `light.turn_on` / `light.turn_off` — body may include `brightness_pct`, `color_temp`
- `climate.set_temperature` — `temperature` in body
- `script.turn_on` — `entity_id: script.my_script`

Akasha plugin tools wrap these; agent should prefer `ha_*` tools over raw curl.

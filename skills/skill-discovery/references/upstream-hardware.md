# Upstream hardware skills (kicad-happy)

Akasha_skills does not mirror the full kicad-happy catalog by default. Install upstream when the user works on KiCad/PCB/BOM/EMC.

## Recommended upstream installs

Use **install_skill** with GitHub tree URLs (MIT license, aklofas/kicad-happy):

| Focus | Upstream path |
|-------|----------------|
| Core KiCad analysis | `https://github.com/aklofas/kicad-happy/tree/main/skills/kicad` |
| BOM lifecycle | `https://github.com/aklofas/kicad-happy/tree/main/skills/bom` |
| EMC pre-check | `https://github.com/aklofas/kicad-happy/tree/main/skills/emc` |

## Requirements

Document in conversation:

- KiCad on PATH for schematic/PCB analysis scripts
- Optional: ngspice, distributor API keys (DigiKey, etc.) in vault
- Scripts run via **run_command** from installed skill directory

## Akasha naming rule

If mirroring into Akasha_skills later, use **`hw-*`** prefix (e.g. `hw-kicad-review`), never identical folder names without recadrage.

Repository: https://github.com/aklofas/kicad-happy

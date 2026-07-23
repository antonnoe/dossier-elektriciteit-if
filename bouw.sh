#!/usr/bin/env bash
# Bouwketen dossier De Franse elektrische installatie.
# De bronnenvalidator draait VOOR de assemblage: faalt hij, dan stopt de bouw
# (set -e) en wordt er niets gegenereerd. Zo wordt de build niet groen op een
# openstaand bronpunt. Argumenten (bijv. --check-urls) gaan door naar de validator.
set -euo pipefail
cd "$(dirname "$0")"

echo "== 1/3  validatie bronnenregister =="
python3 valideer_bronnen.py "$@"

echo "== 2/3  assemblage dossier =="
python3 dossier/_build_dossier.py

echo "== 3/3  assemblage redactie-exemplaar =="
if command -v python3.12 >/dev/null 2>&1; then REDPY=python3.12; else REDPY=python3; fi
"$REDPY" redactie/_build.py

echo "== klaar =="

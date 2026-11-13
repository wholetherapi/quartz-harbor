# Quartz Harbor Launch Kit

Released reference implementation for the Quartz Harbor launch kit.

Quartz Harbor schedules dock crews against berth availability. The repository contains the allocation service, station fixture data, and the tuning notes from the integrator pilot.

## Contents

- `src/harbor.py` - berth allocation service.
- `src/schedules.py` - crew shift helpers.
- `data/stations.csv` - example berth fixtures.
- `experiments/tuning.md` - pilot tuning notes.

## Quick start

    python src/harbor.py --stations data/stations.csv

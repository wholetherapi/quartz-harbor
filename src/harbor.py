#!/usr/bin/env python3
"""Berth allocation service for Quartz Harbor."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Berth:
    code: str
    capacity: int
    turnaround_minutes: int


def load_berths(path: str) -> list[Berth]:
    berths = []
    with open(path, newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            berths.append(
                Berth(
                    code=row['code'],
                    capacity=int(row['capacity']),
                    turnaround_minutes=int(row['turnaround_minutes']),
                )
            )
    return berths


def allocate(berths: list[Berth], arrivals: int) -> list[dict]:
    slots = []
    start = datetime(2026, 9, 1, 6, 0)
    for berth in sorted(berths, key=lambda b: -b.capacity):
        offset = 0
        while offset < arrivals:
            slots.append({
                'berth': berth.code,
                'from': (start + timedelta(minutes=offset)).isoformat(),
                'to': (start + timedelta(minutes=offset + berth.turnaround_minutes)).isoformat(),
            })
            offset += berth.turnaround_minutes
        if len(slots) >= arrivals:
            break
    return slots[:arrivals]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--stations', required=True)
    parser.add_argument('--arrivals', type=int, default=12)
    args = parser.parse_args()
    for slot in allocate(load_berths(args.stations), args.arrivals):
        print(slot)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Crew shift helpers for Quartz Harbor."""

from datetime import time


SHIFT_TEMPLATES = {
    'day': (time(6, 0), time(14, 0)),
    'evening': (time(14, 0), time(22, 0)),
    'night': (time(22, 0), time(6, 0)),
}


def coverage(berths: int, shift: str) -> int:
    if shift not in SHIFT_TEMPLATES:
        raise ValueError(f'unknown shift {shift}')
    return max(1, (berths + 3) // 4)


def plan_shifts(berths: int) -> dict[str, int]:
    return {shift: coverage(berths, shift) for shift in SHIFT_TEMPLATES}

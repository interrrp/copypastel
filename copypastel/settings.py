import re
from os import getenv


def parse_duration(s: str) -> int:
    units = {"w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
    matches = re.findall(r"(\d+)([wdhms])", s)
    total = 0
    for value, unit in matches:
        total += int(value) * units[unit]
    return total


def get_interval_secs() -> int:
    return parse_duration(getenv("COPYPASTEL_INTERVAL", "10m"))

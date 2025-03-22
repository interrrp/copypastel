import random
from pathlib import Path


def get_random_proxy() -> str:
    return random.choice(get_proxies())


def get_proxies() -> list[str]:
    return Path("proxies.txt").read_text().splitlines()

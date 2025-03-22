import random
from pathlib import Path


def get_random_proxy() -> str:
    return random.choice(get_proxies())


def get_proxies() -> list[str]:
    return Path("socks5.txt").read_text().splitlines()

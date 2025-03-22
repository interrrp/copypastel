import random
from dataclasses import dataclass

import requests

from copypastel import REQUEST_TIMEOUT_SECS
from copypastel.proxies import get_random_proxy

COPYPASTA_JSON_URL = "https://reddit.com/r/copypasta.json?limit=100"
USER_AGENT = "Copypastel"


@dataclass(frozen=True)
class Copypasta:
    name: str
    text: str
    url: str


def get_random_copypasta() -> Copypasta:
    return random.choice(get_recent_copypastas())


def get_recent_copypastas() -> list[Copypasta]:
    proxy = get_random_proxy()
    print(f"Using SOCKS5 proxy {proxy} to fetch copypasta")

    response = requests.post(
        COPYPASTA_JSON_URL,
        headers={"User-Agent": USER_AGENT},
        proxies={"https": f"socks5h://{proxy}"},
        timeout=REQUEST_TIMEOUT_SECS,
    )
    json = response.json()

    return [
        Copypasta(
            name=post["data"]["title"],
            text=post["data"]["selftext"],
            url=post["data"]["url"],
        )
        for post in json["data"]["children"]
    ][1:]

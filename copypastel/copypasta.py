from collections.abc import Generator
from dataclasses import dataclass
from difflib import get_close_matches

import requests

from copypastel import REQUEST_TIMEOUT_SECS

COPYPASTA_JSON_URL = "https://reddit.com/r/copypasta.json?limit=100"
USER_AGENT = "Copypastel"


@dataclass(frozen=True)
class Copypasta:
    name: str
    text: str
    url: str


def copypastas() -> Generator[Copypasta]:
    seen_texts = set[str]()

    while True:
        recent = fetch_recent_copypastas()
        skipped = 0

        for copypasta in recent:
            if any(get_close_matches(copypasta.text, seen_texts, n=1, cutoff=0.8)):
                skipped += 1
                continue

            seen_texts.add(copypasta.text)
            yield copypasta

        print(f"Skipped {skipped} duplicate entries")


def fetch_recent_copypastas() -> list[Copypasta]:
    response = requests.post(
        COPYPASTA_JSON_URL,
        headers={"User-Agent": USER_AGENT},
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

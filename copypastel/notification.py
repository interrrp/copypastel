import requests

from copypastel import REQUEST_TIMEOUT_SECS
from copypastel.copypasta import Copypasta

TOPIC = "copypastas"


def send_notification(copypasta: Copypasta) -> None:
    data = {
        "topic": TOPIC,
        "title": copypasta.name,
        "message": copypasta.text,
        "markdown": True,
        "actions": [{"action": "view", "label": "View on Reddit", "url": copypasta.url}],
    }
    requests.post("https://ntfy.sh", json=data, timeout=REQUEST_TIMEOUT_SECS)

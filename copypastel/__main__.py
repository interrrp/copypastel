# ruff: noqa: T201 Allow prints

from time import sleep

from requests import HTTPError

from copypastel.copypasta import get_random_copypasta
from copypastel.notification import send_notification

MINUTE = 60
INTERVAL = 5 * MINUTE


def main() -> None:
    while True:
        try:
            print("Fetching random copypasta")
            copypasta = get_random_copypasta()
            print("Sending notification")
            send_notification(copypasta)
        except (AttributeError, HTTPError) as err:
            print(err)
        sleep(INTERVAL)


if __name__ == "__main__":
    main()

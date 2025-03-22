from time import sleep

from requests import HTTPError

from copypastel.copypasta import get_random_copypasta
from copypastel.notification import send_notification
from copypastel.settings import get_interval_secs


def main() -> None:
    while True:
        try:
            print("Fetching random copypasta")
            copypasta = get_random_copypasta()
            print("Sending notification")
            send_notification(copypasta)
        except (AttributeError, HTTPError) as err:
            print(err)

        interval = get_interval_secs()
        print("Waiting for", interval, "seconds")
        sleep(interval)


if __name__ == "__main__":
    main()

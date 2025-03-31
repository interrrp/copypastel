from time import sleep

from requests import HTTPError

from copypastel.copypasta import copypastas
from copypastel.notification import send_notification
from copypastel.settings import get_interval_secs


def main() -> None:
    for copypasta in copypastas():
        try:
            print("Sending notification")
            send_notification(copypasta)
        except HTTPError as err:
            print(err)

        interval = get_interval_secs()
        print("Waiting for", interval, "seconds")
        sleep(interval)


if __name__ == "__main__":
    main()

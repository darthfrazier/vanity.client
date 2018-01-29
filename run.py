import platform
import requests

from utils.RFID_scanner import SerialRFIDScanner


VANITY_BASE_URL = 'http://vanity-prototype.appspot.com'
VANITY_LOCAL_BASE_URL = 'http://localhost:8080'


def _read_RFID_keyboard_input():
    while True:
        id = input("Scan Tag: ")
        yield id


def run():
    scanner = None
    # TODO:: checkin source should be retrieved from scanner
    checkin_source = 'MASTER-1'

    if platform.system() == 'Linux':
        scanner = SerialRFIDScanner()
    elif platform.system() == 'Darwin':
        scanner = _read_RFID_keyboard_input()

    for id in scanner:
        # Post tag id to vanity service
        params = {'checkinSource': checkin_source}
        r = requests.put(VANITY_LOCAL_BASE_URL + '/piece/checkin/' + str(id), params=params)

        if r.status_code != 200:
            # Alert me to broken service somehow?
            print("Checkin failed")


if __name__ == '__main__':
    run()

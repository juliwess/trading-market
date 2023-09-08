import requests
import threading
import time
from pprint import pprint as pretty_print # Für übersichtliche Textausgabe

def thread_function():
    while(True):
        requests.get("http://localhost:8000/refresh-values")
        time.sleep(10)


def main():
    #The updater Thread continuously refreshes the values
    updater = threading.Thread(target=thread_function, args=(), daemon=True)

    updater.start()

    input()
    # x.join()

if __name__ == '__main__':
    main()
import requests
from pprint import pprint as pretty_print # Für übersichtliche Textausgabe

def print_response(ressource_id = ""):
    base_api_url = "http://localhost:8000/"
    response = requests.get(base_api_url + ressource_id)
    content = response.json()
    print(f"Status Code: {response.status_code}; Content -> ", end='')
    pretty_print(content)

def main():
    print_response()
    print_response("add-trader")
    print_response("remove-trader/1")

if __name__ == '__main__':
    main()
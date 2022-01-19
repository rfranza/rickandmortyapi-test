import requests
from config import utils
from pages import character


def check_that_works(scenario, url):
    response = requests.get(url)
    if response.status_code:
        print(scenario + " | " + "[PASSED]")
    else:
        print(scenario + " | " + "[FAILED]")


def send_request(url):
    return requests.get(url).json()


def that_gets_404(scenario, url):
    response = requests.get(url)
    if response.status_code == 404:
        print(scenario + " | " + "[PASSED]")
    else:
        print(scenario + " | " + "[FAILED]")


def check_the(title, objective, id_to_find):
    response = send_request(character.url + "/" + id_to_find)

    if "episode" in objective:
        location_url = utils.get_from_json_specific_field(response, objective)
    else:
        location_url = utils.get_from_json(response, "url", objective)

    if location_url:
        check_that_works(title, location_url)
    else:
        print("[Automata Log:] Tried with '" + id_to_find + "', that has an Unknown origin. Trying with other "
                                                            "Character.")
        check_the(title, objective, utils.get_random_number(character.max_number_of_characters))

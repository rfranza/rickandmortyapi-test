import pages.character
import pages.episode
import pages.location
import pages.main

from config import test
from config import utils


def main():
    test_main_api()
    test_characters_api()
    test_locations_api()
    test_episodes_api()


def test_main_api():
    print("| Testing: ", pages.main.url, " | ")
    test.check_that_works("Main API Healthcheck", pages.main.url)
    print(" ")


def test_characters_api():
    print("| Testing: ", pages.character.url, " | ")

    test.check_that_works("Characters API | Healthcheck",
                          pages.character.url)
    test.check_that_works("Characters API | Random Character",
                          pages.character.url + "/" + utils.get_random_number(pages.character.max_number_of_characters))
    test.that_gets_404("Characters API | With negative Character Number",
                       pages.character.url + "/-1")
    test.check_that_works("Characters API | For Random Page",
                          pages.character.url + "?page=" + utils.get_random_number(pages.character.max_number_of_pages))
    test.that_gets_404("Characters API | With a Page number above limit",
                       pages.character.url + "?page=" + str(pages.character.max_number_of_pages + 1))
    test.that_gets_404("Characters API | With a Character Number above the limit",
                       pages.character.url + "/" + str(pages.character.max_number_of_characters + 1))
    test.check_the("Characters API | Character's Origin",
                   "origin", str(pages.character.max_number_of_characters))
    test.check_the("Characters API | Character's Last Location",
                   "location", str(pages.character.max_number_of_characters))
    test.check_the("Characters API | Character's First Episode",
                   "episode", str(pages.character.max_number_of_characters))
    print(" ")


def test_locations_api():
    print("| Testing: ", pages.location.url, " | ")
    test.check_that_works("Locations API | Healthcheck", pages.location.url)
    test.that_gets_404("Locations API | With negative Location Number",
                       pages.location.url + "/-1")
    test.check_that_works("Locations API | For Random Page",
                          pages.location.url + "?page=" + utils.get_random_number(pages.location.max_number_of_pages))
    test.that_gets_404("Locations API | With a Page number above limit",
                       pages.location.url + "?page=" + str(pages.location.max_number_of_pages + 1))
    test.that_gets_404("Locations API | With a Locations Number above the limit",
                       pages.location.url + "/" + str(pages.location.max_number_of_locations + 1))
    test.check_that_works("Locations API | Random Location",
                          pages.location.url + "/" + utils.get_random_number(pages.location.max_number_of_locations))
    print(" ")


def test_episodes_api():
    print("| Testing: ", pages.episode.url, " | ")
    test.check_that_works("Episodes API | Healthcheck", pages.episode.url)
    test.that_gets_404("Episodes API | With negative Episode Number",
                       pages.episode.url + "/-1")
    test.check_that_works("Episodes API | For Random Page",
                          pages.episode.url + "?page=" + utils.get_random_number(pages.episode.max_number_of_pages))
    test.that_gets_404("Episodes API | With a Page number above limit",
                       pages.episode.url + "?page=" + str(pages.episode.max_number_of_pages + 1))
    test.that_gets_404("Episodes API | With a Episode Number above the limit",
                       pages.episode.url + "/" + str(pages.episode.max_number_of_episodes + 1))
    test.check_that_works("Episodes API | Random Episode",
                          pages.episode.url + "/" + utils.get_random_number(pages.episode.max_number_of_episodes))
    print(" ")


if __name__ == "__main__":
    main()

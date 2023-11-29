import allure
from pages.main_page import MainPage
from data.positions import Position


@allure.tag("web")
@allure.label("owner", "kirill_r")
@allure.feature("Search position in menu")
def test_searching_position_in_menu():
    main_page = MainPage()

    position = Position(name='Black and white')

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Search position in menu"):
        main_page.search_position_in_menu(position)

    with allure.step("Position must be in menu"):
        main_page.position_must_found(position)

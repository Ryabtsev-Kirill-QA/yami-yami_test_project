import allure
from pages.main_page import MainPage
from data.positions import Position


@allure.tag("web")
@allure.label("owner", "kirill_r")
@allure.feature("Cart")
def test_add_to_cart():
    main_page = MainPage()

    position = Position(name='Black and white')

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Fill address and coose position in menu"):
        main_page.go_to_address_form()
        main_page.choose_city('Санкт-Петербург')
        main_page.fill_street('Дворцовая площадь, д. 2')
        main_page.fill_app_number('10')
        main_page.submit_address()
        main_page.search_position_in_menu(position)
        main_page.add_to_cart()

    with allure.step("Check that position is on the cart"):
        main_page.go_to_cart()
        main_page.position_should_be_in_cart(position)

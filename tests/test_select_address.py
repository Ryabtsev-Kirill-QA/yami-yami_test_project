import allure
from pages.main_page import MainPage

@allure.tag("web")
@allure.label("owner", "kirill_r")
@allure.feature("Select delivery address")
def test_select_delivery_address():
    main_page = MainPage()

    with allure.step("Open the main page"):
        main_page.open()
        main_page.go_to_address_form()

    with allure.step("Fill address"):
        main_page.choose_city('Санкт-Петербург')
        main_page.fill_street('Дворцовая площадь, д. 2')
        main_page.fill_app_number('10')
        main_page.submit_address()

    with allure.step("Checking that delivery will be to current address"):
        main_page.should_have_address()

import time

from selene import browser, by, have, be


class MainPage:

    def __init__(self):
        self.search_button = browser.element(
            '.Button____ap3zV.Button_height76__wKvf0.Button_themeBgNone__bUMsT.DesktopNavbar_search__UbWoN')
        self.search_line = browser.element('.TextField_input__kPCFe.SearchDishesModal_textField__2QATn')
        self.menu_position = browser.element(
            '.Typography____IFtPc.Typography_fs17__YsV_0.Typography_dark__lM1H9.Typography_inline__oyzk9.CatalogItem_title__FbpD_')
        self.exit_button = browser.element(
            '.Button____ap3zV.Button_height48__QNO8u.Button_themeGreen__Kfex_.SearchDishesModal_closeButton__T7KI9')
        self.location = browser.element('.//*[@id="__next"]/main/div/div[2]/header/nav/div[1]/div[1]/div')
        self.city_dropdown = browser.element('.Typography____IFtPc.Typography_fw300__cegVr.Typography_fs17__YsV_0')
        self.city_names = browser.element(
            '.Dropdown_content__sDTm4.Dropdown_content_open__u_PiC.ChangeCity_dropdown_content__6cXJ3')
        self.address_field = browser.element('.TextField_input__kPCFe.DesktopAddressModal_addressField__Xgubk')
        self.app_number = browser.element('#Квартира')
        self.continue_button = browser.element(
            '.Button____ap3zV.Button_height56__m3SdN.Button_themeGreen__Kfex_.Button_isBorderRadius__f1LF7.DesktopAddressModal_submitButton__nHLmI')
        self.current_address = browser.element('.Geo_desktop__n1FYu')
        self.choose_address = browser.element('.AddressHints_link__y3ivD.AddressHints_active__rkYLO')
        self.name_of_street = browser.element(
            '//*[@id="__next"]/main/div/div[2]/header/nav/div[1]/div[1]/div/div/div/span/span/span[1]')
        self.number_of_house = browser.element(
            '//*[@id="__next"]/main/div/div[2]/header/nav/div[1]/div[1]/div/div/div/span/span/span[2]')
        self.add_to_cart_button = browser.element(
            '.SearchResultsProducts_cardContainer__KqCre > div:nth-child(1) > div.CatalogItem_container__wQojW > div > button')
        self.comeback_button = browser.element(
            '.Button____ap3zV.Button_height48__QNO8u.Button_themeGreen__Kfex_.SearchDishesModal_closeButton__T7KI9')
        self.go_to_cart_button = browser.element('.//*[@id="__next"]/main/div/div[2]/header/nav/div[3]/button[2]')
        self.text_in_cart = browser.element('//*[@id="__next"]/main/div/div[2]/div/div/div[2]/div/div/div[2]/a/span')
        self.clear_cart_button = browser.element('.Button____ap3zV.Button_height48__QNO8u.Button_themeBgNone__bUMsT')
        self.clear_confirm_button = browser.element(
            '.Button____ap3zV.Button_height48__QNO8u.Button_themeGreen__Kfex_.DeleteOrderModal_modal_deleteBtn__6fy6U')
        self.messagge_in_cart = browser.element('.Typography____IFtPc.Typography_fw300__cegVr.Typography_lh22__oYBsL')

    def open(self) -> None:
        browser.open("")

    def search_position_in_menu(self, position):
        self.search_button.click()
        self.search_line.type(f'{position.name}')
        return self

    def position_must_found(self, position) -> None:
        self.menu_position.should(have.text(f'{position.name}'))
        self.exit_button.press_enter()

    def go_to_address_form(self) -> None:
        self.location.click()

    def choose_city(self, city_name):
        self.city_dropdown.click()
        self.city_names.element(by.text(f'{city_name}')).click()

    def fill_street(self, current_address):
        self.address_field.clear()
        self.address_field.set_value(current_address)
        self.choose_address.should(be.visible).click()
        time.sleep(3)
        return self

    def fill_app_number(self, app_number):
        self.app_number.click()
        self.app_number.type(app_number)
        return self

    def submit_address(self):
        self.continue_button.click()
        return self

    def should_have_address(self) -> None:
        self.name_of_street.should(have.text('Дворцовая площадь'))
        self.number_of_house.should(have.text(', д. 2'))

    def add_to_cart(self):
        self.add_to_cart_button.click()
        return self

    def go_to_cart(self):
        self.comeback_button.click()
        self.go_to_cart_button.click()
        return self

    def position_should_be_in_cart(self, position):
        self.text_in_cart.should(have.text(f'{position.name}'))
        return self

    def clear_cart(self):
        self.clear_cart_button.click()
        self.clear_confirm_button.click()
        return self

    def cart_should_be_empty(self):
        self.go_to_cart_button.click()
        self.messagge_in_cart.should(have.text('В корзине пока пусто.'))
        return self

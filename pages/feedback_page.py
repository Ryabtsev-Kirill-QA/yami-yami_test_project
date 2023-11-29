from selene import browser, have, be


class FeedbackPage:

    def __init__(self):
        self.fill_name = browser.element('.TextField_input__kPCFe.ContactUsForm_input__pe9F_')
        self.fill_email = browser.element(
            'div.ContactUsPage_formWrap__MY860 > form > fieldset > div:nth-child(2) > div > input')
        self.fill_mobile = browser.element(
            'div.ContactUsPage_formWrap__MY860 > form > fieldset > div:nth-child(3) > div > input')
        self.fill_message = browser.element('.Textarea_textarea__HloBE')
        self.submit_button = browser.element(
            '.Button____ap3zV.Button_height48__QNO8u.Button_themeGreen__Kfex_.ContactUsForm_submitBtn__c60t5')
        self.successful_message = browser.element('/html/body/div[3]/div/div/div/h2[1]')

    def open(self) -> None:
        browser.open("/contact-us")

    def fill_feedback_form(self, feedback):
        self.fill_name.type(f'{feedback.user_name}')
        self.fill_email.type(f'{feedback.user_email}')
        self.fill_mobile.type(f'{feedback.user_mobile_number}')
        self.fill_message.type(f'{feedback.user_message}')
        self.submit_button.click()
        return self

    def feedback_form_should_sending(self):
        self.successful_message.should(be.visible).should(have.text('Ваше письмо отправлено'))
        return self

import allure
from pages.feedback_page import FeedbackPage
from data.users import UserFeedback


@allure.tag("web")
@allure.label("owner", "kirill_r")
@allure.feature("Feedback form")
def test_fill_feedback_form():
    feedback_page = FeedbackPage()

    feedback = UserFeedback(
        user_name='Ivan',
        user_email='example@mail.ru',
        user_mobile_number='+78008885555',
        user_message='тестовое сообщение'
    )

    with allure.step("Open the feedback page"):
        feedback_page.open()

    with allure.step("Fill feedback form"):
        feedback_page.fill_feedback_form(feedback)

    with allure.step("Check feedback"):
        feedback_page.feedback_form_should_sending()

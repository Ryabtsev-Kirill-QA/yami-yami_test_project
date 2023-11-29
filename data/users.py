import dataclasses


@dataclasses.dataclass
class UserFeedback:
    user_name: str
    user_email: str
    user_mobile_number: str
    user_message: str

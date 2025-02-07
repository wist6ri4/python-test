import re

class Validator:
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        """メールアドレスのバリデーション"""
        return bool(re.match(cls.EMAIL_REGEX, email))

    @classmethod
    def is_valid_password(cls, password: str) -> bool:
        """パスワードのバリデーション"""
        return bool(re.match(cls.PASSWORD_REGEX, password))

    @classmethod
    def validate(cls, email: str, password: str) -> dict:
        """メールアドレスとパスワードのバリデーションを行い、結果を返す"""
        return {
            "email_valid": cls.is_valid_email(email),
            "password_valid": cls.is_valid_password(password)
        }


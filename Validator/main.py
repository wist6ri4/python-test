from validator import Validator

# 動作確認
test_email = "testexample.com"
test_password = "StrongP@ss1"

validator = Validator.validate(test_email, test_password)
print(validator)
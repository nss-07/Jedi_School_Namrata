import unittest
import credit_card_validation


class TestValidator(unittest.TestCase):
    def test_validate_all(self):
        self.assertTrue(credit_card_validation.is_valid({"user_name": "Namrata Sharma",
                                                         "card_number": "79927398713",
                                                         "cvv": "333",
                                                         "valid_until": "05/25"}))
        self.assertFalse(credit_card_validation.is_valid({"user_name": "Namrata Sharma 28",
                                                         "card_number": "79927398711",
                                                         "cvv": "3313",
                                                         "valid_until": "05/25"}))

    def test_is_name_valid(self):
        self.assertTrue(credit_card_validation.is_name_valid("Namrata Sharma"))
        self.assertFalse(credit_card_validation.is_name_valid("nss-07"))

    def test_is_card_number_valid(self):
        self.assertTrue(credit_card_validation.is_card_number_valid("79927398713"))
        self.assertFalse(credit_card_validation.is_card_number_valid("79927398714"))

    def test_is_cvv_valid(self):
        self.assertTrue(credit_card_validation.is_cvv_valid(123))
        self.assertTrue(credit_card_validation.is_cvv_valid(1234))
        self.assertFalse(credit_card_validation.is_cvv_valid(12))
        self.assertFalse(credit_card_validation.is_cvv_valid(12345))

    def test_is_exp_date_valid(self):
        self.assertTrue(credit_card_validation.is_exp_date_valid("02/21"))
        self.assertTrue(credit_card_validation.is_exp_date_valid("06/23"))
        self.assertFalse(credit_card_validation.is_exp_date_valid("02-21"))
        self.assertFalse(credit_card_validation.is_exp_date_valid("02/20"))
        self.assertFalse(credit_card_validation.is_exp_date_valid("01/21"))


if __name__ == '__main__':
    unittest.main()


from datetime import datetime


def is_name_valid(name):
    for character in name:
        if not (character.isalpha() or character == ' '):
            print("Name can only contain alphabets and spaces!")
            return False
    return True


def is_card_number_valid(card_number):
    luhn_sum = 0
    even_dig = False

    for i in reversed(range(len(card_number))):
        d = int(card_number[i])
        if even_dig:
            d *= 2
        luhn_sum += (d // 10 + d % 10)

        even_dig = not even_dig
    if luhn_sum % 10 == 0:
        return True
    print("Invalid Card Number!")
    return False


def is_cvv_valid(cvv):
    if 100 < cvv < 10000:
        return True
    print("Invalid CVV!")
    return False


def is_exp_date_valid(exp_date):
    try:
        exp_month, exp_year = map(int,exp_date.split('/'))
    except:
        print("Date format invalid!")
        return False

    curr_month = datetime.now().month
    curr_year = datetime.now().year % 100

    if curr_year < exp_year or (curr_year == exp_year and curr_month < exp_month):
        return True
    print("Card expired!")
    return False


def is_valid(user_info):
    return "Successfully validated card details" if is_name_valid(user_info['user_name']) and is_card_number_valid(
        user_info['card_number']) and is_cvv_valid(int(user_info['cvv'])) and is_exp_date_valid(
        user_info['valid_until']) else "Try Again!"


if __name__ == "__main__":
    user_info = {'user_name': input("Enter name: "),
                 'card_number': input("Card number: "),
                 'cvv': input("CVV: "),
                 'valid_until': input("Valid until (MM/YY): ")}
    print(is_valid(user_info))

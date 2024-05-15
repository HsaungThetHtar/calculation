while True:
    sum_odd_digits = 0
    sum_even_digits = 0
    total = 0

    card_number = input('Enter a credit card number (enter "q" to quit): ')
    if card_number.lower() == 'q':
        break

    # Remove spaces and hyphens
    card_number = card_number.replace("-", "")
    card_number = card_number.replace(" ", "")

    # Check if the input contains only digits
    if not card_number.isdigit():
        print("Invalid input. Please enter a valid credit card number.")
        continue

    # Reverse the card number for processing
    card_number = card_number[::-1]

    for x in card_number[::2]:
        sum_odd_digits += int(x)

    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1 + (x % 10))
        else:
            sum_even_digits += x

    total = sum_odd_digits + sum_even_digits

    if total % 10 == 0:
        print("VALID")
    else:
        print("INVALID")

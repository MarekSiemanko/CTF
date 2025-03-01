from itertools import product

def luhn_check(card_number):
    digits = [int(d) for d in card_number]
    checksum = 0
    odd = True
    for i in range(len(digits) - 1, -1, -1):
        d = digits[i]
        if not odd:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
        odd = not odd
    return checksum % 10 == 0

def brute_force_luhn(partial_card):
    missing_indexes = [i for i, d in enumerate(partial_card) if d == '*']
    for combination in product('0123456789', repeat=len(missing_indexes)):
        temp_card = list(partial_card)
        for index, digit in zip(missing_indexes, combination):
            temp_card[index] = digit
        card_number = "".join(temp_card)
        if luhn_check(card_number) and int(card_number) % 123457 == 0:
            yield card_number  # Zwraca wszystkie poprawne numery

partial_card = "543210******1234"
for restored_card in brute_force_luhn(list(partial_card)):
    print("Odzyskany numer karty:", restored_card)

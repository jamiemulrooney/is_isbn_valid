
def is_valid(isbn_code):
    no_hyphens = ''
    # Remove hyphens from the code
    for i in range(len(isbn_code)):
        letter = isbn_code[i]
        if letter != '-':
            no_hyphens = no_hyphens + letter

    # Multiply each digit by 10, 9, 8 , 7 etc
    # x1*10 + x2*9 + x3*8 + ...
    sum = 0
    for i in range(10):
        letter = no_hyphens[i]
        # If letter is X then digit is 10
        if letter == 'X':
            digit = 10
        else:
            digit = int(letter)
        multiplier = 10 - i
        sum = sum + (digit * multiplier)

    # Get the remainder when divided by 11 as per the ISBN formula
    remainder = sum % 11

    # If the remainder is zero then this ISBN is valid
    if remainder == 0:
        valid = True
    else:
        valid = False

    return valid
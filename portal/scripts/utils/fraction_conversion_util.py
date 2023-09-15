
def repeating_decimal(numerator, denominator):
    # Store the integer part of the fraction
    integer_part = numerator // denominator

    # Initialize variables to track the decimal portion and remainders
    decimal_part = []
    remainders = []

    numerator %= denominator

    # Perform the long division
    while numerator and numerator not in remainders:
        remainders.append(numerator)
        numerator *= 10
        quotient, remainder = divmod(numerator, denominator)
        decimal_part.append(str(quotient))
        numerator = remainder

    # If there's a repeating sequence
    if numerator:
        index_of_repeating_sequence = remainders.index(numerator)
        non_repeating = ''.join(decimal_part[:index_of_repeating_sequence])
        repeating = ''.join(decimal_part[index_of_repeating_sequence:])
        return f"{integer_part}.{non_repeating}({repeating})"
    else:
        return f"{integer_part}." + ''.join(decimal_part)
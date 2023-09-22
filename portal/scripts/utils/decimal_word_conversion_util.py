import inflect
from word2number import w2n

def number_to_words(num):
    p = inflect.engine()
    whole, decimal = str(num).split('.') if '.' in str(num) else (str(num), None)

    word_representation = p.number_to_words(whole)

    if decimal:
        word_representation += " point " + " ".join(p.number_to_words(int(digit)) for digit in decimal)

    return word_representation


# print(number_to_words(921.31))
def round_to_nearest_10th(num):
    return round(num, -1)

def extract_places(num):
    num_str = str(num)
    if '.' in num_str:
        whole, decimal = num_str.split('.')
    else:
        whole, decimal = num_str, '0'

    # Dynamically generate place names
    place_names = {
        0: '1st',
        1: '10th',
        2: '100th',
        3: '1000th',  # This can be extended further if needed
    }
    for i in range(4, len(whole)):
        place_names[i] = f'{10**i}th'

    places_dict = {}
    for i, digit in enumerate(reversed(whole)):
        places_dict[f'{place_names[i]}_place'] = int(digit)

    places_dict['decimal_place'] = int(decimal)

    return places_dict


def text_to_decimal(text):
    try:
        decimal_value = w2n.word_to_num(text)
        return decimal_value
    except ValueError:
        return None
# print(extract_places(21.31))         # Output: {'1st_place': 1, '10th_place': 2, 'decimal_place': 31}
# print(extract_places(1.1))           # Output: {'1st_place': 1, 'decimal_place': 1}
# print(extract_places(1000))          # Output: {'1st_place': 0, '10th_place': 0, '100th_place': 0, '1000th_place': 1, 'decimal_place': 0}
# print(extract_places(2343))          # Output: {'1st_place': 3, '10th_place': 4, '100th_place': 3, '1000th_place': 2, 'decimal_place': 0}
# print(extract_places(12345678))      # Output: {'1st_place': 8, '10th_place': 7, '100th_place': 6, ...}


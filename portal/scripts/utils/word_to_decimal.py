from word2number import w2n

def text_to_decimal(text):
    try:
        decimal_value = w2n.word_to_num(text)
        return decimal_value
    except ValueError:
        return None



from decimal import Decimal, InvalidOperation
from fractions import Fraction

def check_arithmetic(sequence,n):
    diffs = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    return len(set(diffs)) == 1, diffs[0]

def check_geometric(sequence,n):
    ratios = [sequence[i] / sequence[i-1] for i in range(1, len(sequence)) if sequence[i-1] != 0]
    return len(set(ratios)) == 1, ratios[0]

def check_sequence_of_n(sequence, n):
    return all(sequence[i] == i * n for i in range(len(sequence))),n


def identify_and_generate(sequence_str, n):
    sequence = []
    logic_message = ""
    results = []

    n = int(n)

    elements = [x.strip() for x in sequence_str.split(",")]

    for element in elements:
        try:
            sequence.append(Decimal(element))
        except InvalidOperation:
            try:
                sequence.append(Fraction(element))
            except ValueError:
                raise ValueError(f"Invalid element in sequence: {element}")

    # Define pattern-checking functions
    pattern_checkers = [check_arithmetic, check_geometric, check_sequence_of_n]

    for checker in pattern_checkers:
        is_pattern, value = checker(sequence,n)
        if is_pattern:
            if checker == check_arithmetic:
                logic_message = f"a(n-1)d, where a={sequence[-1]}, d={value}."
                results = [str(sequence[-1] + i * value) for i in range(n)]
            elif checker == check_geometric:
                logic_message = f"a * r^(n-1), where a={sequence[0]}, r={value}."
                results = [str(sequence[-1] * (value ** i)) for i in range(n)]
            elif checker == check_sequence_of_n:
                sequence1 = [float(x) for x in sequence]
                for i in range(1,100):
                    is_pattern = checker(sequence, i)
                    if is_pattern:
                        n_value=i
                        logic_message = f"Pattern is i * {value}."
                        last_term = sequence[-1]
                        results = [str(last_term + (j * value)) for j in range(n)]
                        break
            # elif checker == check_sequence_of_n:
            #     logic_message = f"Pattern is i * {value}."
            #     last_term = sequence[-1]
            #     results = [str(last_term + (i * value)) for i in range(n)]
            # break  # Stop checking patterns once one is found

    if not logic_message:
        logic_message = "Pattern not recognized."

    return logic_message, "Next terms are {}".format(results)


# from decimal import Decimal
# from fractions import Fraction
# from decimal import InvalidOperation
#
# def identify_and_generate(sequence_str, n):
#     sequence = []
#     logic_message = ""
#     results = []
#
#     n = int(n)
#
#     elements = [x.strip() for x in sequence_str.split(",")]
#
#     for element in elements:
#         try:
#             sequence.append(Decimal(element))
#         except InvalidOperation:
#             try:
#                 sequence.append(Fraction(element))
#             except ValueError:
#                 raise ValueError(f"Invalid element in sequence: {element}")
#
#     diffs = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
#     ratios = [sequence[i] / sequence[i-1] for i in range(1, len(sequence)) if sequence[i-1] != 0]
#
#     if len(set(diffs)) == 1:
#         common_difference = diffs[0]
#         last_term = sequence[-1]
#         logic_message = f"a(n-1)d, where a={last_term}, d={common_difference}."
#         results = [str(last_term + i * common_difference) for i in range(n + 1)]
#         results = results[1:]
#         # results = [str(last_term + i * common_difference) for i in range(1, n)]
#     elif len(set(ratios)) == 1:
#         common_ratio = ratios[0]
#         first_term = sequence[0]
#         last_term = sequence[-1]
#         logic_message = f"a * r^(n-1), where a={first_term}, r={common_ratio}."
#
#         results = [str(last_term * (common_ratio ** i)) for i in range(n + 1)]
#         results = results[1:]
#     if not logic_message:
#         logic_message = "Pattern not recognized."
#
#     return logic_message, "Next terms are {}".format(results)
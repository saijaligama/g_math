from decimal import Decimal, InvalidOperation
from fractions import Fraction

def check_arithmetic(sequence,n):
    print("in function, arithematic")
    logic_message = ""
    results = ""
    flag = False
    diffs = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    if len(set(diffs)) == 1:
        value = diffs[0]
        logic_message = f"a(n-1)d, where a={sequence[-1]}, d={value}."
        results = [str(sequence[-1] + i * value) for i in range(n+1)]
        results.pop(0)
        flag = True
    return flag, logic_message, results

def check_geometric(sequence,n):
    logic_message = ""
    results = ""
    flag=False
    print("in function, geometric")
    ratios = [sequence[i] / sequence[i-1] for i in range(1, len(sequence)) if sequence[i-1] != 0]
    if len(set(ratios)) == 1:
        value = ratios[0]
        logic_message = f"a * r^(n-1), where a={sequence[0]}, r={value}."
        results = [str(sequence[-1] * (value ** i)) for i in range(n+1)]
        results.pop(0)
        flag=True
    return flag, logic_message, results

def identify_integer_exponents(sequence,n):
    exponent = None
    flag = False
    logic_message = ""
    results = ""
    print(sequence)
    if sequence[0]==1:
        sequence = sequence[1:]
    for term in sequence:
        term = float(term)
        for candidate_exponent in range(2, int(term)):
            root = int(term ** (1/candidate_exponent))
            if root ** candidate_exponent == term:
                print("if condition")
                if exponent is None:
                    exponent = candidate_exponent
                    flag = True
                    logic_message = f"The sequence follows the pattern of integer exponents with exponent {exponent}."
                    results = [str(i ** candidate_exponent) for i in range(len(sequence), len(sequence)+n)]
                    print(results)
                elif exponent != candidate_exponent:
                    flag = False
                    logic_message = "The sequence does not follow the pattern of integer exponents."

    if not flag:
        logic_message = "The sequence is not recognized as following any specific pattern."

    return flag, logic_message, results


def identify_alternating_sequences(sequence,n):
    flag = False
    logic_message = ""
    results = ""
    flag0,msg0, res0 = check_arithmetic([sequence[x] for x in range(0 ,len(sequence) ,2)],n//2 )
    flag1,msg1, res1 = check_arithmetic([sequence[x] for x in range(1 ,len(sequence) ,2)] ,n//2)
    final_seq = []
    if flag0 and flag1:
        flag=True
        print("in identifying alternating sequence and if function")
        for x,y in zip(res0,res1):
            final_seq.append(x)
            final_seq.append(y)
        logic_message = "Alternating arithmetic sequence"

    return flag, logic_message, final_seq




def identify_and_generate(sequence_str, n):
    sequence = []
    logic_message = ""
    results = []
    f=False
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
    pattern_checkers = [check_arithmetic, check_geometric, identify_integer_exponents, identify_alternating_sequences ]

    for checker in pattern_checkers:
        f,l,r = checker(sequence,n)
        if f:
            return l, "Next terms are {}".format(r)
    if not f:
        return "Pattern not recognized."


"""
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
                    is_pattern = checker(sequence1, i)
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

"""

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
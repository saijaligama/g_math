import math
import re


def calculate_log_from_expression(log_expression, radiovalue="dec"):
    # Regular expression to find log expressions
    pattern = r"log\(([^,]+)(?:,(\d+|e))?\)"

    # Find all matches of log expressions in the input
    matches = re.findall(pattern, log_expression)
    print(matches)
    if matches:
        # Calculate logarithm for each matched expression
        results = []
        for match in matches:
            value_str, base_str = match

            if value_str == 'e':
                value = math.e
            else:
                value = float(value_str)
            if base_str.lower() == 'e':
                base = math.e
                # result = math.log(value)
            else:
                base = float(base_str) if base_str else 10  # Set default base to 10 if not provided
                # result = math.log(value, base)

            if base <= 0 or value <= 0 or base == 1:
                return "Invalid input. Base and value must be positive, and base cannot be 1."

            result = math.log(value, base)
            results.append(result)

        # Return the sum of logarithm results
        if radiovalue == "integer":
            return int(sum(results))
        else:
            return sum(results)
    else:
        return "No valid log expression found in the input."

# Examples
# print(calculate_log_from_expression("log(8,2)"))  # Output: 3.0
# print(calculate_log_from_expression("log(8)"))     # Output: 0.903...
# print(calculate_log_from_expression("log(e)"))     # Output: 1.0 (natural logarithm)


# Examples
# print(calculate_log_from_expression("log(8,2)"))  # Output: 3.0
# print(calculate_log_from_expression("log(8)"))     # Output: 0.903...
# print(calculate_log_from_expression("log(e)"))     # Output: 1.0 (natural logarithm)



# def calculate_log_from_expression(log_expression, radiovalue="dec"):
#     # Regular expression to find log expressions
#     pattern = r"log\(([^,]+)(?:,(\d+))?\)"
#
#     # Find all matches of log expressions in the input
#     matches = re.findall(pattern, log_expression)
#
#     if matches:
#         # Calculate logarithm for each matched expression
#         results = []
#         for match in matches:
#             value_str, base_str = match
#
#             value = int(value_str)
#             base = float(base_str) if base_str else 10  # Set default base to 10 if not provided
#
#             if base <= 0 or value <= 0 or base == 1:
#                 return "Invalid input. Base and value must be positive, and base cannot be 1."
#
#             result = math.log(value, base)
#             results.append(result)
#
#         # Return the sum of logarithm results
#         if radiovalue == "integer":
#             return int(sum(results))
#         else:
#             return sum(results)
#     else:
#         return "No valid log expression found in the input."


# def calculate_log_from_expression(log_expression,radiovalue="dec"):
#     # Regular expression to find log expressions
#     pattern = r"log\(([^,]+),(\d+)\)"
#
#     # Find all matches of log expressions in the input
#     matches = re.findall(pattern, log_expression)
#
#     if matches:
#         # Calculate logarithm for each matched expression
#         results = []
#         for match in matches:
#             base_str = match[0]
#             value = int(match[1])
#
#             if base_str == 'e':
#                 result = math.log(value)
#             else:
#                 base = float(base_str)
#                 if base <= 0 or value <= 0 or base == 1:
#                     return "Invalid input. Base and value must be positive, and base cannot be 1."
#                 result = math.log(value, base)
#             results.append(result)
#
#         # Return the sum of logarithm results
#         if radiovalue == "integer":
#             return int(sum(results))
#         else:
#             return sum(results)
#     else:
#         return "No valid log expression found in the input."


# Example
# log_expression_result = calculate_log_from_expression("log(3,5) + log(2,5)")
# print("The result of log(3,5) + log(2,5) is:", log_expression_result)

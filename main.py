# Jackson Bryant
# 04/03/2025
# Arithmetic Formatter
def validate_problems(problems):
    """Validate input problems and return error messages if any."""
    if len(problems) > 5:
        return 'Error: Too many problems.'

    valid_operators = {'+', '-'}
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        first_operand, operator, second_operand = parts

        if operator not in valid_operators:
            return "Error: Operator must be '+' or '-'."

        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    return None  # No errors


def arithmetic_arranger(problems, show_answers=False):
    """Format arithmetic problems into a vertically aligned string."""
    
    error_message = validate_problems(problems)
    if error_message:
        return error_message

    first_operands, second_operands, operators, answers = [], [], [], []

    for problem in problems:
        first_operand, operator, second_operand = problem.split()

        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)

        # Compute the result
        answer = str(int(first_operand) + int(second_operand)) if operator == '+' else str(int(first_operand) - int(second_operand))
        answers.append(answer)

    # Format output
    top_row, bottom_row, dash_row, answer_row = [], [], [], []
    
    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        top_row.append(first_operands[i].rjust(width))
        bottom_row.append(operators[i] + ' ' + second_operands[i].rjust(width - 2))
        dash_row.append('-' * width)
        answer_row.append(answers[i].rjust(width))

    formatted_output = '\n'.join([
        '    '.join(top_row),
        '    '.join(bottom_row),
        '    '.join(dash_row),
    ])
    
    if show_answers:
        formatted_output += '\n' + '    '.join(answer_row)

    return formatted_output


# Test the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

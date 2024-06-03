def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы
    stack = []
    bracket_pairs = {'(': ')'}

    for bracket in brackets_row:
        if bracket in bracket_pairs.keys():   # если это открывающая скобка
            stack.append(bracket)
        elif bracket in bracket_pairs.values():   # если это закрывающая скобка
            if stack == [] or bracket_pairs[stack.pop()] != bracket:
                return False
        else:
            return False

    return stack == []


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False

    print(check_brackets(""))  # True

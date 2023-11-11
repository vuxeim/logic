from io import StringIO

from logic import Atomic
from operation import (Op, Negation,
                       Disjunction, Conjunction,
                       Implication, Bicondition)

def _get_operator(char: str) -> type:
    """
    Given valid operation symbol
    returns corresponding constructor.
    """
    return {"A": Disjunction, "K": Conjunction,
            "C": Implication, "E": Bicondition}[char]

class PolishNotation(Op):

    text = ""

    def __new__(cls, text: str) -> Atomic | Op:
        __class__.text = text
        return __class__._parse(buff=StringIO(text), index=-1)

    @staticmethod
    def _parse(*, buff: StringIO, index: int) -> Atomic | Op:
        """Recursive"""
        char = buff.read(1)
        if len(char) == 0:
            txt = __class__.text
            fmt = "{}\x1b[31m{}\x1b[0m{}".format(txt[:index], txt[index], txt[index+1:])
            raise Exception(f"Not enough arguments for formula at index {index}: {fmt}")
        index += 1
        if char == "N":
            argument = __class__._parse(buff=buff, index=index)
            return Negation(argument=argument)
        elif char in "ACEK":
            op = _get_operator(char)
            predecessor = __class__._parse(buff=buff, index=index)
            successor = __class__._parse(buff=buff, index=index)
            return op(pre=predecessor, suc=successor)
        return Atomic(char)


class ReversePolishNotation(Op):

    text = ""
    index = -1
    stack = list()

    def __new__(cls, text: str) -> Atomic | Op:
        __class__.text = text
        return __class__._parse(buff=StringIO(text))

    @staticmethod
    def _parse(*, buff: StringIO) -> Atomic | Op:
        stack = __class__.stack
        while ...:
            char = buff.read(1)
            if len(char) == 0:
                if len(stack) == 1:
                    break
                if len(stack) != 0:
                    index = __class__.index
                    txt = __class__.text
                    fmt = "{}\x1b[31m{}\x1b[0m{}".format(txt[:index], txt[index], txt[index+1:])
                    print(stack)
                    raise Exception(f"Not enough operations for argument at index {index}: {fmt}")
            __class__.index += 1
            if char == "N":
                argument = stack.pop()
                stack.append(Negation(argument=argument))
            elif char in "ACEK":
                op = _get_operator(char)
                predecessor = stack.pop()
                successor = stack.pop()
                stack.append(op(pre=predecessor, suc=successor))
            else:
                stack.append(Atomic(char))
        return stack.pop()

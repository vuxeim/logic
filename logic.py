from __future__ import annotations

from operation import (Op, Negation)


class Atomic:
    """Represents atomic sentence (p, q, r, ...)"""

    def __init__(self, value: str) -> None:
        if len(value) != 1:
            # TODO: remove that limitation
            msg = f"Variable name of an atomic sentence must be a single character: {value}"
            raise Exception(msg)
        self.value = value.lower()

    def get_atomics(self) -> set[str]:
        return {self.value}

    def eval(self, values: dict[str, int]) -> bool:
        return bool(values[self.value])

    def __str__(self) -> str:
        return self.value


class Expression:
    """Represents complex non-atomic expression"""

    def __init__(self, data: Op | Atomic, evaluation: Evaluation | None = None) -> None:
        self.data: Op | Atomic = data
        self.evaluation = evaluation
        if self.evaluation is None:
            self.evaluation = Evaluation()
        atomics = self._get_all_atomics()
        all_keys = self.evaluation.values.keys()
        diff = atomics - all_keys
        for key in all_keys - atomics:
            _ = self.evaluation.values.pop(key)
        if len(diff) > 0:
            print("Not every atomic sentence has determined value")
            print("Add evaluation for these sentences:", diff)

    def _get_all_atomics(self) -> set[str]:
        """Returns set of all atomic sentences occurring in an expression"""
        return self.data.get_atomics()

    def print(self) -> None:
        self.print_expression()
        self.print_logical_value()
        self.print_tautologicality()

    def print_expression(self) -> None:
        print(self)

    def print_logical_value(self):
        print("Given these values:")
        assert self.evaluation is not None # believe me, it really isn't
        print(*(f"{k}={v}" for k, v in self.evaluation.values.items()))
        print("This expression has a logical value of {}".format(str(self._eval()).lower()))

    def print_tautologicality(self) -> None:
        atomics = self._get_all_atomics()
        atomics_amount = len(atomics)
        # yo mama hates me for the crime below
        possibilities = set(self.data.eval({k: int(j) for k, j in zip(atomics, str(bin(i))[2:].zfill(atomics_amount))}) for i in range(2**atomics_amount))
        if all(possibilities) is True:
            return print("It is a tautology")
        if not any(possibilities) is True:
            return print("It is a contradiction")
        print("It is neither tautology nor contradiction")

    def _eval(self) -> bool:
        """Whether entire expression evaluates to true or false"""
        assert self.evaluation is not None # believe me, it really isn't
        result = self.data.eval(self.evaluation.values)
        return result

    def __str__(self) -> str:
        """Expression with outermost parentheses removed"""
        text = str(self.data)
        if not text.startswith(Negation.symbol):
            return text.removeprefix("(").removesuffix(")")
        return text


class Evaluation:

    # (a, b, ..., z), each with value 1
    default = {chr(k): 1 for k in range(97, 97+26)}

    def __init__(self, **kwargs: int) -> None:
        bad = {k: v for k, v in kwargs.items() if v not in (0, 1)}
        if len(bad) > 0:
            print("An atomic sentence can only have a value either 0 or 1")
            print("Change values for these sentences:", bad)
        good = {k: v for k, v in kwargs.items() if v in (0, 1)}
        self.values = good if len(good) > 0 else self.default
        if len(good) == 0:
            print("Using default evaluation, every atomic sentence has value of 1")

    def __str__(self) -> str:
        return str(self.values)

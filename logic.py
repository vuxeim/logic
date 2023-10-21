from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from operation import _Op


class Atomic:
    """Represents atomic sentence (p, q, r, ...)"""

    def __init__(self, value: str) -> None:
        self.value = value

    def get_atomics(self) -> set[str]:
        return {self.value}

    def eval(self, values: dict[str, int]) -> bool:
        return values.get(self.value)

    def __str__(self) -> str:
        return self.value


class Expression:
    """Represents complex non-atomic expression"""

    def __init__(self, data: _Op | Atomic, evaluation: Evaluation = None) -> None:
        self.data: _Op | Atomic = data
        self.evaluation = evaluation
        if self.evaluation is None:
            self.evaluation = Evaluation()
        diff = self._get_all_atomics() - self.evaluation.values.keys()
        if len(diff) > 0:
            print("Not every atomic sentence has determined value")
            print("Add evaluation for these sentences:", diff)

    def _get_all_atomics(self) -> set[str]:
        """Returns set of all atomic sentences occurring in an expression"""
        return self.data.get_atomics()

    def print(self) -> None:
        print(self)

    def eval(self) -> bool:
        """Whether entire expression evaluates to true or false"""
        result = self.data.eval(self.evaluation.values)
        print("It is {}".format(str(result).lower()))
        return result

    def __str__(self) -> str:
        """Expression with outermost parentheses removed"""
        return str(self.data).removeprefix("(").removesuffix(")")


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

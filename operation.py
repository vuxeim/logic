from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Atomic


class _Op:
    """Represents non-atomic sentence"""

    symbol: str
    table: dict[tuple[bool, bool] | bool, bool]
    def eval(self, values: dict[str, int]) -> bool: ...
    def get_atomics(self) -> set[str]: ...


class _SingleArgumentOp(_Op):

    def __init__(self, argument: _Op | Atomic) -> None:
        self.argument = argument

    def get_atomics(self) -> set[str]:
        return self.argument.get_atomics()

    def eval(self, values: dict[str, int]) -> bool:
        return self.table.get(self.argument.eval(values))

    def __str__(self) -> str:
        return "-{}".format(self.argument)


class _DoubleArgumentOp(_Op):

    def __init__(self, pre: _Op | Atomic, suc: _Op | Atomic) -> None:
        self.predecessor = pre
        self.successor = suc

    def get_atomics(self) -> set[str]:
        return self.predecessor.get_atomics() | self.successor.get_atomics()

    def eval(self, values: dict[str, int]) -> bool:
        pair = self.predecessor.eval(values), self.successor.eval(values)
        return self.table.get(pair)

    def __str__(self) -> str:
        return "({} {} {})".format(self.predecessor, self.symbol, self.successor)


class Negation(_SingleArgumentOp):

    symbol = "-"

    table = {True: False, False: True}


class Disjunction(_DoubleArgumentOp):

    symbol = "v"

    table = {(True, True): True,
             (True, False): True,
             (False, True): True,
             (False, False): False}


class Conjunction(_DoubleArgumentOp):

    symbol = "^"

    table = {(True, True): True,
             (True, False): False,
             (False, True): False,
             (False, False): False}


class Implication(_DoubleArgumentOp):

    symbol = "->"

    table = {(True, True): True,
             (True, False): False,
             (False, True): True,
             (False, False): True}


class Bicondition(_DoubleArgumentOp):

    symbol = "<->"

    table = {(True, True): True,
             (True, False): False,
             (False, True): False,
             (False, False): True}

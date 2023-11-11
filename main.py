from operation import (Op, Negation,
                       Disjunction, Conjunction,
                       Implication, Bicondition)

from logic import Evaluation, Atomic, Expression, PolishNotation


def case1():
    ev = Evaluation(p=1, q=1, r=0)
    conj = Conjunction(pre=Atomic("p"), suc=Atomic("q"))
    impl = Implication(pre=conj, suc=Atomic("r"))
    e = Expression(impl, evaluation=ev)
    e.print()
    e.print_logical_value()
    e.print_tautologicality()

def case2():
    pn = PolishNotation("NANpp")
    e = Expression(pn, evaluation=Evaluation(p=0))
    e.print()
    e.print_logical_value()
    e.print_tautologicality()

def main() -> None:
    case1()
    case2()

if __name__ == "__main__":
    main()

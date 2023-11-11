from operation import (Op, Negation,
                       Disjunction, Conjunction,
                       Implication, Bicondition)

from logic import Evaluation, Atomic, Expression
from notation import PolishNotation, ReversePolishNotation


def case1():
    ev = Evaluation(p=1, q=1, r=0)
    conj = Conjunction(pre=Atomic("p"), suc=Atomic("q"))
    impl = Implication(pre=conj, suc=Atomic("r"))
    e = Expression(impl, evaluation=ev)
    e.print()
    print()

def case2():
    pn = PolishNotation("ANpp")
    e = Expression(pn, evaluation=Evaluation(p=0))
    e.print()
    print()

def case3():
    e = Expression(Atomic('p'), evaluation=Evaluation(p=1))
    e.print()
    print()

def case4():
    rpn = ReversePolishNotation('ppNK')
    e = Expression(rpn)
    e.print()
    print()

def main() -> None:
    case1()
    case2()
    case3()
    case4()

if __name__ == "__main__":
    main()

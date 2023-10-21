from operation import (Op, Negation,
                       Disjunction, Conjunction,
                       Implication, Bicondition)

from logic import Evaluation, Atomic, Expression, PolishNotation


def main() -> None:
    print("Expression number 1:")
    ev = Evaluation(p=1, q=1, r=0)
    conj = Conjunction(pre=Atomic("p"), suc=Atomic("q"))
    impl = Implication(pre=conj, suc=Atomic("r"))
    e = Expression(impl, evaluation=ev)
    e.print()
    e.eval()

    print("\nExpression number 2:")
    var = "AlANAlAlAKAKaoeliAElaAni"
    e = Expression(PolishNotation(var))
    e.print()
    e.eval()


if __name__ == "__main__":
    main()

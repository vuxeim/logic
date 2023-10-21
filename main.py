from operation import (Negation,
                       Disjunction, Conjunction,
                       Implication, Bicondition)

from logic import Evaluation, Atomic, Expression


def main() -> None:
    ev = Evaluation(p=1,q=0)
    impl = Implication(pre=Atomic("p"), suc=Atomic("q"))
    e = Expression(impl, evaluation=ev)
    e.print()
    e.eval()


if __name__ == "__main__":
    main()

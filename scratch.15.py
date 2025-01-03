

def _main():
    tree = ExpressionTree()

    r = tree.add_root("-")
    rl = tree.add_left(r, "/")
    rll = tree.add_left(rl, "*")
    rlll = tree.add_left(rll, "+")
    rllll = tree.add_left(rlll, "3")
    rlllr = tree.add_right(rlll, "1")
    rllr = tree.add_right(rll, "3")
    rlr = tree.add_right(rl, "+")
    rlrl = tree.add_left(rlr, "-")
    rlrll = tree.add_left(rlrl, "9")
    rlrlr = tree.add_right(rlrl, "5")
    rlrr = tree.add_right(rlr, "2")
    rr = tree.add_right(r, "+")
    rrl = tree.add_left(rr, "*")
    rrll = tree.add_left(rrl, "3")
    rrlr = tree.add_right(rrl, "-")
    rrlrl = tree.add_left(rrlr, "7")
    rrlrr = tree.add_right(rrlr, "4")
    rrr = tree.add_right(rr, "6")

    print(tree, end='')
    print('=',tree.evaluate(tree.root))


if __name__ == '__main__':
    _main()

((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))= -13.0

QUESTION 1 

def _main():
    tree = ExpressionTree()

    r = tree.add_root("*")
    rl = tree.add_left(r, "-")
    rll = tree.add_left(rl, "+")
    rlll = tree.add_left(rll, "+")
    rllll = tree.add_left(rlll, "12")
    rlllr = tree.add_right(rlll, "2")
    rllr = tree.add_right(rll, "4")
    rlr = tree.add_right(rl, "+")
    rlrl = tree.add_left(rlr, "-")
    rlrll = tree.add_left(rlrl, "9")
    rlrlr = tree.add_right(rlrl, "5")
    rlrr = tree.add_right(rlr, "2")
    rr = tree.add_right(r, "+")
    rrl = tree.add_left(rr, "*")
    rrll = tree.add_left(rrl, "3")
    rrlr = tree.add_right(rrl, "-")
    rrlrl = tree.add_left(rrlr, "*")
    rrlrll = tree.add_left(rrlrl, "3")
    rrlrlr = tree.add_right(rrlrl, "9")
    rrlrr = tree.add_right(rrlr, "+")
    rrlrrr = tree.add_right(rrlrr, "4")
    rrlrrl = tree.add_left(rrlrr, "5")
    rrr = tree.add_right(rr, "6")

    print(tree, end='')
    print('=',tree.evaluate(tree.root))


if __name__ == '__main__':
    _main()
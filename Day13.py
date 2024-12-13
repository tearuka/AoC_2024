#!/usr/bin/env python
# coding: utf-8

inp = open("inp/input_13.txt").read().split("\n\n")

def push_button(instructions, costA, costB, part):
    total_cost = 0
    shift = 10000000000000
    for line in instructions:
        res = re.split(r"Button A: X\+|, Y\+|\nButton B: X\+|, Y\+|\nPrize: X\=|, Y\=", line)[1:]
        Ax, Ay, Bx, By, Px, Py = [int(num) for num in res]
        if part == 2:
            Px, Py = shift + Px, shift + Py
        pushA = (Py - By*Px/Bx) / (Ay - By*Ax/Bx)
        pushB = Px/Bx - Ax/Bx * (Py - By*Px/Bx) / (Ay - By*Ax/Bx)
        if round(pushA)*Ax + round(pushB)*Bx == Px and round(pushA)*Ay + round(pushB)*By == Py:
            cost = costA*round(pushA) + costB*round(pushB)
            total_cost += cost
    return total_cost

# Part 1
print("Result for part 1: ", push_button(inp,3,1,1))  # 35997

# Part 2
print("Result for part 2: ", push_button(inp,3,1,2))  # 82510994362072

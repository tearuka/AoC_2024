#!/usr/bin/env python
# coding: utf-8

# Read input
inp = open("inp/input_01.txt").read().splitlines()

listA, listB = [], []
for line in inp:
    A, B = line.split("   ")
    listA.append(int(A))
    listB.append(int(B))

distance = 0
for el1, el2 in zip(sorted(listA), sorted(listB)):
    distance += abs(el1 - el2)

similarity_score = 0
for number in listA:
    similarity_score += number * listB.count(number)

# Part 1
print("Result for part 1: ", distance)  # 2904518

# Part 2
print("Result for part 2: ", similarity_score)  # 18650129
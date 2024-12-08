#!/usr/bin/env python
# coding: utf-8

# Read input 
inp = open("inp/input_08.txt").read().splitlines()

ymin, ymax = 0, len(inp)
xmin, xmax = 0, len(inp[0])

antennas = {}
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] != ".":
            if inp[y][x] not in antennas:
                antennas.update({inp[y][x]: [[y,x]]})
            else:
                antennas[inp[y][x]].append([y,x])

def count_antinodes(antennas, start_range, finish_range):
    all_antinodes = []
    for keys in antennas:
        positions = antennas[keys]
        for i in range(len(positions)+1):
            for j in range(i+1,len(positions)):
                delta_y = positions[i][0] - positions[j][0]
                delta_x = positions[i][1] - positions[j][1]
                for n in range(start_range,finish_range):
                    antinodes = [[positions[i][0] + n*delta_y, positions[i][1] + n*delta_x],[positions[j][0] - n*delta_y, positions[j][1] - n*delta_x]]
                    for antinode in antinodes:
                        if antinode[0] in range(ymin,ymax) and antinode[1] in range(xmin,xmax):
                            if antinode not in all_antinodes:
                                all_antinodes.append(antinode)
    return len(all_antinodes)

# Part 1
print("Result for part 1: ", count_antinodes(antennas, 1, 2))  # 214

# Part 2
print("Result for part 2: ", count_antinodes(antennas, 0, len(inp)))  # 809
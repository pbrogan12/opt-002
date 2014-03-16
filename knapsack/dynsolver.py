#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]), int(parts[0]) / float(parts[1])))
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    table = []
    count = 0
    for item in items:
        tempTable = []
        for i in range(0, capacity + 1):
            if count != 0:
                prevRowValue = table[count - 1][i]

                try:
                    newValue = table[count - 1][i - item.weight] + item.value
                except:
                    newValue = prevRowValue

                if i < item.weight:
                    tempTable.append(prevRowValue)
                elif item.weight < newValue > prevRowValue:
                    tempTable.append(newValue)
                else:
                    if prevRowValue > item.value:
                        tempTable.append(prevRowValue)
                    else:
                        tempTable.append(item.value)

            else:
                if i >= item.weight:
                    tempTable.append(item.value)
                else:
                    tempTable.append(0)
        table.append(tempTable)
        count += 1
        print count
    for i in table:
        print i
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'


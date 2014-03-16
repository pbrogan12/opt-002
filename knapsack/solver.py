#!/usr/bin/python
# -*- coding: utf-8 -*-
import ast
import linecache
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def solve_it(input_data):
    # Modify cur code to run your optimization algorithm
    file = open('/Volumes/Foo/table.txt','w')
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
        for thisCapacity in range(0, capacity+1):
            if count:
                prevValue = table[0][thisCapacity]

                if item.weight > thisCapacity:
                    tempTable.append(prevValue)
                    continue
                newValue = table[0][thisCapacity - item.weight] + item.value

                if newValue > prevValue:
                    tempTable.append(newValue)
                else:
                    tempTable.append(prevValue)
            else:
                if thisCapacity >= item.weight:
                    tempTable.append(item.value)
                else:
                    tempTable.append(0)

        table.append(tempTable)
        file.write(str(tempTable) + '\n')
        if count != 0:
            del table[0]
        count += 1
    file.close()
    count = len(items) + 1
    curPos = capacity
    value = 0
    items = sorted(items, key=lambda item: item[0], reverse=True)
    value = ast.literal_eval(linecache.getline('/Volumes/Foo/table.txt',len(items)))[-1]
    for i in items:
        if count > 2:
            curValue = ast.literal_eval(linecache.getline('/Volumes/Foo/table.txt',count - 1))[curPos]
            forValue = ast.literal_eval(linecache.getline('/Volumes/Foo/table.txt',count - 2))[curPos]
            if curValue == forValue:
                count -= 1
            else:
                curPos = curPos - i.weight
                count -= 1
                taken[i.index] = 1
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
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


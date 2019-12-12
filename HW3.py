# Alex McKee
# wsuid : 011659950

from functools import reduce
from typing import List, Any, Tuple

colors = ['red', 'green', 'blue']
# for name in colors:
#   print(name)

d = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5},
     'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan': {'task3': 12},
     'Helen': {'task3': 10}}


# 1a
def sprintLog(sprnt):
    d = {}
    dlist = (sprnt.items())
    # print(sprnt)
    for name, dict in dlist:
        nesteddictlist = list(dict.items())

        for task, hours in nesteddictlist:  # want to add task as key  and name and hours as value
            if task not in d.keys():
                d[task] = {}
                d[task][name] = hours
            else:
                d[task][name] = hours

    return d


d2 = sprintLog(d)
# print(d2)

sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15},
           'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10},
           'task4': {'Helen': 16}}


# 1b
def addSprints(sprint1, sprint2):
    d = {}
    d.update(sprint1)

    sprint2list: List[Any] = list(sprint2.items())
    # this block adds tasks not already in return dict to it
    for task, dict in sprint2list:
        nesteddictlist = list(dict.items())
        if task not in d.keys():
            d[task] = {}
            d[task] = dict
        else:  # task is in dictionary, scan through dictionary (dict) of sprint2 to see if need to add
            for (name, hours) in nesteddictlist:
                if name not in d[task].keys():
                    d[task][name] = hours
                elif name in d[task].keys():  # name already in (task1: {john : 1} ) need to add the extra hours
                    d[task][name] += hours

                    # do nothing, dont double count

        # to d

    return d


mergedDictionary = addSprints(sprint1, sprint2)
print(mergedDictionary)

logList = [{'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5},
            'Alex': {'task1': 11, 'task2': 2, 'task3': 1},
            'Aaron': {'task2': 15}, 'Ethan': {'task3': 12}, 'Helen': {'task3': 10}},
           {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2},
            'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}},
           {'Alex': {'task3': 10, 'task2': 5, 'task4': 6}, 'Rae': {'task3': 5, 'task5': 16}, 'Mark': {'task4': 20},
            'Kelly': {'task2': 5, 'task3': 10, 'task4': 12}, 'Helen': {'task5': 10, 'task4': 8}}]


# 1c
def addNLogs(logList):
    if len(logList) == 0:
        return {}
    mappedLogList1 = map(sprintLog, logList)
    reducedLogList1 = reduce(addSprints, mappedLogList1)
    return reducedLogList1


print(addNLogs(logList))


# BEGIN 2
# 2a
def lookupVal(list, val):
    for dict in reversed(list):
        if val in dict.keys():
            return dict[val]


L1 = [{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}]
keyVal = lookupVal(L1, "T")


# 2b

def lookupVal2Helper(L2: object, key: int, nextIndex: int) -> dict:
    # check if key is in dict
    if key in L2[nextIndex][1].keys():
        return L2[nextIndex][1]
    else:
        return lookupVal2Helper(L2, key, L2[nextIndex][0])


def lookupVal2(L2, key):
    if key in L2[-1][1].keys():
        return L2[-1][1][key]
    else:
        x = {}
        x = lookupVal2Helper(L2, key, L2[-1][0])
        return x[key]


L2b = [(0, {"x": 0, "y": True, "z": "zero"}),
       (0, {"x": 1}),
       (1, {"y": False}),
       (1, {"x": 3, "z": "three"}),
       (2, {})]

shouldBe1 = lookupVal2(L2b, "x")
shouldBeZero = lookupVal2(L2b, "z")


# 3
def unzip(LTrip):
    a = list(map(lambda x: x[0], LTrip))
    b = list(map(lambda x: x[1], LTrip))
    c = list(map(lambda x: x[2], LTrip))
    retList = []
    retList.append(a)
    retList.append(b)
    retList.append(c)
    retTuple: Tuple[List[Any], ...] = tuple(retList)
    return retTuple


LTriples = [(1, "a", {1: "a"}), (2, "b", {2: "b"}), (3, "c", {3: "c"}), (4, "d", {4: "d"})]
tuple3 = unzip(LTriples)


# 4
def numPathsHelper(rows, cols, curRow, curCol, Blocks):
    # base cases
    if curRow == rows and curCol == cols:
        return 1
    elif (curRow, curCol) in Blocks:
        return 0
    elif curRow > rows:
        return 0
    elif curCol > cols:
        return 0
    else:
        return numPathsHelper(rows, cols, curRow + 1, curCol, Blocks) + numPathsHelper(rows, cols, curRow, curCol + 1,
                                                                                       Blocks)


def numPaths(rows, cols, Blocks):
    totalPaths = numPathsHelper(rows, cols, 1, 1, Blocks)
    return totalPaths


paths = numPaths(3, 3, [(2, 3)])


# 5
class iterFile():
    def __init__(self, text: object) -> object:
        self.readFile = open(text, "r")
        self.lineBuffer = []
        self.line = self.readFile.readline()
        self.lineBuffer = self.line.split()

    def __next__(self):
        if len(self.lineBuffer) == 0 and self.line == '':
            raise StopIteration
        elif len(self.lineBuffer) == 0:  # no more tokens, get a new line to read
            while (len(self.lineBuffer) == 0):
                self.line = self.readFile.readline()
                self.lineBuffer = self.line.split()
                if self.line == '':
                    raise StopIteration
            if len(self.lineBuffer) != 0:
                return self.lineBuffer.pop(0)
        else:  # there is at least one token
            return self.lineBuffer.pop(0)

    def __iter__(self):
        return self


def wordHistogram(words):
    x = {}
    for word in words:
        if word in x.keys():
            x[word] += 1
        else:
            x[word] = 1
    return sorted(list(x.items()), key=lambda item: item[1], reverse=True)

print(wordHistogram(iterFile("testfile.txt")))

# tester = iterFile("testfile.txt")

# tester.__next__()
# tester.__next__()

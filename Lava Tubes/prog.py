#%
def get_data():
    with open("data.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    return [[int(l) for l in str(line)] for line in lines]

class DataC:
    row = 0
    col = 1
    def __init__(self):
        self.data = get_data()
        self.height = len(self.data)
        self.width = len(self.data[0])
        self.index = [(x,y) for x in range(self.height) for y in range(self.width)]

    def value(self, entry):
        return self.data[entry[0]][entry[1]]

    def in_bounds(self, n):
        return n[DataC.row] >= 0 and n[DataC.col] >= 0 and n[DataC.row] <self.height and n[DataC.col] <self.width

    def get_neighbors(self, test):
        neigh = [(test[DataC.row]+1,test[DataC.col]),
               (test[DataC.row]-1,test[DataC.col]),
               (test[DataC.row],test[DataC.col]+1),
               (test[DataC.row],test[DataC.col]-1)]
        return [n for n in neigh if self.in_bounds(n)]

    def is_min(self, test):
        def condition(self,test,against):
            return self.value(test) < self.value(against)
        return all([condition(self,test,against) for against in self.get_neighbors(test)])

    def get_basin(self, test, basin):
        basin.add(test)
        neigh = [n for n in self.get_neighbors(test) if self.value(n) != 9 and n not in basin]
        for next in neigh:
            if not next in basin:
                basin = self.get_basin(next, basin)
        return basin

    def get_basins(self):
        mins = [test for test in self.index if self.is_min(test)]
        return [self.get_basin(test, set()) for test in mins]

def top3(li):
    out =[]
    for i in range (2):
        out.append(max(li))
        li = [l for l in li if l != out[i]]
    out.append(max(li))
    return out

data = DataC()
basins_size = [len(b) for b in data.get_basins()]
t3 = top3(basins_size)

print(t3[0]*t3[1]*t3[2])

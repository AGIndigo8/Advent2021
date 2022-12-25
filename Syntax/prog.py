#%
import copy
from tables import Tables
import time
t0=time.time()
class delim_count:
    error_points_table = Tables.points #Dictionary for counting score key:value -> delim:points_per. Static ref.
    correction_points_table = Tables.correction
    actions = Tables.actions #table describing how certain chars take effect. key:value -> other*char*:(self.count_section , effect_on_self.count_section*+or-1*)
    def __init__(self):
        self.count = copy.deepcopy(Tables.count_init) #Dictionary for tallying delims. '(','[','{','<' : 0
        self.stack = []
        self.bad = "*"

    def get_points(self):
        return sum([delim_count.error_points_table[key] * self.count[key] for key in self.count])

    def settle_stack(self, key, act):
        if act >0 : #opening delimiter
            self.stack.append(key)
        elif key == self.stack[-1]: #matching closing delimiter
            self.stack.pop(-1)
        else: #unmatching closing delimiter
            self.bad = key

    def __iadd__(self, other):
        if other in self.actions:
            key, act = self.actions[other]
            self.count[key] += act
            self.settle_stack(key, act)
        return self

    def correction_score(self):
        """"Returns the correction score. Assumes that all chars have been added"""
        score = 0
        for token in reversed(self.stack):
            score = (score*5) + delim_count.correction_points_table[token]
        return score

class line_manager:
    def prepare(self):
        for c in self.line:
            self.count += c
            if self.count.bad != "*":
                break

    def __init__(self, line):
        self.count = delim_count()
        self.line = line
        self.prepare()
        self.correction_score = self.count.correction_score()

    def bad(self):
        return self.count.bad

with open('data.txt') as f:
    lines = [line.strip() for line in f.readlines()]

results = [line_manager(line) for line in lines]
error_count = delim_count()
for count in results:
    error_count += count.bad()
print("Error Score: ", error_count.get_points())
results = [line.correction_score for line in results if line.bad() =="*"]
results.sort()
print("Correction Score: ", results[(len(results)//2)+1])
t1=time.time()
print(t1-t0)

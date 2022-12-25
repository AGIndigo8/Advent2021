class lanternfish:
    reset_days = 6
    spawn_days = 8
    def __init__(self, clock):
        self.clock = clock

    def total(self, days):
        days -= self.clock
        out=1
        for remaining_days in range(days,0,-lanternfish.reset_days-1):
            out += lanternfish(lanternfish.spawn_days).total(remaining_days-1)
        return out

def fishcount_by_days():
    with open('data.txt') as f:
        data = f.read()
    data = data.split(',')
    data = [int(datum) for datum in data]
    out = [0] * lanternfish.spawn_days
    for datum in data:
        out[datum] += 1
    print(out)
    return out

fish = fishcount_by_days()
fish = [lanternfish(days).total(256) * pop for days, pop in enumerate(fish)]
print(sum(fish))

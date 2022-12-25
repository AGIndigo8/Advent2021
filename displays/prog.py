#%
def sts(s):
    out =""
    for c in s:
        out+=c
    return out

class display:
    #key is number of segments, value is number on display
    magic_lengths = {2 : 1,
                    4 : 4,
                    3 : 7,
                    7 : 8}
    def __init__(self, data):
        self.pattern = data["pattern"]
        self.output = data["output"]

    def decipher_magic(self):
        def magic_match(p):
            return any([len(p) == magic for magic in display.magic_lengths])
        magic_patterns = [p for p in self.pattern if magic_match(p)]
        for p in magic_patterns:
            self.cipher[sts(p)] = display.magic_lengths[len(p)]
        #inverted dictionary for magic values for convenience
        self.invd = {digit : pattern for pattern, digit in self.cipher.items()}
        #getting rid of all of the magic patterns for convenience
        self.pattern = [p for p in self.pattern if p not in magic_patterns]

    def intersectional_decipher(self):
        def algorithm(self, magic_pattern, solution):
            def condition(pattern, magic_pattern, solution):
                return len(pattern.intersection(magic_pattern)) == solution
            match = [pattern for pattern in self.pattern if condition(pattern, magic_pattern, solution)]
            return match[0]

        def decipher_number(self, magic_pattern, solution, digit_value):
            pattern = algorithm(self, magic_pattern, solution)
            self.cipher[sts(pattern)] = digit_value
            self.pattern.remove(pattern)
            return pattern

        decipher_number(self, magic_pattern=self.invd[4], solution=4, digit_value=9)
        two = decipher_number(self, magic_pattern=self.invd[4], solution=2, digit_value=2)
        decipher_number(self, magic_pattern=two, solution=3, digit_value=5)
        six = decipher_number(self, magic_pattern=self.invd[7], solution=2, digit_value=6)
        decipher_number(self, magic_pattern=six, solution=5, digit_value=0)
        decipher_number(self, magic_pattern=six, solution=4, digit_value=3)


    def decipher(self):
        self.cipher = dict() #key:value -> pattern:digit
        self.decipher_magic()
        self.intersectional_decipher()

    def read(self):
        self.decipher()
        output = [sts(out) for out in self.output]
        code = [str(self.cipher[out]) for out in output]
        code = "".join(code)
        return int(code)

def extract_data(line):
    data = [l.strip() for l in line.split('|')]
    pattern = data[0].split(' ')
    output = data[1].split(' ')
    data = {'pattern': [set(sorted(p)) for p in pattern],
            'output': [set(sorted(o)) for o in output]}
    return data

with open('data.txt') as f:
    lines = f.readlines()
displays = [display(extract_data(line)) for line in lines]
print(sum([dis.read() for dis in displays]))

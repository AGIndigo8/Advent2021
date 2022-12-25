#Externalized appendix of dictionaries used in delim_count class.

class Tables:
    #points scored for each error
    points = {
                '(':3,
                '[':57,
                '{':1197,
                '<':25137
    }

    #points scored for each correction
    correction = {
                '(':1,
                '[':2,
                '{':3,
                '<':4
    }

    #table describing how certain chars take effect. key:value -> other:(self.count_section , effect_on_self.count_section)
    actions = {
                '(': ('(',1),
                ')': ('(',-1),
                '[': ('[',1),
                ']': ('[',-1),
                '{': ('{',1),
                '}': ('{',-1),
                '<': ('<',1),
                '>': ('<',-1)
    }
    #table to initialize delim_count.count
    #use deep copy
    count_init = {
                    "(" : 0,
                    "[" : 0,
                    "{" : 0,
                    "<" : 0
    }

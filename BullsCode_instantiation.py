import random

"""""
def sort(iterable):
    result = []
    for i in iterable:
        if i == "B":
            result += "B"
            iterable.remove(i)
    result += iterable
    return result
"""

def shuffle(iterable):
    result = []
    while len(iterable) > 0:
        num = random.randint(0, len(iterable)-1)
        result += iterable[num]
        iterable.remove(iterable[num])
    return result


class BullsCode:
    code = None

    def __init__(self, code=None):
        if code is None:
            code = ""
            for x in range(0, 4):
                code += str(random.randint(0, 9))
            #print(int(*code))
        self.code = code

    def check(self, guess):
        score = []
        potential = []
        for i in range(0, len(guess)):
            if self.code[i] == guess[i]:
                char = self.code[i]
                self.code.replace(char, "")
                score += "B"
                if char in potential:
                    if char not in self.code:
                        potential.remove(char)
                        score.remove("C")
            elif guess[i] in self.code:
                potential += guess[i]
                score += "C"
        return shuffle(score)


a = BullsCode("2787")
print(a.check("7782"))

import random


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

    def get_answer(self):
        return self.code
    def check(self, guess):
        code = self.code
        score = []
        potential = []
        for i in range(0, len(guess)):
            if code == "":
                break
            if self.code[i] == guess[i]:
                char = self.code[i]
                code = code.replace(char, "")
                print(f"code: {code}, b, {guess[i]}")
                score += "B"

                if char in potential:
                    if char not in code:
                        potential.remove(char)
                        score.remove("C")
            elif guess[i] in code and potential.count(guess[i]) < code.count(guess[i]):
                potential += guess[i]
                score += "C"
        return shuffle(score)


a = BullsCode("2787")
print(a.check("7782"))

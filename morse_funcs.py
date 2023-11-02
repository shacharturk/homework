def morse_translation(txt):
    morse = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0", "/": " "}
    freq = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    f = open(txt, "r")
    result = ""
    for x in f.read().split():
        try:
            result += morse[x]
            if morse[x] in freq.keys():
                freq[morse[x]] += 1
        except:
            raise Exception("Error in Morse code")
    f.close()
    max = 0
    for m in range(97, 123):
        if freq[chr(m)] > max:
            max = freq[chr(m)]
    while max > 0:
        frequancy = ""
        for x in range(97, 123):
            if freq[chr(x)] == max:
                frequancy += chr(x)
        if frequancy != "":
            print(str(frequancy) + "-" + str(max))
        max -= 1
    return result

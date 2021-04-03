# Jameel H. Khan
# Module 8 Assignment - LFSR

class LFSR:
    # create an LFSR with initial state 'seed' and tap 'tap'
    def __init__(self, seed: str, tap: int):
        self.seed = seed
        self.tap = tap

    # return the number of bits in the LFSR
    def length(long):
        numOfBits = len(long.seed)
        return numOfBits

    # return the bit at index 'i'
    def bit(mit, i: int):
        return mit.seed[i]

    # execute one LFSR iteration and return new (rightmost) bit as an int
    def step(go):
        lastBit = bin(int(go.seed[0]) ^ int(go.seed[-(go.tap)]))
        newBit = lastBit[-1]
        go.seed = go.seed[1:len(go.seed)] + newBit

        return newBit

    def __str__(self):
        print(self.seed)


def main():
    reg1 = LFSR("0110100111", 2)
    reg2 = LFSR("0100110010", 8)
    reg3 = LFSR("1001011101", 5)
    reg4 = LFSR("0001001100", 1)
    reg5 = LFSR("1010011101", 7)

    regList = [reg1, reg2, reg3, reg4, reg5]

    for i in range(len(regList)):
        n = regList[i].step()
        print(regList[i].seed + " " + n)

if __name__ == "__main__":
    main()

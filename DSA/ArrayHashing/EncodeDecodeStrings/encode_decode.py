

class EncodeDecode:

    def __init__(self, strs: list[str]) -> None:
        self.strs = strs
        self.encoded = ''
        self.decoded = []

    def encode(self):
        for s in self.strs:
            self.encoded += str(len(s)) + "#" + s

    def decode(self):
        i = 0

        while i < len(self.encoded):
            j = i
            while self.encoded[j] != '#':
                j += 1

            length = int(self.encoded[i:j])

            self.decoded.append(self.encoded[j + 1: j + 1 + length])

            i = j + 1 + length

    def show_encoded(self):
        print(self.encoded)

    def show_decoded(self):
        print(self.decoded)


if __name__ == '__main__':
    strs = ['lint', 'code', 'love', 'you']

    test = EncodeDecode(strs)
    test.encode()
    test.show_encoded()
    test.decode()
    test.show_decoded()

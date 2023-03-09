class Codec:
    def encode(self, strs: List[str]) -> str:
        encoder = ["".join([str(len(s)), "#", s]) for s in strs]
        return "".join(encoder)

    def decode(self, s: str) -> List[str]:
        decoder = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            w_len = int(s[i:j])
            j += 1
            decoder.append(s[j:j + w_len])
            i = j + w_len
        return decoder


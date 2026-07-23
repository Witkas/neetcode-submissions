class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
        return enc

    def decode(self, s: str) -> List[str]:
        # dec, i = [], 0
        # l, l_found = "", False
        # while i < len(s):
        #     if not l_found:
        #         if s[i] != "#":
        #             l += s[i]
        #         else:
        #             l_found = True
        #         i += 1
        #     else:
        #         dec.append(s[i:i+int(l)])
        #         i = i+int(l)
        #         l = ""
        #         l_found = False
        # return dec

        dec, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            dec.append(s[j+1:j+1+l])
            i = j+1+l
        return dec

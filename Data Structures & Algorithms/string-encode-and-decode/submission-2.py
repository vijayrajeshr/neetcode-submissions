class Solution:
    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc += f"{len(i)}#{i}"
        return enc

    def decode(self, s: str) -> List[str]:
        i = 0
        decodstr = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length

            res = s[start:end]
            decodstr.append(res)
            i=end
        return decodstr

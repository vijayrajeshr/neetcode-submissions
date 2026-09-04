class Solution:
    def encode(self, strs: List[str]) -> str:
        enc=""
        for word in strs:
            enc+=f"{len(word)}#{word}"
        return enc
        

    def decode(self, s: str) -> List[str]:
        decoded = []
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            word_length = int(s[i:j])

            start = j+1
            end = start+word_length
            decoded.append(s[start:end])
            i=end

        return decoded
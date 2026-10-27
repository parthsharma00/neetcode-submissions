class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + i + "`"
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        temp = ''
        for i in s:
            if i != "`":
                temp = temp + i
            else:
                result.append(temp)
                temp = ""
        return result
                

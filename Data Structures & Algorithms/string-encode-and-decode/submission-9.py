class Solution:

    def encode(self, strs: List[str]) -> str:
        rstr = ""
        for s in strs:
            length = len(s)%10

            temp = f"{s}{length}_##_"
            rstr += temp
        print(rstr)
        return rstr
    
    def decode(self, s: str) -> List[str]:
        output = []
        for i in s.split("_##_"):
            if i:
                output.append(i[:-1])
        return output


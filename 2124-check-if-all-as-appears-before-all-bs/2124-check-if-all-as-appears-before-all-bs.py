class Solution:
    def checkString(self, s: str) -> bool:
        # found = False
        # for ch in s:
        #     if ch == 'b':
        #         found = True
        #     elif ch =='a' and found:
        #         found = False
        # return True
        return "ba" not in s
            

            
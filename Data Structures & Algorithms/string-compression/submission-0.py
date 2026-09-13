class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""

        slow = 0
        fast = 0
        count = 0
        while fast < len(chars):
            c1 = chars[slow]
            c2 = chars[fast]

            if c1 == c2:
                count += 1
                fast += 1
                continue
            elif count == 1: 
                s = s + c1
                slow = fast
                count = 0
            else: 
                s = s + c1 + str(count)
                slow = fast
                count = 0
        
        if count == 1:
            s = s + chars[len(chars) - 1]
        else: 
            s = s + chars[len(chars) - 1] + str(count)
            print(s)
        
        chars[:len(s)] = list(s)
        return len(s)
        


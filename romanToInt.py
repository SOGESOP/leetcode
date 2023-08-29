class Solution(object):
    def __init__(self):
        self.romanToInt("MCMXCIV")

    def romanToInt(self, s):
        
        self.dict={"I":1, "V":5, "X":10,"L":50,
            "C":100,"D":500, "M":1000}
        
        self.listFormat=[]
        for i in s:
            self.listFormat.append(i)
        
        self.listCount=-1
        for x in self.listFormat:
            self.listCount+=1
            if x in self.dict:
                self.listFormat.remove(x)
                self.listFormat.insert(self.listCount, self.dict[x])

        self.total=0
        if sorted(self.listFormat, reverse=True)==self.listFormat:
            for x in self.listFormat:
                self.total+=x
        else:
            self.subtract=0
            self.highest=self.listFormat[0]
            for x in self.listFormat:
                if x>self.highest:
                    self.subtract+=self.highest*2
                self.highest=x

            for x in self.listFormat:
                self.total+=x
            self.total-=self.subtract

        return self.total

program=Solution()

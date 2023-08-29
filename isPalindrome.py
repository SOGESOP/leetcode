class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.listForm=[]
        x=str(x)
        for i in x:
            self.listForm.append(i)
        self.reverseForm=self.listForm[::-1]
        if self.reverseForm==self.listForm:
            return True
        else:
            return False

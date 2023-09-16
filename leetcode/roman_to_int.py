

 i have mis understood how roman intagers work

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={"I":1, "V": 5, "X":10, "L":50, 'C': 100, 'D': 500,'M': 1000}

        int_list=[]
        # converts the list to int form to allow for easier checking
        for char in s:
            int_list.append(roman_dict[char])
        largest=0
        for idx, x in enumerate(int_list):
            if x>largest:
                largest=x
                index=idx
        positive=0
        negative=0
        # if value in list less than largest and comes before largests then it is taking away from largests, and if it is after largest then it is adding on
        for i in range(len(int_list)):

            if int_list[i]<largest:
                if i<index:
                    negative+=int_list[i]
                elif i>index:
                    positive+=int_list[i]
            elif int_list[i]==largest:
                positive+=int_list[i]
        return positive-negative
        
 
    

test_case="IIXL"
instance=Solution()
print(instance.romanToInt(test_case))
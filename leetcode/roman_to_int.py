
wrong!!!

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={"I":1, "V": 5, "X":10, "L":50}
        total=0 
        int_list=[]
        # convers the list to int form to allow for easier checking
        for char in s:
            int_list.append(roman_dict[char])
        # runs through the list and checks for if it is a negative or a posotive
        for i in range(len(int_list)-1):
            j=i+1
            if int_list[j]>=int_list[i]:
                total-=int_list[i]                
            else:
                total+=int_list[i]
        return total




test_case="IIX"
instance=Solution()
print(instance.romanToInt(test_case))
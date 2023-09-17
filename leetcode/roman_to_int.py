


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
        current=0
        # if value in list less than largest and comes before largests then it is taking away from largests, and if it is after largest then it is adding on
        for i in range(len(int_list)-1):
            j=i+1
            # holds multiple consecutive numbers in a value
            if int_list[i]==int_list[j]:
                current+=int_list[i]
            elif int_list[i]<int_list[j]:
                current+=int_list[i]
                negative+=current
                current=0
            elif int_list[i]>int_list[j]:
                current+=int_list[i]
                positive+=current
                current=0

        positive+=int_list[-1]+current
        return positive-negative



    

test_case="III"
instance=Solution()
print(instance.romanToInt(test_case))
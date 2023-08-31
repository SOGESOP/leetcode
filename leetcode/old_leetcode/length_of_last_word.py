import logging
logging.basicConfig(level=logging.DEBUG)


class Solution:
    def __init__(self) -> None:
        self.lengthOfLastWord("luffy is still joyboy")
 
    def lengthOfLastWord(self, str: str,)-> int:
        alphabet="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
        current_word=""
        word_list=[]
        for i in str:
            if i in alphabet:
                current_word+=i
            else:
                if len(current_word)>0:
                    word_list.append(current_word)
                    current_word=""
        if current_word!="":
            word_list.append(current_word)    
        
        logging.debug(word_list)
        
        length=len(word_list[-1])
        logging.debug(length)

        return length



















# ("   fly me   to   the moon  "













    # def lengthOfLastWord(self, str: str)-> int:
    #     word_list=[]
    #     current_word=""
    #     for i in str:
    #         if i!=" ":
    #             current_word+=i
    #         else:
    #             word_list.append(current_word)
    #             current_word=""
    #     word_list.append(current_word)

        

    #     length=len(word_list[-1])
    #     return length


instance=Solution()
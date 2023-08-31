class Solution():
    def __init__(self) -> None:
        self.longestCommonPrefix([])

    def longestCommonPrefix(self, strs: list[str])->str:
        self.first_word=strs[0]
        self.first_word_list_form=[]
        self.index_count=-1
        self.current_list_form=[]
        self.common_prefix=[""]
        self.common_prefix_string=""
        self.prefix_list=[]
        self.break_string=""
        if len(strs)==1:
            self.common_prefix_string=strs[0]
            return self.common_prefix_string
        else:
            for i in self.first_word:
                self.first_word_list_form.append(i)
            for x in strs:
                self.current_list_form.clear()
                self.index_count=-1
                for i in x:
                    self.index_count+=1
                    self.current_list_form.append(i)
                    if self.index_count<len(self.first_word_list_form):
                        if self.first_word_list_form[self.index_count]==self.current_list_form[self.index_count]:
                            self.common_prefix.append(i)
                            self.common_prefix_string+=i
                        elif len(self.common_prefix)<1:
                            self.common_prefix_string=""
                        else:
                            if self.index_count<1:
                                self.common_prefix_string=""
                            break
                self.prefix_list.append(self.common_prefix_string)
                self.common_prefix_string=""
            
            self.prefix_list.pop(0)
            self.shortest_common_prefix=201
            self.prefix_list=list(set(self.prefix_list))
            if "" in self.prefix_list:
                self.common_prefix_string=""
            else:
                for i in self.prefix_list:
                    if len(i)<self.shortest_common_prefix:
                        self.shortest_common_prefix=len(i)
                for i in self.prefix_list:
                    if len(i)>self.shortest_common_prefix:
                        self.prefix_list.remove(i)
                if len(self.prefix_list)>0:
                    self.common_prefix_string=self.prefix_list[0]
                else:
                    self.common_prefix_string=""

            return self.common_prefix_string


instance=Solution()

# i just need to ensure that if the letter appears at
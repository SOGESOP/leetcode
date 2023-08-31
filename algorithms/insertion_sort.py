class insertion_algorithm_ascending:
    def __init__(self,initial_array) -> None:
        self.first_pass(initial_array)
    
    
    def first_pass(self, array):
        sorted_array=[]
        for idx, x in enumerate(array):
            if x>array[-1]:
                sorted_array.append(x)
            else:
                sorted_array.insert(idx,x)
        
    
    def new_addition(self, current_change):
        
        
        
        pass
    
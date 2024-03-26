import logging
logging.basicConfig(level=logging.DEBUG)

def isValid(s: str):

    pair_sets={")":"(", "]":"[", "}":"{"}
    print(pair_sets.values())
    temporary=[]
    
    
    for i in s:
        if i in list(pair_sets.values()):
            temporary.append(i)
        elif i in list(pair_sets.keys()):
            if temporary[-1]==pair_sets[i]:
                temporary=temporary.pop(-1)
        
        
                
        else:
            logging.debug("Error 1: Condition not considered") 
    
    
    
        
        
        
    pass

    
    # opening=["(", "[", "{"]
    # closing=[")", "]", "}"] 

isValid("([])")
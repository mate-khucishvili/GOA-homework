#1

def lowercase_count(strng):
    count = 0  
    for char in strng:  
        if char.islower():  
            count += 1 
    return count 

#2

def capitals(word):
    indices = []  
    for i in range(len(word)): 
        if word[i].isupper():
            indices.append(i)  
    return indices  

#3

def array(string):
    parts = string.split(',')
    
    if len(parts) <= 2:
        return None
    

    return ' '.join(parts[1:-1])

#4


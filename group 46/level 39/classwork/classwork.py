# 1 

# Generate range of integers


def generate_range(start, stop, step):
    result = []
    
    current = start
    
    if step > 0:
        while current <= stop:
            result.append(current)
            current += step  

            
    elif step < 0:
        while current >= stop:
            result.append(current)  
            current += step
    
    
    return result

# 2



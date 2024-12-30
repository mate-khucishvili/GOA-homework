#task- 1
def get_volume_of_cuboid(length, width, height):

        return length * width * height

#task- 2

def find_average(nums):

    if not nums:
        return 0 
    return sum(nums) / len(nums)


#task- 3

def no_boring_zeros(n):
    if n == 0:
        return 0  
    while n % 10 == 0:
        n //= 10  
    return n

#task- 4

def remove_zeros(num):

    if num == 0:
        return 0  
    while num % 10 == 0:
        num //= 10  
    return num

#task- 5

def no_boring_zeros(n):
    if n == 0:
        return 0
    while n % 10 == 0:
        n //= 10
    return n

#task- 6
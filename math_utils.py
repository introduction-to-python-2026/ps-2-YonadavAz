def find_max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
         my_max_number = num1  # Replace 'pass' with code
    if num2 >= num1 and num2 >= num3:
        my_max_number = num2
    if num3 >= num1 and num3 >= num2:
        my_max_number = num3
    return my_max_number  # Replace 'pass' with code

def find_mean(num1, num2, num3):
    return (num1 + num2 + num3)/3  # Replace 'pass' with code

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    snum1 = (num1-mean)**2
    snum2 = (num2-mean)**2
    snum3 = (num3-mean)**2
    std = find_ mean(snum1 ,snum2 ,snum3)
    std = std**0.5
    return std  # Replace 'pass' with code


def sum_even_odd(numbers):
    even_sum = sum( num for num in numbers if num % 2 == 0)
    odd_sum = sum( num for num in numbers if num % 2 != 0)
    return(even_sum,odd_sum)
def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average}")
#Alternatively, you could raise an exception
def calculate_average_exception(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    total = sum(numbers)
    average = total / len(numbers)
    return average
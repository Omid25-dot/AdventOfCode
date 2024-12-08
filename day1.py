numbers = []
numbers2 = []

with open('new.txt', 'r') as file:
    for line in file:
        left_numbers,right_numbers = map(int,line.split())
        numbers.append(left_numbers)
        numbers2.append(right_numbers)






left_sorted = sorted(numbers)
right_sorted = sorted(numbers2)

total_difference = 0
for index in zip(left_sorted,right_sorted):
    num1 = max(index)
    num2 = min(index)

    difference = abs(num1 - num2)
    total_difference += difference
print(total_difference)
similarity_score = 0
for num in left_sorted:
    count_in_right = right_sorted.count(num) # Count occurrences in the right list
    l = count_in_right * num
    similarity_score += l
print(similarity_score)
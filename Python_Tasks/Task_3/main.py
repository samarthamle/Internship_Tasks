from solutions import (
word_frequency,
character_frequency,
first_non_repeating_character,
are_anagrams,
first_repeating_character,
move_zeros_to_end,
second_highest_distinct,
remove_duplicates,
find_missing_number,
two_sum_first_pair,
closest_to_zero,
common_elements,
rotate_right,
maximum_consecutive_pair_sum,
all_pairs_with_target_sum
)

# Q1

print("Q1:", word_frequency("python is easy and python is powerful"))
print("Q1 Test:", word_frequency("data data science"))

# Q2

print("Q2:", character_frequency("banana"))
print("Q2 Test:", character_frequency("hello"))

# Q3

print("Q3:", first_non_repeating_character("swiss"))
print("Q3 Test:", first_non_repeating_character("aabb"))

# Q4

print("Q4:", are_anagrams("listen", "silent"))
print("Q4 Test:", are_anagrams("hello", "world"))

# Q5

print("Q5:", first_repeating_character("programming"))
print("Q5 Test:", first_repeating_character("abcdef"))

# Q6

print("Q6:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Test:", move_zeros_to_end([1, 0, 2]))

# Q7

print("Q7:", second_highest_distinct([10, 20, 40, 30, 40, 20]))
print("Q7 Test:", second_highest_distinct([5, 5]))

# Q8

print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Test:", remove_duplicates([1, 1, 2, 3, 2]))

# Q9

print("Q9:", find_missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Test:", find_missing_number([1, 3, 4], 4))

# Q10

print("Q10:", two_sum_first_pair([2, 7, 11, 15], 9))
print("Q10 Test:", two_sum_first_pair([1, 4, 6, 8], 10))

# Q11

print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Test:", closest_to_zero([-4, 4, -1]))

# Q12

print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 Test:", common_elements([2, 2, 3, 4], [4, 2]))

# Q13

print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Test:", rotate_right([1, 2, 3], 4))

# Q14

print("Q14:", maximum_consecutive_pair_sum([4, 7, 2, 9, 5]))
print("Q14 Test:", maximum_consecutive_pair_sum([-5, -2, -7]))

# Q15

print("Q15:", all_pairs_with_target_sum([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Test:", all_pairs_with_target_sum([1, 2, 3, 4, 5], 6))

# The form of the list comprehension:
# new_list = [new_item for item in numbers]

# The form of the conditional list comprehension:
# new_list = [new_item for item in list if test]

# New list with increased numbers:
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# New list with letters of a name:
# name = "Angela"
# new_name = [letter for letter in name]

# New list with the range function:
# new_range = [n * 2 for n in range(1,5)]

# New list with functions and conditionals:
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# upper_names = [name.upper() for name in names if len(name) > 5]

# Dictionary Comprehension:
# new_dict ={new_key:new_value for item in list}
# new_dict ={new_key:new_value for (key, value) in dict.items() if test}

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# student_scores = {student:random.randint(1, 100) for student in names}
# passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
#
# # Write your code below:
# result = {word:len(word) for word in sentence.split()}
#
#
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
#
#
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)
#
import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# #Loop through a data frame:
# for (key, value) in student_data_frame.items():
#     print(value)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
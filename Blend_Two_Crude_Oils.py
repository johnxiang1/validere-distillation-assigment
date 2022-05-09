from utils import distillation_model, all_dict_values, crudes_dictionary, get_numeric_input

print(f"The full list of Crude Oils {all_dict_values(crudes_dictionary())}")
oil1 = input("Enter 1st Crude Oil Acronym: ")
oil2 = input("Enter 2nd Crude Oil Acronym: ")

while oil1.upper() not in all_dict_values(crudes_dictionary()):
    print("Please enter a valid Crude Oil Acronym ")
    oil1 = input("Enter 1st Crude Oil Acronym: ")
while oil2.upper() not in all_dict_values(crudes_dictionary()):
    print("Please enter a valid Crude Oil Acronym ")
    oil2 = input("Enter 2nd Crude Oil Acronym: ")

v1, v2 = get_numeric_input(oil1, oil2)

print(f"The Distillation Profile of a Blend of {oil1.upper()} with Volume {v1} "
      f"and {oil2.upper()} with Volume {v2}:")
print(distillation_model(v1, v2, oil1, oil2, dictionary=True))
from utils import distillation_model, all_dict_values, crudes_dictionary

print(f"The full list of Crude Oils {all_dict_values(crudes_dictionary())}")
oil1 = input("Enter 1st Crude Oil Acronym: ")
oil2 = input("Enter 2nd Crude Oil Acronym: ")

while oil1.upper() not in all_dict_values(crudes_dictionary()):
    print("Please enter a valid Crude Oil Acronym ")
    oil1 = input("Enter 1st Crude Oil Acronym: ")
while oil2.upper() not in all_dict_values(crudes_dictionary()):
    print("Please enter a valid Crude Oil Acronym ")
    oil2 = input("Enter 2nd Crude Oil Acronym: ")

def get_numeric_input(oil1):
    while True:
      try:
         vol = float(input(f"Enter volume of {oil1.upper()}: "))
      except ValueError:
         print("Not a valid number!")
         continue
      else:
         break
    return vol
v1 = get_numeric_input(oil1)
v2 = get_numeric_input(oil2)

print(f"The Distillation Profile of a Blend of {oil1.upper()} with Volume {v1} "
      f"and {oil2.upper()} with Volume {v2}:")
print(distillation_model(v1=10, v2=12, oil1="BCL", oil2="OSH", dictionary=True))
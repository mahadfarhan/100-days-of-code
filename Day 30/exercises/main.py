# FileNotFound
# try:
#     file = open("./excercises/a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("./excercises/a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"They key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("This is an error that I made up.")

# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 metres")

# bmi = weight / height**2
# print(bmi)

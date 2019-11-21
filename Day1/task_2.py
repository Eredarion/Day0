import os

""" Just text """
text_one = "ее скотчем к пульту от телевизора и звонить на него, когда тот теряется!"
text_two = "Только мой папа догадался купить новую мобилу, примотать"

""" Write file one """
with open("2_file_1.txt", "w") as file_one:
      file_one.write(text_one)

""" Write file two """
with open("2_file_2.txt", "w") as file_two:
      file_two.write(text_two)

""" Get string from file one and append the line to file two"""
with open("2_file_1.txt", "r") as file_one:
      s = file_one.read()
      with open("2_file_2.txt", "a") as file_two:
            file_two.write(s)

""" Delete file one """ 
os.remove("2_file_1.txt")
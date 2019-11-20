import os

# -- Just text --
text_one = "ее скотчем к пульту от телевизора и звонить на него, когда тот теряется!"
text_two = "Только мой папа догадался купить новую мобилу, примотать"

# -- Write file one --
file_one = open("2_file_1.txt", "w")
file_one.write(text_one)
file_one.close()

# -- Write file two --
file_two = open("2_file_2.txt", "w")
file_two.write(text_two)
file_two.close()

# -- Get string from file one --
file_one = open("2_file_1.txt", "r")
s = file_one.read()
file_one.close()

# -- Append the line to file two --
file_two = open("2_file_2.txt", "a")
file_two.write(s)
file_two.close()

# -- Delete file one -- 
os.remove("2_file_1.txt")

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

from pathlib import Path

my_file_path = Path("./myfile.txt")

try:
    if my_file_path.exists():
        print(f"{my_file_path} exists! Opening the file as r mode.")
        file_obj = open("myfile.txt", "r")
        for line in file_obj.readlines():
            print(line)
    else:
        print(f"{my_file_path} doesn't exist! Opening the file as a mode.")
        file_obj = open("myfile.txt", "a")
        file_obj.write("Yea Buddy!\n")
        file_obj.write("Yea Buddy!\n")
except Exception as err:
    print(err)

print("end of the program")
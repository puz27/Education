import os
import datetime


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, 'x') as file:
        file.write(comments)
        filesize = os.path.getsize(b'')
    return(filesize)


def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open(filename, 'x') as file:
    file.write(filename)

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))


def file_date(filename):
    # Create the file in the current directory

    timestamp = open(filename, 'x')
    timestamp.close()
    # Convert the timestamp into a readable format, then into a string
    tim = os.path.getatime(filename)
    m = datetime.datetime.fromtimestamp(tim).strftime("%Y-%m-%d")
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(m))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join(os.getcwd(), os.pardir)

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)

print(parent_directory())

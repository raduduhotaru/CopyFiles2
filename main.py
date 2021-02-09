import os
import sys
import shutil
import getpass
import datetime


counter = 0


def get_username():
    return getpass.getuser()


# Write in LOGfile. Create if it doesn't exists, append if it already exists
def write_in_logFile(path, text):
    f = open(path + "LOG_File.log", "a+")
    f.write(text)
    f.close()


# Parse in the input directory and check for pattern in the files name
def parse_and_copy(inputPath, outputPath, pattern):
    global counter
    for basePath, directory, files in os.walk(inputPath):
        for file in files:
            if pattern in file:
                counter += 1
                shutil.copy2(os.path.join(basePath, file), os.path.join(outputPath, file))
                write_in_logFile(outputPath,
                                 f"{datetime.datetime.now().time()} : {os.path.join(basePath, file)} "
                                 f"-- moved to --> {os.path.join(outputPath, file)}\n")


# Main function - handle for all the other functions
def main():
    global counter

    if len(sys.argv) != 4:
        print("Incorrect number of arguments!  Please give as arguments: \n "
              "1. Input folder path \n "
              "2. Output folder path \n "
              "3. Wanted pattern\n")
        sys.exit()

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    pattern = sys.argv[3]

    if not os.path.isdir(inputPath):
        print("\n Invalid input path! Make sure it is a directory! \n")
        sys.exit()
    if not os.path.isdir(outputPath):
        print("\n Invalid output path! Make sure it is a directory! \n")
        sys.exit()

    write_in_logFile(outputPath, f"Hello, {get_username()}!\n\n Started to search for \"{pattern}\" in {inputPath}\n")
    parse_and_copy(inputPath, outputPath, pattern)

    if counter > 0:
        write_in_logFile(outputPath, f"\n-->  {counter} files moved  <--\n")
    else:
        write_in_logFile(outputPath, f"\n-->  There are no files containing \"{pattern}\"  <--\n")

    write_in_logFile(outputPath, "\nProgram successfully ended!\n")
    print("\nProgram successfully ended! Check the LOG file (in the output path) for more information!")


main()

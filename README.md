# Handling Files in C

## Introduction
This project demonstrates basic file handling operations in C, including reading from and writing to files. The purpose of this task is to familiarize students with file input/output (I/O) functions in C, such as `fopen`, `fgets`, `fputs`, and `fclose`.

## Project Structure
The project consists of the following files:

1. **fileRead.c** - A C program for reading content from a file.
2. **fileWrite.c** - A C program for writing content to a file.
3. **main.c** - The main program that integrates file reading and writing functionality.
4. **test.txt** - A test file with some predefined content for the reading operation.
5. **test1.txt** - A secondary test file.
6. **test2.txt** - Another test file for practice and validation.

### Contents of Test Files
- **test.txt**: Contains repeated text and some fun messages like `lol kek cheburek`&#8203;:contentReference[oaicite:0]{index=0}.
- **test1.txt**: Contains a basic test text&#8203;:contentReference[oaicite:1]{index=1}.
- **test2.txt**: Similar to `test.txt` but with fewer lines&#8203;:contentReference[oaicite:2]{index=2}.

## Task Requirements

Your task is to:

### Task 1: Modify the Provided Code
1. **Analyze the provided code in `fileRead.c`, `fileWrite.c`, and `main.c`**:
   - Understand how file reading and writing operations work.
   - Ensure that you can compile and run these programs successfully.

2. **Add comments to explain each function and step**:
   - What does each line of code do? Why are certain functions used?
   - Make sure to explain the purpose of the file pointers and the steps for file I/O.

### Task 2: Write Your Own File Reader
1. **Write a new program (`myFileRead.c`) that does the following**:
   - Asks the user to input the filename.
   - Reads the entire content of the file.
   - Counts the number of words in the file and prints the word count along with the file content.

2. **Handle edge cases**:
   - What happens if the file doesn't exist?
   - What if the file is empty?
   
3. **Enhancements** (Optional):
   - Add functionality to count characters and lines in the file as well.

### Task 3: Write Your Own File Writer
1. **Write a new program (`myFileWrite.c`) that does the following**:
   - Asks the user to input text.
   - Writes this text to a new file (use a filename provided by the user).
   - If the file already exists, ask the user whether they want to overwrite it or append to it.

2. **Handle edge cases**:
   - Ensure the program handles user input correctly.
   - Check for any file creation or write errors.

### Task 4: Merge File Operations
1. **Write a new program (`myFileOperations.c`) that combines reading and writing**:
   - Read the content of a file and print it to the console.
   - Append additional text to the same file, and then read and print the updated content.
   - Make sure the user can choose whether to append or overwrite the file.

2. **Bonus Challenge**:
   - Implement a menu system that lets the user choose between:
     - Reading a file.
     - Writing to a file.
     - Appending to a file.
     - Counting words, lines, and characters in a file.

### Task 5: Advanced Challenge - Binary File Handling (Optional)
1. **Create a new program (`myBinaryFile.c`) that handles binary files**:
   - Write a program that writes an array of integers to a binary file.
   - Read the binary file and print the integers to the console.

2. **Handle edge cases**:
   - Check for file errors, such as failure to open the file.
   - Ensure the correct reading and writing of binary data.

### Task 6: Documentation
1. **Write documentation (`myREADME.md`) for your programs**:
   - For each program you write, add a short explanation of how it works, what it does, and any special features or edge cases it handles.
   - Use clear comments within your code to explain how each function works.



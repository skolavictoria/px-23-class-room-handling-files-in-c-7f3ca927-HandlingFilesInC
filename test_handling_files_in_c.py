import subprocess
import os
import pytest
import re

# Constants for file paths and test contents
TEST_FILES_CONTENT = {
    "test.txt": "lol kek cheburek\nlol kek cheburek\n",
    "test1.txt": "basic test text\n",
    "test2.txt": "lol kek cheburek\n",
}

# Helper function to create test files
def setup_test_files():
    for filename, content in TEST_FILES_CONTENT.items():
        with open(filename, "w") as file:
            file.write(content)

# Helper function to compile a specific C file
def compile_c_file(c_file, output_file):
    result = subprocess.run(["gcc", c_file, "-o", output_file], capture_output=True, text=True)
    assert result.returncode == 0, f"Failed to compile {c_file}: {result.stderr}"

# Run setup files before all tests
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    setup_test_files()
    yield
    # Clean up test files and compiled files after all tests
    for filename in TEST_FILES_CONTENT.keys():
        os.remove(filename)
    for output_file in ["fileRead", "fileWrite", "main", "myFileRead", "myFileWrite", "myFileOperations", "myBinaryFile"]:
        if os.path.exists(output_file):
            os.remove(output_file)

# Cleanup after each test
@pytest.fixture(autouse=True)
def cleanup_files():
    yield
    for temp_file in ["test_output.txt", "overwrite_test.txt", "binary_test.dat"]:
        if os.path.exists(temp_file):
            os.remove(temp_file)

# Bonus Challenge: Test for menu system in myFileOperations.c
def test_menu_system():
    compile_c_file("myFileOperations.c", "myFileOperations")
    
    # Define expected menu options and valid inputs
    menu_options = ["read", "write", "append", "count", "R", "W", "O", "A", "C"]
    valid_inputs = ["1", "2", "3", "4", "R", "W", "O", "A", "C"] + [option[0] for option in ["read", "write", "append", "count"]]
    
    # Run the program and capture output
    result = subprocess.run(["stdbuf", "-oL", "./myFileOperations"], input="test.txt\n", capture_output=True, text=True)
    
    # Check if any expected menu options are present in the output (flexible format check)
    menu_detected = any(re.search(option, result.stdout, re.IGNORECASE) for option in menu_options)
    assert menu_detected, "Menu system not detected in myFileOperations"

    # Check if the program accepts any valid input (numbers, full words, first letters, abbreviations in any case)
    results = []
    for input_value in valid_inputs:
        result = subprocess.run(
            ["stdbuf", "-oL", "./myFileOperations"],
            input=f"test.txt\n{input_value}\n",
            capture_output=True,
            text=True,
            timeout=5  # Set timeout in seconds
            )

        results.append(result)
    
    # Assert that at least one valid input was accepted by checking the return codes
    assert any(result.returncode == 0 for result in results), f"None of the inputs were accepted as valid: {valid_inputs}"

    # Skip further checks if menu system is implemented
    if menu_detected:
        pytest.skip("Bonus menu detected; lower-level tasks are not required.")


# Bonus Challenge: Test binary file handling in myBinaryFile.c
def test_binary_file_handling():
    compile_c_file("myBinaryFile.c", "myBinaryFile")
    integers = [1, 2, 3, 4, 5]
    
    # Run binary file program and capture output
    result = subprocess.run(["./myBinaryFile"], capture_output=True, text=True)
    
    # Check if each integer appears in the output
    binary_detected = all(re.search(fr"\b{num}\b", result.stdout) for num in integers)
    assert binary_detected, "Binary file handling not correctly implemented or output missing expected integers"

    # Skip lower-level tasks if binary functionality is correct
    pytest.skip("Binary file handling detected; lower-level tasks are not required.")

# Fallback Tests: Lower-Level Requirements (if bonus is not met)

# Test for fileRead.c
def test_file_read():
    compile_c_file("fileRead.c", "fileRead")


# Test for fileWrite.c
def test_file_write():
    compile_c_file("fileWrite.c", "fileWrite")


# Test for myFileRead.c (word counting and file existence check)
def test_my_file_read():
    compile_c_file("myFileRead.c", "myFileRead")
    # Calculate expected word count
    with open('test.txt') as f:
        txt = f.read()
        word_cnt = len(txt.split())
    result = subprocess.run(["./myFileRead"], input="test.txt\n", capture_output=True, text=True)
    
    # Check for word count presence and flexible content check
    assert re.search(rf"\b{word_cnt}\b", result.stdout), "Expected word count not found in output"
    assert all(word in result.stdout for word in txt.split()), "File content not fully displayed as expected"

    # Test non-existent file
    result = subprocess.run(["./myFileRead"], input="nonexistent.txt\n", capture_output=True, text=True)
    assert re.search("error|not found", result.stdout, re.IGNORECASE), \
        "No appropriate error message for non-existent file"

# Test for myFileWrite.c (overwrite or append)
def test_my_file_write():
    compile_c_file("myFileWrite.c", "myFileWrite")
    overwrite_text = "Overwrite content\n"
    append_text = "Appended content\n"
    
    # Overwrite test
    subprocess.run(["./myFileWrite"], input="overwrite_test.txt\n" + 'w\n' + overwrite_text, capture_output=True, text=True)
    with open("overwrite_test.txt", "r") as f:
        content = f.read()
    assert re.search(rf"\b{overwrite_text.strip()}\b", content), "Overwrite functionality failed"

    # Append test
    subprocess.run(["./myFileWrite"], input="overwrite_test.txt\n" + 'a\n' + append_text, capture_output=True, text=True)
    with open("overwrite_test.txt", "r") as f:
        content = f.read()
    assert re.search(rf"\b{append_text.strip()}\b", content), "Append functionality failed"

# Test for main.c
def test_main():
    compile_c_file("main.c", "main")

#if __name__ == '__main__':
#    setup_module()
#    test_my_file_read()

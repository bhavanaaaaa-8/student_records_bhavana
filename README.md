# Student Marks Management System

## Description
The Student Marks Management System is a Python program that stores student names and marks using a dictionary. It allows users to add student records, display all students, search for a student, sort students by marks, and find the highest score.

## Features
- **Add Student:** Enter a student's name and marks.
- **Display Students:** View all stored student records.
- **Search Student:** Search for a student by name.
- **Sort Students:** Display students in ascending order of marks.
- **Find Highest Score:** Identify the student or students with the highest marks.
- **Input Validation:** Ensures marks are between 0 and 100 and handles invalid menu choices.

## Technologies Used
- Python 3
- Dictionary data structure
- Functions
- Loops and conditional statements
- Built-in functions such as `max()`, `sorted()`, and `input()`

## How to Run
1. Install Python 3 on your computer.
2. Save the program in a file named `student_marks.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the command:

   ```bash
   python student_marks.py
   ```

## Data Structure
The program uses a dictionary where student names are keys and their marks are values.

Example:
```python
students = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78
}
```

## Future Improvements
- Support multiple students with the same name using unique student IDs.
- Save student records to a file.
- Add options to update and delete student records.
- Generate class averages and grade reports.

## Author
Student project developed using Python.

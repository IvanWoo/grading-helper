# Grading-Helper
An integrated solution for automatic marking and entering grades of MATLAB code assignment.

## Logic
Based on [MATLAB tesing frameworks](https://www.mathworks.com/help/matlab/matlab-unit-test-framework.html), a csv file of unit test result is generated in every students' submitting folder. Reading and entering the grade via [pandas](http://pandas.pydata.org/), an easy-to-use data structures and data analysis tools for the Python programming language.

## Usage
- **hw1** folder consists of assignments submitted by students.
- **unit_test** folder consists of the unit test code and relative running script.
- A csv_reader class is saved in the **library** folder.
- The grading results are read and entered in the **read_result** folder.
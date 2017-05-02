import sys
sys.path.insert(0, '../library')

from csv_reader import CsvReader

task = "hw1"
# replace with absolute address of assignments folder
base_dir = "../hw1"
grade_suffix = "q1"
scale = 10
new_task = CsvReader(task, base_dir)
new_task.read(grade_suffix, scale)
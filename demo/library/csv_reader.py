#!/usr/bin/python3

import os
import pandas as pd


class CsvReader:
    """
    task is a string for the file name of grade csv and relative unit test csv.
    base_dir is the full address of saved assignment files.
    """
    def __init__(self, task, base_dir):
        self.task = task
        self.base_dir = base_dir

    def _mark(self, test_result):
        return sum(test_result['Passed']) / len(test_result['Passed'])

    def read(self, grade_suffix, scale=1):
        # save the original dir for later returning to the start folder
        start_dir = os.getcwd()

        # open the grade csv which downloaded from LEARN platform.
        grade_table = pd.read_csv(open(self.task + '.csv', 'rb')).set_index('OrgDefinedId')

        # cd to the address where assignments stored
        os.chdir(self.base_dir)

        valid_folders = [name for name in os.listdir(self.base_dir) if
                         not (name.startswith('.') or name.startswith('index') or name.startswith('unzip'))]

        # Go through every students' submitted folder and relative results
        for i in range(len(valid_folders)):
            os.chdir(valid_folders[i])

            # Use student ID as data frame key
            key = '#' + valid_folders[i].split(' - ')[2]

            # Check the key is in the index list or not:
            # http://stackoverflow.com/questions/23549231/check-if-a-value-exists-in-pandas-dataframe-index
            if key not in grade_table.index:
                os.chdir(self.base_dir)
                continue
            try:
                test_result = pd.read_csv(open(self.task + '_results.csv', 'rb'))
            except:
                os.chdir(self.base_dir)
                continue

            # mark it
            grade_table.loc[key, grade_suffix] = self._mark(test_result) * scale

            # go back to base dir
            os.chdir(self.base_dir)

        # go back to original folder
        os.chdir(start_dir)

        # save the edited grade table
        grade_table.to_csv(self.task + '_marked.csv')


if __name__ == "__main__":
    task = ""
    base_dir = ""
    grade_suffix = ""
    new_task = CsvReader(task, base_dir)
    new_task.read(grade_suffix)

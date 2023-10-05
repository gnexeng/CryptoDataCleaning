# To extract the following NIST tests from files in
# C:\Users\gnexe\OneDrive\Documents\GitHub\coning-analysis\with-v2.0-fixes

# Tests: Frequency, BlockFrequency, CumulativeSums, Runs, LongestRun, Rank, FFT
# OverlappingTemplate, Universal, ApproximateEntropy, Serial, LinearComplexity

# First batch: f-vector (3,3) applying coning between 3750-3849 times
# file structure: 3,3-c3750-v2-0-0.txt  ---> 3,3-c3849-v2-0-0.txt


# Second batch: f-vector (4,5) -> (103-203) applying coning 3750 times
# file structure: 4,5-c3750-v2-0-0.txt  --->  103,203-c3750-v2-0-0.txt

import os
import re

path = f'C:\\Users\\gnexe\\OneDrive\\Documents\\GitHub\\coning-analysis\\with-v2.0-fixes\\'
tests = ['Frequency',
 'BlockFrequency',
 'CumulativeSums',
 'Runs',
 'LongestRun',
 'Rank',
 'FFT',
 'OverlappingTemplate',
 'Universal',
 'ApproximateEntropy',
 'Serial',
 'LinearComplexity']

#f_vectors = [(x, y) for x in range(4, 104) for y in range(5, 204, 2)]


# ONLY RUN ONE TIME
def create_files():
    for val in tests:
        extension = '.csv'
        file = open(f'{val + extension}', 'w')
        file.close()

def testing_file(val):
    in_file = open(path + f'3,3-c{val}-v2-0-0.txt', 'r')
    for line in in_file:
        try:
            # if line.index(' Frequency'):
            #     idx = line.find('0.')
            #     print(line[idx: idx + 8])
            if line.index(' 0.'):
                idx = line.find(' 0.')
                p_value = float(line[idx + 1:idx + 9])
                # extract the name of test for this p_value
                test_name = line.split(' ')[-1].strip()
                print(p_value, test_name)
                # open file test_name.csv
                # append pair VAL, p-value to filename test_name.csv
                # close file test_name.csv
                # if test_name in tests:
                #     print('true')
                #     out_file = open(test_name + '.csv', 'a')
                #     # append pair VAL, p-value to filename test_name.csv
                #     out_file.write(f'{p_value},{val}')
                #     # close file test_name.csv
                #     out_file.close()
        except ValueError:
            continue



def extract_first_batch():
    # for each value VAL between 3750 - 3849
    for val in range(3750, 3850):
        #Open filename 3,3-cVAL-v2-0-0.txt at path
        in_file = open(path + f'3,3-c{val}-v2-0-0.txt', 'r')

        #For each line:
        for line in in_file:
        #    split line at spaces
            try:
                if line.index(' 0.'):
                    idx = line.find(' 0.')
                    p_value = float(line[idx+1:idx+9])   # extract the p-value
                    test_name = line.split(' ')[-1].strip()  # extract the name of test for this p_value
                    # open file test_name.csv
                    if test_name in tests:
                        out_file = open(test_name + '.csv', 'a')
                        # append pair VAL, p-value to filename test_name.csv
                        out_file.write(f'{p_value},{val}\n')
                        # close file test_name.csv
                        out_file.close()
            except ValueError:
                continue
    # close all files
    in_file.close()

def extract_second_batch():
    # for each value VAL between 3750 - 3849
    for val in range(3750, 3850):
        #Open filename 3,3-cVAL-v2-0-0.txt at path
        in_file = open(path + f'3,3-c{val}-v2-0-0.txt', 'r')

        #For each line:
        for line in in_file:
        #    split line at spaces
            try:
                if line.index(' 0.'):
                    idx = line.find(' 0.')
                    p_value = float(line[idx+1:idx+9])   # extract the p-value
                    test_name = line.split(' ')[-1].strip()  # extract the name of test for this p_value
                    # open file test_name.csv
                    if test_name in tests:
                        out_file = open(test_name + '.csv', 'a')
                        # append pair VAL, p-value to filename test_name.csv
                        out_file.write(f'{p_value},{val}\n')
                        # close file test_name.csv
                        out_file.close()
            except ValueError:
                continue

def main():
    print(f_vectors)
    #create_files()
    #testing_file(3750)
    #extract_first_batch()
    pass


if __name__ == "__main__":
    main()


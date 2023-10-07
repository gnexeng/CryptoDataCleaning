# To extract the following NIST tests from files in https://github.com/gnexeng/CryptoDataCleaning.git

# Tests: Frequency, BlockFrequency, CumulativeSums, Runs, LongestRun, Rank, FFT
# OverlappingTemplate, Universal, ApproximateEntropy, Serial, LinearComplexity

# First batch: f-vector (3,3) applying coning between 3750-3849 times
# file structure: 3,3-c3750-v2-0-0.txt  ---> 3,3-c3849-v2-0-0.txt


# Second batch: f-vector (4,5) -> (103-203) applying coning 3750 times
# file structure: 4,5-c3750-v2-0-0.txt  --->  103,203-c3750-v2-0-0.txt


path = 'C:\\Users\\gnexe\\PycharmProjects\\CryptoDataCleaning\\coning-analysis\\with-v2.0-fixes\\'
# path = './coning-analysis/with-v2.0-fixes/'
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


def create_list_f_vectors(x: int, y: int, total: int):
    """
    Creates a list of f-vectors starting such that (x,y)->(x+1,y+2)->...
    :param x: starting value for f-vector dim 1
    :param y: starting value for f-vector dim 2
    :param total: total number of f-vectors to generate
    :return: list of f-vectors as tuples
    """
    from itertools import count
    x_counter = count(x)
    y_counter = count(y, 2)
    f_vectors = [(next(x_counter), next(y_counter)) for _ in range(total)]
    return f_vectors


def file_processing(file_name, val, vector, out_file_name_modifier='', out_path_modifier=''):
    # For each line:
    for line in file_name:
        #    split line at spaces
        try:
            if line.index(' 0.'):
                idx = line.find(' 0.')
                p_value = float(line[idx + 1:idx + 9])  # extract the p-value
                test_name = line.split(' ')[-1].strip()  # extract the name of test for this p_value
                # open file test_name.csv
                if test_name in tests:
                    # In windows must add \\ to path names
                    out_file = open(f'{test_name}-{out_file_name_modifier}.csv', 'a')
                    # append pair VAL, p-value to filename test_name.csv
                    out_file.write(f'{p_value},{val},{vector}\n')
                    # close file test_name.csv
                    out_file.close()
        except ValueError:
            continue


def extract_coning_test(local_dir_name='3-3-3750-3849'):
    global path
    # for each value VAL between 3750 - 3849
    for val in range(3750, 3850):
        # Open filename 3,3-cVAL-v2-0-0.txt at path
        in_file = open(path + f'3,3-c{val}-v2-0-0.txt', 'r')
        file_processing(in_file, val=val, vector=(3, 3), out_file_name_modifier='coning',
                        out_path_modifier=f'\\{local_dir_name}\\')
        in_file.close()


def extract_vectors_test(local_dir_name='4-5-103-203-3750'):
    global path
    # for each f-vector between (4,5) ---> (103,203)
    f_vectors = create_list_f_vectors(4, 5, 100)
    for x, y in f_vectors:
        # Open filename x,y-c3750-v2-0-0.txt at path
        in_file = open(path + f'{x},{y}-c3750-v2-0-0.txt', 'r')
        file_processing(in_file, val=3750, vector=(x, y), out_file_name_modifier='vectors',
                        out_path_modifier=f'\\{local_dir_name}\\')
        in_file.close()


def main():
    extract_coning_test()
    extract_vectors_test()
    pass


if __name__ == '__main__':
    main()

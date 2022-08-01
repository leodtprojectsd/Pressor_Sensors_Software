import config
import numpy as np

n=20

DATA_FILENAME= config.paths_["DATA_FILENAME"]
WEIGHT_FILENAME= config.paths_["WEIGHT_FILENAME"]
COMBINED_FILENAME = config.paths_["COMBINED_FILENAME"]

with open(DATA_FILENAME) as f1, open(WEIGHT_FILENAME) as f2:
    storage = np.zeros((2, 33))

    for line in (f1.readlines()[-n:]):  # read the las n lines
        arr = np.array(line.split(",")).reshape(1, 33)
        storage = np.append(storage, arr, axis=0).astype(float)
        print(storage[2:, :].mean(axis=0).reshape(1, 33))
  # for x, y in zip(f1, f2):
  #    print("{0}\t{1}".format(x.strip(), y.strip()))


filenames = [DATA_FILENAME, WEIGHT_FILENAME]

# Open file3 in write mode
with open('file3.txt', 'w') as outfile:
    # Iterate through list
    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")
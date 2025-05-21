import numpy as np

# creating a large file to store (250 MB)
a = np.random.rand(1000, 10000)

# storing as .csv
np.savetxt("large-file.csv", a, delimiter = ",")
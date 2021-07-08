import os
import numpy as np
from scipy.io import loadmat

def extract_mat(mat_file):
    
    mat_dict = loadmat(mat_file)
    # The first two indices are only contain a single dimension,
    #    remove these extraneous dimensions.
    data = mat_dict['data'][0][0]
    labels = list(mat_dict['data'].dtype.names)
    
    # Re-organize data into a dict
    arr_dict = {}
    for key, arr in zip(labels, data):
        if arr.size == 1:
            # Value is an int or float
            arr_dict[key] = arr.flatten()[0]
        else:
            # Value is an array
            arr_dict[key] = arr
    
    # Arrays need to be flatten as they contain an
    #   unnecessary dimension 
    arr_dict['spikes'] = arr_dict['spikes'].flatten()
    arr_dict['channel'] = arr_dict['channel'].flatten()
    
    return arr_dict

# Extract data
pwd = os.getcwd()
data_dir = os.path.join(pwd, 'Data')
mat_files = sorted(os.listdir(data_dir))

for mat_file in mat_files:
    arr_dict = extract_mat(os.path.join(data_dir, mat_file))
    np.save(mat_file[:-4] + '.npy', arr_dict) 
    
# Example loading to dict
test_load = np.load('file.npy', allow_pickle=True)
test_load = test_load.tolist()
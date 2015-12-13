from scipy.sparse import csr_matrix
import numpy as np

def read_rudy_data(path):
    cleaned = list()
    with open(path) as f:
        #print f.read()
        content = f.read().splitlines()
        #print content
        cleaned = [x.split(' ') for x in content if x != ""]
    return cleaned

def construct_matrices(clean_data):
    basic_info = clean_data.pop(0)
    d = int(basic_info[0])
    e = int(basic_info[1])
    print "len(state) = " + str(d)
    W = np.zeros((d, d))
    #print W
    S = np.random.randint(2, size=d)
    #print S
    for item in clean_data:
        start = int(item[0]) - 1
        end = int(item[1]) - 1
        weight = int(item[2])
        if start != end:
            W[start][end] = weight
            W[end][start] = weight
        else:
            W[start][end] = weight
    return [S, W, e]

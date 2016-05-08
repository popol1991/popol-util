from scipy.sparse import csc_matrix

def load_mapping(path, key_type=lambda x: x, val_type=lambda x: x, reverse=False):
    mapping = {}
    fin = open(path)
    for line in fin:
        fields = line.strip().split('\t')
        key, val = fields[:2]
        if reverse:
            key, val = val, key
        mapping[key_type(key)] = val_type(val)
    fin.close()
    return mapping

def load_mapping_counter(path, separator="\t", key_type=lambda x: x, val_type=lambda x: x, reverse=False):
    mapping = {}
    fin = open(path)
    for line in fin:
        fields = line.strip().split(separator)
        key, val = fields[:2]
        if reverse:
            key, val = val, key
        key = key_type(key)
        val = val_type(val)
        if key not in mapping:
            mapping[key] = {}
        if val not in mapping[key]:
            mapping[key][val] = 0
        mapping[key][val] += 1
    fin.close()
    return mapping

def load_key_list_map(path, key_type=lambda x: x, val_type=lambda x: x, reverse=False):
    mapping = {}
    fin = open(path)
    for line in fin:
        key, val = line.strip().split('\t')[:2]
        if reverse:
            key, val = val, key
        if key not in mapping:
            mapping[key] = []
        mapping[key_type(key)].append(val_type(val))
    fin.close()
    return mapping


def sparse_vector(line):
    fields = line.split(' ')
    data = []
    col_ind = []
    for field in fields:
        key, val = field.split(':')
        col_ind.append(int(key))
        data.append(float(val))
    vector = csc_matrix((data, ([0] * len(col_ind), col_ind)))
    return vector

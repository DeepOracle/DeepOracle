import numpy as np


def embeding(data, embed_size):
    result = []
    for X in data:
        tmp = np.array([np.concatenate([x, [0] * (embed_size - len(x))]) if len(x) < embed_size else x for x in X])
        result.append(tmp)
    return result


def normalization_array(data):
    max_num = -1e10
    min_num = 1e10
    for line in data:
        max_num = max(max_num, max(line))
        min_num = min(min_num, min(line))
    # print(max_num,min_num)
    out = []
    for line in data:
        temp = [(x - min_num) / (max_num - min_num) for x in line]
        out.append(temp)
    return out, max_num, min_num


def normalization_seq(data):
    max_num = -1e10
    min_num = 1e10
    for line in data:
        for word in line:
            max_num = max(max_num, max(word))
            min_num = min(min_num, min(word))
    words = []
    out = []
    for line in data:
        words = []
        for word in line:
            temp = [(x - min_num) / (max_num - min_num) for x in word]
            words.append(temp)
        out.append(words)
    return out


def padding_array(X, max_len, padding=0):
    return np.array([np.concatenate([x, [padding] * (max_len - len(x))]) if len(x) < max_len else x for x in X])


def padding_sequence(X, max_len, embed_size, padding=0):
    return np.array(
        [np.concatenate([x, [[padding] * embed_size] * (max_len - len(x))]) if len(x) < max_len else x for x in X])


def return_before(dataSet, max_num, min_num):
    out = []
    out = np.round(dataSet * (max_num - min_num) + min_num)
    '''for line in dataSet:
        temp = [round(x * (max_num - min_num)) + min_num for x in line]
        out.append(temp)'''
    return out


def load_array(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            data = [float(x) for x in words]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_array_split(filename, spliter):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.strip().split(spliter)
            data = [float(x) if len(x) > 0 else 0 for x in words]

            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_sequence(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline().strip()
        while line:
            data = [ord(x) for x in list(line)]
            dataSet.append(data)
            line = f.readline().strip()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)

    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_sequence_split(filename, spliter):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline().strip()
        lst = line.split(spliter)
        line = ' '.join(lst)
        while line:
            data = [ord(x) for x in list(line)]
            dataSet.append(data)
            line = f.readline().strip()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)

    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_label(filename):
    labelSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            arr = line.split()
            label = [int(x) for x in arr]
            labelSet.append(label)
            line = f.readline()
    labelSet = np.array(labelSet)
    labelSet = labelSet.reshape(labelSet.shape[0], 1)
    return labelSet


def normalization_dimention(dataSet):
    maxs = np.max(dataSet, axis=0)
    mins = np.min(dataSet, axis=0)
    out = []
    for line in dataSet:
        temp = []
        for j in range(len(line)):
            if maxs[j] == mins[j]:
                num = (line[j] - mins[j]) / 1
            else:
                num = (line[j] - mins[j]) / (maxs[j] - mins[j])
            temp.append(num)
        out.append(temp)
    return out, maxs, mins


def load_before_time14(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            data = []
            words = line.split('#')
            data.append(int(words[0]))
            nums = words[1].split('-')
            for x in nums:
                if x != '':
                    data.append(int(x))
            dataSet.append(data)
            line = f.readline()

    # normalization
    # dataSet = normalization_dimention(dataSet)
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    # dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_after_time14(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            data = []
            nums = line.split('-')
            for x in nums:
                if x != '':
                    data.append(int(x))
            dataSet.append(data)
            line = f.readline()

    # normalization
    # dataSet = normalization_dimention(dataSet)
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    # dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_data_time3(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split('#')
            data = [int(x) for x in words]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Maxs, Mins = normalization_dimention(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Maxs, Mins


def load_data_mockito6(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            if words[0] != 'null':
                data = [int(x) for x in words]
            else:
                for word in words:
                    data = [ord(x) for x in list(word)]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_data_math15(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            if words[0] != 'Infinity':
                data = [float(x) for x in words]
            else:
                data = [0]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_data_exp_time7(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            data = [float(word) for word in words]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_data_compress40(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split('#')
            lst = words[0].split()
            data = [int(x) for x in lst]
            data.append(int(words[1]))
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_classification(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            data = []
            if line == 'true\n':
                data.append(1)
            else:
                data.append(0)
            dataSet.append(data)
            line = f.readline()
    # normalization
    dataSet, Max, Min = normalization_array(dataSet)

    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_M1_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M1_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M2_before(filename):
    X, seq_len_X, max_x, min_x = load_array(filename)
    return X, seq_len_X, max_x, min_x


def load_M2_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M3_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M3_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M4_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M4_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M5_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M5_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M6_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M6_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M7_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M7_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M8_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M8_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M9_before(filename):
    X, seq_len_X, max_x, min_x = load_before_time14(filename)
    return X, seq_len_X, max_x, min_x


def load_M9_after(filename):
    Y, seq_len_Y, max_y, min_y = load_after_time14(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M10_before(filename):
    X, seq_len_X, max_x, min_x = load_before_time14(filename)
    return X, seq_len_X, max_x, min_x


def load_M10_after(filename):
    Y, seq_len_Y, max_y, min_y = load_after_time14(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M11_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M11_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M12_before(filename):
    X, seq_len_X, max_x, min_x = load_array(filename)
    return X, seq_len_X, max_x, min_x


def load_M12_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M13_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M13_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M14_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M14_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M15_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M15_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M16_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M16_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M17_before(filename):
    X, seq_len_X, max_x, min_x = load_data_mockito6(filename)
    return X, seq_len_X, max_x, min_x


def load_M17_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M18_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M18_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M19_before(filename):
    X, seq_len_X, max_x, min_x = load_data_math15(filename)
    return X, seq_len_X, max_x, min_x


def load_M19_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M20_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M20_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M21_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M21_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M22_before(filename):
    X, seq_len_X, max_x, min_x = load_data_compress40(filename)
    return X, seq_len_X, max_x, min_x


def load_M22_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M23_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M23_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_Exp_time7_before(filename):
    Y, seq_len_Y, max_y, min_y = load_data_exp_time7(filename)
    return Y, seq_len_Y, max_y, min_y


def load_Exp_time7_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_compare_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_compare_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getSignificand_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getSignificand_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getPackageName_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getPackageName_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_firstCharOnlyToUpper_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_firstCharOnlyToUpper_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_repeat_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_repeat_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_integerToRoman_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_integerToRoman_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_convert_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_convert_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_ascToBcd_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_ascToBcd_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_absVal_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_absVal_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_sumOfDigits_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_sumOfDigits_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isFormatLetter_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isFormatLetter_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isPalindrome_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isPalindrome_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_toUpperCase_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_toUpperCase_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isValidPort_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isValidPort_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isInner_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isInner_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isHexChar_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isHexChar_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getStart_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getStart_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_reverseWithSwaps_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_reverseWithSwaps_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isDigit_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isDigit_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_next_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_next_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_before_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_before_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isOutOfBounds_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isOutOfBounds_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_patch_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_patch_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_chars_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_chars_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_lowerFirst_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_lowerFirst_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_swapCase_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_swapCase_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_formatNumber_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_formatNumber_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_formatEscapeCharsForListing_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_formatEscapeCharsForListing_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_ceil_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_ceil_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_floor_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_floor_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_max_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_max_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isOneByte_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isOneByte_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isTwoBytes_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isTwoBytes_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isNotTrailingByte_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isNotTrailingByte_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_addText_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_addText_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_slashify_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_slashify_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_setPattern_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_setPattern_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isTextual_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isTextual_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getAgeType_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_getAgeType_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_min_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_min_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_maxofKnowledge_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_maxofKnowledge_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_count_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_count_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_trimUni_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_trimUni_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_stripIsbnSeparator_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_stripIsbnSeparator_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_toASCII_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_toASCII_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_trimRegexSlashes_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_trimRegexSlashes_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_rCnt_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_rCnt_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_mCnt_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_mCnt_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_escapeEncode_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_escapeEncode_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_escapeDecode_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_escapeDecode_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_makeUniqueKey_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_makeUniqueKey_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_append_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_append_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_prepend_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_prepend_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_enclose_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_enclose_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_encode_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_encode_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_unquote_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_unquote_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_unescape_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_unescape_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_determinePath_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_determinePath_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_determinePort_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_determinePort_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_Address_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_Address_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_increment_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_increment_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_setUserInfo_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_setUserInfo_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_ProxyHandshaker_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_ProxyHandshaker_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_createFixedSizeStripedCounterV6_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_createFixedSizeStripedCounterV6_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isWord_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isWord_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isAlphabetical_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isAlphabetical_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isLowerCase_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isLowerCase_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isUpperCase_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_isUpperCase_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y

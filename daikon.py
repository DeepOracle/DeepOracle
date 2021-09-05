import numpy as np
import random

train_num = 1000000
M1_path = 'JacksonCore/jacksoncore_6/'
M2_path = 'Compress/compress_30/'
M3_path = 'Csv/csv_14/'
M4_path = 'Time/time_3_addYears/'
M5_path = 'Time/time_3_addMonths/'
M6_path = 'Time/time_3_addWeeks/'
M7_path = 'Time/time_3_addDays/'
M8_path = 'Time/time_3_add/'
M9_path = 'Time/time_14_minusMonths/'
M10_path = 'Time/time_14_plusMonths/'
M11_path = 'Csv/csv_3/'
M12_path = 'Lang/lang_21/'
M13_path = 'IO/io_18/'
M14_path = 'Shiro_web/shiro_web_3/'
M15_path = 'Johnzon_core/johnzon_core_2/'
M16_path = 'Compress/compress_39/'
M17_path = 'Mockito/mockito_6/'
M18_path = 'Geometry_core/geometry_core_3/'
M19_path = 'Math/math_15/'
M20_path = 'Codec/codec_15/'
M21_path = 'Codec/codec_3/'
M22_path = 'Compress/compress_40/'
M23_path = 'IO/io_25/'
M24_path = 'Validator/validator_15/'


def M1(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants do not exist

        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to daikon, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M2(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        lst = in_line.split()
        # daikon invariants
        if lst[1] == out_line:
            flag += 1
        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M3(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        dataSet.append([in_line, out_line, label_line])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to daikon invariants, sort the dataSet
    Data = sorted(dataSet, key=lambda x: (x[0] == x[1]))

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M4_8(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        lst = in_line.split('#')
        flag = 0
        month = int(lst[0])
        orig_Millis = int(lst[1])
        return_Millis = int(out_line)
        # daikon invariants
        if return_Millis != orig_Millis:
            flag += 1
        if return_Millis > month:
            flag += 1

        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to daikon, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M9_10(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        orig_month = 3
        orig_day = 31
        lst = out_line.split('-')
        flag = 0
        month = int(lst[2])
        day = int(lst[3])
        # daikon invariants
        if month <= day:
            flag += 1
        if month >= 1 or day >= 1:
            flag += 1
        if orig_month < day:
            flag += 1
        if month < orig_day:
            flag += 1

        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to daikon, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M11(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        dataSet.append([in_line, out_line, label_line])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to daikon invariants, sort the dataSet
    Data = sorted(dataSet, key=lambda x: (x[0] in x[1]))

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M12(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        if out_line == 'true' or out_line == 'false':
            flag += 1
        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    random.shuffle(dataSet)
    # according to daikon, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M13(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        output_num = int(out_line)
        if output_num >= 0:
            flag += 1
        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M15(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        if out_line == 'true' or out_line == 'false':
            flag += 1
        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M16(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        if in_line == out_line:
            flag += 1

        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M17(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        if out_line == 'not null':
            flag += 1

        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M18(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        if out_line == 'true' or out_line == 'false':
            flag += 1
        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M19(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    eps = 1e-6
    while in_line and out_line and label_file:
        flag = 0
        lst = in_line.split(' ')
        x = float(lst[0])
        y = float(lst[1])
        # daikon invariants
        if abs(y - 0) < eps and abs(y - x) > eps:
            if out_line == '1.0':
                flag += 1
        if abs(x - 0) < eps and x > y:
            if out_line == 'Infinity':
                flag += 1
        if abs(x - 0) < eps and out_line == '0.0':
            flag += 1
        if abs(x + 1.0) < eps and (abs(y - 5e15) < eps or abs(y + 5e15) < eps):
            if out_line == '1.0':
                flag += 1
        if abs(y - 0) > eps and out_line != lst[1]:
            flag += 1
        if x >= 1.0 and abs(y - 0) > eps:
            if float(out_line) >= 1e-10:
                flag += 1

        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M20(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        if len(out_line) > 0:
            flag += 1

        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M21(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        if len(out_line) > 0:
            flag += 1
        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''


def M23(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    daikon_in = path + 'daikon_input.txt'
    daikon_out = path + 'daikon_out.txt'
    daikon_label = path + 'daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file:
        flag = 0
        # daikon invariants
        out_num = int(out_line)
        if in_line == '~' and out_num == 2:
            flag += 1
        elif out_num >= -1:
            flag += 1
        dataSet.append([in_line, out_line, label_line, flag])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    dataSet = dataSet[train_num:]
    random.shuffle(dataSet)
    # according to flag, sort the dataSet
    Data = sorted(dataSet, key=lambda x: x[3])

    # write daikon file
    Data = np.array(Data)
    in_f = open(daikon_in, 'w')
    out_f = open(daikon_out, 'w')
    label_f = open(daikon_label, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    return ''

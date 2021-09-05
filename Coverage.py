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


def calculate_Coverage(dataSet):
    # dataSet: input,output,label,line coverage
    random.shuffle(dataSet)
    size = len(dataSet)
    total_line = set([])
    for i in range(0, size):
        line_info = dataSet[i][3]
        line_info = line_info.strip(' ')
        lst = line_info.split(' ')
        num = len(lst)
        for j in range(0, num):
            total_line.add(float(lst[j]))
        dataSet[i].append(num)
    # Data: input,output,label,line coverage,flag
    Data = sorted(dataSet, key=lambda x: -x[4])
    for i in range(0, size):
        line_info = Data[i][3]
        line_info = line_info.strip(' ')
        lst = line_info.split(' ')
        num = len(lst)
        line = [float(x) for x in lst]
        Data[i][4] = 0
        for j in range(0, num):
            if line[j] in total_line:
                Data[i][4] += 1
                total_line.remove(line[j])
    Data = sorted(Data, key=lambda x: -x[4])
    return Data


def load_file(path):
    input_file = path + 'before_data.txt'
    output_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    line = path + 'line.txt'
    coverage_in = path + 'coverage_input.txt'
    coverage_out = path + 'coverage_output.txt'
    coverage_label = path + 'coverage_label.txt'
    coverage_line = path + 'coverage_line.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    coverage_f = open(line, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    line_line = coverage_f.readline().strip('\n')

    dataSet = []
    Data = []
    while in_line and out_line and label_file and line_line:
        dataSet.append([in_line, out_line, label_line, line_line])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
        line_line = coverage_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    coverage_f.close()
    dataSet = dataSet[train_num:]
    # according to coverage, sort the dataSet
    Data = calculate_Coverage(dataSet)
    # write coverage file
    Data = np.array(Data)
    in_f = open(coverage_in, 'w')
    out_f = open(coverage_out, 'w')
    label_f = open(coverage_label, 'w')
    coverage_f = open(coverage_line, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
        coverage_f.write(Data[i, 3] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    coverage_f.close()
    return ''


load_file(M22_path)

import numpy as np
import Coverage
import daikon
import random
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

filename = 'label.txt'
M1 = M1_path + filename
M2 = M2_path + filename
M3 = M3_path + filename
M4 = M4_path + filename
M5 = M5_path + filename
M6 = M6_path + filename
M7 = M7_path + filename
M8 = M8_path + filename
M9 = M9_path + filename
M10 = M10_path + filename
M11 = M11_path + filename
M12 = M12_path + filename
M13 = M13_path + filename
M14 = M14_path + filename
M15 = M15_path + filename
M16 = M16_path + filename
M17 = M17_path + filename
M18 = M18_path + filename
M19 = M19_path + filename
M20 = M20_path + filename
M21 = M21_path + filename
M22 = M22_path + filename
M23 = M23_path + filename

# random:(1100000,)
# coverage: (100000,)
# daikon: (100000,)
begin_num = 1000000
number = 100


def count_num(filename, rootPath):
    top_1 = 0
    top_5 = 0
    top_10 = 0
    top_100 = 0
    for i in range(0, number):
        labelSet = []
        # Coverage
        # Coverage.load_file(rootPath)
        # Daikon
        # daikon.M24(rootPath)
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                arr = line.split()
                label = [int(x) for x in arr]
                labelSet.append(label)
                line = f.readline()
        DataSet = labelSet[begin_num:]
        # random
        # random.shuffle(DataSet)
        DataSet = np.array(DataSet)
        top_1 += 1 - np.sum(DataSet[0])
        top_5 += 5 - np.sum(DataSet[0:5])
        top_10 += 10 - np.sum(DataSet[0:10])
        top_100 += 100 - np.sum(DataSet[0:100])
    ave_1 = float(top_1) / number
    ave_5 = float(top_5) / number
    ave_10 = float(top_10) / number
    ave_100 = float(top_100) / number
    print('average top_1:', ave_1)
    print('average top_5:', ave_5)
    print('average top_10:', ave_10)
    print('average top_100:', ave_100)
    return ''


count_num(M21, M21_path)

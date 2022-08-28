import numpy as np
import random

train_num = 1000000
TM1_path = 'JacksonCore/jacksoncore_6/'
TM2_path = 'Compress/compress_30/'
TM3_path = 'Csv/csv_14/'
TM4_path = 'Time/time_3_addYears/'
TM5_path = 'Time/time_3_addMonths/'
TM6_path = 'Time/time_3_addWeeks/'
TM7_path = 'Time/time_3_addDays/'
TM8_path = 'Time/time_3_add/'
TM9_path = 'Time/time_14_minusMonths/'
TM10_path = 'Time/time_14_plusMonths/'
TM11_path = 'Csv/csv_3/'
TM12_path = 'Lang/lang_21/'
TM13_path = 'IO/io_18/'
TM14_path = 'Shiro_web/shiro_web_3/'
TM15_path = 'Johnzon_core/johnzon_core_2/'
TM16_path = 'Compress/compress_39/'
TM17_path = 'Mockito/mockito_6/'
TM18_path = 'Geometry_core/geometry_core_3/'
TM19_path = 'Math/math_15/'
TM20_path = 'Codec/codec_15/'
TM21_path = 'Codec/codec_3/'
TM22_path = 'Compress/compress_40/'
TM23_path = 'IO/io_25/'

mutation_path = 'MutationTest/'
mm1_name = 'getPackageName'
mm2_name = 'getSignificand'
mm3_name = 'firstCharOnlyToUpper'
mm4_name = 'compare'
mm5_name = 'repeat'
mm6_name = 'integerToRoman'
mm7_name = 'convert'
mm8_name = 'decimalToHex'
mm9_name = 'absVal'
mm10_name = 'sumOfDigits'
mm11_name = 'isPalindrome'
mm12_name = 'toUpperCase'
mm13_name = 'isAlphabetical'
mm14_name = 'ceil'
mm15_name = 'floor'
mm16_name = 'max'
mm17_name = 'strToBcd'
mm18_name = 'ascToBcd'
mm19_name = 'isFormatLetter'
mm20_name = 'isValidPort'
mm21_name = 'isInner'
mm22_name = 'isHexChar'
mm23_name = 'getStart'
mm24_name = 'getEndByStart'
mm25_name = 'reverseWithSwaps'
mm26_name = 'reverseWithXOR'
mm27_name = 'isDigit'
mm28_name = 'next'
mm29_name = 'previous'
mm30_name = 'isOutOfBounds'
mm31_name = 'patch'
mm32_name = 'chars'
mm33_name = 'isUpperCase'
mm34_name = 'isLowerCase'
mm35_name = 'reverse'
mm36_name = 'lowerFirst'
mm37_name = 'swapCase'
mm38_name = 'formatNumber'
mm39_name = 'formatEscapeCharsForListing'
mm40_name = 'checkPositive'
mm41_name = 'checkPositiveOrZero'
mm42_name = 'checkLessThan'
mm43_name = 'createFixedSizeStripedCounterV6'
mm44_name = 'createFixedSizeStripedCounterV8'
mm45_name = 'longValue'
mm46_name = 'add'
mm47_name = 'set'
mm48_name = 'PaddedAtomicLong'
mm49_name = 'requirePositive'
mm50_name = 'requireInRange'
mm51_name = 'requireNegative'
mm52_name = 'lowerCase'
mm53_name = 'isWord'
mm54_name = 'isOneByte'
mm55_name = 'isTwoBytes'
mm56_name = 'isNotTrailingByte'
mm57_name = 'trailingByteValue'
mm58_name = 'CommonResult'
mm59_name = 'validateFailed'
mm60_name = 'failed'
mm61_name = 'escapeTags'
mm62_name = 'addText'
mm63_name = 'slashify'
mm64_name = 'setPattern'
mm65_name = 'isTextual'
mm66_name = 'add_flink'
mm67_name = 'merge'
mm68_name = 'reduce'
mm69_name = 'getAgeType'
mm70_name = 'of'
mm71_name = 'error'
mm72_name = 'ProductCategory'
mm73_name = 'CartDTO'
mm74_name = 'min'
mm75_name = 'max_knowledge'
mm76_name = 'count'
mm77_name = 'trimUni'
mm78_name = 'stripIsbnSeparator'
mm79_name = 'toASCII'
mm80_name = 'trimRegexSlashes'
mm81_name = 'rCnt'
mm82_name = 'mCnt'
mm83_name = 'escapeEncode'
mm84_name = 'escapeDecode'
mm85_name = 'makeUniqueKey'
mm86_name = 'append'
mm87_name = 'encode'
mm88_name = 'unquote'
mm89_name = 'unescape'
mm90_name = 'determinePath'
mm91_name = 'determinePort'
mm92_name = 'Address'
mm93_name = 'increment'
mm94_name = 'setUserInfo'
mm95_name = 'ProxyHandshaker'


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


def mm1(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm2(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm3(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm4(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (x in ['-1', '0', '1'] for x in lst):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm9(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_num = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (ret >= in_num):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm13(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm14(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_num = float(in_line.split('$')[0])
    ret = float(out_line.split('$')[0])
    if (ret >= 1):
        flag += 1
    if (ret >= in_num):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm15(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_num = float(in_line.split('$')[0])
    ret = float(out_line.split('$')[0])

    if (ret <= in_num):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm16(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    out_lst = out_line.split('$')
    a = int(in_lst[0])
    b = int(in_lst[1])
    ret = int(out_lst[0])

    if (ret >= a):
        flag += 1
    if (ret >= b):
        flag += 1
    if (ret != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm17(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm18(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_num = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (ret == in_num and in_num == 53):
        flag += 1

    return [in_line, out_line, label_line, flag]


def mm19_20_22(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm21(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    num, be, en = int(in_lst[0]), int(in_lst[1]), int(in_lst[2])
    if (ret == 1 and be <= en):
        flag += 1
    if (ret == 0 and be != en):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm23(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    pageNo, pageSize = int(in_lst[0]), int(in_lst[1])
    if (ret >= 0):
        flag += 1
    if (ret != pageNo):
        flag += 1
    if (pageNo != 0 and ret % pageNo == 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm24(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    start, pageSize = int(in_lst[0]), int(in_lst[1])
    if (ret >= start):
        flag += 1
    if (ret > pageSize):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm25_26(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm27(in_line: str, out_line: str, label_line: str):
    flag = 0
    s = in_line[0]
    ret = int(out_line.split('$')[0])
    if (ord(s) == 53 and ret == 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm28(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    cur, m = int(in_lst[0]), int(in_lst[1])
    if (ret >= 0):
        flag += 1
    if (ret != cur):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm29(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    cur, m = int(in_lst[0]), int(in_lst[1])
    if (cur == 1 and ret == m - 1):
        flag += 1
    elif (ret == cur - 1):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm30(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    idx, len, cap = int(in_lst[0]), int(in_lst[1]), int(in_lst[2])
    if (idx < cap and ret == 0):
        flag += 1
    if (len != cap and ret == 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm31(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_num = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (in_num == 1 and ret == 0):
        flag += 1
    if (ret <= in_num):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm32_39(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm40_41(in_line: str, out_line: str, label_line: str):
    flag = 0
    n = int(in_line.split('$')[0])
    name = in_line.split('$')[1]
    ret = int(out_line.split('$')[0])
    if (ret == n):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm42(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    n, exp, name = int(in_lst[0]), int(in_lst[1]), in_lst[2]
    if (ret < exp):
        flag += 1
    if (ret != 0):
        flag += 1
    if (ret != n):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm43_44(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm45(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm46_48(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm49(in_line: str, out_line: str, label_line: str):
    flag = 0
    val = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (ret == val):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm50(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    ret = int(out_line.split('$')[0])
    val, fir, exc = int(in_lst[0]), int(in_lst[1]), int(in_lst[2])
    if (ret == val):
        flag += 1
    if (ret > fir):
        flag += 1
    if (ret < exc):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm51(in_line: str, out_line: str, label_line: str):
    flag = 0
    val = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (ret == val):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm52(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm53(in_line: str, out_line: str, label_line: str):
    flag = 0
    num = ord(in_line[0])
    ret = int(out_line.split('$')[0])
    if (num == 102 and ret == 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm54(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm55(in_line: str, out_line: str, label_line: str):
    flag = 0
    num = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (num == 0 and ret == 1):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm56(in_line: str, out_line: str, label_line: str):
    flag = 0
    num = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (num == 0 and ret == 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm57(in_line: str, out_line: str, label_line: str):
    flag = 0
    ret = int(out_line.split('$')[0])
    if (ret >= 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm58(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm59(in_line: str, out_line: str, label_line: str):
    flag = 0
    s = in_line.split('$')[0]
    lst = out_line.split('$')
    code, mess = int(lst[0]), lst[1]
    if (code == 404 and len(mess) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm60(in_line: str, out_line: str, label_line: str):
    flag = 0
    s = in_line.split('$')[0]
    lst = out_line.split('$')
    code, mess = int(lst[0]), lst[1]
    if (code == 500 and len(mess) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm61(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm62(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = in_line.split('$')
    s1, s2 = lst[0], lst[1]
    ret = out_line.split('$')[0]
    if (ret >= s2):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm63(in_line: str, out_line: str, label_line: str):
    flag = 0
    s = in_line.split('$')[0]
    ret = out_line.split('$')[0]
    if (s == ret):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm64_65(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm72_73(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm74_77(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm78_80(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm81(in_line: str, out_line: str, label_line: str):
    flag = 0
    ret = int(out_line.split('$')[0])
    if (ret != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm82(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = in_line.split('$')
    ccnt, mcnt = int(lst[0]), int(lst[1])
    ret = int(out_line.split('$')[0])
    if (mcnt == 0 and ret == 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm83_85(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm86(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm87_90(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = out_line.split('$')
    if (len(lst) != 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm91(in_line: str, out_line: str, label_line: str):
    flag = 0
    lst = in_line.split('$')
    port, sec = int(lst[0]), int(lst[1])
    ret = int(out_line.split('$')[0])
    if (ret >= port):
        flag += 1

    return [in_line, out_line, label_line, flag]


def mm92(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    host, port = int(in_lst[0]), in_lst[1]
    out_lst = out_line.split('$')
    mhost, mport = int(out_lst[0]), out_lst[1]
    if (mhost <= host):
        flag += 1
    if (host % mhost == 0):
        flag += 1
    return [in_line, out_line, label_line, flag]


def mm93(in_line: str, out_line: str, label_line: str):
    flag = 0
    mcount = int(in_line.split('$')[0])
    ret = int(out_line.split('$')[0])
    if (ret >= mcount):
        flag += 1
    if (mcount == 0 and ret == 0):
        flag += 1

    return [in_line, out_line, label_line, flag]


def mm94(in_line: str, out_line: str, label_line: str):
    flag = 0
    return [in_line, out_line, label_line, flag]


def mm95(in_line: str, out_line: str, label_line: str):
    flag = 0
    in_lst = in_line.split('$')
    out_lst = in_line.split('$')
    host, port = in_lst[0], int(in_lst[1])
    mhost, mport = out_lst[0], int(out_lst[1])
    if (mport != 0):
        flag += 1
    if (mport <= port):
        flag += 1
    return [in_line, out_line, label_line, flag]


def main(path):
    input_file = path + '/before_data.txt'
    output_file = path + '/after_data.txt'
    label_file = path + '/label.txt'
    daikon_in = path + '/daikon_input.txt'
    daikon_out = path + '/daikon_out.txt'
    daikon_label = path + '/daikon_label.txt'

    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_line:
        dataSet.append(mm1(in_line, out_line, label_line))
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


if __name__ == '__main__':
    method_path = mutation_path + mm95_name
    main(method_path)

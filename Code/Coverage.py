import numpy as np
import random
import os
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

compare_path = 'MutationTest/compare/'
getPackageName_path = 'MutationTest/getPackageName/'
firstCharOnlyToUpper_path = 'MutationTest/firstCharOnlyToUpper/'
repeat_path = 'MutationTest/repeat/'
getSignificand_path = 'MutationTest/getSignificand/'
integerToRoman_path = 'MutationTest/integerToRoman/'
convert_path = 'MutationTest/convert1/'
ascToBcd_path = 'MutationTest/ascToBcd/'
absVal_path = 'MutationTest/absVal1/'
sumOfDigits_path = 'MutationTest/sumOfDigits1/'
isFormatLetter_path = 'MutationTest/isFormatLetter2/'
isPalindrome_path = 'MutationTest/isPalindrome/'
toUpperCase_path = 'MutationTest/toUpperCase/'
isValidPort_path = 'MutationTest/isValidPort/'
isInner_path = 'MutationTest/isInner/'
isHexChar_path = 'MutationTest/isHexChar/'
getStart_path = 'MutationTest/getStart/'
reverseWithSwaps_path = 'MutationTest/reverseWithSwaps/'
isDigit_path = 'MutationTest/isDigit/'
next_path = 'MutationTest/next/'
previous_path = 'MutationTest/previous/'
isOutOfBounds_path = 'MutationTest/isOutOfBounds/'
patch_path = 'MutationTest/patch/'
chars_path = 'MutationTest/chars/'
isUpperCase_path = 'MutationTest/isUpperCase/'
isLowerCase_path = 'MutationTest/isLowerCase/'
lowerFirst_path = 'MutationTest/lowerFirst/'
swapCase_path = 'MutationTest/swapCase/'
formatNumber_path = 'MutationTest/formatNumber/'
formatEscapeCharsForListing_path = 'MutationTest/formatEscapeCharsForListing/'
ceil_path = 'MutationTest/ceil/'
floor_path = 'MutationTest/floor/'
max_path = 'MutationTest/max/'
isOneByte_path = 'MutationTest/isOneByte/'
isTwoBytes_path = 'MutationTest/isTwoBytes/'
isNotTrailingByte_path = 'MutationTest/isNotTrailingByte/'
addText_path = 'MutationTest/addText/'
slashify_path = 'MutationTest/slashify/'
setPattern_path = 'MutationTest/setPattern/'
isTextual_path = 'MutationTest/isTextual/'
getAgeType_path = 'MutationTest/getAgeType/'
min_path = 'MutationTest/min/'
max_path = 'MutationTest/max/'
count_path = 'MutationTest/count/'
trimUni_path = 'MutationTest/trimUni/'
stripIsbnSeparator_path = 'MutationTest/stripIsbnSeparator/'
toASCII_path = 'MutationTest/toASCII/'
trimRegexSlashes_path = 'MutationTest/trimRegexSlashes/'
rCnt_path = 'MutationTest/rCnt/'
mCnt_path = 'MutationTest/mCnt/'
escapeEncode_path = 'MutationTest/escapeEncode/'
escapeDecode_path = 'MutationTest/escapeDecode/'
makeUniqueKey_path = 'MutationTest/makeUniqueKey/'
append_path = 'MutationTest/append/'
prepend_path = 'MutationTest/prepend/'
enclose_path = 'MutationTest/enclose/'
encode_path = 'MutationTest/encode/'
unquote_path = 'MutationTest/unquote/'
unescape_path = 'MutationTest/unescape/'
determinePath_path = 'MutationTest/determinePath/'
determinePort_path = 'MutationTest/determinePort/'
Address_path = 'MutationTest/Address/'
increment_path = 'MutationTest/increment/'
setUserInfo_path = 'MutationTest/setUserInfo/'
ProxyHandshaker_path = 'MutationTest/ProxyHandshaker/'
createFixedSizeStripedCounterV6_path = 'MutationTest/createFixedSizeStripedCounterV6/'
isWord_path = 'MutationTest/isWord/'
isAlphabetical_path = 'MutationTest/isAlphabetical/'


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
    line = path + 'line_coverage.txt'
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

if __name__=='__main':
    load_file(compare_path)

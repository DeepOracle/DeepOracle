import numpy as np
import Coverage
import daikon
import random
from enum import Enum
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

mutation_path = 'MutationTest/'


class Name(Enum):
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


# random:(1100000,)
# coverage: (100000,)
# daikon: (100000,)
begin_num = 0
number = 10


def count_num(filename, rootPath):
    top_1 = 0
    top_5 = 0
    top_10 = 0
    top_100 = 0
    for i in range(0, number):
        labelSet = []
        # Coverage
        Coverage.load_file(rootPath)
        # Daikon
        # daikon
        # daikon.main(rootPath)
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
    # ave_5 = float(top_5) / number
    ave_10 = float(top_10) / number
    ave_100 = float(top_100) / number
    # print('average top_1:', ave_1)
    # print('average top_5:', ave_5)
    # print('average top_10:', ave_10)
    # print('average top_100:', ave_100)
    print('{}, {}, {}'.format(ave_1, ave_10, ave_100))
    print('---------------------')
    return ''


if __name__ == '__main__':
    filename = 'coverage_label.txt'
    l, r = 94, 94
    for i, name in enumerate(Name):
        # print(i,name)
        if (i >= l-1 and i <= r-1):
            path = mutation_path + name.value + '/'
            print(i+1, path + filename)
            count_num(path + filename, path)
    # for i in range(4, 10):

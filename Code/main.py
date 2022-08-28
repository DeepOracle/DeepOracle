import numpy as np
import tensorflow as tf
import loadData
import time
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

Exp_time7_path = 'Exception/Time/time_7/'

compare_path = 'MutationTest/compare1/'
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


def one_hot(label, num_class):
    label = np.array(label)
    num_label = label.shape[0]
    index = np.arange(num_label) * num_class
    out = np.zeros((num_label, num_class))
    out.flat[index + label.ravel()] = 1
    return out


def model(input_tensor, hidden_size, output_size):
    with tf.variable_scope("Dense"):
        '''tensor1 = tf.layers.dense(inputs=input1,
                                  units=hidden_size,
                                  activation=tf.nn.relu)
        tensor2 = tf.layers.dense(inputs=tensor1, units=1)'''
        layer1 = tf.layers.dense(inputs=input_tensor,
                                 units=hidden_size,
                                 activation=tf.nn.relu,
                                 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.01))
        drop1 = tf.layers.dropout(inputs=layer1, rate=0.2)
        layer2 = tf.layers.dense(inputs=drop1,
                                 units=hidden_size,
                                 activation=tf.nn.relu,
                                 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.01))
        drop2 = tf.layers.dropout(inputs=layer2, rate=0.2)
        layer3 = tf.layers.dense(inputs=drop2,
                                 units=hidden_size,
                                 activation=tf.nn.relu,
                                 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.01))
        drop3 = tf.layers.dropout(inputs=layer3, rate=0.2)

        layer = tf.layers.dense(inputs=drop3, units=output_size)
    return layer


def main():
    start = time.time()
    lr = 0.0001
    hidden_size = 256
    batch_size = 512
    train_num = 1000000
    iterations = 100000
    max_pre1 = 0
    max_pre5 = 0
    max_pre10 = 0
    max_pre100 = 0
    path = isInner_path
    before_file = path + 'before_data.txt'
    after_file = path + 'after_data.txt'
    label_file = path + 'label.txt'
    X, seq_len_X, max_x, min_x = loadData.load_isInner_before(before_file)
    Y, seq_len_Y, max_y, min_y = loadData.load_isInner_after(after_file)
    # X_original = loadData.return_before(X, max_x, min_x)
    Y_original = loadData.return_before(Y, max_y, min_y)
    # Y_original = Y
    Y = np.array(Y)
    Label = loadData.load_label(label_file)
    embed_X = X.shape[1]
    embed_Y = Y.shape[1]

    x_train = X[0:train_num]
    x_test = X[train_num:]

    y_train = Y[0:train_num]
    y_test = Y[train_num:]
    # y_original_train = Y_original[0:train_num]
    y_original_test = Y_original[train_num:]
    y_len_test = seq_len_Y[train_num:]

    # label_train = Label[0:train_num]
    label_test = Label[train_num:]

    g1 = tf.Graph()
    sess1 = tf.Session(graph=g1)
    with sess1.as_default():
        with g1.as_default():
            x_place = tf.placeholder(dtype=tf.float32, shape=[None, embed_X])
            y_place = tf.placeholder(dtype=tf.float32, shape=[None, embed_Y])
            output = model(x_place, hidden_size, embed_Y)
            with tf.name_scope('Loss'):
                loss = tf.reduce_mean(tf.square(y_place - output))
                losses = tf.reduce_mean(tf.square(y_place - output), axis=1, keep_dims=False)
                # loss = tf.reduce_mean(tf.abs(y_place-output)/y_place)
                # losses = tf.reduce_mean(tf.abs(y_place-output)/y_place, axis=1, keep_dims=False)
            with tf.name_scope('Optimizer'):
                optimizer = tf.train.AdamOptimizer(learning_rate=lr).minimize(loss)
            init = tf.global_variables_initializer()
        sess1.run(init)
    index = 0
    for i in range(1, iterations):
        X_train = x_train[index:(index + batch_size)]
        Y_train = y_train[index:(index + batch_size)]
        index += batch_size

        if i % (train_num // batch_size) == 0:
            index = 0
        feed_dic = {x_place: X_train, y_place: Y_train}
        train_loss, train_optimizer, train_out = sess1.run([loss, optimizer, output], feed_dict=feed_dic)
        if i % 200 == 0:
            test_loss, test_out, test_losses = sess1.run([loss, output, losses],
                                                         feed_dict={
                                                             x_place: x_test,
                                                             y_place: y_test
                                                         })
            loss_index = np.argsort(test_losses)  # 将测试用例按照loss差距排序，取最大的前n个判断正负
            # top-100
            samples_index = loss_index[-1 * int(100):]
            samples_index = samples_index[::-1]
            label_output = []
            for j in range(len(samples_index)):
                label_output.append(label_test[samples_index[j]])
            fn100 = np.sum(label_output)  # 判断为负样本，判断错误
            tn100 = 100 - fn100  # 判断为负样本，判断正确
            max_pre100 = max(max_pre100, tn100)
            # top-10
            samples_index = loss_index[-1 * int(10):]
            samples_index = samples_index[::-1]
            label_output = []
            for j in range(len(samples_index)):
                label_output.append(label_test[samples_index[j]])
            fn10 = np.sum(label_output)  # 判断为负样本，判断错误
            tn10 = 10 - fn10  # 判断为负样本，判断正确
            max_pre10 = max(max_pre10, tn10)
            # top-5
            samples_index = loss_index[-1 * int(5):]
            samples_index = samples_index[::-1]
            label_output = []
            for j in range(len(samples_index)):
                label_output.append(label_test[samples_index[j]])
            fn5 = np.sum(label_output)  # 判断为负样本，判断错误
            tn5 = 5 - fn5  # 判断为负样本，判断正确
            max_pre10 = max(max_pre5, tn5)
            # top-1
            samples_index = loss_index[-1:]
            if label_test[samples_index] == 1:
                fn1 = 1
            else:
                fn1 = 0
            tn1 = 1 - fn1
            max_pre1 = max(max_pre1, tn1)
            print(test_losses[loss_index[-1]], test_losses[loss_index[0]])
            print(
                'step: %d  train loss: %f  test loss: %f  tn100: %.1f  fn100: %.1f  tn10:%.1f fn10:%.1f tn5:%.1f fn5:%.1f tn1:%.1f max_pre100: %.1f max_pre10:%.1f max_pre5:%.1f max_pre1:%.1f'
                % (i, train_loss, test_loss, tn100, fn100, tn10, fn10, tn5, fn5, tn1, max_pre100, max_pre10, max_pre5,
                   max_pre1))
            if i % 2000 == 0:
                y_pred = loadData.return_before(test_out, max_y, min_y)
                seq_dis, seq_match_rate, max_seq_dis, min_seq_dis = calculate_dis_seq(
                    y_pred, y_original_test, y_len_test)
                arr_dis, arr_match_rate = calculate_dis_array(y_pred, y_original_test, y_len_test)
                print(max_y, min_y)
                print('sequence distance: %f array distance: %f' % (seq_dis, arr_dis))
                print('seq match rate: %f, arr match rate: %f' % (seq_match_rate, arr_match_rate))
                print('max_seq_distance: %f \t min_seq_distance: %f' % (max_seq_dis, min_seq_dis))
                print('max_arr_distance: %f \t min_arr_distance: %f' % (max(test_losses), min(test_losses)))
                end = time.time()
                print('time:', end - start)
    test_loss, test_out, test_losses = sess1.run([loss, output, losses], feed_dict={x_place: x_test, y_place: y_test})
    loss_index = np.argsort(test_losses)  # 将测试用例按照loss差距排序，取最大的前n个判断正负
    samples_index = loss_index[-1 * int(100):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])

    fn100 = np.sum(label_output)  # 判断为负样本，判断错误
    tn100 = 100 - fn100  # 判断为负样本，判断正确

    samples_index = loss_index[-1 * int(10):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])
    fn10 = np.sum(label_output)  # 判断为负样本，判断错误
    tn10 = 10 - fn10  # 判断为负样本，判断正确

    samples_index = loss_index[-1 * int(5):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])
    fn5 = np.sum(label_output)  # 判断为负样本，判断错误
    tn5 = 5 - fn5  # 判断为负样本，判断正确
    samples_index = loss_index[-1 * int(1):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])
    fn1 = np.sum(label_output)  # 判断为负样本，判断错误
    tn1 = 1 - fn1  # 判断为负样本，判断正确
    # print('select num:%f  tn:%f  fn:%f' % (select_num, tn, fn))
    '''data = np.array([[100, int(tn100), int(fn100)],
                        [10, int(tn10), int(fn10)],
                        [5, int(tn5), int(fn5)],
                        [1, int(tn1), int(fn1)]])
    np.savetxt(path + '1_data.txt', data)
    np.savetxt(path + '1.txt', test_out)'''


def calculate_dis_seq(y_pred, y_true, seq_length):
    # 最小编辑距离，字符不匹配就+1
    distance = 0
    max_dis = 0
    min_dis = 1000
    match_num = 0
    cnt = 0
    lst = []
    for i in range(0, len(y_pred)):
        length = seq_length[i]
        lt_pred = np.array(y_pred[i][0:length])
        lt_true = np.array(y_true[i][0:length])
        edit_dis = sum(lt_pred != lt_true) / (length * 2)
        if edit_dis <= 0.05:
            match_num += 1
        elif cnt < 10:
            lst.append((i, lt_pred, lt_true))
            cnt += 1
        dis = float(pow(edit_dis, 2))
        max_dis = max(dis, max_dis)
        min_dis = min(dis, min_dis)
        distance += dis
    distance /= len(y_pred)
    match_rate = match_num / len(y_pred)
    # print(lst)
    return distance, match_rate, max_dis, min_dis


def calculate_dis_array(y_pred, y_true, arr_length):
    # 计算每个样本的每个参数之间的差值取平均值
    distance = 0
    match_num = 0
    Sum = 0
    for i in range(0, len(y_pred)):
        tmp = 0
        length = arr_length[i]
        Sum += length
        for j in range(0, len(y_pred[i])):
            if j >= length:
                break
            if y_true[i][j] == 0:
                array_dis = abs(y_pred[i][j] - y_true[i][j])
            else:
                array_dis = abs((y_pred[i][j] - y_true[i][j]) / y_true[i][j])
            if array_dis <= 0.05:
                match_num += 1
            tmp += array_dis
        distance += tmp / length
    distance /= len(y_pred)
    match_rate = match_num / Sum
    return distance, match_rate


if __name__ == '__main__':
    main()

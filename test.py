
# -*- coding: utf-8 -*-

import os
import glob
import statistics
"""
1. ref와 pred 디렉토리를 만들어주세요.
2. ref의 정답을 pred에 띄어쓰기 결과를 각각 넣어주세요. (.txt)
"""

def tagging(_ref_text_file):
    """
    :param _ref_text_file: text file
    :return: tag list
    """
    result = []
    for each_line in _ref_text_file:
        string = each_line.strip()
        length = len(string)
        buffer = []
        for i in range(0, length - 1):
            if string[i] == ' ':
                continue
            if string[i + 1] == ' ':
                buffer.append('1')
            else:
                buffer.append('0')
        buffer.append('1')
        result.append(buffer)
    return result


def scoring(_ref, _tc, _path):
    """
    :param _ref: 정답 tag list
    :param _tc: 시스템이 예측한 tag list
    :param _path: 시스템이 예측한 file 의 경로
    :return: 각각의 file 에 대한 Precision, Recall, F-measure 값을 console 에 출력
    """
    # tag score
    # ------------ ------------- -------------
    #  0 -> 0 =  1|  1 -> 0 =  0|  2 -> 0 =  1|
    #       1 =  0|       1 =  1|       1 =  1|
    # ------------ ------------- -------------

    number_of_tags = 0
    number_of_correct_tags = 0
    tag_predicted_by_system = 0

    number_of_sentences = 0
    number_of_correct_sentences = 0

    for i in range(len(_ref)):
        number_of_sentences += 1
        flag = 1
        for j in range(len(_ref[i])):
            reference = _ref[i][j]
            predicted = _tc[i][j]
            if reference == '2':
                continue
            if predicted == '1':
                tag_predicted_by_system += 1
            if reference == '1':
                number_of_tags += 1
                if predicted == reference:
                    number_of_correct_tags += 1
            if reference != predicted:
                flag += 1
        if flag == 1:
            number_of_correct_sentences += 1
    try:
        value = [(number_of_correct_tags/tag_predicted_by_system),
                 (number_of_correct_tags/number_of_tags)]
    except ZeroDivisionError as e:
        print(_path)
        print(e)
        return

    print("===================================")
    print(_path)
    print("Precision  /1     : ", float("{:.4f}".format(value[0])))
    print("Recall     /1     : ", float("{:.4f}".format(value[1])))
    #print("F-measure  /1     : ", float("{:.4f}".format(statistics.harmonic_mean(value))))
    print("F-measure  /1     : ", float("{:.4f}".format(statistics.mean(value))))
    print("Sentence Accuracy : ", float("{:.4f}".format(number_of_correct_sentences / number_of_sentences)))


if __name__ == "__main__":

    ext = '*.txt'
    path = os.getcwd()  # path of project directory

    ref_file_name = glob.glob(os.path.join(path + r'/ref', ext))

    if len(ref_file_name) > 1:
        print('Please put only one file in reference folder')
        exit(0)

    ref_path = str(ref_file_name[0])

    with open(ref_path, 'r', encoding='utf-8-sig') as ref_file:
        ref = list(tagging((ref_file)))

    tc_file_list = glob.glob(os.path.join(path + r'/pred', ext))

    for tc_file_name in tc_file_list:
        with open(tc_file_name, 'r', encoding='utf-8-sig') as tc_file:
            tc = list(tagging(tc_file))
        scoring(ref, tc, tc_file_name)

import re

import Tree as tr
import numpy as np
import os
import tensorflow as tf

import flag


def _shuffle_data(x, y):
    random_seed = np.random.permutation(len(x))
    shuffle_x = list()
    shuffle_y = list()
    for randIndex in random_seed:
        shuffle_x.append(x[randIndex])
        shuffle_y.append(y[randIndex])
    return shuffle_x, shuffle_y


class BatchManager:
    def __init__(self, x, y, batch_size, valid_ratio=0.1, rand=True):
        self.train_x, self.train_y = None, None
        self.valid_x, self.valid_y = None, None
        if len(x) != len(y):
            raise ValueError("입력 x와 y의 갯수가 일치하지 않습니다.")
        self.batch_size = batch_size
        self.is_random = rand
        self.valid_ratio = valid_ratio
        self.non_bug_x = list()
        self.non_bug_y = list()
        self.bug_x = list()
        self.bug_y = list()
        for x_d, y_d in zip(x, y):
            print(y_d)
            if y_d == '1':
                self.bug_x.append(x_d)
                self.bug_y.append(y_d)
            else:
                self.non_bug_x.append(x_d)
                self.non_bug_y.append(y_d)
        self.bug_x, self.bug_y = _shuffle_data(self.bug_x, self.bug_y)
        self.non_bug_x, self.non_bug_y = _shuffle_data(self.non_bug_x, self.non_bug_y)
        self.num_data = len(y)
        self.num_train = int(self.num_data * (1 - valid_ratio))
        self.num_valid = self.num_data - self.num_train

    def cross_setting(self, index):
        max_index = int(1 / self.valid_ratio) - 1
        if index == max_index:
            self.valid_x = self.bug_x[int(index * (self.num_valid / 2)):]
            self.valid_x.extend(self.non_bug_x[int(index * (self.num_valid / 2)):])
            self.valid_y = self.bug_y[int(index * (self.num_valid / 2)):]
            self.valid_y.extend(self.non_bug_y[int(index * (self.num_valid / 2)):])
            self.train_x = self.bug_x[:int(index * (self.num_valid / 2))]
            self.train_x.extend(self.non_bug_x[:int(index * (self.num_valid / 2))])
            self.train_y = self.bug_y[:int(index * (self.num_valid / 2))]
            self.train_y.extend(self.non_bug_y[:int(index * (self.num_valid / 2))])
        else:
            self.valid_x = self.bug_x[int(index * (self.num_valid / 2)):int((index + 1) * (self.num_valid / 2))]
            self.valid_x.extend(
                self.non_bug_x[int(index * (self.num_valid / 2)):int((index + 1) * (self.num_valid / 2))])
            self.valid_y = self.bug_y[int(index * (self.num_valid / 2)):int((index + 1) * (self.num_valid / 2))]
            self.valid_y.extend(
                self.non_bug_y[int(index * (self.num_valid / 2)):int((index + 1) * (self.num_valid / 2))])
            self.train_x = self.bug_x[int((index + 1) * (self.num_valid / 2)):]
            self.train_x.extend(self.non_bug_x[int((index + 1) * (self.num_valid / 2)):])
            self.train_y = self.bug_y[int((index + 1) * (self.num_valid / 2)):]
            self.train_y.extend(self.non_bug_y[int((index + 1) * (self.num_valid / 2)):])

        self.train_x, self.train_y = _shuffle_data(self.train_x, self.train_y)
        self.valid_x, self.valid_y = _shuffle_data(self.valid_x, self.valid_y)

    def reshuffle(self):
        self.train_x, self.train_y = _shuffle_data(self.train_x, self.train_y)

    def get_batches(self):
        self.reshuffle()
        batch_x, batch_y = list(), list()
        for item_x, item_y in zip(self.train_x, self.train_y):
            batch_x.append(item_x)
            batch_y.append(item_y)
            if len(batch_x) >= self.batch_size:
                yield batch_x, batch_y
                batch_x.clear()
                batch_y.clear()
        if len(batch_x) > 0:
            yield batch_x, batch_y

    def get_valid_batches(self):
        batch_x, batch_y = list(), list()
        for item_x, item_y in zip(self.valid_x, self.valid_y):
            batch_x.append(item_x)
            batch_y.append(item_y)
            if len(batch_x) >= self.batch_size:
                yield batch_x, batch_y
                batch_x.clear()
                batch_y.clear()
        if len(batch_x) > 0:
            yield batch_x, batch_y


class FileManager:
    def __init__(self, source_tree_dir, word_embadding=False):
        self.path_dir = source_tree_dir  # output == data directory path
        # file_list = os.listdir(source_tree_dir)
        CategoryName = [
            '1_Development/',
            '2_ScientificEngineering/',
            '3_Business/',
            '4_System/',
            '5_Communication/',
        ]
        # CategoryName = [
        #     '1_Development/',
        #     '2_Internet/',
        #     '3_ScientificEngineering/',
        #     '4_Business/',
        #     '5_System/',
        #     '6_Communication/',
        #     '7_Multimedia/',
        #     '8_Games/'
        # ]

        # CategoryName = [
        #     'Development\\',
        #     'Internet\\',
        #     'ScientificEngineering\\',
        #     'System\\',
        #     'Business\\',
        #     'Communication\\',
        #     'Multimedia\\',
        #     'Games\\'
        # ]


        all_api_list = list()
        all_api_frequency_list = list()

        self.root_node_list = list()
        self.all_api_list_for_category = list()
        self.all_api = list()

        for category_dir in CategoryName:
            # print(category_dir)
            sub_dir = os.listdir(source_tree_dir + category_dir)  # sub_category in a main category
            # print(src_dir)
            # print("-----sub_dir-----")
            # print(sub_dir)
            for sub_dir_list in sub_dir:

                root_node_list_for_category = list()
                api_list_for_category = list()
                src_dir = os.listdir(source_tree_dir + category_dir + sub_dir_list) # the contents in each sub_category
                # print("-----src_dir-----")
                # print(src_dir)
                for src_dir_list in src_dir:

                    api_path = os.path.join(source_tree_dir, category_dir, sub_dir_list,
                                            src_dir_list, 'api')  # sub_dir\\src_dir_list\\api
                    api_text = os.listdir(api_path)

                    ast_path = os.path.join(source_tree_dir, category_dir, sub_dir_list,
                                            src_dir_list, 'ast')  # sub_dir\\src_dir_list\\ast
                    ast_text = os.listdir(ast_path)

                    root_node_list_for_project = list()
                    api_name_for_project = list()

                    for file in ast_text:
                        all_node_list = list()  # 한파일내 모든 노드들 level 단위로 저장하기위한 리스트
                        # full_name = os.path.join(source_tree_dir, file)  # 파일의 풀네임 == 디렉토리/파일.txt
                        ast_full_name = os.path.join(ast_path, file)
                        text_file = open(ast_full_name, 'r', encoding="utf-8", errors="ignore")  # 파일객체
                        file_lines = text_file.read().splitlines()  # 파일 전체읽기. 줄마다 리스트
                        # print(file_lines)

                        if not file_lines:
                            continue

                        for line in file_lines:
                            clean_line = cleanLine(line)
                            all_node_list.append(clean_line)

                        root_node_list_for_project.append(all_node_list)

                    for api_file in api_text:
                        temp_api_name = list()
                        api_full_name = os.path.join(api_path, api_file)

                        api_text_file = open(api_full_name, 'r', encoding="utf-8", errors="ignore")  # 파일객체
                        api_file_lines = api_text_file.read().splitlines()  # 파일 전체읽기. 줄마다 리스트
                        for line in api_file_lines:
                            temp = cleanText(line)
                            temp = temp.lower()
                            # if len(temp) < 3:
                            #     continue
                            # temp = remove_s(temp)
                            if len(temp) < 3:
                                continue
                            if temp not in all_api_list:
                                all_api_list.append(temp)
                                temp_api_name.append(temp)
                                all_api_frequency_list.append(1)
                            else:
                                index = all_api_list.index(temp)
                                all_api_frequency_list[index] += 1
                        if len(temp_api_name) != 0:
                            api_name_for_project.append(temp_api_name)

                    root_node_list_for_category.append(root_node_list_for_project)
                    api_list_for_category.append(api_name_for_project)

                self.root_node_list.append(root_node_list_for_category)
                self.all_api_list_for_category.append(api_list_for_category)
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(self.root_node_list[0])
            #
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(self.all_api_list_for_category[0])

        api_num = 0
        for index, api_name in enumerate(all_api_list):
            if all_api_frequency_list[index] > 0:
                api_num += 1
                self.all_api.append(api_name)


def remove_s(data):
    if data[len(data) - 1] == 's':
        api_name = data[len(data) - 2:]
    elif len(data) > 3 and data[len(data) - 3] == "ies":
        api_name = data[len(data) - 4:] + "y"
    else:
        api_name = data
    return api_name


def cleanLine(line):
    text = re.sub("\t", "", line)
    return text


def cleanText(readData):
    text = re.sub("([0-9])", "", readData)
    text = re.sub("_", "", text)
    text = re.sub("([a-z])([A-Z])", "\g<1> \g<2>", text)  # camel case split
    text = re.sub("([A-Z])([A-Z])", "\g<1> \g<2>", text)
    text = re.sub("([A-Z])([A-Z])([a-z])", "\g<1> \g<2>\g<3>", text)
    text_list = text.split(" ")
    api_name = text_list[len(text_list) - 1]
    return api_name


def convert_node_to_vector_list(root, option, split_add=False, test_func=False):
    result_vector_list = list()
    if root.level != 1:
        raise ValueError("루트노드가 아닌 노드를 입력했습니다.")
    if option == 1:  # 1번그림처럼 읽는거
        search_node = root
        _recursive_for_1option(result_vector_list, search_node)
        return result_vector_list
    elif option == 2:  # 2번그림처럼 읽는거
        all_node = root.all_node_list
        for leveled_node in all_node:
            for one_node in leveled_node:
                result_vector_list.append(one_node.vector)
            if split_add is True:
                result_vector_list.append(np.zeros(flag.node_dim))
        return result_vector_list
    elif option == 3:  # 3번그림
        all_node = root.all_node_list
        for leveled_node in all_node:
            for one_node in leveled_node:
                if len(one_node.child) != 0:
                    result_vector_list.append(one_node.vector)
                    for child_node in one_node.child:
                        result_vector_list.append(child_node.vector)
                    if test_func is True:
                        result_vector_list.append("\n")
                    elif split_add is True:
                        result_vector_list.append(np.zeros(flag.total_dim))
        return result_vector_list


def _recursive_for_1option(append_list, node):
    if node.level == 1:
        append_list.append(node.vector)
    if len(node.child) == 0:
        pass
    for child_node in node.child:
        append_list.append(child_node.vector)
        _recursive_for_1option(append_list, child_node)

import tensorflow as tf
import numpy as np
import time
import re
from sklearn import preprocessing

from keras import optimizers, regularizers
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, concatenate, Dense, Activation, Input, Reshape, Dropout, Flatten

import WordVecModeler_new
import flag
import utils_new
import model_new
import random

def remove_s(data):
    if data[len(data) - 1] == 's':
        api_name = data[len(data) - 2:]
    elif len(data) > 3 and data[len(data) - 3] == "ies":
        api_name = data[len(data) - 4:] + "y"
    else:
        api_name = data
    return api_name

def cleanText(readData):
    text = re.sub("([0-9])", "", readData)
    text = re.sub("_", "", text)
    text = re.sub("([a-z])([A-Z])", "\g<1> \g<2>", text)  # camel case split
    text = re.sub("([A-Z])([A-Z])", "\g<1> \g<2>", text)
    text = re.sub("([A-Z])([A-Z])([a-z])", "\g<1> \g<2>\g<3>", text)
    text_list = text.split(" ")
    api_name = text_list[len(text_list) - 1]
    return api_name

if __name__ == '__main__':
    f_manager = utils_new.FileManager(flag.data_dir)
    print("Success load file")
    root_nodes_for_category = f_manager.root_node_list
    wordVecModel = WordVecModeler_new.WordVecModeler(flag.word_vec_dim)
    wordVecModel.load_word_vec("GoogleNews-vectors-negative300.bin")
    print("Success load word vector")
    data_list_for_category = np.array([])
    max_element_word_num = 0
    for category_index, root_nodes_for_project in enumerate(root_nodes_for_category):
        data_list_for_project = np.array([])
        for project_index, root_nodes in enumerate(root_nodes_for_project):
            data_list = np.array([])
            element_word_list = list()
            for idx, node in enumerate(root_nodes):
                for element in node:

                    if len(element.split("@")) == 1:
                        word_list = list()
                    else:
                        word_part = element.split("@")[1]
                        word_list = word_part.split(",")

                    for one_word in word_list:
                        temp = cleanText(one_word)
                        temp = temp.lower()

                        if temp in element_word_list:
                            continue

                        if wordVecModel.get_vector_from_word(temp) is not None:
                            c_vec = wordVecModel.get_vector_from_word(temp)
                            element_word_list.append(temp)
                            data_list = np.concatenate((data_list, c_vec), axis=0)


                    # word_vec = word_vec[:flag.word_vec_dim * flag.word_vec_num]

                    # data_list.append(word_vec)
                    # if word_vec is None:
                    #     word_vec = list()
                    # if len(word_vec) < flag.word_vec_dim * flag.word_vec_num:
                    #     zeros = np.zeros(flag.word_vec_dim * flag.word_vec_num - len(word_vec))
                    #     word_vec = np.concatenate((word_vec, zeros))
            if max_element_word_num < len(element_word_list):
                max_element_word_num = len(element_word_list)

            if 0 <= data_list.size <= flag.word_vec_dim * flag.word_num_for_project:
                zeros = np.zeros(flag.word_vec_dim * flag.word_num_for_project - data_list.size)
                data_list = np.concatenate((data_list, zeros), axis=0)
                data_list_for_project = np.concatenate((data_list_for_project, data_list), axis=0)
            else:
                print(category_index, " , ", project_index)
                print(len(element_word_list))
        data_list_for_category = np.concatenate((data_list_for_category, data_list_for_project), axis=0)
    print("Success initiate ast2vec")
    all_api_list = f_manager.all_api
    api_for_category = f_manager.all_api_list_for_category
    preprocess_api_for_category = np.array([])
    label_for_project = []

    print("max num element word : ", max_element_word_num)

    label_size = 0
    max_api_word_size = 0
    for category_index, api_for_project in enumerate(api_for_category):
        preprocess_api_for_project = np.array([])
        for _, api_for_file in enumerate(api_for_project):
            label_for_project.append(category_index)
            # preprocess_api = np.array([0 for i in range(flag.word_num_for_project)], dtype=float)
            api_project = list()
            preprocess_api = np.array([])
            for _, apis in enumerate(api_for_file):
                for _, a in enumerate(apis):
                    # if a not in all_api_list:
                    #     continue
                    if a in api_project:
                        continue
                    # index = all_api_list.index(a)

                    if wordVecModel.get_vector_from_word(a) is not None:
                        c_vec = wordVecModel.get_vector_from_word(a)
                        preprocess_api = np.concatenate((preprocess_api, c_vec), axis=0)
                        api_project.append(a)

                    # if preprocess_api[index] == 0.0:
                    #     preprocess_api[index] = 1.0
            if max_api_word_size < len(api_project):
                max_api_word_size = len(api_project)
            if 0 <= preprocess_api.size <= flag.api_num_for_project * flag.word_vec_dim:
                zeros = np.zeros(flag.api_num_for_project * flag.word_vec_dim - preprocess_api.size)
                preprocess_api = np.concatenate((preprocess_api, zeros), axis=0)
                preprocess_api_for_project = np.concatenate((preprocess_api_for_project, preprocess_api), axis=0)

        if preprocess_api_for_project.size < flag.word_num_for_project:
            zeros = np.zeros(flag.word_num_for_project - preprocess_api_for_project.size)
            preprocess_api_for_project = np.concatenate((preprocess_api_for_project, zeros), axis=0)
        preprocess_api_for_category = np.concatenate((preprocess_api_for_category, preprocess_api_for_project), axis=0)
        print("category ", category_index, " : ", len(label_for_project) - label_size)
        label_size = len(label_for_project)

    # print("Success initiate api2vec")
    # print("max api word num : ", max_api_word_size)
    #
    data_list_for_category = data_list_for_category.reshape(-1, flag.word_num_for_project, flag.word_vec_dim)
    # preprocess_api_for_category = preprocess_api_for_category.reshape(-1, flag.api_num_for_project, flag.word_vec_dim)
    print("ast vector shape : ", np.shape(data_list_for_category))
    # print("api vector shape : ", np.shape(preprocess_api_for_category))

    print("label vector shape : ", len(label_for_project))
    # print("api number : ", len(all_api_list))

    le = preprocessing.LabelEncoder()
    enc = preprocessing.OneHotEncoder()
    le.fit(label_for_project)
    assign_num = len(set(label_for_project))
    y_to_number = np.array(le.transform(label_for_project))
    y_to_number = np.reshape(y_to_number, [-1, 1])
    enc.fit(y_to_number)
    one_hot_y = enc.transform(y_to_number).toarray()
    print("label encoding shape : ", np.shape(one_hot_y))

    # train_data = np.concatenate((preprocess_api_for_category, data_list_for_category), axis=2)
    #
    # print("train data shape : ", np.shape(train_data))
    # shuffle
    for _ in range(800):
        random_index = random.randrange(0, len(label_for_project))
        i = random.randrange(0, len(label_for_project))
        temp = data_list_for_category[random_index]
        data_list_for_category[random_index] = data_list_for_category[i]
        data_list_for_category[i] = temp

        # temp = preprocess_api_for_category[random_index]
        # preprocess_api_for_category[random_index] = preprocess_api_for_category[i]
        # preprocess_api_for_category[i] = temp

        temp = one_hot_y[random_index]
        one_hot_y[random_index] = one_hot_y[i]
        one_hot_y[i] = temp

    #
    # MODEL
    epoch = flag.epochs
    batch_size = flag.batch_size
    filter = 512
    filter2 = 256

    # api_input_layer = Input(shape=(flag.api_num_for_project, flag.word_vec_dim))
    ast_input_layer = Input(shape=(flag.word_num_for_project, flag.word_vec_dim))

    # reshape_api_input_layer = Reshape((flag.api_num_for_project, flag.word_vec_dim, 1))(api_input_layer)
    reshape_ast_input_layer = Reshape((flag.word_num_for_project, flag.word_vec_dim, 1))(ast_input_layer)

    # conv_api_layer1 = Conv2D(filter, kernel_size=[2, flag.word_vec_dim], activation='relu', kernel_regularizer=regularizers.l2(0.01))(reshape_api_input_layer)
    # pool_api_layer1 = MaxPooling2D(pool_size=[flag.api_num_for_project - 1, 1], strides=1)(conv_api_layer1)
    # pool_api_layer1 = Dropout(0.25)(pool_api_layer1)
    # reshape_conv_api_layer1 = Reshape((1, filter))(pool_api_layer1)
    # result_conv_api_layer1 = Reshape(target_shape=(filter,))(reshape_conv_api_layer1)
    #
    # conv_api_layer2 = Conv2D(filter, kernel_size=[3, flag.word_vec_dim], activation='relu', kernel_regularizer=regularizers.l2(0.01))(reshape_api_input_layer)
    # pool_api_layer2 = MaxPooling2D(pool_size=[flag.api_num_for_project - 2, 1], strides=1)(conv_api_layer2)
    # pool_api_layer2 = Dropout(0.25)(pool_api_layer2)
    # reshape_conv_api_layer2 = Reshape((1, filter))(pool_api_layer2)
    # result_conv_api_layer2 = Reshape(target_shape=(filter,))(reshape_conv_api_layer2)

    # conv_api_layer3 = Conv2D(filter, kernel_size=[4, flag.word_vec_dim], activation='relu', kernel_regularizer=regularizers.l2(0.01))(reshape_api_input_layer)
    # pool_api_layer3 = MaxPooling2D(pool_size=[flag.api_num_for_project - 3, 1], strides=1)(conv_api_layer3)
    # pool_api_layer3 = Dropout(0.25)(pool_api_layer3)
    # reshape_conv_api_layer3 = Reshape((1, filter))(pool_api_layer3)
    # result_conv_api_layer3 = Reshape(target_shape=(filter,))(reshape_conv_api_layer3)

    conv_ast_layer1 = Conv2D(filter, kernel_size=[3, flag.word_vec_dim], activation='relu', kernel_regularizer=regularizers.l2(0.01))(reshape_ast_input_layer)
    pool_ast_layer1 = MaxPooling2D(pool_size=[flag.word_num_for_project - 2, 1], strides=1)(conv_ast_layer1)
    pool_ast_layer1 = Dropout(0.25)(pool_ast_layer1)
    reshape_conv_ast_layer1 = Reshape((1, filter))(pool_ast_layer1)
    result_conv_ast_layer1 = Reshape(target_shape=(filter,))(reshape_conv_ast_layer1)

    conv_ast_layer2 = Conv2D(filter, kernel_size=[4, flag.word_vec_dim], activation='relu', kernel_regularizer=regularizers.l2(0.01))(reshape_ast_input_layer)
    pool_ast_layer2 = MaxPooling2D(pool_size=[flag.word_num_for_project - 3, 1], strides=1)(conv_ast_layer2)
    pool_ast_layer2 = Dropout(0.25)(pool_ast_layer2)
    reshape_conv_ast_layer2 = Reshape((1, filter))(pool_ast_layer2)
    result_conv_ast_layer2 = Reshape(target_shape=(filter,))(reshape_conv_ast_layer2)

    conv_ast_layer3 = Conv2D(filter, kernel_size=[5, flag.word_vec_dim], activation='relu', kernel_regularizer=regularizers.l2(0.01))(reshape_ast_input_layer)
    pool_ast_layer3 = MaxPooling2D(pool_size=[flag.word_num_for_project - 4, 1], strides=1)(conv_ast_layer3)
    pool_ast_layer3 = Dropout(0.25)(pool_ast_layer3)
    reshape_conv_ast_layer3 = Reshape((1, filter))(pool_ast_layer3)
    result_conv_ast_layer3 = Reshape(target_shape=(filter,))(reshape_conv_ast_layer3)

    # conv_ast_layer4 = Conv2D(filter2, kernel_size=[6, flag.word_vec_dim], activation='relu')(reshape_ast_input_layer)
    # pool_ast_layer4 = MaxPooling2D(pool_size=[flag.word_num_for_project - 5, 1], strides=1)(conv_ast_layer4)
    # pool_ast_layer4 = Dropout(0.25)(pool_ast_layer4)
    # reshape_conv_ast_layer4 = Reshape((1, filter2))(pool_ast_layer4)
    # result_conv_ast_layer4 = Reshape(target_shape=(filter2,))(reshape_conv_ast_layer4)
    #
    # conv_ast_layer5 = Conv2D(filter2, kernel_size=[7, flag.word_vec_dim], activation='relu')(reshape_ast_input_layer)
    # pool_ast_layer5 = MaxPooling2D(pool_size=[flag.word_num_for_project - 6, 1], strides=1)(conv_ast_layer5)
    # pool_ast_layer5 = Dropout(0.25)(pool_ast_layer5)
    # reshape_conv_ast_layer5 = Reshape((1, filter2))(pool_ast_layer5)
    # result_conv_ast_layer5 = Reshape(target_shape=(filter2,))(reshape_conv_ast_layer5)

    # result_api = concatenate([result_conv_api_layer1, result_conv_api_layer2], axis=1)
    result = concatenate([result_conv_ast_layer1, result_conv_ast_layer2, result_conv_ast_layer3], axis=1)
    # result_api = concatenate([result_conv_api_layer1, result_conv_api_layer2], axis=1)
    # result_ast = concatenate([result_conv_ast_layer1, result_conv_ast_layer2], axis=1)
    # result = concatenate([result_api, result_ast], axis=1)
    # result = Flatten()(result)
    # result = Dense(units=filter)(result)
    # result = Dropout(0.75)(result)
    result = Dropout(0.75)(result)
    result = Dense(units=assign_num, activity_regularizer=regularizers.l2(0.01))(result)
    result = Activation('softmax')(result)

    model = Model(inputs=[ast_input_layer], outputs=[result])

    #
    # Training
    length = int(len(label_for_project) * (1 - 0.2))

    test_length = int(len(label_for_project) * (1 - 0.2))

    # api_train = preprocess_api_for_category[:length]
    ast_train = data_list_for_category[:length]

    # api_valid = preprocess_api_for_category[length:]
    ast_valid = data_list_for_category[length:]

    # api_test = preprocess_api_for_category[test_length:]
    ast_test = data_list_for_category[test_length:]

    train_y = one_hot_y[:length]
    valid_y = one_hot_y[length:]

    train_x = ast_train
    valid_x = ast_valid

    test_x = ast_test
    test_y = one_hot_y[test_length:]

    # train_x = [preprocess_api_for_category, data_list_for_category]
    # train_y = one_hot_y

    adam = optimizers.Adam(lr=0.00001)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    # model.fit(x=train_x, y=train_y, validation_data=(test_x, test_y), batch_size=batch_size, epochs=epoch, shuffle=True)
    model.fit(x=train_x, y=train_y, validation_data=(valid_x, valid_y), batch_size=batch_size, epochs=epoch, shuffle=True)
    model.save_weights('./Model_onlyAST.h5')
    score = model.evaluate(test_x, test_y, verbose=0)
    print('\n')
    print('Overall Test score: ', score[0])
    print('Overall Test accuracy: ', score[1])





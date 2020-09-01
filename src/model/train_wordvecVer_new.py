import numpy as np
import re
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
# from my_evaluation import macro_f1, macro_double_soft_f1
import csv
# import evaluation
from my_evaluation import *

from keras import optimizers, regularizers
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, concatenate, Dense, Activation, Input, Reshape, Dropout, Flatten
from keras.optimizers import SGD

import WordVecModeler_new
import flag
import utils_new 
import random
from random import randint, randrange


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


def init_model(num_label, ast_filter=512, api_filter=256, api_num=flag.api_num_for_project,
               word_num=flag.word_num_for_project, vec_dim=flag.word_vec_dim):

    # input layer
    api_input_layer = Input(shape=(api_num, vec_dim))
    ast_input_layer = Input(shape=(word_num, vec_dim))

    reshape_api_input_layer = Reshape((api_num, vec_dim, 1))(api_input_layer)
    reshape_ast_input_layer = Reshape((word_num, vec_dim, 1))(ast_input_layer)

    # API ConvNet
    conv_api_layer1 = Conv2D(api_filter, kernel_size=[2, vec_dim], activation='relu',
                             kernel_regularizer=regularizers.l2(0.01))(reshape_api_input_layer)
    pool_api_layer1 = MaxPooling2D(pool_size=[api_num - 1, 1], strides=1)(conv_api_layer1)
    pool_api_layer1 = Dropout(0.25)(pool_api_layer1)
    reshape_conv_api_layer1 = Reshape((1, api_filter))(pool_api_layer1)
    result_conv_api_layer1 = Reshape(target_shape=(api_filter,))(reshape_conv_api_layer1)

    conv_api_layer2 = Conv2D(api_filter, kernel_size=[3, vec_dim], activation='relu',
                             kernel_regularizer=regularizers.l2(0.01))(reshape_api_input_layer)
    pool_api_layer2 = MaxPooling2D(pool_size=[api_num - 2, 1], strides=1)(conv_api_layer2)
    pool_api_layer2 = Dropout(0.25)(pool_api_layer2)
    reshape_conv_api_layer2 = Reshape((1, api_filter))(pool_api_layer2)
    result_conv_api_layer2 = Reshape(target_shape=(api_filter,))(reshape_conv_api_layer2)

    # AST ConvNet
    conv_ast_layer1 = Conv2D(ast_filter, kernel_size=[3, vec_dim], activation='relu',
                             kernel_regularizer=regularizers.l2(0.01))(reshape_ast_input_layer)
    pool_ast_layer1 = MaxPooling2D(pool_size=[word_num - 2, 1], strides=1)(conv_ast_layer1)
    pool_ast_layer1 = Dropout(0.25)(pool_ast_layer1)
    reshape_conv_ast_layer1 = Reshape((1, ast_filter))(pool_ast_layer1)
    result_conv_ast_layer1 = Reshape(target_shape=(ast_filter,))(reshape_conv_ast_layer1)

    conv_ast_layer2 = Conv2D(ast_filter, kernel_size=[4, vec_dim], activation='relu',
                             kernel_regularizer=regularizers.l2(0.01))(reshape_ast_input_layer)
    pool_ast_layer2 = MaxPooling2D(pool_size=[word_num - 3, 1], strides=1)(conv_ast_layer2)
    pool_ast_layer2 = Dropout(0.25)(pool_ast_layer2)
    reshape_conv_ast_layer2 = Reshape((1, ast_filter))(pool_ast_layer2)
    result_conv_ast_layer2 = Reshape(target_shape=(ast_filter,))(reshape_conv_ast_layer2)

    conv_ast_layer3 = Conv2D(ast_filter, kernel_size=[5, vec_dim], activation='relu',
                             kernel_regularizer=regularizers.l2(0.01))(reshape_ast_input_layer)
    pool_ast_layer3 = MaxPooling2D(pool_size=[word_num - 4, 1], strides=1)(conv_ast_layer3)
    pool_ast_layer3 = Dropout(0.25)(pool_ast_layer3)
    reshape_conv_ast_layer3 = Reshape((1, ast_filter))(pool_ast_layer3)
    result_conv_ast_layer3 = Reshape(target_shape=(ast_filter,))(reshape_conv_ast_layer3)

    # Concatenation
    result_api = concatenate([result_conv_api_layer1, result_conv_api_layer2], axis=1)
    result_ast = concatenate([result_conv_ast_layer1, result_conv_ast_layer2, result_conv_ast_layer3], axis=1)
  
    result = concatenate([result_api, result_ast], axis=1)

    result = Dropout(0.25)(result)
    result = Dense(units=num_label, activity_regularizer=regularizers.l2(0.01))(result)
    #result = Activation('softmax')(result)
    result = Activation('sigmoid')(result)

    model = Model(inputs=[api_input_layer, ast_input_layer], outputs=[result])
    return model


def load_label(path):
    f = open(path, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    label = []
    for line in rdr:
        label.append(line[1:])
    f.close()
    return label


def shuffle_data(data_ast, data_api, label_L1, label_L2,
                 num_L1_category=flag.num_L1_class, list_num_L2=flag.label_num_L2, count=800):
    for _ in range(0, count):
        rand_src = random.randrange(0, len(label_L1))
        begin = 0
        for i in range(0, num_L1_category):
            end = begin + list_num_L2[i]
            if rand_src in range(begin, end):
                rand_trg = random.randrange(begin, end)

                temp = data_ast[rand_src]
                data_ast[rand_src] = data_ast[rand_trg]
                data_ast[rand_trg] = temp

                temp = data_api[rand_src]
                data_api[rand_src] = data_api[rand_trg]
                data_api[rand_trg] = temp

                temp = label_L1[rand_src]
                label_L1[rand_src] = label_L1[rand_trg]
                label_L1[rand_trg] = temp

                temp = label_L2[i][rand_src - begin]
                label_L2[i][rand_src] = label_L2[i][rand_trg]
                label_L2[i][rand_trg] = temp


def split_data(data_ast, data_api, label_L1, label_L2,
               num_L1_category=flag.num_L1_class, list_num_L2=flag.label_num_L2):
    list_ast_train = []
    list_api_train = []
    list_label_L1_train = []
    list_label_L2_train = []

    list_ast_valid = []
    list_api_valid = []
    list_label_L1_valid = []
    list_label_L2_valid = []

    list_ast_test = []
    list_api_test = []
    list_label_L1_test = []
    list_label_L2_test = []

    begin = 0
    for i in range(0, num_L1_category):
        end = begin + list_num_L2[i]
        length = int(list_num_L2[i] * (1 - 0.1))
        test_length = int(list_num_L2[i] * (1 - 0.1))
        print("begin: ", begin, " end: ", end, " valid length: ", length, " test length: ", test_length)
        print("train data: [", begin, ", ", begin+length, ")")
        print("valid data: [", begin+length, ", ", end, ")")
        print("test data: [", begin+test_length, ", ", end, ")")
        list_ast_train.append(data_ast[begin:begin+length])
        list_api_train.append(data_api[begin:begin+length])
        list_label_L1_train.append(label_L1[begin:begin+length])
        list_label_L2_train.append(labels_L2[i][:length])

        list_ast_valid.append(data_ast[begin+length:end])
        list_api_valid.append(data_api[begin+length:end])
        list_label_L1_valid.append(label_L1[begin+length:end])
        list_label_L2_valid.append(labels_L2[i][length:])

        list_ast_test.append(data_ast[begin+test_length:end])
        list_api_test.append(data_api[begin+test_length:end])
        list_label_L1_test.append(label_L1[begin+test_length:end])
        list_label_L2_test.append(labels_L2[i][test_length:])

        begin = end

    train_x_L1 = [np.concatenate(list_api_train), np.concatenate(list_ast_train)]
    train_y_L1 = np.concatenate(list_label_L1_train)
    train_x_L2 = []
    for api, ast in zip(list_api_train, list_ast_train):
        train_x_L2.append([api, ast])
    train_y_L2 = list_label_L2_train
    train = (train_x_L1, train_y_L1, train_x_L2, train_y_L2)

    valid_x_L1 = [np.concatenate(list_api_valid), np.concatenate(list_ast_valid)]
    valid_y_L1 = np.concatenate(list_label_L1_valid)
    valid_x_L2 = []
    for api, ast in zip(list_api_valid, list_ast_valid):
        valid_x_L2.append([api, ast])
    valid_y_L2 = list_label_L2_valid
    valid = (valid_x_L1, valid_y_L1, valid_x_L2, valid_y_L2)

    test_x_L1 = [np.concatenate(list_api_test), np.concatenate(list_ast_test)]
    test_y_L1 = np.concatenate(list_label_L1_test)
    test_x_L2 = []
    for api, ast in zip(list_api_test, list_ast_test):
        test_x_L2.append([api, ast])
    test_y_L2 = list_label_L2_test
    test = (test_x_L1, test_y_L1, test_x_L2, test_y_L2)

    return train, valid, test


if __name__ == '__main__':
    f_manager = utils_new.FileManager(flag.data_dir)
    print("Success load file")
    root_nodes_for_category = f_manager.root_node_list
    wordVecModel = WordVecModeler_new.WordVecModeler(flag.word_vec_dim)
    #wordVecModel.load_word_vec('../module/GoogleNews-vectors-negative300.bin')
    wordVecModel.load_word_vec('GoogleNews-vectors-negative300.bin')
    print("Success load word vector")

    data_list_for_category = np.array([])
    max_element_word_num = 0

# AST vector initialize

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



            if max_element_word_num < len(element_word_list): # max word number
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
    print("api_for_category -> len : ", len(api_for_category))
    print("api_for_category -> shape : ", np.shape(api_for_category))
    preprocess_api_for_category = np.array([])
    # label_for_project = []

    print("max num element word : ", max_element_word_num)

# API vector initialize
    label_size = 0
    max_api_word_size = 0
    for sub_index, api_for_project in enumerate(api_for_category): # sub_category shape : 25
        preprocess_api_for_project = np.array([])

        for idx, api_for_file in enumerate(api_for_project): # project shape : 1598

            api_project = list()
            preprocess_api = np.array([])
            for _, apis in enumerate(api_for_file):
                for _, a in enumerate(apis):
                    if a in api_project:
                        continue

                    if wordVecModel.get_vector_from_word(a) is not None:
                        c_vec = wordVecModel.get_vector_from_word(a)
                        preprocess_api = np.concatenate((preprocess_api, c_vec), axis=0)
                        api_project.append(a)

            if max_api_word_size < len(api_project):
                max_api_word_size = len(api_project)
            if 0 <= preprocess_api.size <= flag.api_num_for_project * flag.word_vec_dim:
                zeros = np.zeros(flag.api_num_for_project * flag.word_vec_dim - preprocess_api.size)
                preprocess_api = np.concatenate((preprocess_api, zeros), axis=0)
                preprocess_api_for_project = np.concatenate((preprocess_api_for_project, preprocess_api), axis=0)

        preprocess_api_for_category = np.concatenate((preprocess_api_for_category, preprocess_api_for_project), axis=0)

    item_list = []
    print("Success initiate api2vec")
    print("max api word num : ", max_api_word_size)

    print("item Count : ", item_list)

    data_list_for_category = data_list_for_category.reshape(-1, flag.word_num_for_project, flag.word_vec_dim)
    preprocess_api_for_category = preprocess_api_for_category.reshape(-1, flag.api_num_for_project, flag.word_vec_dim)
    print("ast vector shape : ", np.shape(data_list_for_category))
    print("api vector shape : ", np.shape(preprocess_api_for_category))


    print("api number : ", len(all_api_list))
    # Multi-Labeling Step
    label_L1 = load_label(flag.label_L1_path)
    one_hot = OneHotEncoder(sparse=False)#categories=flag.category_L1)
    label_L1 = np.array(one_hot.fit_transform(label_L1))
    labels_L2 = []

    for i in range(flag.num_L1_class):
        label = load_label(flag.label_L2_path[i])
        mlb = MultiLabelBinarizer(classes=flag.category_L2[i])
        label = np.array(mlb.fit_transform(label))
        labels_L2.append(label)

    assign_num_L1 = len(label_L1[0])
    assign_num_L2 = []
    for label in labels_L2:
        assign_num_L2.append(len(label[0]))
    print("assign_num for L1 (output dimension) : ", assign_num_L1) # 25 -> 242
    print("label vector shape : ", np.shape(label_L1))
    print("labeling Complete")

    shuffle_data(data_list_for_category, preprocess_api_for_category, label_L1, labels_L2)

    epoch = flag.epochs
    batch_size = flag.batch_size
    model_L1 = init_model(num_label=assign_num_L1)
    models_L2 = []
    for assign_num in assign_num_L2:
        models_L2.append(init_model(num_label=assign_num))


    print("data spliting...")
    train, valid, test = split_data(data_list_for_category, preprocess_api_for_category, label_L1, labels_L2)
    train_x_L1, train_y_L1, train_x_L2, train_y_L2 = train
    valid_x_L1, valid_y_L1, valid_x_L2, valid_y_L2 = valid
    test_x_L1, test_y_L1, test_x_L2, test_y_L2 = test
    print("data spliting complete.")
    print("")
    print("L1 train x: [", len(train_x_L1[0]), ", ", len(train_x_L1[1]), "], y: ", len(train_y_L1))
    print("L1 valid x: ", len(valid_x_L1[0]), ", ", len(valid_x_L1[1]), "], y: ", len(valid_y_L1))
    print("L1 test x: ", len(test_x_L1[0]), ", ", len(test_x_L1[1]), "], y: ", len(test_y_L1))

    for i in range(0, flag.num_L1_class):
        print("L2_", i, " train x: ", len(train_x_L2[i][0]), ", ", len(train_x_L2[i][1]), "], y: ", len(train_y_L2[i]))
        print("L2_", i, " valid x: ", len(valid_x_L2[i][0]), ", ", len(valid_x_L2[i][1]), "], y: ", len(valid_y_L2[i]))
        print("L2_", i, " test x: ", len(test_x_L2[i][0]), ", ", len(test_x_L2[i][1]), "], y: ", len(test_y_L2[i]))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    
    model_L1.compile(
        loss=macro_double_soft_f1,
        optimizer=sgd,
        metrics=[soft_accuracy, soft_recall, soft_precision, macro_f1, soft_jaccard]
    )
    model_L1.fit(
        x=train_x_L1, y=train_y_L1,
        validation_data=(valid_x_L1, valid_y_L1),
        batch_size=batch_size,
        epochs=epoch, shuffle=True
    )
    

    for i in range(0, flag.num_L1_class):
        models_L2[i].compile(
            loss=macro_double_soft_f1,
            optimizer=sgd,
            metrics=[soft_accuracy, soft_recall, soft_precision, macro_f1, soft_jaccard]
        )
        models_L2[i].fit(
            x=train_x_L2[i], y=train_y_L2[i],
            validation_data=(valid_x_L2[i], valid_y_L2[i]),
            batch_size=batch_size,
            epochs=epoch, shuffle=True
        )
    
    score_L1 = model_L1.evaluate(test_x_L1, test_y_L1, verbose=0)
    print("L1 Loss : ", score_L1[0])
    print("L1 Accuracy : ", score_L1[1])
    print("L1 Recall : ", score_L1[2])
    print("L1 Precision : ", score_L1[3])
    print("L1 F1-Score : ", score_L1[4])
    print("L1 Jaccard : ", score_L1[5])
    
    for idx, L2 in enumerate(models_L2):
        score_L2 = L2.evaluate(test_x_L2[idx], test_y_L2[idx])
        print("L2 ", idx, "th child loss : ", score_L2[0])
        print("L2 ", idx, "th child accuracy : ", score_L2[1])
        print("L2 ", idx, "th child Recall : ", score_L2[2])
        print("L2 ", idx, "th child Precision : ", score_L2[3])
        print("L2 ", idx, "th child F1-score : ", score_L2[4])
        print("L2 ", idx, "th child Jaccard : ", score_L2[5])

    
    

    





import os

count_ast = 0
count_api = 0
root_name = ('sourceforge/')
root = os.listdir(root_name)
# print("main category : ")
# print(root)

# ast file이 겹쳐있다면? 
# ast folder >= 2 : print

for main_category in root:
    print('main category count..')
    sub_dir = os.listdir(root_name + main_category)
    # print("sub_category : ")
    # print(sub_dir)
    for sub_dir_list in sub_dir:
        src_dir = os.listdir(root_name + main_category + '/' + sub_dir_list)
        # print("src_list : ")
        # print(src_dir)
        for src_dir_list in src_dir: 
            project_dir = os.listdir(root_name + main_category + '/' + sub_dir_list + '/' + src_dir_list)
            # print(project_dir)
            count_api = project_dir.count('api')
            count_ast = project_dir.count('ast')
            print(count_api)
            print(count_ast)

            # print(count)
            if count_api >= 2 or count_ast >=2:
                print(count_api)
                print(count_ast)
            

            api_path = os.listdir(root_name + main_category + '/' + sub_dir_list + '/' + src_dir_list + '/' + 'api')
            ast_path = os.listdir(root_name + main_category + '/' + sub_dir_list + '/' + src_dir_list + '/' + 'ast')
            # count += 1

            api_dir = os.path.join(root_name + main_category + '/' + sub_dir_list + '/' + src_dir_list + '/' + 'api')
            ast_dir = os.path.join(root_name + main_category + '/' + sub_dir_list + '/' + src_dir_list + '/' + 'ast')

            # print(src_dir_list, ' ', len(api_path))
            # print(src_dir_list, ' ', len(ast_path))
            if(len(api_path) != len(ast_path)):
                print('ddddddddddddddddddddddddddddddddddddddd')
            elif(len(ast_path) == 0):
                print(os.getcwd())
                print('ddddddddddddddddddddddddddddddddddd')


            if os.path.exists(ast_dir) or os.path.exists(api_dir):
                pass
            else:
                print("없다 !")



            # if len(ast_path) != len(api_path):
            #     print("발견 !")
            #     print("위치 : " + os.getcwd())
            # else:
                # print("ast file length : ", len(ast_path))
                # print("api file length : ", len(api_path))

# print("number : ", count)
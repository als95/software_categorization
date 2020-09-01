DEBUG = False

word_vec_dim = 300
word_num_for_project = 10270
api_num_for_project = 308
# label_num_L1 = 242
num_L1_class = 5
label_num_L2 = [439, 355, 172, 234, 229]
category_L1 = [
    'SoftwareDevelopment',
    'ScientificEngineering',
    'Business',
    'System',
    'Communication']
category_L2 = [
    [
        'Build-tools',
        'Code-generators',
        'Compilers',
        'Framework',
        'Interpreters',
        'Object Brokering',
        'Libraries',
        'User-Interface',
    ],
    [
        'Bio-Informatics',
        'Human Machine Interfaces',
        'Mathematics',
        'Visualization',
    ],
    [
        'Enterprise',
        'Financial',
        'Scheduling',
    ],
    [
        'Networking',
        'Storage',
        'System-administration',
    ],
    [
        'Chat',
        'Email',
        'File-Sharing',
        'Telephony',
    ],
]

#data_dir = "new_jdt_only" # data folder?
# data_dir = "../data/sourceforge/" # server
# data_dir = "E:\\data\\sourceforge\\" # local
data_dir = "sourceforge/"

label_L1_path = "data/MainCategory_Label.csv"
label_L2_path = [
                    "data/SoftwareDevelopment_Label.csv",
                    "data/ScientifficEngineering_Label.csv",
                    "data/Business_Label.csv",
                    "data/System_Label.csv",
                    "data/Communication_Label.csv",
                ]
batch_size = 32
epochs = 100
#tensorboard_url = "haesung_cnn/adam" # maybe output folder
#tensorboard_url = 'C:\\Users\\MH\\RTSE_Workspace\\SCAC\\data\\embedding_output'
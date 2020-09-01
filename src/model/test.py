import csv
import src.model.flag as flag
from sklearn.preprocessing import MultiLabelBinarizer

label = []

# f = open('E:\\data\\label\\CSVtest.csv', 'r', encoding='utf-8')
f = open(flag.label_L2_path[0], 'r', encoding='utf-8')

rdr = csv.reader(f)
for line in rdr:
    label.append(line[1:])

mlb = MultiLabelBinarizer(classes=flag.category_L2[0])
label = mlb.fit_transform(label)

print(label)
print(label.classes_)
f.close()

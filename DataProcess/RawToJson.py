import json
from tqdm import tqdm

raw_data_dir = "D:\\data\\Reuters-21578\\raw\\"
data_target_dir = "D:\\data\\Reuters-21578\\BalancedLossNLP\\"

train_data_target_path = data_target_dir + "training_data.json"
test_data_target_path = data_target_dir + "test_data.json"
train_data_target = list()
test_data_target = list()

cats_path = raw_data_dir + "cats.txt"
i = 0
for line in tqdm(open(cats_path)):
    line_item = line.split()               #对行内容进行按空格分隔, 因为每行后面有\n, 所以不带参数可以分隔空格包含\n
    text_path = raw_data_dir + line_item[0]
    text_file = open(text_path)
    text_context = text_file.read()
    data_item = dict()
    data_item['text'] = text_context
    data_item['labels'] = line_item[1:]

    if(line_item[0].split("/")[0] == "test"):
        test_data_target.append(data_item)
    else:
        train_data_target.append(data_item)

train_data_target_json = json.dumps(train_data_target)
train_data_target_file = open(train_data_target_path, 'w+')
train_data_target_file.write(train_data_target_json)
train_data_target_file.close()

test_data_target_json = json.dumps(test_data_target)
test_data_target_file = open(test_data_target_path, 'w+')
test_data_target_file.write(test_data_target_json)
test_data_target_file.close()

print("data process done")


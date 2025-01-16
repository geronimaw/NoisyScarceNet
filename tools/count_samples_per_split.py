import os
import json

# split1_path = "/home/lmigliorelli/ScarceNet-main_noisy/data/animalpose/annotations/ap10k-train-split1.json"
# out_path = "/home/lmigliorelli/ScarceNet-main_noisy/data/label_list"

# with open(split1_path, 'r') as file:
#     data = json.load(file)

# all_ids = []
# for sample in data["annotations"]:
#     all_ids.append(sample["image_id"])

# out_file = open(os.path.join(out_path, "annotation_list_all1"), 'w')
# json.dump(all_ids, out_file)
# out_file.close()

with open("/home/lmigliorelli/ScarceNet-main_noisy/data/label_list/annotation_list_0", "r") as file:
    data = json.load(file)
print(len(data))
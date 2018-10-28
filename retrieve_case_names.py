import os
import json
import csv

cluster_directory = '/home/jrjflei/Downloads/scotus_clusters'
csv_directory = '/home/jrjflei/dev/case_name_generator'

case_name_list = []
case_name_full_list = []
case_name_short_list = []
count = 0

for filename in os.listdir(cluster_directory):
    if filename.endswith('.json'):
        count += 1
        with open(os.path.join(cluster_directory, filename), encoding='utf-8') as f:
            data = json.load(f)
            if data['case_name']:
                case_name_list.append(data['case_name'])
            if data['case_name_full']:
                case_name_full_list.append(data['case_name_full'])
            if data['case_name_short']:
                case_name_short_list.append(data['case_name_short'])
        print(count)

with open(os.path.join(csv_directory, 'case_names.csv'), 'w', newline='') as f:
    case_name_writer = csv.writer(f)
    for case_name in case_name_list:
        case_name_writer.writerow([case_name])

with open(os.path.join(csv_directory, 'case_names_full.csv'), 'w', newline='') as f:
    case_name_writer = csv.writer(f)
    for case_name in case_name_full_list:
        case_name_writer.writerow([case_name])

with open(os.path.join(csv_directory, 'case_names_short.csv'), 'w', newline='') as f:
    case_name_writer = csv.writer(f)
    for case_name in case_name_short_list:
        case_name_writer.writerow([case_name])
            
        
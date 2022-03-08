import yaml
import datetime

with open(r'E:\KLA\Milestone1\Milestone1A.yaml') as file:
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(datetime.datetime.now())
        print(item, ":", doc)
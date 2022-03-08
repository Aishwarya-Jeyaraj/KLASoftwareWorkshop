import yaml
import datetime
import csv 

with open(r'E:\KLA\Milestone1\Milestone1A.yaml') as file:
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"),end="")
        print("000000")
        
        print(item, ":", doc)
        
        with open('Milestone1.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(doc)
            
        with open('Milestone1.txt', 'w') as f:
            for line in doc:
                f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
                f.write("000000 ")
                f.write(line)
                f.write('\n')


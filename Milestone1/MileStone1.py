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

        rehearsal=0

        with open('Milestone1.txt', 'w') as f:
            for line in doc:
                f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
                f.write("000000 ")
                f.write(line)
                
        
                print()

                a_yaml_file = open("Milestone1A.yaml")
                parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
                print(parsed_yaml_file["M1A_Workflow"])

                print()

                try:
                    for key,val in (parsed_yaml_file["M1A_Workflow"]):
                        print(key,val)
                except ValueError:
                    print("M1A_Workflow Entry")
                    if(rehearsal%2==0):
                        f.write(" M1A_Workflow Entry")
                    else:
                        f.write(" M1A_Workflow Exit")
                    f.write("\n")
                    rehearsal+=1
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Trailing the log.')



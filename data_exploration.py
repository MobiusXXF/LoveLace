import pandas

def data_to_list_of_dicts():
    file = open("reprocessed.hungarian.data", "r")
    database = []
    val_info = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]
    for line in file:
        entry = dict()
        values = line.split()
        for index, item in enumerate(values):
            entry[val_info[index]] = item
            database.append(entry)
        print(database)
    file.close()

def data_processing_via_pandas():
    val_info = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]
    heart_disease_data = pandas.read_csv("heart.csv")
    print(heart_disease_data.head())


data_processing_via_pandas()    

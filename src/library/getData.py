import csv
from src.library.getPath import getDataPath


# def getDataFromCsv():
#     all_test_data = []
#     with open(getDataPath('register_testdata.csv')) as e:
#         filereader = csv.reader(e)
#         next(e)
#         for row in filereader:
#             all_test_data.append(row)
#     return all_test_data

def get_csv_data(filename):
    all_data = []
    with open(getDataPath(filename)) as e:
        filereader = csv.reader(e)
        next(e)
        for row in filereader:
            all_data.append(row)
        return all_data

# print(get_csv_data('issue_data.csv'))




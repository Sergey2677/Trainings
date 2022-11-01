import csv
import pandas as pd

with open('test1.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    obj = pd.Series(reader)


pd.set_option('display.max_colwidth', None)
print(obj.take([i for i in range(1, 10)]))




@property
def capacity(self):
    return self.__capacity
    
@capacity.setter
def capacity(self, capacity):
    self.__capacity = capacity
    

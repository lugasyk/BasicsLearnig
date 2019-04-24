Class as decorator
import os
import sys
import pandas as pd

class ReadFileToDataFrame(object):
   def __init__(self, function):
       print("Hello! Class")
       self.function = function

   def __call__(self, *args, **kwargs):
       print("Hello! Call")
       self.function(*args, **kwargs)


@ReadFileToDataFrame
def function(fileName):
   print("Hello! Function")
   # fileName = str(sys.argv[1]) - how to read in function from stream line
   get_path_to_data_csv = os.getcwd() + "\\" + "data" + "\\" + fileName
   # load data
   data = pd.read_csv(get_path_to_data_csv, sep=',', header=0)
   print(data.head(1))
   return data.head(1)



class E(object):
    def __init__(self, name, value=''):
        self.name = name
        self._value = value
        self._childs = {}

    def set_value(self, value):
        self._value = value
        return self

    def __getattr__(self, name):
        return self._childs.setdefault(name, self.__class__(name))

    def __call__(self, value):
        return self.set_value(value)

    def render(self):
        return '<{name}>\n\t{tags}\n\t{value}\r\n</{name}>'.format(name=self.name, tags='\n'.join(child.render() for child in self._childs.values()), value = self._value)
root = E('root')
root.a(12).p.i('FFFFF')


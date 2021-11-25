import os
import yaml


def read_testcase(yaml_name):
    with open(os.getcwd()+'/data/'+yaml_name,mode='r',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value
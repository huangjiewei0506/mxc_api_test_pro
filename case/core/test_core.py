import pytest
import requests
from config.config import host,Cookie
from commom.yaml_util import read_testcase
headers = {
    "Cookie": Cookie
}


class TestCore:
    def test_core01(self):
        args=read_testcase('getCurrentAccount.yaml')
        #args[0]['request']['url']中的[0]代表yaml文件中的第一条符合条件的数据，必须传入，否则报错，如果是第二个测试用例数据，则使用[1]
        url= host + args[0]['request']['url']
        res=requests.get(url,headers=headers)
        assert  res.status_code==200
        assert '操作成功' in res.text
        print(res.text)


    def test_core02(self):
        args=read_testcase('getResources.yaml')
        url= host + args[0]['request']['url']
        res=requests.post(url, headers=headers)
        assert res.status_code == 200
        assert '操作成功' in res.text
        print(res.text)


    def test_core03(self):
        url = host+'/core/saler/getCurrentSaler'
        res = requests.get(url, headers=headers)
        assert res.status_code == 200
        assert '操作成功' in res.text
        print(res.text)

    def test_core04(self):
        url = host+'/core/account/getCurrentRoles'
        res=requests.request("post",url=url,headers=headers)
        #res = requests.get(url, headers=headers)
        assert res.status_code == 200
        assert '操作成功' in res.text
        print(res.text)

    def test_core05(self):
        url = host+'/core/lockLeads/getCountOfLockLeadsBySaler'
        res=requests.request("get",url=url,headers=headers)
        assert res.status_code == 200
        assert '操作成功' in res.text
        print(res.text)



    def test_core06(self):
        args=read_testcase('updateDay.yaml')
        url = host + args[0]['request']['url']

        data=args[0]['request']['data']
        method=args[0]['request']['method']
        res = requests.request(method=method, url=url, headers=headers,data=data)
        assert res.status_code == 200
        assert '上课日期修改前后无变化' in res.text
        print(res.text)



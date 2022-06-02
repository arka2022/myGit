import  requests
import json
import jsonpath

from Uitls.XLUtils import XLRead
from Uitls.readText import Read_Write_Txt
from Uitls.readUrl import URLS
import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='/Users/arkapdas/PycharmProjects/REST_API_Final_Project/Log/ToDoList_API_UserUpdate.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)


class TestUser:


    def test_register_user(self):
        url=URLS.register_User_url
        file=open("/Users/arkapdas/PycharmProjects/REST_API_Final_Project/TestData/register_user.json")
        json_ip=file.read()
        request_json=json.loads(json_ip)
        response=requests.post(url,json=request_json)
        assert response.status_code==201
        logger.info('Status code:  %s'%(response.status_code))
        #respo_json = json.loads(response.text)
        #t = jsonpath.jsonpath(respo_json, 'token')
        #print(str(t[0]))


    def test_login(self):
        url=URLS.login_User_url
        file = open("/Users/arkapdas/PycharmProjects/REST_API_Final_Project/TestData/login_user.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        response = requests.post(url, json=request_json)
        assert response.status_code==200
        logger.info('Status code:  %s'%(response.status_code))

        respo_json=json.loads(response.text)
        t=jsonpath.jsonpath(respo_json,'token')
        Read_Write_Txt.token_write(self,str(t[0]))

    def test_GetLoginUserViaToken(self):
        url=URLS.login_user_via_token
        tok=Read_Write_Txt.token_read(self)
        headers_dict = {"Authorization": "Bearer " + tok}
        req = requests.get(url, headers=headers_dict)
        print(req.text)
        assert req.status_code==200
        logger.info('Status code:  %s' % (req.status_code))

    def test_updateUserProfile(self):
        url=URLS.update_User_url
        #Load/read json file
        file = open("/Users/arkapdas/PycharmProjects/REST_API_Final_Project/TestData/update_user.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        #Set header
        tok = Read_Write_Txt.token_read(self)
        headers_dict = {"Authorization": "Bearer " + tok}

        resp = requests.put(url, json=request_json, headers=headers_dict)
        assert resp.status_code==200
        logger.info('Status code:  %s' % (resp.status_code))

    def test_User_logout(self):
        url=URLS.logout_url
        tok = Read_Write_Txt.token_read(self)
        headers_dict = {"Authorization": "Bearer " + tok}

        resp = requests.post(url, headers=headers_dict)
        assert resp.status_code == 200
        logger.info('Status code:  %s' % (resp.status_code))























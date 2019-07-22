# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/4/24 8:16'



from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from SecureHTTP import AESEncrypt

class Crypt(MiddlewareMixin):
    def process_response(self, request, response):
        data_str = str(response.content, encoding='utf8')
        aeskey = settings.ServerAESkey
        response.content = AESEncrypt(aeskey, data_str)
        return response


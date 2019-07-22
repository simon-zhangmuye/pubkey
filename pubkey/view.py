# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/4/23 22:21'

from rest_framework.views import APIView
from django.conf import settings
from django.http import JsonResponse


class ServerKeypair(APIView):

    def get(self, request):
        res = {"state_code": 200}
        res['serverPublicKey'] = settings.ServerPubKey
        res['serverPrivateKey'] = settings.ServerPrivKey
        res['expired'] = settings.ExpiredTime

        return JsonResponse(res)


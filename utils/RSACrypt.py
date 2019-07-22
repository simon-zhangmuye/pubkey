# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/4/3 13:03'

#生成rsa密钥对
from SecureHTTP import generate_rsa_keys
from django.conf import settings
import datetime
from django.utils.timezone import utc


def generate_key():
    (pubkey, privkey) = generate_rsa_keys(incall=True)
    pubkey =str(pubkey, encoding='utf-8')
    privkey = str(privkey, encoding='utf-8')

    settings.ServerPubKey = pubkey
    settings.ServerPrivKey = privkey
    utcnow = datetime.datetime.utcnow().replace(tzinfo=utc)
    delta = datetime.timedelta(days=1)

    expired = utcnow + delta
    settings.ExpiredTime = expired
    settings.ServerAESkey = '6Q&J-wstnQKhWMDn8f(%rnI%5.8bsRi>'



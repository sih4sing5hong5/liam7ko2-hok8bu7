import http
import io
import json
from urllib.parse import quote

from django.core.management.base import BaseCommand


from 收音.models import 例句表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        for 例句 in 例句表.objects.all():
            conn = http.client.HTTPConnection(
                "xn--lhrz38b.xn--v0qr21b.xn--kpry57d")
            conn.request(
                "GET",
                "/%E6%BC%A2%E5%AD%97%E9%9F%B3%E6%A8%99%E5%B0%8D%E9%BD%8A" +
                "?%E6%9F%A5%E8%A9%A2%E8%85%94%E5%8F%A3=%E9%96%A9%E5%8D%97%E8%AA%9E" +
                "&%E6%BC%A2%E5%AD%97=" + quote(例句.漢字) +
                "&%E9%9F%B3%E6%A8%99=" + quote(例句.臺羅)
            )
            r1 = conn.getresponse()
            if r1.status != 200:
                print(r1.status, r1.reason)
                raise RuntimeError()
            資料 = json.loads(r1.read().decode('utf-8'))
            if '失敗' in 資料:
                print(例句.pk, 例句.漢字, 例句.臺羅)

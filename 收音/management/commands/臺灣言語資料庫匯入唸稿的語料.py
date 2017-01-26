import http
import json
from os.path import join
from posix import listdir
import re
from urllib.parse import quote

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


from 收音.models import 例句表
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from 臺灣言語資料庫.資料模型 import 影音表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        call_command('顯示資料數量')

        公家內容 = {
            '收錄者': 來源表.objects.get_or_create(名='系統管理員')[0].編號(),
            '來源': 來源表.objects.get_or_create(名='唸稿')[0].編號(),
            '版權': 版權表.objects.get_or_create(版權='會使公開')[0].pk,
            '種類': '字詞',
            '語言腔口': '閩南語',
            '著作所在地': '臺灣',
            '著作年': '2016',
        }
        切 = re.compile(r'錄音檔-(.+)-(\d+).wav\Z')
        資料夾 = join(settings.BASE_DIR, '原始檔案')
        for 檔名 in sorted(listdir(資料夾)):
            結果 = 切.match(檔名)
            if 結果:
                編號 = int(結果.group(2))
                例句 = 例句表.objects.get(pk=編號)
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

                音檔路徑 = join(資料夾, 檔名)
                音 = 聲音檔.對檔案讀(音檔路徑)
                json資料 = [{
                    '內容': 資料['分詞'],
                    '語者': 結果.group(1),
                    '開始時間': 0.3,
                    '結束時間': 音.時間長度()
                }]
                影音內容 = {'影音所在': 音檔路徑}
                影音內容.update(公家內容)
                影音 = 影音表.加資料(影音內容)

                聽拍內容 = {'聽拍資料': json資料}
                聽拍內容.update(公家內容)
                影音.寫聽拍(聽拍內容)

        call_command('顯示資料數量')


from base64 import b64decode
import json

from django.core.files.base import ContentFile
from django.db import transaction
from django.db.models.aggregates import Max
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.views import View


from 收音.models import 例句音檔表
from 收音.models import 例句表


class 稿(View):

    def get(self, request):
        try:
            這馬第幾句 = int(request.GET['這馬第幾句'])
        except:
            return self.揣後一筆(request.GET['啥人唸的'].strip())

        try:
            例句 = 例句表.objects.get(pk=這馬第幾句 + 1)
        except:
            例句 = 例句表.objects.get(pk=1)
        資料 = model_to_dict(例句)
        資料['編號'] = 資料['id']
        return JsonResponse(資料)

    def post(self, request):
        啥人唸的 = request.POST['啥人唸的'].strip()
        編號 = request.POST['編號']
        資料陣列 = bytes(json.loads(
            '[' + b64decode(request.POST['blob']).decode('utf-8') + ']'
        ))
        with transaction.atomic():
            例句音檔 = 例句音檔表.objects.create(
                啥人唸的=啥人唸的,
                例句=例句表.objects.get(pk=編號),
            )
            例句音檔.音檔.save(
                '錄音檔-{}-{}.wav'.format(啥人唸的, 編號),
                ContentFile(資料陣列)
            )

        return self.揣後一筆(啥人唸的)

    def 揣後一筆(self, 啥人唸的):
        數量 = (
            例句音檔表.objects
            .filter(啥人唸的=啥人唸的)
            .aggregate(上尾一句=Max('例句__pk'))['上尾一句']
        )
        try:
            例句 = 例句表.objects.get(pk=數量 + 1)
        except:
            例句 = 例句表.objects.get(pk=1)
        資料 = model_to_dict(例句)
        資料['編號'] = 資料['id']
        return JsonResponse(資料)

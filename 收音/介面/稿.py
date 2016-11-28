
from django.db.models.aggregates import Max
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.views import View
from 收音.models import 例句音檔表
from 收音.models import 例句表


class 稿(View):

    def get(self, request):
        return self.揣後一筆(request.GET['啥人唸的'])

    def post(self, request):
        例句音檔表.objects.create(
            啥人改的=request.POST['啥人唸的'],
            例句=例句表.objects.get(pk=request.POST['id']),
            音檔=request.POST['blob'],
        )
        return self.揣後一筆(request.POST['啥人唸的'])

    def 揣後一筆(self, 啥人唸的):
        數量 = 例句音檔表.objects.filter(啥人唸的=啥人唸的).aggregate(上尾一句=Max('pk'))['上尾一句']
        try:
            例句 = 例句表.objects.get(pk=數量 + 1)
        except:
            例句 = 例句表.objects.get(pk=1)
        return JsonResponse(model_to_dict(例句))

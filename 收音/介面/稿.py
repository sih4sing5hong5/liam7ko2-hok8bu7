
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.views import View
from 收音.models import 例句音檔表
from 收音.models import 例句表


class 稿(View):

    def get(self, request):
        數量 = 例句音檔表.objects.filter(啥人唸的=request.GET['啥人唸的']).count()
        例句 = 例句表.objects.get(pk=數量 + 1)
        return JsonResponse(model_to_dict(例句))

    def post(self, request):
        物件 = 書面表.objects.get(pk=pk)
        物件.資料.create(
            啥人改的=request.user,
        )
        return JsonResponse({
            '狀態': '無問題'
        })

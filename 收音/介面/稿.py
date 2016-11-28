
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.views import View


class 稿(View):

    def get(self, request, pk):
        物件 = 書面表.objects.get(pk=pk)
        資料 = model_to_dict(物件, ['id', '編號', '文章名', '作者', '聽拍的人'])
        書面資料 = 物件.上新的資料()
        資料.update(model_to_dict(書面資料, ['漢字', '臺羅']))
        資料['原始檔網址'] = 物件.原始檔.url
        try:
            資料['啥人改的'] = 書面資料.啥人改的.last_name + 書面資料.啥人改的.first_name
        except:
            資料['啥人改的'] = ''
        return JsonResponse({
            '資料': 資料
        })

    def post(self, request, pk):
        物件 = 書面表.objects.get(pk=pk)
        物件.資料.create(
            啥人改的=request.user,
            漢字=request.POST['漢字'].rstrip(),
            臺羅=request.POST['臺羅'].rstrip(),
        )
        return JsonResponse({
            '狀態': '無問題'
        })

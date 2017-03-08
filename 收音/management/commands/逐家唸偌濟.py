import json

from django.core.management.base import BaseCommand


from 收音.models import 例句音檔表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        全部 = {}
        for 啥人唸的 in 例句音檔表.objects.values_list('啥人唸的', flat=True):
            try:
                全部[啥人唸的] += 1
            except:
                全部[啥人唸的] = 1
        print(json.dumps(全部, indent=2, ensure_ascii=False))

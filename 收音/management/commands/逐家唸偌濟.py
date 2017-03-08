import json

from django.core.management import call_command
from django.core.management.base import BaseCommand


from 收音.models import 例句音檔表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        call_command('顯示資料數量')
        全部 = {}
        for 例句音檔 in 例句音檔表.objects.values_list('啥人唸的', flat=True):
            try:
                全部[例句音檔.啥人唸的] += 1
            except:
                全部[例句音檔.啥人唸的] = 1
        print(json.dumps(全部, indent=2, ensure_ascii=False))

import csv

from django.core.management.base import BaseCommand


from 收音.models import 例句表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        with open('例句.csv', 'w') as csvfile:
            fieldnames = ['編號', '漢字', '臺羅']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for 例句 in 例句表.objects.all():
                writer.writerow({'編號': 例句.pk, '漢字': 例句.漢字, '臺羅':  例句.臺羅})

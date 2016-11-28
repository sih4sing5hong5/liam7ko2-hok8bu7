from django.contrib import admin
from 拍字.models import 書面表


class 袂使台(admin.ModelAdmin):

    def get_actions(self, request):
        return []

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(書面表, 袂使台)

from django.contrib import admin


class 袂使台(admin.ModelAdmin):

    def get_actions(self, request):
        return []

    def has_delete_permission(self, request, obj=None):
        return False



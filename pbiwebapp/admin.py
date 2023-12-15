from django.contrib import admin
from .models import *

# Register your models here.
class CapacityAdmin(admin.ModelAdmin):
    list_display = ['capacityId', 'capacityName', 'insertedDate', 'powerbi_setting']

class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ['workspaceId', 'workspaceName', 'insertedDate', 'capacityId']


admin.site.register(PowerBI_Setting)
admin.site.register(Capacity,CapacityAdmin)
admin.site.register(Workspace,WorkspaceAdmin)
admin.site.register(Dataset)


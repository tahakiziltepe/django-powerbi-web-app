from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .utils import *
# Create your views here.

def IndexView(request):
    capacities = Capacity.objects.annotate(workspace_count=Count('workspace'))
    # workspaces = Workspace.objects.filter(insertedDate__lte=timezone.now()).order_by("-insertedDate")[:5]
    workspaces = Workspace.objects.annotate(dataset_count=Count('dataset')).order_by('-dataset_count')[:5]
    datasets = Dataset.objects.filter(insertedDate__lte=timezone.now()).order_by("-insertedDate")[:5]
    data = {'capacities': capacities,
            'workspaces': workspaces,
            'datasets': datasets,
            }
    return render(request, 'pbiwebapp/index.html', data)

class WorkspaceView(generic.ListView):
    model = Workspace
    template_name = "pbiwebapp/workspaces.html"
    context_object_name = "workspaces"

    def get_queryset(self):
        queryset = super().get_queryset()
        annotated_queryset = queryset.annotate(dataset_count=Count('dataset')).order_by('-dataset_count')
        return annotated_queryset



def update_capacities(request):
    pbi_settings = PowerBI_Setting.objects.get(id=1)
    print(f"1 -- Views -- PBI_SETTINGS ---{pbi_settings}")
    access_token = request_access_token(pbi_settings.app_id,
                                        pbi_settings.tenant_id,
                                        pbi_settings.username,
                                        pbi_settings.password)
    print(f"2 -- Views -- ACCESS TOKEN ---{access_token}")
    func_update_capacities(access_token)
    print(f"3 -- Views -- RUN FUNCTION ---")
    return redirect('pbiwebapp:index')

def delete_capacity_from_db(request,v_id):
    c = Capacity.objects.filter(id=v_id)
    c.delete()
    return redirect('pbiwebapp:index')

def update_workspaces(request):
    pbi_settings = PowerBI_Setting.objects.get(id=1)
    print(f"1 -- Views -- PBI_SETTINGS ---{pbi_settings}")
    access_token = request_access_token(pbi_settings.app_id,
                                        pbi_settings.tenant_id,
                                        pbi_settings.username,
                                        pbi_settings.password)
    print(f"2 -- Views -- ACCESS TOKEN ---{access_token}")
    func_update_workspaces(access_token)
    print(f"3 -- Views -- RUN FUNCTION ---")
    return redirect('pbiwebapp:index')

def delete_workspace_from_db(request,v_id):
    c = Workspace.objects.filter(id=v_id)
    c.delete()
    return redirect('pbiwebapp:index')


def update_datasets(request):
    pbi_settings = PowerBI_Setting.objects.get(id=1)
    print(f"1 -- Views -- PBI_SETTINGS ---{pbi_settings}")
    access_token = request_access_token(pbi_settings.app_id,
                                        pbi_settings.tenant_id,
                                        pbi_settings.username,
                                        pbi_settings.password)
    print(f"2 -- Views -- ACCESS TOKEN ---{access_token}")
    func_update_datasets(access_token)
    print(f"3 -- Views -- RUN FUNCTION ---")
    return redirect('pbiwebapp:index')


def delete_dataset_from_db(request,v_id):
    c = Dataset.objects.filter(id=v_id)
    c.delete()
    return redirect('pbiwebapp:index')


def workspaces(request):
    return render(request, 'pbiwebapp/workspaces.html')
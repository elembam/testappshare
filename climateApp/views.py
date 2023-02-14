from django.shortcuts import render
from .models import DataSource, Resource
from datetime import datetime
# Create your views here.
import pandas as pd
import numpy as np

def data_sources(request):
    list_sources = DataSource.objects.all()
    return render(request, 'climateApp/source_list.html', {
        'list_sources': list_sources,
    })

def material_list(request):
    materials = Resource.objects.all()
    return render(request, 'climateApp/materials.html', {
        'materials': materials,
    })

def chart_view(request):
    ls = DataSource.objects.all().values()
    lr = Resource.objects.all().values()
    resources = Resource.objects.all()
    data = pd.DataFrame(ls)
    data1 = pd.DataFrame(lr)


    cotwo_value = data1['cotwovalue_aonethree'].tolist()
    cfour_value = data1['cotwovalue_conefour'].tolist()
    multiple= list(np.multiply(np.array(cotwo_value),np.array(cfour_value)))
    identity = data1['id'].tolist()


    context = {
        'identity':identity,
        'cotwo_value': cotwo_value,
        'cfour_value': cfour_value,
        'score': multiple,
        'resources': resources,
        "data": [1, 2, 3],
    }

    return render(request, 'climateApp/chartsJS.html', context)




def home(request):
    name = "Name"
    now = datetime.now()
    day = now.strftime('%j')
    week = now.strftime('%W')
    zone = now.strftime('%Z')
    month = now.strftime('%B')
    year = now.strftime('%G')
    time = now.strftime('%H:%M:%S.%f')

    return render(request,
        'climateApp/home.html', {
        "name": name,
        "day": day,
        "week": week,
        "month": month,
        "year": year,
        "time": time,
        "zone": zone,

    })


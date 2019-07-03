from django.shortcuts import render
from products.models import Feature


def search_item(request):
    features = Feature.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'features.html', {"features": features})



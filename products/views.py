from django.shortcuts import render, get_object_or_404
from .models import Feature


def all_features(request):
    features = Feature.objects.all()
    return render(request, 'features.html', {'features': features})


def newest_feature(request):
    newest_feature = Feature.objects.filter(published=True).order_by('-date_posted').first()
    return {'newest_feature': newest_feature}


def feature_detail(request, feature_id):
    feature_detail = get_object_or_404(Feature, pk=feature_id)
    context = {'feature_detail': feature_detail}
    return render(request, 'feature_detail.html', context)

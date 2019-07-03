from .models import Feature


def newest_feature(request):
    newest_feature = Feature.objects.filter(published=True).order_by('-date_posted').first()
    return {'newest_feature': newest_feature}
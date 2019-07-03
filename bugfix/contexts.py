from .models import BugTable


def newest_bugs(request):
    newest_bugs = BugTable.objects.order_by('-date_posted').first()
    return {'newest_bugs': newest_bugs}

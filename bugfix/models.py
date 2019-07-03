from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BugTable(models.Model):

    BUG_POSTED = 'bug_posted'
    FIXING_IN_PROCESS = 'fixing_in_process'
    BUG_FIXED = 'bug_fixed'
    STATUS = (
        (BUG_POSTED, 'bug_posted'),
        (FIXING_IN_PROCESS, 'fixing_in_process'),
        (BUG_FIXED, 'bug_fixed')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    bug_name = models.CharField(max_length=50, blank=False)
    bug_description = models.TextField()
    bug_solution = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default=BUG_POSTED)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.bug_name


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(BugTable, on_delete=models.CASCADE, related_name='voter')

    class Meta:
        unique_together = (('user', 'bug'),)


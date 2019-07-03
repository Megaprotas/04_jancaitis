from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from .models import BugTable, Vote
from .forms import BugTableForm


def bugfix(request):
    bugs = BugTable.objects.all().order_by('-status', '-date_posted')
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugfix.html', context)


def new_bug(request):
    if request.method == 'POST':
        form = BugTableForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(bugfix)
    else:
            form = BugTableForm()
    return render(request, 'new_bug.html', {'form': form})


def edit_bug(request, id):
    bug = get_object_or_404(BugTable, pk=id)

    if request.method == 'POST':
        form = BugTableForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect(bugfix)
    else:
        form = BugTableForm(instance=bug)
    return render(request, 'new_bug.html', {'form': form})


def delete_bug(request, id=None):
    bug = get_object_or_404(BugTable, pk=id)
    author = bug.author.username

    if request.method == 'POST' and request.user.is_authenticated and request.user.username == author:
        bug.delete()
        messages.success(request, 'You have successfully deleted your post')
        return redirect(bugfix)
    context = {'bug': bug,
               'author': author}
    return render(request, 'delete_bug.html', context)


def detail(request, bug_id):
   bug = get_object_or_404(BugTable, pk=bug_id)
   return render(request, 'detail.html', {'bug': bug})


def vote(request, bug_id):
    bug = get_object_or_404(BugTable, pk=bug_id)
    current_user_voted = bug.voter.filter(user=request.user).exists()
    if request.user.is_authenticated:
        bug.vote += 1
        try:
            Vote.objects.create(bug=bug, user=request.user)
            bug.save()
        except IntegrityError:
            messages.success(request, 'You already voted for this bug')
            return redirect(bugfix)
        context = {'bug': bug,
                   'current_user_voted': current_user_voted,
                  }
    return render(request, 'detail.html', context)


def graph(request):
    bug_all = BugTable.objects.filter()
    bug_all_total = bug_all.count()

    bug_posted = BugTable.objects.filter(
        status=BugTable.BUG_POSTED)
    bug_posted_total = bug_posted.count()

    bug_fixing_in_process = BugTable.objects.filter(
        status=BugTable.FIXING_IN_PROCESS)
    bug_fixing_in_process_total = bug_fixing_in_process.count()

    bug_fixed = BugTable.objects.filter(
        status=BugTable.BUG_FIXED)
    bug_bug_fixed_total = bug_fixed.count()

    one_day = timezone.now() - timedelta(days=1)
    one_week = timezone.now() - timedelta(days=7)
    one_month = timezone.now() - timedelta(days=30)

    one_day_all_bugs = BugTable.objects.filter(
        date_posted__gte=one_day).count()
    one_day_bug_posted = BugTable.objects.filter(
        date_posted__gte=one_day,
        status=BugTable.BUG_POSTED).count()
    one_day_fixing_in_process = BugTable.objects.filter(
        date_posted__gte=one_day,
        status=BugTable.FIXING_IN_PROCESS).count()
    one_day_bug_fixed = BugTable.objects.filter(
        date_posted__gte=one_day,
        status=BugTable.BUG_FIXED).count()

    one_week_all_bugs = BugTable.objects.filter(
        date_posted__gte=one_week).count()
    one_week_bug_posted = BugTable.objects.filter(
        date_posted__gte=one_week,
        status=BugTable.BUG_POSTED).count()
    one_week_fixing_in_process = BugTable.objects.filter(
        date_posted__gte=one_week,
        status=BugTable.FIXING_IN_PROCESS).count()
    one_week_bug_fixed = BugTable.objects.filter(
        date_posted__gte=one_week,
        status=BugTable.BUG_FIXED).count()

    one_month_all_bugs = BugTable.objects.filter(
        date_posted__gte=one_month).count()
    one_month_bug_posted = BugTable.objects.filter(
        date_posted__gte=one_month,
        status=BugTable.BUG_POSTED).count()
    one_month_fixing_in_process = BugTable.objects.filter(
        date_posted__gte=one_month,
        status=BugTable.FIXING_IN_PROCESS).count()
    one_month_bug_fixed = BugTable.objects.filter(
        date_posted__gte=one_month,
        status=BugTable.BUG_FIXED).count()

    context = {'bug_all_total': bug_all_total,
               'bug_posted_total': bug_posted_total,
               'bug_fixing_in_process_total': bug_fixing_in_process_total,
               'bug_bug_fixed_total': bug_bug_fixed_total,
               'one_day_all_bugs': one_day_all_bugs,
               'one_day_bug_posted': one_day_bug_posted,
               'one_day_fixing_in_process': one_day_fixing_in_process,
               'one_day_bug_fixed': one_day_bug_fixed,
               'one_week_all_bugs': one_week_all_bugs,
               'one_week_bug_posted': one_week_bug_posted,
               'one_week_fixing_in_process': one_week_fixing_in_process,
               'one_week_bug_fixed': one_week_bug_fixed,
               'one_month_all_bugs': one_month_all_bugs,
               'one_month_bug_posted': one_month_bug_posted,
               'one_month_fixing_in_process': one_month_fixing_in_process,
               'one_month_bug_fixed': one_month_bug_fixed,
    }
    return render(request, 'graph.html', context)

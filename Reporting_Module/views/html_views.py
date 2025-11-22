from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import DailyReport
from django.utils import timezone

@login_required
def daily_report_list(request):
    # Show reports for the logged-in user
    reports = DailyReport.objects.filter(user=request.user).order_by("-date")
    return render(request, "reporting/daily_report_list.html", {"reports": reports})

@login_required
def daily_report_detail(request, pk):
    report = DailyReport.objects.get(pk=pk, user=request.user)
    return render(request, "reporting/daily_report_detail.html", {"report": report})

@login_required
def daily_report_chart(request):
    # گرفتن گزارش‌های 7 روز گذشته کاربر
    today = timezone.localdate()
    last_week = today - timezone.timedelta(days=6)
    reports = DailyReport.objects.filter(user=request.user, date__range=[last_week, today]).order_by('date')

    # آماده کردن داده‌ها برای Chart.js
    labels = [report.date.strftime("%b %d") for report in reports]
    tasks_data = [report.tasks_completed for report in reports]
    pomodoros_data = [report.pomodoros_completed for report in reports]
    productivity_data = [report.productivity_score for report in reports]

    context = {
        "labels": labels,
        "tasks_data": tasks_data,
        "pomodoros_data": pomodoros_data,
        "productivity_data": productivity_data,
    }
    return render(request, "reporting/daily_report_chart.html", context)
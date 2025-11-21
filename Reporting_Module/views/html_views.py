from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import DailyReport

@login_required
def daily_report_list(request):
    # Show reports for the logged-in user
    reports = DailyReport.objects.filter(user=request.user).order_by("-date")
    return render(request, "reporting/daily_report_list.html", {"reports": reports})

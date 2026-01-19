from django.shortcuts import render

# Create your views here.


# def top_reports(request):
#     return render(request, 'cheaterreports/top_reports.html')


# def reports_by_username(request):
#     return render(request, 'cheaterreports/reports_by_username.html')


def new_report(request):
    return render(request, 'cheaterreports/new_report.html')


def report_detail(request, report_id):
    context = {
        'report_id': report_id,
    }
    return render(request, 'cheaterreports/report_detail.html', context)

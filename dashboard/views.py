import json
from django.shortcuts import render
from .models import CrimeRecord
from .forms import CrimeFilterForm


def home(request):
    total_records = CrimeRecord.objects.count()
    total_metrics = CrimeRecord.objects.values_list('metric', flat=True).distinct().count()
    years = list(CrimeRecord.objects.values_list('year', flat=True).distinct())

    context = {
        'total_records': total_records,
        'total_metrics': total_metrics,
        'min_year': min(years) if years else None,
        'max_year': max(years) if years else None,
    }
    return render(request, 'dashboard/home.html', context)


def data_table(request):
    records = CrimeRecord.objects.all().order_by('year', 'metric')
    form = CrimeFilterForm(request.GET or None)

    if form.is_valid():
        metric = form.cleaned_data.get('metric')
        year_from = form.cleaned_data.get('year_from')
        year_to = form.cleaned_data.get('year_to')

        if metric:
            records = records.filter(metric__icontains=metric)
        if year_from:
            records = records.filter(year__gte=year_from)
        if year_to:
            records = records.filter(year__lte=year_to)

    context = {
        'form': form,
        'records': records[:300],
    }
    return render(request, 'dashboard/data_table.html', context)


def charts(request):
    all_records = CrimeRecord.objects.all()

    metrics = list(
        CrimeRecord.objects.values_list('metric', flat=True).distinct().order_by('metric')
    )

    default_metric = metrics[0] if metrics else ''
    selected_metric = request.GET.get('metric', default_metric)

    metric_records = all_records.filter(metric=selected_metric).order_by('year')

    line_labels = [record.year for record in metric_records]
    line_values = [record.value for record in metric_records]

    latest_year = all_records.order_by('-year').values_list('year', flat=True).first()

    latest_records = all_records.filter(year=latest_year).order_by('metric') if latest_year else []

    bar_labels = [record.metric for record in latest_records]
    bar_values = [record.value for record in latest_records]

    context = {
        'metrics': metrics,
        'selected_metric': selected_metric,
        'latest_year': latest_year,
        'line_labels': json.dumps(line_labels),
        'line_values': json.dumps(line_values),
        'bar_labels': json.dumps(bar_labels),
        'bar_values': json.dumps(bar_values),
    }
    return render(request, 'dashboard/charts.html', context)
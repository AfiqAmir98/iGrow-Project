from django.shortcuts import render, redirect
from .models import Chart
from .forms import ChartForm

# Create your views here.
def index(request):
    charts = Chart.objects.all()

    if request.method == 'POST':
        form = ChartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('charts:index')
    else:
        form = ChartForm()

    context = {
        "charts": charts,
        "form": form
    }

    return render(request, 'charts/index.html', context)
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406348282',
        'name': 'Neal Guarddin',
        'class': 'PBP E'
    }

    return render(request, "index.html", context)
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    if request.method == 'POST':
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
        c = int(request.POST.get('c'))
        d = int(request.POST.get('d'))
        result = process_values(a, b, c, d)
        context['result'] = result
    return render(request, 'index.html', context)

def process_values(a, b, c, d):
    if a < b:
        if c > d:
            return "Condition a < b and c > d"
        elif c == d:
            return "Condition a < b and c == d"
        else:
            return "Condition a < b and c < d"
    elif a == b:
        return "Condition a == b"
    elif c == d:
        return "Condition c == d"
    else:
        return "Other condition"

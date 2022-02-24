from django.shortcuts import render

# Create your views here.

def search(request):
    if request.method == 'POST':
        print(request.POST['input'])
        return render(request, 'search/search.html', {'output': request.POST['input']})
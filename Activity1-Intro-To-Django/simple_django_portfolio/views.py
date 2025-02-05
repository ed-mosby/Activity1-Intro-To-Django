from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'Your Name', 'bio': 'Short bio about yourself'})

from django.shortcuts import render , HttpResponse

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def feature(request):
    return render(request, 'feature.html')


def service(request):
    return render(request, 'service.html')


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def cars(request):
    return render(request, 'cars.html')


def error_404(request):
    return render(request, '404.html')

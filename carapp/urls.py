# from django.urls import path
# from .views import home , about , blog , cars , contact , feature , service , team , testimonial , error_404

# urlpatterns = [
#     path('' , home , name='home'),
#     path('about' , about , name='about'),
#     path('blog' , blog , name='blog'),
#     path('cars' , cars , name='cars'),
#     path('contact' , contact , name='contact'),
#     path('feacture' , feature , name='feature'),
#     path('service' , service , name='service'),
#     path('team' , team , name='team'),
#     path('testimonial' , testimonial , name='testimonial'),
#     path('error_404' , error_404 , name='error_404'),
# ]


from django.urls import path
from .views import home, about, blog, cars, contact, feature, service, team, testimonial, error_404

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),  # Ensure this line exists
    path('blog/', blog, name='blog'),
    path('cars/', cars, name='cars'),
    path('contact/', contact, name='contact'),
    path('feature/', feature, name='feature'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('404/', error_404, name='error_404'),
]

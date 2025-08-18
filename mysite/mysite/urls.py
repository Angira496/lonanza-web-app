from django.contrib import admin
from django.urls import path

###############
from mlapp.views import contact, send_email, test_page
########################

import mlapp.views

urlpatterns = [
    path("", mlapp.views.home),
    path("about/", mlapp.views.about),
    path("myui/", mlapp.views.myui),
    path("myapi/", mlapp.views.myapi),
    path("ourteam/", mlapp.views.ourteam),
    path("predict/", mlapp.views.predict),
    path("contact/", mlapp.views.contact),
    path("model_accuracy/", mlapp.views.model_accuracy),
    path("analysis/", mlapp.views.analysis),
    path("result/",mlapp.views.result),
     # ... other url patterns ...
    path('send-email/', send_email, name='send_email'),
    path('test/', test_page, name='test')

]
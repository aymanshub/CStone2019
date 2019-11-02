from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'main'

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home",
    ),
    path(
        "about-us/",
        TemplateView.as_view(template_name="about_us.html"),
        name="about_us",
    ),
    path(
        "new-quote/",
        TemplateView.as_view(template_name="new_quote.html"),
        name="new_quote",
    ),
    path(
        "contact-us/",
        views.ContactUsView.as_view(),
        name="contact_us",
    ),
]
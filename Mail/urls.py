from django.urls import path
from Mail.views import contact, user_confirmation_email


urlpatterns = [
    path("user_confirmation_email/", user_confirmation_email, name="user_confirmation_email"),
    path("contact/", contact, name="contact"),    
]

from django.urls import path
from TopKala_account.views import login_page, register_page

urlpatterns = [
    path('login', login_page),
    path('register', register_page),
]

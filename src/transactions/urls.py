from django.urls import path
from .views import deposit_view, withdrawal_view


app_name = 'transactions'

urlpatterns = [
    # url(r'^$', home_view, name='home'),
    path('deposit/', deposit_view, name='deposit'),
    path('withdrawal/', withdrawal_view, name='withdrawal'),
]

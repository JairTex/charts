from django.urls import path

from .views import DadosJSONView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
]

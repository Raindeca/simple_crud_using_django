from django.urls import path, re_path
from . import views

# Create this app section as 'transaction'
app_name = 'transaction'

# urls for accessing the content
urlpatterns = [
    # /transaction/
    path('', views.IndexView.as_view(), name='index'),

    #/transaction/{id}/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/transaction/buy/
    path('buy/', views.TransactionCreate.as_view(), name='transaction-add'),

    #/transaction/buy/2/
    re_path(r'buy/(?P<pk>[0-9]+)/$', views.TransactionUpdate.as_view(), name='transaction-update'),

    #/transaction/buy/2/delete
    re_path(r'buy/(?P<pk>[0-9]+)/delete$', views.TransactionDelete.as_view(), name='transaction-delete'),
]

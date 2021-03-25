from django.urls import path, re_path
from . import views

# Create this app section as 'costumer'
app_name = 'costumer'

# urls for accessing the content
urlpatterns = [
    # /costumer/
    path('', views.IndexView.as_view(), name='index'),

    #/costumer/{id}/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/costumer/new/add/
    path('new/add/', views.CostumerCreate.as_view(), name='costumer-add'),

    #/costumer/new/2/
    re_path(r'new/(?P<pk>[0-9]+)/$', views.CostumerUpdate.as_view(), name='costumer-update'),

    #/costumer/new/2/delete
    re_path(r'new/(?P<pk>[0-9]+)/delete$', views.CostumerDelete.as_view(), name='costumer-delete'),
]

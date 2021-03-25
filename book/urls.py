from django.urls import path, re_path
from . import views

# Create this app section as 'book'
app_name = 'book'

# urls for accessing the content
urlpatterns = [
    # /book/
    path('', views.IndexView.as_view(), name='index'),

    #/book/{id}/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/book/list/add/
    path('list/add/', views.BookCreate.as_view(), name='book-add'),

    #/costumer/list/2/
    re_path(r'list/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book-update'),

    #/costumer/list/2/delete
    re_path(r'list/(?P<pk>[0-9]+)/delete$', views.BookDelete.as_view(), name='book-delete'),
]

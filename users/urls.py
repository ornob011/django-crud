from django.urls import path
from . import views
from .api_views import ParentListCreateView, ParentRetrieveUpdateDestroyView, ChildListCreateView, ChildRetrieveUpdateDestroyView


urlpatterns = [
    path('', views.home, name='home'),
    path('parents/', views.list_parents, name='list_parents'),
    path('children/', views.list_children, name='list_children'),
    path('parent/create/', views.create_parent, name='create_parent'),
    path('parent/update/<int:parent_id>/', views.update_parent, name='update_parent'),
    path('parent/delete/<int:parent_id>/', views.delete_parent, name='delete_parent'),
    path('child/create/', views.create_child, name='create_child'),
    path('child/update/<int:child_id>/', views.update_child, name='update_child'),
    path('child/delete/<int:child_id>/', views.delete_child, name='delete_child'),
]


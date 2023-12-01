from django.contrib import admin
from .models import Parent, Child

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Parent model.
    """
    list_display = ('first_name', 'last_name', 'street', 'city', 'state', 'zip_code')
    search_fields = ('first_name', 'last_name', 'city', 'state')
    list_filter = ('state',)

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    """
    Admin configuration for Child model.
    """
    list_display = ('first_name', 'last_name', 'parent')
    search_fields = ('first_name', 'last_name', 'parent__first_name', 'parent__last_name')
    list_filter = ('parent__state',)
    raw_id_fields = ('parent',)
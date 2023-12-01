from django import forms
from .models import Parent, Child

class ParentForm(forms.ModelForm):
    """
    ModelForm for creating and updating Parent instances.
    """
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'street', 'city', 'state', 'zip_code']

class ChildForm(forms.ModelForm):
    """
    ModelForm for creating and updating Child instances. Only includes Parent reference.
    """
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'parent']

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)
        # Customize the queryset or add other form field customizations here
        self.fields['parent'].queryset = Parent.objects.all()

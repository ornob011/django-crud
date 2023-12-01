from django.shortcuts import render, redirect, get_object_or_404
from .models import Parent, Child
from .forms import ParentForm, ChildForm

def home(request):
    """
    Display the home page with a list of all parents and their children.
    """
    parents = Parent.objects.prefetch_related('child_set').all()
    return render(request, 'home.html', {'parents': parents})

def list_parents(request):
    """
    Display a list of all parents.
    """
    parents = Parent.objects.all()
    return render(request, 'list_parents.html', {'parents': parents})

def list_children(request):
    """
    Display a list of all children.
    """
    children = Child.objects.all()
    return render(request, 'list_children.html', {'children': children})

def create_parent(request):
    """
    Create a new parent record.
    """
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_parents')
    else:
        form = ParentForm()
    return render(request, 'create_update_parent.html', {'form': form})

def update_parent(request, parent_id):
    """
    Update an existing parent record.
    """
    parent = get_object_or_404(Parent, id=parent_id)
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('list_parents')
    else:
        form = ParentForm(instance=parent)
    return render(request, 'create_update_parent.html', {'form': form, 'parent': parent})

def delete_parent(request, parent_id):
    """
    Delete an existing parent record.
    """
    parent = get_object_or_404(Parent, id=parent_id)
    parent.delete()
    return redirect('list_parents')

def create_child(request):
    """
    Create a new child record.
    """
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_children')
    else:
        form = ChildForm()
    return render(request, 'create_update_child.html', {'form': form})

def update_child(request, child_id):
    """
    Update an existing child record.
    """
    child = get_object_or_404(Child, id=child_id)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('list_children')
    else:
        form = ChildForm(instance=child)
    return render(request, 'create_update_child.html', {'form': form, 'child': child})

def delete_child(request, child_id):
    """
    Delete an existing child record.
    """
    child = get_object_or_404(Child, id=child_id)
    child.delete()
    return redirect('list_children')

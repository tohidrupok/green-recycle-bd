from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):

    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard')

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.is_staff:

                login(request, user)

                return redirect('dashboard')

            else:

                error = "Access Denied"

        else:

            error = "Invalid Username or Password"

    return render(
        request,
        "panel/login.html",
        {
            "error": error
        }
    )


@login_required(login_url='panel_login')


@login_required(login_url='panel_login')
def logout_view(request):

    logout(request)

    return redirect("panel_login")


from functools import wraps

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .registry import MODEL_REGISTRY


# ---------- access control ----------
def staff_required(view_func):
    """login_required + is_staff check, redirect to panel_login on failure."""
    @wraps(view_func)
    @login_required(login_url='panel_login')
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('panel_login')
        return view_func(request, *args, **kwargs)
    return wrapper


def get_registry_entry(model_name):
    entry = MODEL_REGISTRY.get(model_name)
    if not entry:
        raise Http404("Unknown model: %s" % model_name)
    return entry



# ---------- dashboard ----------
@staff_required
def dashboard(request):
    cards = [
        {'key': key, 'label': entry['label'], 'count': entry['model'].objects.count()}
        for key, entry in MODEL_REGISTRY.items()
    ]
    return render(request, 'panel/dashboard.html', {'cards': cards})

from django.template.loader import get_template
# ---------- generic CRUD ----------


@staff_required
def item_list(request, model_name):
    t = get_template("panel/item_list.html")
    print("Template origin:", t.origin)

    entry = get_registry_entry(model_name)
    Model = entry['model']

    qs = Model.objects.all()
    if hasattr(Model, 'order'):
        qs = qs.order_by('order')
    else:
        qs = qs.order_by('-id')

    return render(request, 'panel/item_list.html', {
        'items': qs,
        'model_name': model_name,
        'label': entry['label'],
        'list_fields': entry['list_fields'],
    })


@staff_required
def item_create(request, model_name):
    entry = get_registry_entry(model_name)
    Model = entry['model']
    Form = modelform_factory(Model, fields=entry['fields'])

    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{entry['label']} added.")
            return redirect('panel_item_list', model_name=model_name)
    else:
        form = Form()

    return render(request, 'panel/item_form.html', {
        'form': form,
        'model_name': model_name,
        'label': entry['label'],
        'action': 'Add',
    })


@staff_required
def item_update(request, model_name, pk):
    entry = get_registry_entry(model_name)
    Model = entry['model']
    obj = get_object_or_404(Model, pk=pk)
    Form = modelform_factory(Model, fields=entry['fields'])

    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f"{entry['label']} updated.")
            return redirect('panel_item_list', model_name=model_name)
    else:
        form = Form(instance=obj)

    return render(request, 'panel/item_form.html', {
        'form': form,
        'model_name': model_name,
        'label': entry['label'],
        'action': 'Edit',
        'object': obj,
    })


@staff_required
def item_delete(request, model_name, pk):
    entry = get_registry_entry(model_name)
    Model = entry['model']
    obj = get_object_or_404(Model, pk=pk)

    if request.method == 'POST':
        obj.delete()
        messages.success(request, f"{entry['label']} deleted.")
        return redirect('panel_item_list', model_name=model_name)

    return render(request, 'panel/item_confirm_delete.html', {
        'object': obj,
        'model_name': model_name,
        'label': entry['label'],
    })
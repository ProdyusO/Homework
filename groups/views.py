from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from faker import Faker

from groups.forms import GroupCreateForm, GroupUpdateForm
from groups.models import Group

from webargs import fields
from webargs.djangoparser import use_args, use_kwargs


fake = Faker()


@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=10
     )},
    location="query"
    )
def generate_students(request, count):
    fake = Faker()
    fake_n = []
    for i in range(count):
        fake_n.append(str(fake.name()).split())
        fake_n.append(fake.phone_number())
    s = Group(first_name=fake_n[0][0], last_name=fake_n[0][1], phone_number=fake_n[1])
    s.save()
    return HttpResponse(fake_n)


@use_args({
    "first_name": fields.Str(
        required=False
        ),
    "last_name": fields.Str(
        required=False
        ),
    "city": fields.Str(
        required=False
        ),
    "birthday": fields.Str(
        required=False
        ),
    "phone_number": fields.Str(
        required=False
        ),
    "email": fields.Str(
        required=False
        )},
    location="query"
        )
def get_groups(request, args):
    groups = Group.objects.all()
    for param_name, param_values in args.items():
        if param_values:
            groups = groups.filter(**{param_name: param_values})

    return render(
        request=request,
        template_name='groups/list.html',
        context={'groups': groups}
    )


def create_group(request):

    if request.method == 'GET':

        form = GroupCreateForm()

    elif request.method == 'POST':

        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):

    group = get_object_or_404(Group, id=pk)

    if request.method == 'GET':

        form = GroupUpdateForm(instance=group)

    elif request.method == 'POST':

        form = GroupUpdateForm(instance=group, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form}
    )


def delete_group(request, pk):

    groups = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        groups.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/delete.html',
        context={'groups': groups}
    )

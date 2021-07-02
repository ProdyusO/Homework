from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
    "first_name": fields.Str(
        required=False
        ),
    "last_name": fields.Str(
        required=False
        ),
    "phone_number": fields.Str(
        required=False
        ),
    "city": fields.Str(
        required=False
        )},
    location="query"
        )
def get_teachers(request, args):
    teachers = Teacher.objects.all()
    for param_name, param_values in args.items():
        if param_values:
            teachers = teachers.filter(**{param_name: param_values})

    obj_filter = TeacherFilter(data=request.GET, queryset=teachers)

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'teachers': teachers,
            'obj_filter': obj_filter,
        }
    )

def create_teacher(request):

    if request.method == 'GET':

        form = TeacherCreateForm()

    if request.method == 'POST':

        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )

def update_teacher(request, pk):

    teachers = get_object_or_404(Teacher, id=pk)

    if request.method == 'GET':

        form = TeacherUpdateForm(instance=teachers)

    elif request.method == 'POST':

        form = TeacherUpdateForm(instance=teachers, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )


def delete_teacher(request, pk):

    teachers = get_object_or_404(Teacher, id=pk)

    if request.method == 'POST':
        teachers.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/delete.html',
        context={'teachers': teachers}
    )
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from courses.forms import CourseCreateForm, CourseUpdateForm
from courses.models import Course


def get_course(request):
    course = Course.objects.all()

    return render(
        request=request,
        template_name='courses/list.html',
        context={'course': course}
    )

def create_course(request):

    if request.method == 'GET':

        form = CourseCreateForm()

    elif request.method == 'POST':

        form = CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/create.html',
        context={'form': form}
    )

def update_course(request, pk):

    course = get_object_or_404(Course, id=pk)

    if request.method == 'GET':

        form = CourseUpdateForm(instance=course)

    elif request.method == 'POST':

        form = CourseUpdateForm(instance=course, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/update.html',
        context={'form': form}
    )

def delete_course(request, pk):

    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/delete.html',
        context={'course': course}
    )
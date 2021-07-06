from courses.forms import CourseBaseForm, CourseCreateForm, CourseDeleteForm, CourseUpdateForm
from courses.models import Course
from django.http import HttpResponseRedirect # noqa

from django.shortcuts import get_object_or_404, render # noqa
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from django.urls import reverse, reverse_lazy # noqa


class CourseListView(ListView):
    model = Course
    form_class = CourseBaseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/list.html'

# def get_course(request):
#     course = Course.objects.all()
#
#     return render(
#         request=request,
#         template_name='courses/list.html',
#         context={'course': course}
#     )


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'

# def create_course(request):
#
#     if request.method == 'GET':
#
#         form = CourseCreateForm()
#
#     elif request.method == 'POST':
#
#         form = CourseCreateForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('courses:list'))
#
#     return render(
#         request=request,
#         template_name='courses/create.html',
#         context={'form': form}
#     )


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['course'] = self.get_object().form
# def update_course(request, pk):
#
#     course = get_object_or_404(Course, id=pk)
#
#     if request.method == 'GET':
#
#         form = CourseUpdateForm(instance=course)
#
#     elif request.method == 'POST':
#
#         form = CourseUpdateForm(instance=course, data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('courses:list'))
#
#     return render(
#         request=request,
#         template_name='courses/update.html',
#         context={'form': form}
#     )


class CourseDeleteView(DeleteView):
    model = Course
    form_class = CourseDeleteForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'

# def delete_course(request, pk):
#
#     course = get_object_or_404(Course, id=pk)
#
#     if request.method == 'POST':
#         course.delete()
#         return HttpResponseRedirect(reverse('courses:list'))
#
#     return render(
#         request=request,
#         template_name='courses/delete.html',
#         context={'course': course}
#     )

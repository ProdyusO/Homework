# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy  # noqa
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from teachers.forms import TeacherBaseForm, TeacherCreateForm, TeacherDeleteForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher

from copy import copy
# from webargs import fields
# from webargs.djangoparser import use_args


# @use_args({
#     "first_name": fields.Str(
#         required=False
#         ),
#     "last_name": fields.Str(
#         required=False
#         ),
#     "phone_number": fields.Str(
#         required=False
#         ),
#     "city": fields.Str(
#         required=False
#         )},
#     location="query"
#         )
# def get_teachers(request, args):
#     teachers = Teacher.objects.all()
#     # for param_name, param_values in args.items():
#     #     if param_values:
#     #         teachers = teachers.filter(**{param_name: param_values})
#
#     obj_filter = TeacherFilter(data=request.GET, queryset=teachers)
#
#     return render(
#         request=request,
#         template_name='teachers/list.html',
#         context={
#             'teachers': teachers,
#             'obj_filter': obj_filter,
#         }
#     )
#
# def create_teacher(request):
#
#     if request.method == 'GET':
#
#         form = TeacherCreateForm()
#
#     if request.method == 'POST':
#
#         form = TeacherCreateForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#
#     return render(
#         request=request,
#         template_name='teachers/create.html',
#         context={'form': form}
#     )
#
# def update_teacher(request, pk):
#
#     teachers = get_object_or_404(Teacher, id=pk)
#
#     if request.method == 'GET':
#
#         form = TeacherUpdateForm(instance=teachers)
#
#     elif request.method == 'POST':
#
#         form = TeacherUpdateForm(instance=teachers, data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#
#     return render(
#         request=request,
#         template_name='teachers/update.html',
#         context={'form': form}
#     )
#
#
# def delete_teacher(request, pk):
#
#     teachers = get_object_or_404(Teacher, id=pk)
#
#     if request.method == 'POST':
#         teachers.delete()
#         return HttpResponseRedirect(reverse('teachers:list'))
#
#     return render(
#         request=request,
#         template_name='teachers/delete.html',
#         context={'teachers': teachers}
#     )


class TeacherListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    model = Teacher
    form_class = TeacherBaseForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/list.html'

    def get_filter(self):
        return TeacherFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().order_by('id')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()
        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']
        context['get_params'] = params.urlencode()
        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    form_class = TeacherDeleteForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'

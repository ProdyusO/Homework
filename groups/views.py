from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect # noqa
from django.shortcuts import get_object_or_404, render # noqa
from django.urls import reverse, reverse_lazy # noqa
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from faker import Faker # noqa

from groups.forms import GroupBaseForm, GroupCreateForm, GroupDeleteForm, GroupUpdateForm, GroupsFilter
from groups.models import Group


from webargs import fields # noqa
from webargs.djangoparser import use_args, use_kwargs # noqa

from copy import copy
# fake = Faker()
#
#
# @use_kwargs({
#     "count": fields.Int(
#         required=False,
#         missing=10
#      )},
#     location="query"
#     )
# def generate_students(request, count):
#     fake = Faker()
#     fake_n = []
#     for i in range(count):
#         fake_n.append(str(fake.name()).split())
#         fake_n.append(fake.phone_number())
#     s = Group(first_name=fake_n[0][0], last_name=fake_n[0][1], phone_number=fake_n[1])
#     s.save()
#     return HttpResponse(fake_n)


# @use_args({
#     "first_name": fields.Str(
#         required=False
#         ),
#     "last_name": fields.Str(
#         required=False
#         ),
#     "city": fields.Str(
#         required=False
#         ),
#     "birthday": fields.Str(
#         required=False
#         ),
#     "phone_number": fields.Str(
#         required=False
#         ),
#     "email": fields.Str(
#         required=False
#         )},
#     location="query"
#         )


class GroupListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    model = Group
    form_class = GroupBaseForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/list.html'

    def get_filter(self):
        return GroupsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('number_course').order_by('id')
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


# def get_groups(request):
#     groups = Group.objects.all().select_related('teacher')
#     # for param_name, param_values in args.items():
#     #     if param_values:
#     #         groups = groups.filter(**{param_name: param_values})
#
#     obj_filter = GroupsFilter(data=request.GET, queryset=groups)
#
#     return render(
#         request=request,
#         template_name='groups/list.html',
#         context={
#             #'groups': groups,
#             'obj_filter': obj_filter,
#         }
#     )


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'A new student successfully added')

        return result

# def create_group(request):
#
#     if request.method == 'GET':
#
#         form = GroupCreateForm()
#
#     elif request.method == 'POST':
#
#         form = GroupCreateForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request=request,
#         template_name='groups/create.html',
#         context={'form': form}
#     )


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'


# def update_group(request, pk):
#
#     group = get_object_or_404(Group, id=pk)
#
#     if request.method == 'GET':
#
#         form = GroupUpdateForm(instance=group)
#
#     elif request.method == 'POST':
#
#         form = GroupUpdateForm(instance=group, data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request=request,
#         template_name='groups/update.html',
#         context={'form': form}
#     )


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    form_class = GroupDeleteForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'

# def delete_group(request, pk):
#
#     groups = get_object_or_404(Group, id=pk)
#
#     if request.method == 'POST':
#         groups.delete()
#         return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request=request,
#         template_name='groups/delete.html',
#         context={'groups': groups}
#     )

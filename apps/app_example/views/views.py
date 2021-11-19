from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView,
    DetailView, UpdateView,
    CreateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from app_example.models import Book
from app_example.forms import BookForms

class index_1(TemplateView):
    '''Class based view (just example)'''
    template_name = 'app_example/index.html'

    def get_context_data(self, **kwargs):
        context = super(index_1, self).get_context_data(**kwargs)
        context['page_title'] = 'Welcome'
        return context


class ObjectDetailView(DetailView):
    model = Book
    template_name = 'app_example/detail_object.html'

    def get_context_data(self, **kwargs):
        context = super(ObjectDetailView, self).get_context_data(**kwargs)
        context['page_title'] = 'Object Detail'
        return context


class ObjectsView(ListView):
    model = Book
    template_name = 'app_example/list_objects.html'

    def get_queryset(self):
        queryset = super(ObjectsView, self).get_queryset()
        queryset = queryset.filter(id__gte=2) # show only id > 2
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ObjectsView, self).get_context_data(**kwargs)
        context['page_title'] = 'Objects'
        ## a test to send message in any view
        # context['messages'] = [
        #     {
        #         'text': 'This is just some data',
        #         'tags': 'success',
        #     },
        # ]
        return context


class ObjectCreateView(SuccessMessageMixin, CreateView):
    model = Book
    # fields = ['title', 'genre', 'author']
    form_class = BookForms
    template_name = 'app_example/create_object.html'
    success_url = 'objects'
    success_message = 'Object created with success'

    def get_context_data(self, **kwargs):
        context = super(ObjectCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Object'
        return context


class ObjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = 'app_example/create_object.html'
    form_class = BookForms
    success_url = reverse_lazy('objects')
    success_message = 'Object updated with success'

    def get_context_data(self, **kwargs):
        context = super(ObjectUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Object'
        return context


class ObjectDeleteView(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = 'app_example/delete_object.html'
    success_url = reverse_lazy('objects')
    success_message = 'Object deleted with success'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(ObjectDeleteView, self).delete(request, *args, **kwargs)


def index_2(request):
    '''Function based view'''
    context = {
        'page_title': 'Welcome'
    }
    return render(request, 'app_example/index.html', context)
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = 'search/search-view.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        if query is None:
            query = ''
        context['query'] = query
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        print(query)
        if query is not None and query is not '':
            queryset = Product.objects.filter(title__icontains=query)
            print(queryset)
            return queryset
        else:
            return Product.objects.filter(featured=True)

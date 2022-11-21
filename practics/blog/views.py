from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def index(request):
    news = Articles.objects.order_by('-date')
    context = {'news': news}
    return render(request, 'blog/index.html', context)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'blog/details_news.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'blog/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'blog/delete_news.html'



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Form incorrect"
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)


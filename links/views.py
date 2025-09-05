from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from .forms import LinkForm

def index(request):
    links = Link.objects.all()
    context = {
        'links': links
    }
    return render(request, 'links/index.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.increment_clicks()   # <-- fixed method name
    return redirect(link.url)


def add_links(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('home')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = LinkForm()

    return render(request, 'links/create.html', {"form": form})


    
    
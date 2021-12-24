from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import AddProject, UpdateProject
from .models import Project, Category, Comment
from django.views.generic import UpdateView


# Create your views here.


def addproject(request):
    form = AddProject(request.POST or None, request.FILES or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.user = request.user
        project.save()
        return redirect('index')
    return render(request, 'addProject.html', {'form': form})


def all(request):
    projects = Project.objects.filter(available=True).order_by("-id")
    categories = Category.objects.all()
    query = request.GET.get('q')
    if query:
        projects = Project.objects.filter(name__icontains=query)

    return render(request, "projects.html", {"projects": projects, 'categories': categories})


def project_by_category(request, category_slug):
    projects = Project.objects.filter(
        category__slug=category_slug, available=True)

    return render(request, 'project_by_category.html', {'projects': projects})


def detail(request, id):
    project = get_object_or_404(Project, id=id)
    comments = project.comments.all()
    return render(request, 'detail.html', {'project': project, 'comments': comments})


def comment(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        name = request.user
        text = request.POST.get('comment_text')

        project = get_object_or_404(Project, id=id)
        newComment = Comment(comment_author=name, comment_text=text)
        newComment.project = project
        newComment.save()

    return redirect(reverse('detail', kwargs={'id': id}))


def delete(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()

    return redirect('profile')


class update(UpdateView):
    model = Project
    # fields = ['name', 'describtion', 'category', 'image']
    template_name = 'update.html'
    form_class = UpdateProject

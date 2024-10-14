from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import F
from .models import Project, BlogPost, Category
from .forms import ContactForm, ConsultationForm

def home(request):
    # Используем F() для добавления случайного значения к дате создания
    # Это заставит Django выполнять новый запрос каждый раз
    featured_projects = Project.objects.order_by(F('created_at').desc(nulls_last=True))[:4]
    consultation_form = ConsultationForm()
    return render(request, 'home.html', {
        'featured_projects': featured_projects,
        'consultation_form': consultation_form
    })

def about(request):
    consultation_form = ConsultationForm()
    return render(request, 'about.html', {'consultation_form': consultation_form})

class CatalogView(ListView):
    model = Project
    template_name = 'catalog.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['consultation_form'] = ConsultationForm()
        return context

def services(request):
    consultation_form = ConsultationForm()
    return render(request, 'services.html', {'consultation_form': consultation_form})

class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultation_form'] = ConsultationForm()
        return context

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultation_form'] = ConsultationForm()
        return context

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('contact')
    else:
        form = ContactForm()
    consultation_form = ConsultationForm()
    return render(request, 'contact.html', {'form': form, 'consultation_form': consultation_form})

def consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка на консультацию успешно отправлена!')
            return redirect('home')
    else:
        form = ConsultationForm()
    return render(request, 'consultation.html', {'form': form})
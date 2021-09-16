from django.http import request
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView,ListView
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect,HttpResponse,HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin
# Create your views here.
from django.views.generic.base import TemplateResponseMixin
from . models import  *
from django.db.models import Q
# from . forms import *
from django.template import RequestContext
from django.core.paginator import Paginator



from django.http import request
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView,ListView
from django.urls import reverse_lazy
# from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin
# Create your views here.
from . models import  *
from django.db.models import Q
from . forms import *
from django.template import RequestContext
from django.core.paginator import Paginator

class  IndexView(TemplateView):
    post_form_class = ContactusForm
    comment_form_class = ReviewsForm
    success_url = reverse_lazy("bourki:thanks")
    template_name="index.html"

    def post(self, request):
        post_data = request.POST or None
        post_form = self.post_form_class(post_data, prefix='post')
        comment_form = self.comment_form_class(post_data, prefix='comment')

        context = self.get_context_data(post_form=post_form,comment_form=comment_form)

        if post_form.is_valid():
            # url_slug = self.kwargs['slug']
            # product = Product.objects.get(slug=url_slug)
            # post_form.instance.product = product
            # post_form.save()
            self.form_save(post_form)
            
        if comment_form.is_valid():
            self.form_save(comment_form)
            return HttpResponseRedirect("/blogs/")
            # return HttpResponse("ddcsfdcfsd")

        return self.render_to_response(context)  
    
    
    def form_save(self, form):
        obj = form.save()
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
       
        
        context['reviews'] = Reviews.objects.all().order_by("-id")
        context['blogs'] = Blog.objects.all().filter().order_by('-id')[0:3]  
        # context['productes'] = Product.objects.all().order_by("-id")        
        # context['blogs'] = Blog.objects.all().filter().order_by('-id')[0:4]   
        # context['cat_blog'] = Categoryblog.objects.all().order_by("-id")
        # context['pro'] = Product.objects.all().filter().order_by('-id')[0:6]   
        # context['speciales'] = SpecialesOfrres.objects.all().order_by("-id")
        # context['specialelatest'] = SpecialesOfrres.objects.filter().order_by('-id')[0:4]   
        # context['allhotels'] =Hotels.objects.all().order_by("-id")    
        
        return context
    

# class  IndexView(CreateView):
#     template_name="index.html"
#     form_class = ContactusForm
#     success_url = reverse_lazy("bourki:thanks")
#     def form_valid(self, form):
#         form.save()
#         messages.add_message(
#             self.request,messages.SUCCESS,"thanks we will talk you"
#         )
#         return super().form_valid(form)  
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
       
        
    #     context['reviews'] = Reviews.objects.all().order_by("-id")
    #     context['blogs'] = Blog.objects.all().filter().order_by('-id')[0:3]  
    #     # context['productes'] = Product.objects.all().order_by("-id")        
    #     # context['blogs'] = Blog.objects.all().filter().order_by('-id')[0:4]   
    #     # context['cat_blog'] = Categoryblog.objects.all().order_by("-id")
    #     # context['pro'] = Product.objects.all().filter().order_by('-id')[0:6]   
    #     # context['speciales'] = SpecialesOfrres.objects.all().order_by("-id")
    #     # context['specialelatest'] = SpecialesOfrres.objects.filter().order_by('-id')[0:4]   
    #     # context['allhotels'] =Hotels.objects.all().order_by("-id")    
        
    #     return context
    
    
    
def error_404(request,exception):
    return render(request,'404.html')

def error_500(request):
    return render(request,'500.html')


class  Contactus(CreateView):
    template_name="contact.html"
    form_class = ContactusForm
    success_url = reverse_lazy("bourki:thanks")
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['allcategories'] = Category.objects.all().order_by("-id")
    #     context['cat_blog'] = Categoryblog.objects.all().order_by("-id")
    #     context['pro'] = Product.objects.all().filter().order_by('-id')[0:6]   
    #     return context
    def form_valid(self, form):
        return super().form_valid(form)        
    
    
    
    
    
class  thanks(TemplateView):
    template_name="thanks.html"
    
class  VediosView(TemplateView):
    template_name="vedio.html"
class  BlogsView(TemplateView):
    template_name="blog.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        context['blogs'] = Blog.objects.all().order_by("-id")
        context['cat_blog'] = Categoryblog.objects.all().order_by("-id")
        return context
    
class  PortfolioView(TemplateView):
    template_name="portfolio.html"
    
    
    
class  Projectdetail(TemplateView):
    template_name="projectdetail.html"
    
    
class  DlogdetailView(CreateView):
    model=Comment
    template_name="blogdetail.html"
    form_class = CommentForm
    success_url = reverse_lazy("bourki:thanks")
    def form_valid(self, form):
        url_slug = self.kwargs['slug']
        blog = Blog.objects.get(slug=url_slug)
        form.instance.blog = blog
        form.save()
        messages.add_message(
            self.request,messages.SUCCESS,"thanks we will talk you"
        )
        return super().form_valid(form)  
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        blog = Blog.objects.get(slug=url_slug)
        blog.view_count += 1
        blog.save()
        context['blog'] = blog
    

        context['reviews'] = Reviews.objects.all().order_by("-id")
        context['blogs'] = Blog.objects.all().filter().order_by('-id')[0:3]  
        return context
    

    
        
class  VediodetaildetailView(TemplateView):
    template_name="vediodetail.html"
    
    
class CatblogListView(ListView,FormView):
    template_name = 'category morocco travel blogs.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['allcategories'] = Category.objects.all().order_by("-id")
        context['cat_blog'] = Categoryblog.objects.all().order_by("-id")
        # context['pro'] = Product.objects.all().filter().order_by('-id')[0:6]   

        return context

    context_object_name = 'catlistblog'

    def get_queryset(self):
        content = {
            'cate': self.kwargs['categoryblog'],
            'blogs': Blog.objects.filter(category__title=self.kwargs['categoryblog'])            
                       
        }
        return content    
    

def AboutView(request):
    
    
    if request.method=="POST":
        if request.POST.get("name"):
            contact=Reviews()
            contact.name=request.POST.get("name")
            contact.email=request.POST.get("email")
            contact.text=request.POST.get("text")
   
            contact.save()
            return render(request,'about.html')
    else:
        return render(request,'about.html')    
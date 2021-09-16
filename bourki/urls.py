from django.urls import path
from .views import  *
from bourki import  views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


app_name="bourki"

urlpatterns = [
    path("",IndexView.as_view(),name="home"),  
    path("about/",AboutView,name="about"),
    path("contact/",Contactus.as_view(),name="contact"),
    path("thanks/",thanks.as_view(),name="thanks"),
    path("Projectdetail/",Projectdetail.as_view(),name="projectdetail"),
    path("vlogs/",VediosView.as_view(),name="vedio"),
    path("blogs/",BlogsView.as_view(),name="blogs"),
    path("portfolio/",PortfolioView.as_view(),name="portfolio"),
    path("blogdetail/<slug:slug>/",DlogdetailView.as_view(),name="blogdetail"),
    path("vlogdetaildetail/<slug:slug>/",VediodetaildetailView.as_view(),name="vlogdetaildetail"),
    
    # path("tours_detail/<slug:slug>/",DetailtoursView.as_view(),name="detailtours"),
    # path("test/",views.TestView,name='test'),
    # path("about/",AboutusView.as_view(),name='aboutus'),
    # path("contactus/",ContactView.as_view(),name='contactus'),
    # path("buildtour/", BuildtourtView.as_view(), name='buildtour'),
    # path("faq/",FaqView.as_view(),name="faqs"),
    # path("specialtourdetail/<slug:slug>/",Specialdetailview.as_view(),name='specialdetail'),
    # path("specialtours/",SpecialoffrsViews.as_view(),name="specilaoffre"),
    # path("blogdetail/<slug:slug>/",Blogdetail.as_view(),name="blogdetail"),
    # path("Thanks/",ThankstView.as_view(),name="Thanks"),
    # path("searchblog/",SearchblogView.as_view(),name="searchblog"),
    # path("search/",SearchView.as_view(),name="search"),
    # path("hoteldetail/<slug:slug>/", HoteldetailView.as_view(), name='hotelsdetail'),
    # path('category/<category>/', views.CatListView.as_view(), name='category'),
    # path("categoryblog/<categoryblog>/",CatblogListView.as_view(),name="categoryblog"),
    # path("hotels/",AllhotelsView.as_view(),name="allhotels"),
    # path("vlogs/",VlogsView.as_view(),name="vlogs"),


 ]#+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)




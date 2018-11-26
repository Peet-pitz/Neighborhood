from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'indexPage'),
    url('^hoodpost',views.hoodpost,name = 'hoodpost'),
    url('^hoodbusiness',views.hoodbusiness,name = 'hoodbusiness'),
    url('^hoodhood',views.hoodhood,name = 'hoodhood'),
    url('^hoodhealth',views.hoodhealth,name = 'hoodhealth'),
    url(r'^hodpolice$', views.hoodpolice, name='hoodpolice'),
    url(r'^profile/',views.profile,name = 'Profile'),
    url(r'^edit/profile',views.edit_profile,name = 'edit-profile'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^hood/(\d+)',views.hood,name ='hood'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^new/health$', views.new_health, name='new-health'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^search/', views.search, name='search'),
    url(r'^search-detail/(\d+)',views.search_details,name = 'search-detail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
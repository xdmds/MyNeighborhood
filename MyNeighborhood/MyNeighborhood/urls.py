from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyNeighborhood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/complaints/', views.complaints, name='complaints' ),
    url(r'^api/categories/', views.complaint_types, name='complaint_types')
)

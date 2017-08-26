"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from students.views.ratings import ratings_ajax_next_page
from django.conf.urls import url
from django.contrib import admin
from students.views import students, groups, journal, exams, ratings, contact_admin
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.journal import JournalView
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static

urlpatterns = [
	# Students urls
	url(r'^$', students.students_list, name='home'), 
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),
    
    # Groups urls
    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', groups.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),

    #Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    # Exams urls
    url(r'^exams/$', exams.exams_list, name='exams'),
    url(r'^exams/add/$', exams.exams_add, name='exams_add'),
    url(r'^exams/(?P<pid>\d+)/edit/$', exams.exams_edit, name='exams_edit'),
    url(r'^exams/(?P<pid>\d+)/delete/$', exams.exams_delete, name='exams_delete'),

    # Ratings urls
    url(r'^ratings/$', ratings.ratings_list, name='ratings'),
    url(r'^ratings/add/$', ratings.ratings_add, name='ratings_add'),
    url(r'ratings/next_page$', ratings.ratings_ajax_next_page, name ='ratings_next_page'),

	url(r'^admin/', admin.site.urls),

    # Contact admin Form
    url(r'^contact-admin/$', contact_admin.contact_admin, name = 'contact_admin'),
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

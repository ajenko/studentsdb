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
#from students.views.ratings import ratings_ajax_next_page
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.i18n import javascript_catalog
from students.views import students, groups, journal, exams, ratings, contact_admin
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.groups import GroupUpdateView, GroupDeleteView, GroupAddView
from students.views.exams import ExamUpdateView, ExamDeleteView
from students.views.ratings import RatingUpdateView, RatingDeleteView
from students.views.journal import JournalView
from students.util import choose_lang
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static
from django.views.generic.base import RedirectView, TemplateView

js_info_dict = {
    'packages': ('students', ), 
}   

urlpatterns = [
	# Students urls
	url(r'^$', students.students_list, name='home'), 
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),
    
    # Groups urls
    url(r'^groups/$', groups.groups_list, name='groups'),
   # url(r'^groups/add/$', groups.groups_add, name='groups_add'),
   url(r'^groups/add/$', GroupAddView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),

    #Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    # Exams urls
    url(r'^exams/$', exams.exams_list, name='exams'),
    url(r'^exams/add/$', exams.exams_add, name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$', ExamUpdateView.as_view(), name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$', ExamDeleteView.as_view(), name='exams_delete'),

    # Ratings urls
    url(r'^ratings/$', ratings.ratings_list, name='ratings'),
    url(r'^ratings/add/$', ratings.ratings_add, name='ratings_add'),
    url(r'^ratings/(?P<pk>\d+)/edit/$', RatingUpdateView.as_view(), name='ratings_edit'),
    url(r'^ratings/(?P<pk>\d+)/delete/$', RatingDeleteView.as_view(), name='ratings_delete'),
   # url(r'ratings/next_page$', ratings.ratings_ajax_next_page, name ='ratings_next_page'),

	url(r'^admin/', admin.site.urls),

    # Contact admin Form
    url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),

    # javascript
    url(r'^jsi18n\.js$', javascript_catalog, js_info_dict, name='javascript_catalog'),

    # Choose Lang 
    url(r'^choose-lang-cookie-name/$', choose_lang, name='choose_lang'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # User Releted urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

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

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.i18n import javascript_catalog
from django.conf.urls.static import static
from django.views.generic.base import RedirectView, TemplateView


from students.views import students, groups, journal, exams, ratings, contact_admin
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.groups import GroupUpdateView, GroupDeleteView, GroupAddView
from students.views.exams import ExamUpdateView, ExamDeleteView
from students.views.ratings import RatingUpdateView, RatingDeleteView
from students.views.journal import JournalView
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG


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
    url(r'^groups/$', login_required(groups.groups_list), name='groups'),
    url(r'^groups/(?P<pk>\d+)/edit/$', login_required(GroupUpdateView.as_view()), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()), name='groups_delete'),

    # Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    # Exams urls
    url(r'^exams/$', login_required(exams.exams_list), name='exams'),
    url(r'^exams/add/$', login_required(exams.exams_add), name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$', login_required(ExamUpdateView.as_view()), name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$', login_required(ExamDeleteView.as_view()), name='exams_delete'),

    # Ratings urls
    url(r'^ratings/$', login_required(ratings.ratings_list), name='ratings'),
    url(r'^ratings/add/$', login_required(ratings.ratings_add), name='ratings_add'),
    url(r'^ratings/(?P<pk>\d+)/edit/$', login_required(RatingUpdateView.as_view()), name='ratings_edit'),
    url(r'^ratings/(?P<pk>\d+)/delete/$', login_required(RatingDeleteView.as_view()), name='ratings_delete'),
    # url(r'ratings/next_page$', ratings.ratings_ajax_next_page, name ='ratings_next_page'),
    url(r'^admin/', admin.site.urls),

    # Contact admin Form
    url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),

    # javascript
    url(r'^jsi18n\.js$', javascript_catalog, js_info_dict, name='javascript_catalog'),

    # Choose Lang 
    # url(r'^set_language/(?P<user_language>\w+)/$', choose_lang, name='choose_lang'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # User Releted urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

    # Social Auth Releted urls
    url('^social/', include('social_django.urls', namespace='social'))
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

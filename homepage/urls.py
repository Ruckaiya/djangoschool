from django.urls import path
from . import views
app_name="homepage"

urlpatterns = [
    path('', views.index.as_view(), name="homepage"),
    path('pages/submenu-1', views.submenu_1.as_view(), name="submenu-1"),
    path('pages/submenu-2', views.submenu_2.as_view(), name="submenu-2"),
    path('pages/submenu-3', views.submenu_3.as_view(), name="submenu-3"),
    path('pages/submenu-4', views.submenu_4.as_view(), name="submenu-4"),
    path('pages/submenu-5', views.submenu_5.as_view(), name="submenu-5"),
    path('pages/submenu-6', views.submenu_6.as_view(), name="submenu-6"),
    path('pages/submenu-7', views.submenu_7.as_view(), name="submenu-7"),
    path('pages/submenu-8', views.submenu_8.as_view(), name="submenu-8"),
    path('pages/management', views.management.as_view(), name="management"),
    path('pages/faculty', views.faculty.as_view(), name="faculty"),
    path('pages/non-faculty', views.non_faculty.as_view(), name="non_faculty"),
    path('pages/calender', views.caldr.as_view(), name='caldr'),
    path('pages/timetable&syllabus', views.t_s.as_view(), name='t_s'),
    path('pages/notice&events', views.n_e.as_view(), name='n_e'),
    path('pages/dresscode', views.d_c.as_view(), name='d_c'),
    path('pages/exam_rules', views.e_r.as_view(), name='e_r'),
    path('pages/gallery', views.gallery.as_view(), name="gallery"),
    path('pages/contact', views.contact.as_view(), name="contact"),
    
    path('pages/admin', views.admin.as_view(), name="admin"),



   
]
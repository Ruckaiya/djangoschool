
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.views import View
from .models import Calender
from django.core.files.storage import FileSystemStorage


# Create your views here.
class index(View):
    homepage = "homepage/index.html"
    def get(self, request):
        
        return render(request, self.homepage)

class submenu_1(View):
    template_name = "homepage/pages/submenu-1.html"
    def get(self, request):
        return render(request, self.template_name)


class submenu_2(View):
    template_name = "homepage/pages/submenu-2.html"
    def get(self, request):
        return render(request, self.template_name)

class submenu_3(View):
    template_name = "homepage/pages/submenu-3.html"
    def get(self, request):
        return render(request, self.template_name)

class submenu_4(View):
    template_name = "homepage/pages/submenu-4.html"
    def get(self, request):
        return render(request, self.template_name)

class submenu_5(View):
    template_name = "homepage/pages/submenu-5.html"
    def get(self, request):
        return render(request, self.template_name)

class submenu_6(View):
    template_name = "homepage/pages/submenu-6.html"
    def get(self, request):
        return render(request, self.template_name)

class submenu_7(View):
    template_name = "homepage/pages/submenu-7.html"
    def get(self, request):
        return render(request, self.template_name)

class submenu_8(View):
    template_name = "homepage/pages/submenu-8.html"
    def get(self, request):
        return render(request, self.template_name)

class management(View):
    template_name = "homepage/pages/management.html"
    def get(self, request):
        return render(request, self.template_name)

class faculty(View):
    template_name = "homepage/pages/faculty.html"
    def get(self, request):
        return render(request, self.template_name)

class non_faculty(View):
    template_name = "homepage/pages/non-faculty.html"
    def get(self, request):
        return render(request, self.template_name)

class caldr(View):
    template_name = "homepage/pages/calender.html"
    def get(self, request):
        return render(request, self.template_name)

class t_s(View):
    template_name = "homepage/pages/timetable_syllabus.html"
    def get(self, request):
        return render(request, self.template_name)

class n_e(View):
    template_name = "homepage/pages/notice_events.html"
    def get(self, request):
        return render(request, self.template_name)

class d_c(View):
    template_name = "homepage/pages/dresscode.html"
    def get(self, request):
        return render(request, self.template_name)

class e_r(View):
    template_name = "homepage/pages/examrules.html"
    def get(self, request):
        return render(request, self.template_name)

class gallery(View):
    template_name = "homepage/pages/gallery.html"
    def get(self, request):
        return render(request, self.template_name)

class contact(View):
    template_name = "homepage/pages/contact.html"
    def get(self, request):
        return render(request, self.template_name)


class admin(View):
    template_name = "homepage/pages/admin.html"
    def get(self, request):
        return render(request, self.template_name)



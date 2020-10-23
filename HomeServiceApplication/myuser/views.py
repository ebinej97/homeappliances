from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import UserRegistrationFrm,LoginFrm
# Create your views here.




class RegistrationView(TemplateView):
    model=User
    form_class=UserRegistrationFrm()
    template_name = "myuser/registration.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context['form']=self.form_class
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=UserRegistrationFrm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class LoginView(TemplateView):
    model=User
    template_name = "myuser/userlogin.html"
    form_class=LoginFrm()
    context={}
    def get(self, request, *args, **kwargs):
        self.context['form']=self.form_class
        return render(request,self.template_name,self.context)

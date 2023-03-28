from django.shortcuts import render
from AppPesca.models import Pesca, Profile
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "AppPesca/index.html")

def about(request):
    return render(request, "AppPesca/about.html")


class PescaList(ListView):
    model = Pesca
    context_object_name = "pescados"

class PescaMineList(LoginRequiredMixin, PescaList):
    
    def get_queryset(self):
        return Pesca.objects.filter(propietario=self.request.user.id).all()


class PescaDetail(DetailView):
    model = Pesca
    context_object_name = "pescado"


class PescaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pesca
    success_url = reverse_lazy("pescado-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        pescado_id =  self.kwargs.get("pk")
        return Pesca.objects.filter(propietario=user_id, id=pescado_id).exists()


class PescaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pesca
    context_object_name = "pescado"
    success_url = reverse_lazy("pescado-list")

    def test_func(self):
        user_id = self.request.user.id
        pescado_id =  self.kwargs.get("pk")
        return Pesca.objects.filter(propietario=user_id, id=pescado_id).exists()


class PescaCreate(LoginRequiredMixin, CreateView):
    model = Pesca
    success_url = reverse_lazy("pescado-list")
    fields = '__all__'


class PescaSearch(ListView):
    model = Pesca
    context_object_name = "pescados"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Pesca.objects.filter(nombre=criterio).all()
        return result

class Login(LoginView):
    next_page = reverse_lazy("pescado-list")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('pescado-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"


class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy('pescado-list')
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProfileUpdate(UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy ('pescado-list')
    fields = ['avatar']

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()




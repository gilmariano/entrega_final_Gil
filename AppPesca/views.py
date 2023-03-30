from django.db.models import Q
from django.shortcuts import render
from AppPesca.models import Pesca, Profile, Mensaje
from AppPesca.forms import PostForm, SearchForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor'] = self.object.propietario.username
        return context


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
    success_url = reverse_lazy("pescado-mine")
    fields = ['nombre', 'detalle', 'peso', 'imagen']

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        form.instance.autor = self.request.user.username
        return super().form_valid(form)



class PescaSearch(ListView):
    model = Pesca
    context_object_name = "pescados"
    template_name = "pesca_search.html"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        if criterio:
            result = Pesca.objects.filter(
                Q(nombre__icontains=criterio) |
                Q(detalle__icontains=criterio) |
                Q(peso__icontains=criterio) |
                Q(propietario__username__icontains=criterio)
            )
        else:
            result = []
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

class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()
    
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'pescados'

    def get_queryset(self):
        return Pesca.objects.order_by('-creado_el').all()[:2]



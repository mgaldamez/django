from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin,generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin,generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form) 

class CategoriaDelete(LoginRequiredMixin,generic.DeleteView):
    model = Categoria
    template_name = "inv/catalogo_del.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'

#SubCategoria

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class SubCategoriaNew(LoginRequiredMixin,generic.CreateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class= SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin,generic.UpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form) 

class SubCategoriaDelete(LoginRequiredMixin,generic.DeleteView):
    model = SubCategoria
    template_name = "inv/subcategoria_del.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = 'bases:login'

#Marca

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class MarcaNew(LoginRequiredMixin,generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin,generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form) 

#Vista basada en funciones
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/marca_inactivar.html"

    if not marca:
        return redirect("inv:marca_list")
    
    if request.method == 'GET':
        contexto = {'obj':marca}
    
    if request.method == 'POST':
        if marca.estado == True:
            marca.estado = False
            messages.success(request, 'Marca Inactivada.')
            
        else:
            marca.estado = True
            messages.success(request, 'Marca Reactivada.')
        marca.save()
        return redirect("inv:marca_list")

    return render(request,template_name, contexto)

#Unidades de Medida

class UMView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class UMNew(LoginRequiredMixin,generic.CreateView):
    model = Marca
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class=UMForm
    success_url = reverse_lazy("inv:um_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class UMEdit(LoginRequiredMixin,generic.UpdateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class=UMForm
    success_url = reverse_lazy("inv:um_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/um_inactivar.html"

    if not um:
        return redirect("inv:um_list")
    
    if request.method == 'GET':
        contexto = {'obj':um}
    
    if request.method == 'POST':
        if um.estado == True:
            um.estado = False
        else:
            um.estado = True
        um.save()
        return redirect("inv:um_list")

    return render(request,template_name, contexto)

#Producto

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = 'bases:login'

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin,
                   generic.UpdateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/producto_inactivar.html"

    if not prod:
        return redirect("inv:producto_list")
    
    if request.method=='GET':
        contexto={'obj':prod}
    
    if request.method=='POST':
        if prod.estado == True:
            prod.estado = False
        else:
            prod.estado = True
        prod.save()
        return redirect("inv:producto_list")

    return render(request,template_name,contexto)
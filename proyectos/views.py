from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile, Proyecto # Importa el modelo UserProfile
from .forms import CreateForm


def index(request):
    if request.method == 'GET':
        if 'logout' in request.GET:
            logout(request)
            return redirect('index')
        else:
            proyectos = Proyecto.objects.all()  # Obtener todos los proyectos
            return render(request, 'index.html', {'proyectos': proyectos})
    else:
        if 'register-password' in request.POST:
            if request.POST['register-password'] == request.POST['register-password2']:
                try:
                    user = User.objects.create_user(username=request.POST['register-name'], email=request.POST['register-email'],
                                                    password=request.POST['register-password'])
                    user.save()
                    # Verificar si la casilla "¿Eres profesor?" está marcada
                    es_profesor = request.POST.get('is-professor', False) == 'on'
                    # Crear UserProfile con la información del usuario y si es profesor o no
                    profile=UserProfile.objects.create(user=user, es_profesor=es_profesor)
                    login(request, user)
                    messages.success(request, 'Usuario creado correctamente')
                    return redirect('index')
                except:
                    messages.error(request, 'El usuario ya existe')
            else:
                messages.error(request, 'Las contraseñas no coinciden')
            return redirect('index')

        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('index')
            else:
                messages.error(request, 'Credenciales inválidas')
                return redirect('index')


def crearProyectos(request):
    return render(request, 'CrearProyectos.html',{
        'form': CreateForm
    })
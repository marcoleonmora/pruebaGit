from django.shortcuts import render, redirect
from .models import Account
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# ************************************************************

def registrarse(request):
    context ={}
    if request.method == 'POST':
        rol = request.POST['rol']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        username = request.POST['username']
        email = request.POST['correo']

        # VALIDACION DE CAMPOS
        ok = True
        if not email:
            context['alarma'] = 'Ingrese el correo electrónico'
            ok = False
        if not password or len(password) < 5:
            context['alarma'] = 'Ingrese un password de cinco (5) o mas caracteres'
            ok = False
        if password != confirmPassword:
            context['alarma'] = '¡El password no coincide!'
            ok = False

        #Todo OK
        if ok:
            existe = Account.objects.filter(email=email).exists()
            if not existe:
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.rol = rol
                user.save()
                context['mensaje'] = 'Usuario guardado con exito!'
            else:
                context['alarma'] = '¡El correo ya existe!'

    return render(request, 'usuarios/registro.html', context)

    
#******** CONTROL DE INGRESO DE USUARIOS  ***********************************************************
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email= email, password = password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'usuarios/login.html', {'alarma': 'Correo o password no valido!'})

    else:
        return render(request, 'usuarios/login.html')


#********* DESACTIVACION DEL USUARIO **********************************************************
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
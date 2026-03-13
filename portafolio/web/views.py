from django.shortcuts import render

def inicio(request):
    return render(request, 'web/inicio.html')

def paisajes(request):
    return render(request, 'web/paisajes.html')

def viajes(request):
    return render(request, 'web/viajes.html')

def retratos(request):
    return render(request, 'web/retratos.html')

def vida_silvestre(request):
    return render(request, 'web/vida_silvestre.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        print(nombre, email, mensaje)  # Aquí va el codigo para enviar correo o guardar en base de datos
        context = {'mensaje_enviado': True}
    else:
        context = {}
    return render(request, 'web/contacto.html', context)
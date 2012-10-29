# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from app1.models import Equipo
import datetime
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
def home(request):
    fechaActual=datetime.datetime.now()
    fechaFinal=datetime.datetime(2012,11,12,14,00,00)
    diferencia=fechaFinal-fechaActual
    dias=diferencia.days
    horas=diferencia.seconds/3600
    minutos=(diferencia.seconds/60)%60
    segundos=diferencia.seconds-(horas*3600+minutos*60)
    fechaRestante=str(dias)+':'+str(horas)+':'+str(minutos)+':'+str(segundos)
    print "fecha: "
    print fechaRestante
    return render_to_response('home.html',{'hora':fechaRestante}, context_instance=RequestContext(request))

def registrarse(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        nombre1 = request.POST.get('nombre1')
        nombre2 = request.POST.get('nombre2')
        nombre3 = request.POST.get('nombre3')
        nombre4 = request.POST.get('nombre4')
        nombre5 = request.POST.get('nombre5')
        email = request.POST.get('email')
        #path = default_storage.save(nombre, request.FILES.get('avatar'))
        e=Equipo.objects.all()
        band=True
        for i in e:
            if nombre==i.Nombre:
                band=False
                break
        if band:
            equipo = Equipo.objects.create(Nombre=nombre,Integrante1=nombre1,Integrante2=nombre2,Integrante3=nombre3,Integrante4=nombre4,Integrante5=nombre5,email=email)
            equipo.save()
            e = Equipo.objects.all()
            return render_to_response('equipos.html',{'registrado':True,'equipos':e}, context_instance=RequestContext(request))
        else:
            return render_to_response('registro.html',{'errorRegistro':True}, context_instance=RequestContext(request))
    else:
        return render_to_response('registro.html', context_instance=RequestContext(request))

def equipos(request):
    e = Equipo.objects.all()
    return render_to_response('equipos.html',{'equipos':e}, context_instance=RequestContext(request))

def basesConcurso(request):
    fechaActual=datetime.datetime.now()
    fechaFinal=datetime.datetime(2012,11,12,14,00,00)
    diferencia=fechaFinal-fechaActual
    dias=diferencia.days
    horas=diferencia.seconds/3600
    minutos=(diferencia.seconds/60)%60
    segundos=diferencia.seconds-(horas*3600+minutos*60)
    fechaRestante=str(dias)+':'+str(horas)+':'+str(minutos)+':'+str(segundos)
    return render_to_response('basesConsurso.html',{'hora':fechaRestante},context_instance=RequestContext(request))
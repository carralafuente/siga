import csv , io
from django.shortcuts import render, redirect
from .models import Upload
from django.http import HttpResponse


def UploadFile(request):
#Carga de un archivo csv con las columnas designadas en el modelo previamente
    if request.method == 'GET':
        return render(request, 'upload_app/upload_carga.html')
    #Si el método es POST se ejecuta el siguiente código
    csv_file = request.FILES['a']#El archivo que viene del input del template

    data_set = csv_file.read().decode('latin-1')#Variable que ejecuta la función de lectura del csv
    io_string = io.StringIO(data_set)#Convertimos el data set de byte a string
    next(io_string)#Salta los headers del csv
    for column in csv.reader(io_string, delimiter = ','):#Iteramos sobre las columnas con delimitador de comas
        _, created = Upload.objects.update_or_create(
            fecha=column[0],
            serie=column[1],
            folio=column[2],
            cliente=column[3],
            razonsocial=column[4],
            rfc=column[5],
            estado=column[6],
            neto=column[7],
            descuentos=column[8],
            impuestos=column[9],
            total=column[10],
        )
    context = {}

    return render(request, 'upload_app/upload_list.html', context)

def UploadCrear(request):
#Crea un registro nuevo en el modelo
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(fichero_listar)
    else:
        form = UploadForm()
    return render(request, 'upload_app/upload_form.html', {'form':form})

def UploadList(request):
#Genera una vista del modelo en un template
    upload = Upload.objects.all().order_by('folio')
    contexto = {'Uploads':upload}
    return render(request, 'upload_app/upload_list.html', contexto)

def UploadEdit(request, id_upload):
#Update de una instancia concreta del modelo
    upload = Upload.objects.get(id=id_upload)
    if request.method=='GET':
        form = UploadForm(instance=upload)#Carga la instancia en una variable llamada form
    else:
        form = UploadForm(request.POST, instance=upload)#Modifica la instancia y la almacena en una variable que se pasa luego como contexto
        if form.is_valid():
            form.save()
        return redirect('fichero_listar')
    return render(request, 'upload_app/upload_form.html', {'form':form})

def UploadDelete(request,id_upload):
#Borra una instancia del objeto
    upload = Upload.objects.get(id=id_upload)
    if request.method =='POST':
        upload.delete()
        return redirect('fichero_listar')
    return render(request, 'upload_app/upload_delete.html', {'upload':upload})
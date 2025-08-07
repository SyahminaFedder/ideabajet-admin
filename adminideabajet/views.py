from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Admin, Elemen1, Lokasi, Elemen2, Elemen3, Elemen4, Elemen5, Elemen6, Elemen7, Elemen8, Aset
# Create your views here.

def login(request):
    if request.method == 'POST':
        adminid = request.POST.get('id')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(adminid=adminid, password=password)
            request.session['id'] = admin.adminid  # simpan dalam session
            request.session['message'] = 'Login berjaya!'
            return redirect('unified_view')  # redirect to main dashboard
        except Admin.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid Admin ID or Password',})
    return render (request,"login.html")

def unified_view(request):
    """Unified view that handles all sections in one template"""

    if request.method == 'POST':
        # Handle form submissions for different sections
        if 'aset' in request.POST:
            listaset = request.POST.get('aset')
            if listaset:
                Aset.objects.create(aset=listaset)
        elif 'list_lokasi' in request.POST:
            listloc = request.POST.get('list_lokasi')
            if listloc:
                Lokasi.objects.create(list_lokasi=listloc)
        elif 'e1' in request.POST:
            liste1 = request.POST.get('e1')
            if liste1:
                Elemen1.objects.create(e1=liste1)
        elif 'e2' in request.POST:
            liste2 = request.POST.get('e2')
            if liste2:
                Elemen2.objects.create(e2=liste2)
        elif 'e3' in request.POST:
            liste3 = request.POST.get('e3')
            if liste3:
                Elemen3.objects.create(e3=liste3)
        elif 'e4' in request.POST:
            liste4 = request.POST.get('e4')
            if liste4:
                Elemen4.objects.create(e4=liste4)
        elif 'e5' in request.POST:
            liste5 = request.POST.get('e5')
            if liste5:
                Elemen5.objects.create(e5=liste5)
        elif 'e6' in request.POST:
            liste6 = request.POST.get('e6')
            if liste6:
                Elemen6.objects.create(e6=liste6)
        elif 'e7' in request.POST:
            liste7 = request.POST.get('e7')
            if liste7:
                Elemen7.objects.create(e7=liste7)
        elif 'e8' in request.POST:
            liste8 = request.POST.get('e8')
            if liste8:
                Elemen8.objects.create(e8=liste8)

        return redirect('unified_view')

    
    message = request.session.pop('message', None)

    # Gather all data
    context = {
        'aset_data': Aset.objects.all(),
        'lokasi_data': Lokasi.objects.all(),
        'e1_data': Elemen1.objects.all(),
        'e2_data': Elemen2.objects.all(),
        'e3_data': Elemen3.objects.all(),
        'e4_data': Elemen4.objects.all(),
        'e5_data': Elemen5.objects.all(),
        'e6_data': Elemen6.objects.all(),
        'e7_data': Elemen7.objects.all(),
        'e8_data': Elemen8.objects.all(),
        'message': message,
    }

    return render(request, 'main.html', context)


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return redirect('login')

# Edit views
def edit_aset(request, asetid):
    if request.method == 'POST':
        aset = Aset.objects.get(asetid=asetid)
        aset.aset = request.POST.get('aset')
        aset.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_lokasi(request, lid):
    if request.method == 'POST':
        lokasi = Lokasi.objects.get(lid=lid)
        lokasi.list_lokasi = request.POST.get('list_lokasi')
        lokasi.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e1(request, e1id):
    if request.method == 'POST':
        e1 = Elemen1.objects.get(e1id=e1id)
        e1.e1 = request.POST.get('e1')
        e1.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e2(request, e2id):
    if request.method == 'POST':
        e2 = Elemen2.objects.get(e2id=e2id)
        e2.e2 = request.POST.get('e2')
        e2.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e3(request, e3id):
    if request.method == 'POST':
        e3 = Elemen3.objects.get(e3id=e3id)
        e3.e3 = request.POST.get('e3')
        e3.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e4(request, e4id):
    if request.method == 'POST':
        e4 = Elemen4.objects.get(e4id=e4id)
        e4.e4 = request.POST.get('e4')
        e4.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e5(request, e5id):
    if request.method == 'POST':
        e5 = Elemen5.objects.get(e5id=e5id)
        e5.e5 = request.POST.get('e5')
        e5.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e6(request, e6id):
    if request.method == 'POST':
        e6 = Elemen6.objects.get(e6id=e6id)
        e6.e6 = request.POST.get('e6')
        e6.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e7(request, e7id):
    if request.method == 'POST':
        e7 = Elemen7.objects.get(e7id=e7id)
        e7.e7 = request.POST.get('e7')
        e7.save()
        return redirect('unified_view')
    return redirect('unified_view')

def edit_e8(request, e8id):
    if request.method == 'POST':
        e8 = Elemen8.objects.get(e8id=e8id)
        e8.e8 = request.POST.get('e8')
        e8.save()
        return redirect('unified_view')
    return redirect('unified_view')

# Delete views
def delete_aset(request, asetid):
    if request.method == 'POST':
        aset = Aset.objects.get(asetid=asetid)
        aset.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_lokasi(request, lid):
    if request.method == 'POST':
        lokasi = Lokasi.objects.get(lid=lid)
        lokasi.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e1(request, e1id):
    if request.method == 'POST':
        e1 = Elemen1.objects.get(e1id=e1id)
        e1.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e2(request, e2id):
    if request.method == 'POST':
        e2 = Elemen2.objects.get(e2id=e2id)
        e2.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e3(request, e3id):
    if request.method == 'POST':
        e3 = Elemen3.objects.get(e3id=e3id)
        e3.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e4(request, e4id):
    if request.method == 'POST':
        e4 = Elemen4.objects.get(e4id=e4id)
        e4.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e5(request, e5id):
    if request.method == 'POST':
        e5 = Elemen5.objects.get(e5id=e5id)
        e5.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e6(request, e6id):
    if request.method == 'POST':
        e6 = Elemen6.objects.get(e6id=e6id)
        e6.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e7(request, e7id):
    if request.method == 'POST':
        e7 = Elemen7.objects.get(e7id=e7id)
        e7.delete()
        return redirect('unified_view')
    return redirect('unified_view')

def delete_e8(request, e8id):
    if request.method == 'POST':
        e8 = Elemen8.objects.get(e8id=e8id)
        e8.delete()
        return redirect('unified_view')
    return redirect('unified_view')  
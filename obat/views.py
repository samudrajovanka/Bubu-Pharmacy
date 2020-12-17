from django.shortcuts import redirect, render
from django.contrib import messages
import pyodbc
from django.utils.safestring import mark_safe
import datetime
import modules as database
    
def index(request):
    records = database.getData('OBAT')
    
    if request.method == 'POST':
        column = request.POST['column']
        valueFilter = '-'.join(request.POST['value-filter'].split())
        
        return redirect('obat:filter', column, valueFilter)
    
    context = {
        'title': 'Obat',
        'obatActive': 'active',
        'records': records,
        'hide': 'hide',
        'isEmpty': True if len(records) == 0 else False,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'obat/index.html', context)

def filterData(request, **query):
    column = query['column']
    
    if column == 'tgl_produksi' or column == 'tgl_kadaluarsa':
        valueFilter = query['value'].strip()
    else:
        valueFilter = ' '.join(query['value'].strip().split('-'))
    
    records = database.filterData('OBAT', column, valueFilter)
    
    if request.method == 'POST':
        column = request.POST['column']
        valueFilter = '-'.join(request.POST['value-filter'].split())
        
        return redirect('filter', column, valueFilter)
    
    context = {
        'title': 'Obat',
        'obatActive': 'active',
        'records': records,
        'column': ' '.join(column.split('_')),
        'valueFilter': valueFilter,
        'isEmpty': True if len(records) == 0 else False,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'obat/index.html', context)

def edit(request, **query):
    if 'admin' not in request.session:
        return redirect('index')
    
    kodeObat = query['kode_obat']
    
    record = database.filterData('OBAT', 'kode_obat', kodeObat)[0]
    
    if request.method == 'POST':
        hargaSatuan = request.POST['harga_satuan']
        hostName = database.getHostName()
        database.updateData('OBAT', 'harga_satuan', hargaSatuan, 'kode_obat', kodeObat)
        messages.success(request, mark_safe(f'''
                                            Data Obat berhasil di <b>Update</b><br>
                                            <b>Dimodifikasi</b> : {datetime.datetime.now().strftime('%b %d %Y %H:%M%p')}<br>
                                            <b>Nama Host</b> : {hostName}
                                            '''))
        
        return redirect('obat:index')
    
    context = {
        'title': 'Obat - Edit',
        'obatActive': 'active',
        'record': record,
        'kodeObat': kodeObat,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'obat/edit.html', context)
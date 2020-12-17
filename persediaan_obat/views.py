from django.shortcuts import redirect, render
import pyodbc
import modules as database

def index(request):
    records = database.getData('PERSEDIAAN')
    
    if request.method == 'POST':
        column = request.POST['column']
        valueFilter = '-'.join(request.POST['value-filter'].split())
        
        return redirect('persediaan:filter', column, valueFilter)
    
    context = {
        'title': 'Persediaan Obat',
        'persediaanActive': 'active',
        'records': records,
        'hide': 'hide',
        'isEmpty': True if len(records) == 0 else False,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'persediaan/index.html', context)

def filterData(request, **query):
    if request.method == 'POST':
        column = request.POST['column']
        valueFilter = '-'.join(request.POST['value-filter'].split())
        
        return redirect('persediaan:filter', column, valueFilter)
    
    column = query['column']    
    valueFilter = ' '.join(query['value'].split('-'))
    
    isValid = True
    isEmpty = True
    if column == 'jumlah_sedia' and not valueFilter.isnumeric():
        isValid = False
    
    records = []
    if isValid:
        records = database.filterData('PERSEDIAAN', column, valueFilter)
        isEmpty = True if len(records) == 0 else False
    
    context = {
        'title': 'Persediaan Obat',
        'persediaanActive': 'active',
        'records': records,
        'column': ' '.join(column.split('_')),
        'valueFilter': valueFilter,
        'isEmpty': isEmpty,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'persediaan/index.html', context)

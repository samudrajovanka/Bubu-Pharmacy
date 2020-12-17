from django.shortcuts import render, redirect
import pyodbc
import modules as database
    
def index(request):    
    records = database.dashboard()

    if request.method == 'POST':
        column = request.POST['column']
        valueFilter = '-'.join(request.POST['value-filter'].split())
        
        return redirect('filter', column, valueFilter)
    
    context = {
        'title': 'Dashboard',
        'dashboardActive': 'active',
        'records': records,
        'hide': 'hide',
        'isEmpty': True if len(records) == 0 else False,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'base.html', context)

def filterData(request, **query):
    column = query['column']
    
    nameTable = 'O' if column != 'jumlah_sedia' else 'P'
    if column == 'tgl_produksi' or column == 'tgl_kadaluarsa':
        valueFilter = query['value'].strip()
    else:
        valueFilter = ' '.join(query['value'].strip().split('-'))
    
    records = database.filterDataDashboard(nameTable, column, valueFilter)
    
    if request.method == 'POST':
        column = request.POST['column']
        valueFilter = '-'.join(request.POST['value-filter'].split())
        
        return redirect('filter', column, valueFilter)
    
    context = {
        'title': 'Dashboard',
        'dashboardActive': 'active',
        'records': records,
        'column': ' '.join(column.split('_')),
        'valueFilter': valueFilter,
        'isEmpty': True if len(records) == 0 else False,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'base.html', context)

def login(request):
    username = 'admin'
    password = 'admin'
    
    if 'admin' in request.session:
        if request.session['admin']:
            return redirect('index')
    
    context = {
        'title': 'Login',
        'loginActive': 'active',
    }

    if request.method == 'POST':
        if request.POST['username'] == username and request.POST['password'] == password:
            request.session['admin'] = True
            return redirect('index')
        else:
            context['loginFailed'] = True
    
    return render(request, 'login.html', context)

def logout(request):
    if 'admin' not in request.session:
        return redirect('index')
            
    if request.method == 'POST':
        del request.session['admin']
        return redirect('index')
    
    context = {
        'title': 'Log Out',
        'logoutActive': 'active',
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'logout.html', context)

# def pageNotFound(request):
#     return render(request, '404.html')
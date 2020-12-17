from django.shortcuts import redirect, render
import pyodbc
import modules as database

def index(request):
    if 'admin' not in request.session:
        return redirect('index')
    
    database.createTempTable('##PENJUALAN_APRIL')
    
    if request.method == 'POST':
        kodeObat = request.POST['kode_obat'];
        tglTransaksi = request.POST['tgl_transaksi']
        jumlahDibeli = int(request.POST['jumlah_dibeli'])
        
        bulan = tglTransaksi.split('-')[1]
        table = ''
        if bulan == '01':
            table = 'PENJUALAN_JANUARI'
        elif bulan == '02':
            table = 'PENJUALAN_FEBRUARI'
        elif bulan == '03':
            table = 'PENJUALAN_MARET'
        elif bulan == '04':
            database.updateStock('PERSEDIAAN', jumlahDibeli, 'kode_obat', kodeObat)
            table = '##PENJUALAN_APRIL'
        
        database.insertData(table, kodeObat, tglTransaksi, jumlahDibeli)

        database.mergeData()
    
    listKodeObat = database.getDataSpecific('OBAT', 'kode_obat')

    transaksi = database.getTopFiveData('TRANSAKSI')
    
    context = {
        'title': 'Transaksi',
        'transaksiActive': 'active',
        'listKodeObat': listKodeObat,
        'transaksi': transaksi,
        'isGreaterThan5': True if len(transaksi) >=5 else False,
        'isEmpty': True if len(transaksi) == 0 else False,
        'admin': request.session['admin'] if 'admin' in request.session else False
        }
    
    return render(request, 'transaksi/index.html', context)

def logTransaksi(request, **query):
    if 'admin' not in request.session:
        return redirect('index')
    
    database.createTempTable('##PENJUALAN_APRIL')
    
    recordsJanuari = database.getData('PENJUALAN_JANUARI')
    recordsFebruari = database.getData('PENJUALAN_FEBRUARI')
    recordsMaret = database.getData('PENJUALAN_MARET')
    recordsApril = database.getData('##PENJUALAN_APRIL')
    
    lenghtData = 0
    if len(recordsJanuari) != 0:
        lenghtData += 1
    if len(recordsFebruari) != 0:
        lenghtData += 1
    if len(recordsMaret) != 0:
        lenghtData += 1
    if len(recordsApril) != 0:
        lenghtData += 1
    btnTitle = "Lihat Semua"
    
    context = {
        'title': 'Log Transaksi',
        'logTransaksiActive': 'active',
        'lengthTable': lenghtData,
        'grid2': 'grid-2' if lenghtData > 1 else '',
        'recordsJanuari': recordsJanuari,
        'lengthJanuari': len(recordsJanuari),
        'recordsFebruari': recordsFebruari,
        'lengthFebruari': len(recordsFebruari),
        'recordsMaret': recordsMaret,
        'lengthMaret': len(recordsMaret),
        'recordsApril': recordsApril,
        'lengthApril': len(recordsApril),
        'getAll': False,
        'admin': request.session['admin'] if 'admin' in request.session else False
    }
    
    return render(request, 'transaksi/log_transaksi.html', context)
    
def logDetailTransaction(request):
    if 'admin' not in request.session:
        return redirect('index')

    records = database.getData('TRANSAKSI')
    lenghtData = len(records)
        
    context = {
        'title': 'Log Transaksi',
        'logTransaksiActive': 'active',
        'lengthTable': lenghtData,
        'records': records,
        'showAll': True,
        'admin': request.session['admin'] if 'admin' in request.session else False
        }
    return render(request, 'transaksi/log_transaksi.html', context)
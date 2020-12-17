import pyodbc

server = 'LAPTOP-2BRADEPN\SQLEXPRESS2019'
database = 'Apotek'

try:    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                        Server=' + server + '; \
                        DATABASE=' + database + '; \
                        Trusted_Connection=yes;')
    print('Database Connect')
except:
    print('Database Not Connect')
    
def getHostName():
    cursor = conn.cursor()
    cursor.execute('select HOST_NAME()')
    hostName = cursor.fetchone()[0]
    
    return hostName
    
def dashboard():
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT O.KODE_OBAT, O.NAMA_OBAT, O.BENTUK_OBAT, O.TGL_PRODUKSI, O.TGL_KADALUARSA, O.HARGA_SATUAN, P.JUMLAH_SEDIA
                        FROM OBAT O
                        JOIN PERSEDIAAN P
                        ON O.KODE_OBAT = P.KODE_OBAT
                    ''')
    
    records = cursor.fetchall()
    
    return records

def filterDataDashboard(nameTable, column, valueFilter):
    cursor = conn.cursor()
    cursor.execute(f'''
                    SELECT O.KODE_OBAT, O.NAMA_OBAT, O.BENTUK_OBAT, O.TGL_PRODUKSI,
                    O.TGL_KADALUARSA, O.HARGA_SATUAN, P.JUMLAH_SEDIA
                        FROM OBAT O
                        JOIN PERSEDIAAN P
                        ON O.KODE_OBAT = P.KODE_OBAT
                        WHERE {nameTable}.{column} = \'{valueFilter}\'''')
    records = cursor.fetchall()
    
    return records

def getData(table):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    records = cursor.fetchall()
    
    return records

def getDataSpecific(table, column):
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column} FROM {table}')
    records = cursor.fetchall()
    
    return records

def getTopFiveData(table):
    cursor = conn.cursor()
    cursor.execute(f'SELECT TOP 5 * FROM {table}')
    records = cursor.fetchall()
    
    return records

def filterData(table, column, valueFilter):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table} WHERE {column} = \'{valueFilter}\'')
    records = cursor.fetchall()
    
    return records

def updateData(table, columns, value, columnFilter, valueFilter):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE {table} SET {columns} = {value} WHERE {columnFilter} = \'{valueFilter}\'')
    cursor.commit()
    
def updateStock(table, value, columnFilter, valueFilter):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE {table} SET jumlah_sedia = jumlah_sedia - {value} WHERE {columnFilter} = \'{valueFilter}\'')
    cursor.commit()
    
def insertData(table, kodeObat, tglTransaksi, jumlahDibeli):
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {table} VALUES (\'{kodeObat}\', \'{tglTransaksi}\', {jumlahDibeli})')
    cursor.commit()
    
def createTempTable(table):
    cursor = conn.cursor()
    cursor.execute(f'''               
                    IF OBJECT_ID('tempdb.dbo.{table}') IS NULL
                    BEGIN
                        CREATE TABLE {table}(
                            kode_obat char(9),
                            tgl_transaksi date,
                            jumlah_terjual int
                        )
                    END
                    ''')
    cursor.commit()
    
def mergeData():
    cursor = conn.cursor()
    cursor.execute('''
                    MERGE INTO TRANSAKSI AS TARGET
                    USING (SELECT * FROM PENJUALAN_JANUARI
                            UNION
                            SELECT * FROM PENJUALAN_FEBRUARI
                            UNION
                            SELECT * FROM PENJUALAN_MARET)
                    AS SOURCE
                    ON (SOURCE.kode_obat = TARGET.kode_obat AND SOURCE.tgl_transaksi = TARGET.tgl_transaksi)
                    WHEN NOT MATCHED THEN
                        INSERT (kode_obat, tgl_transaksi, jumlah_terjual)
                        VALUES (SOURCE.kode_obat, SOURCE.tgl_transaksi, SOURCE.jumlah_terjual);
                    ''')
    cursor.commit()
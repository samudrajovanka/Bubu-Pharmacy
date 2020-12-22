create database apotek;

use apotek;

------------- table obat
drop table obat
create table OBAT (
	kode_obat char(9) not null primary key,
	nama_obat varchar(50) not null,
	bentuk_obat varchar(50) not null,
	tgl_produksi date not null,
	tgl_kadaluarsa date not null,
	harga_satuan int not null
)

insert into OBAT values
('SLMNZ1520', 'MICONAZOLE', 'SALEP', '2015-09-15', '2020-09-14', 18000),
('SRSCF1723', 'SUCRALFATE', 'SYRUP', '2017-03-23', '2023-02-20', 62500),
('SRZNP1723', 'ZINCPRO', 'SYRUP', '2017-02-02', '2023-01-30', 15000),
('KPRNS1723', 'RHINNOS', 'KAPLET', '2017-02-02', '2023-01-30', 45000),
('TBALD1723', 'AMLODIPINE', 'TABLET', '2017-02-02', '2023-01-30', 51000)

SELECT * FROM OBAT
SELECT * FROM OBAT where tgl_produksi = '2-2-2017'
SELECT kode_obat FROM OBAT

------------- table persediaan
drop table persediaan
create table PERSEDIAAN(
	kode_obat char(9) FOREIGN KEY REFERENCES OBAT(kode_obat),
	jumlah_sedia int,
)

insert into PERSEDIAAN values
	('SLMNZ1520',100),
	('SRSCF1723',100),
	('SRZNP1723',100),
	('KPRNS1723',100),
	('TBALD1723',100)

select * from PERSEDIAAN

update PERSEDIAAN set jumlah_sedia = 100 where KODE_OBAT = 'SLMNZ1520'
update PERSEDIAAN set jumlah_sedia = 100 where KODE_OBAT = 'SRSCF1723'
update PERSEDIAAN set jumlah_sedia = 100 where KODE_OBAT = 'SRZNP1723'
update PERSEDIAAN set jumlah_sedia = 100 where KODE_OBAT = 'KPRNS1723'
update PERSEDIAAN set jumlah_sedia = 100 where KODE_OBAT = 'TBALD1723'

------------- table penjualan januari
create table PENJUALAN_JANUARI (
	kode_obat char(9) FOREIGN KEY REFERENCES OBAT(kode_obat),
	tgl_transaksi date,
	jumlah_terjual int
)

insert into PENJUALAN_JANUARI values
	('SLMNZ1520','20190115',32),
	('SRSCF1723','20190115',14),
	('SRZNP1723','20190115',5),
	('KPRNS1723','20190115',51),
	('TBALD1723','20190115',40)

------------- table penjualan februari
create table PENJUALAN_FEBRUARI(
	kode_obat char(9) FOREIGN KEY REFERENCES OBAT(kode_obat),
	tgl_transaksi date,
	jumlah_terjual int
)

insert into PENJUALAN_FEBRUARI values
	('SRZNP1723','20190202',12),
	('TBALD1723','20190210',20)

------------- table penjualan maret
create table PENJUALAN_MARET(
	kode_obat char(9) FOREIGN KEY REFERENCES OBAT(kode_obat),
	tgl_transaksi date,
	jumlah_terjual int
)

insert into PENJUALAN_MARET values
	('SLMNZ1520','20190321',2),
	('SRSCF1723','20190315',6),
	('TBALD1723','20190330',21)

------------- table penjualan april (temp)
drop table ##PENJUALAN_APRIL
create table ##PENJUALAN_APRIL(
	kode_obat char(9),
	tgl_transaksi date,
	jumlah_terjual int
)

------------- table penjualan
drop table PENJUALAN_JANUARI
drop table PENJUALAN_FEBRUARI
drop table PENJUALAN_MARET

select * from PENJUALAN_JANUARI
select * from PENJUALAN_FEBRUARI
select * from PENJUALAN_MARET
select * from ##PENJUALAN_APRIL

------------- join table persediaan sama obat
select o.kode_obat, o.nama_obat, o.bentuk_obat, o.tgl_produksi, o.tgl_kadaluarsa, o.harga_satuan, p.jumlah_sedia
	from obat o
	join persediaan p
	on o.kode_obat = p.kode_obat
	where o.kode_obat = 'SLMNZ1520'

------------- trigger untuk update data
create trigger OBAT_TRIGGER 
on OBAT
after update as
	print 'Data Obat berhasil di UPDATE'
	print 'Dimodifikasi : ' +  CONVERT( VARCHAR  , GETDATE())
	Print  'Nama Host : ' + HOST_NAME()

------------- sample update
update OBAT set HARGA_SATUAN = 18000 where KODE_OBAT = 'SLMNZ1520'
update OBAT set HARGA_SATUAN = 21000 where KODE_OBAT = 'SLMNZ1520'

------------- dapetin hostname
select HOST_NAME()


------------- table transaksi
drop table transaksi
create table TRANSAKSI(
	kode_obat char(9) FOREIGN KEY REFERENCES OBAT(kode_obat),
	tgl_transaksi date,
	jumlah_terjual int
)

insert into transaksi values
('SLMNZ1520', '2017-02-02', 10),
('SLMNZ1520', '2017-02-02', 10),
('SLMNZ1520', '2017-02-02', 10),
('SLMNZ1520', '2017-02-02', 10)

select * from transaksi
select top 5 * from transaksi

------------- beresin data
delete from TRANSAKSI where kode_obat = 'SLMNZ1520'
delete from TRANSAKSI where kode_obat = 'SRSCF1723'
delete from TRANSAKSI where kode_obat = 'SRZNP1723'
delete from TRANSAKSI where kode_obat = 'KPRNS1723'
delete from TRANSAKSI where kode_obat = 'TBALD1723'

delete from PENJUALAN_JANUARI where kode_obat = 'SLMNZ1520'
delete from PENJUALAN_JANUARI where kode_obat = 'SRSCF1723'
delete from PENJUALAN_JANUARI where kode_obat = 'SRZNP1723'
delete from PENJUALAN_JANUARI where kode_obat = 'KPRNS1723'
delete from PENJUALAN_JANUARI where kode_obat = 'TBALD1723'

delete from PENJUALAN_FEBRUARI where kode_obat = 'SLMNZ1520'
delete from PENJUALAN_FEBRUARI where kode_obat = 'SRSCF1723'
delete from PENJUALAN_FEBRUARI where kode_obat = 'SRZNP1723'
delete from PENJUALAN_FEBRUARI where kode_obat = 'KPRNS1723'
delete from PENJUALAN_FEBRUARI where kode_obat = 'TBALD1723'

delete from PENJUALAN_MARET where kode_obat = 'SLMNZ1520'
delete from PENJUALAN_MARET where kode_obat = 'SRSCF1723'
delete from PENJUALAN_MARET where kode_obat = 'SRZNP1723'
delete from PENJUALAN_MARET where kode_obat = 'KPRNS1723'
delete from PENJUALAN_MARET where kode_obat = 'TBALD1723'

delete from ##PENJUALAN_APRIL where kode_obat = 'SLMNZ1520'
delete from ##PENJUALAN_APRIL where kode_obat = 'SRSCF1723'
delete from ##PENJUALAN_APRIL where kode_obat = 'SRZNP1723'
delete from ##PENJUALAN_APRIL where kode_obat = 'KPRNS1723'
delete from ##PENJUALAN_APRIL where kode_obat = 'TBALD1723'

------------- merge penjualan ke table transaksi
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

------------ trigger untuk update data di persediaan
drop trigger transaksi_januari
drop trigger transaksi_februari
drop trigger transaksi_maret
create trigger TRANSAKSI_JANUARI
on PENJUALAN_JANUARI
after insert as
    declare @triggerJumlah int;
    declare @triggerKode char(9);

    select @triggerJumlah = PEMBELIAN_JANUARI.jumlah_terjual from inserted PEMBELIAN_JANUARI;
    select @triggerKode = PEMBELIAN_JANUARI.kode_obat from inserted PEMBELIAN_JANUARI;

    update PERSEDIAAN set PERSEDIAAN.jumlah_sedia = (PERSEDIAAN.jumlah_sedia - @triggerJumlah)
    where kode_obat = @triggerKode;
    print 'Data PENJUALAN JANUARI berhasil di INSERT'

create trigger TRANSAKSI_FEBRUARI
on PENJUALAN_FEBRUARI
after insert as
    declare @triggerJumlah int;
    declare @triggerKode char(9);

    select @triggerJumlah = PENJUALAN_FEBRUARI.jumlah_terjual from inserted PENJUALAN_FEBRUARI;
    select @triggerKode = PENJUALAN_FEBRUARI.kode_obat from inserted PENJUALAN_FEBRUARI;

    update PERSEDIAAN set PERSEDIAAN.jumlah_sedia = (PERSEDIAAN.jumlah_sedia - @triggerJumlah)
    where kode_obat = @triggerKode;
    print 'Data PENJUALAN FEBRUARI berhasil di INSERT'

create trigger TRANSAKSI_MARET
on PENJUALAN_MARET
after insert as
    declare @triggerJumlah int;
    declare @triggerKode char(9);

    select @triggerJumlah = PENJUALAN_MARET.jumlah_terjual from inserted PENJUALAN_MARET;
    select @triggerKode = PENJUALAN_MARET.kode_obat from inserted PENJUALAN_MARET;

    update PERSEDIAAN set PERSEDIAAN.jumlah_sedia = (PERSEDIAAN.jumlah_sedia - @triggerJumlah)
    where kode_obat = @triggerKode;
    print 'Data PENJUALAN MARET berhasil di INSERT'

----------------- insert manual
insert into PENJUALAN_JANUARI values
	('SLMNZ1520','20190115',32)
insert into PENJUALAN_JANUARI values
	('SRSCF1723','20190115',14)
insert into PENJUALAN_JANUARI values
	('SRZNP1723','20190115',5)
insert into PENJUALAN_JANUARI values
	('KPRNS1723','20190115',51)
insert into PENJUALAN_JANUARI values
	('TBALD1723','20190115',40)

insert into PENJUALAN_FEBRUARI values
	('SRZNP1723','20190202',12)
insert into PENJUALAN_FEBRUARI values
	('TBALD1723','20190210',20)

insert into PENJUALAN_MARET values
	('SLMNZ1520','20190321',2)
insert into PENJUALAN_MARET values
	('SRSCF1723','20190315',6)
insert into PENJUALAN_MARET values
	('TBALD1723','20190330',21)

----------------- update stock untuk pembelian april
UPDATE PERSEDIAAN SET jumlah_sedia = jumlah_sedia - 50 WHERE kode_obat = 'SLMNZ1520'

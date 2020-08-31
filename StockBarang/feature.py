from json import dump, load
from os import system
from time import sleep

fileUser = 'user.json'
fileBarang = 'barang.json'
user = {}
member = {}



def loadData():
	global user, member

	with open(fileUser) as f:
		user = load(f)

	with open(fileBarang) as f:
		member = load(f)

	return True



def saveData():
	global user, member

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileBarang, 'w') as f:
		dump(member, f)

	return True



def login():
	counter = 1
	Username = input('Enter Username : ')
	Password = input('Enter Password : ')
	dataCheck = False
	passLogin = False
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)

	while (not dataCheck) or (not passLogin):
		counter += 1
		if counter > 3:
			return False
		print('Combination Username and Password is Wrong')
		Username = input('Enter Username : ')
		Password = input('Enter Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
	else:
		print('Login Pass')
		return True



def print_menu():
	print('Gudang Item Indomerit')
	print('[1] Lihat daftar Barang')
	print('[2] Tambah Barang')
	print('[3] Hapus Barang')
	print('[4] Update Barang')
	print('[q] Keluar Aplikasi')



def print_member():
	if len(member) > 0:
		for info in member:
			print(f'Nama \t: {info}\t Jumlah \t: {member[info]}')
	else:
		print('Gaada stock barang.')



def tambah_barang():
	print('Tambah Barang Baru\n')

	nama = input('Nama \t:')
	saldo = input('Jumlah \t:')

	member[nama] = saldo
	saveData()
	print('proses dulu tunggu yak ...')
	sleep(1)
	print('Udah disimpan.')




def hapus_barang():
	print('Hapus Barang\n')

	nama = input('Nama \t:')

	if nama in member:
		del member[nama]
		saveData()
		print('Proses dulu coy ...')
		sleep(1)
		print('Udah di Hapus.')
	else:
		print(f'{nama} Barang yang ingin dihapus tidak ditemukan')



def update_barang():
	print('Update barang\n')

	nama = input('Nama Barang \t:')
	Jumlah = input('Jumlah Barang baru \t:')

	member[nama] = Jumlah
	saveData()
	print('Proses dulu yak ...')
	sleep(1)
	print('Udh selesai nih.')	


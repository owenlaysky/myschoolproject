from os import system
from time import sleep
import feature

statusLoading = feature.loadData()
system('cls')




if statusLoading :
	passLogin = feature.login()
	if passLogin:
		print('Acc Granted!')
		sleep(1.5)
		menu_choice = ''

		while menu_choice != 'q':
			system('cls')
			feature.print_menu()
			menu_choice = input('Tulis angka : ').lower()
			if menu_choice == '1':
				feature.print_member()
				input('ENTER untuk keluar')
			elif menu_choice == '2':
				feature.tambah_barang()
				input('ENTER untuk keluar')
			elif menu_choice == '3':
				feature.hapus_barang()
				input('ENTER untuk keluar')
			elif menu_choice == '4':
				feature.update_barang()
				input('ENTER untuk keluar')
			elif menu_choice == 'q':
				break
			else: 
				print('Tulis yang bener woe')
				input('ENTER untuk keluar')
	else:
		print('Anda ketahuan membajak.')
else:
	print('Aplikasi gak bisa jalan.')

import os

# Fungsi untuk menampilkan daftar transaksi
def show_transaction():
    try:
        total = 0
        trxn_file = open('trxn.txt', 'r')
        trxn_id = trxn_file.readline()
        while trxn_id != '':
            trxn_num = trxn_file.readline()
            product = trxn_file.readline()
            quantity = trxn_file.readline()
            price = trxn_file.readline()
            subtotal = trxn_file.readline()
            
            trxn_id = trxn_id.rstrip('\n')
            trxn_num = trxn_num.rstrip('\n')
            product = product.rstrip('\n')
            quantity = quantity.rstrip('\n')
            price =  price.rstrip('\n')
            subtotal = subtotal.rstrip('\n')

            print('\nDaftar Transaksi')
            print('ID Transaksi:', trxn_id)
            print('Nomor Transaksi:', trxn_num)
            print('Nama Produk:', product)
            print('Qty:', quantity)
            print('Harga:', price)
            print('Subtotal:', subtotal)

            total += int(subtotal)

            trxn_id = trxn_file.readline()
        trxn_file.close()
        print('\nTotal Keseluruhan:', total)
    except FileNotFoundError:
        print('\nFile trxn.txt tidak ditemukan')
    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")

# Fungsi untuk menambahkan data transaksi
def add_transaction():
    try:
        another = 'y'
        trxn_file = open('trxn.txt', 'a')
        while another == 'y' or another == 'Y':
            print('\nInput Data Transaksi Baru')
            trxn_id = input('ID Transaksi: ')
            trxn_num = input('Nomor Transaksi: ')
            product = input('Nama Produk: ')
            try:
                quantity = int(input('Qty: '))
                price = int(input('Harga: '))
            except ValueError:
                print('Qty dan Harga harus berupa angka.')
                continue
            subtotal = price * quantity

            trxn_file.write(trxn_id + '\n')
            trxn_file.write(trxn_num + '\n')
            trxn_file.write(product + '\n')
            trxn_file.write(str(quantity) + '\n')
            trxn_file.write(str(price) + '\n')
            trxn_file.write(str(subtotal) + '\n')

            another = input('\nApakah anda ingin menambahkan catatan lain? (Y or N):  ')
        trxn_file.close()
        print('\nTransaksi telah ditambahkan ke trxn.txt')
    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")

# Fungsi untuk mengubah data transaksi
def modify_transaction():
    try:
        found = False
        print('\nEdit Data Transaksi')
        search = input('Silahkan masukkan Nomor Transaksi: ')
        trxn_file = open('trxn.txt', 'r')
        temp_file = open('temp.txt', 'w')
        trxn_id = trxn_file.readline()
        while trxn_id != '':
            trxn_num = trxn_file.readline()
            product = trxn_file.readline()
            quantity = trxn_file.readline()
            price = trxn_file.readline()
            subtotal = trxn_file.readline()

            trxn_id = trxn_id.rstrip('\n')
            trxn_num = trxn_num.rstrip('\n')
            product = product.rstrip('\n')
            quantity = quantity.rstrip('\n')
            price =  price.rstrip('\n')
            subtotal = subtotal.rstrip('\n')

            if trxn_num == search:
                print('\nID Transaksi:', trxn_id)
                print('Nomor Transaksi:', trxn_num)
                print('Nama Produk:', product)
                print('Qty:', quantity)
                print('Harga:', price)
                print('Subtotal:', subtotal)
                print()

                new_product = input('Nama Produk: ')
                new_qty = int(input('Qty: '))
                new_price = int(input('Harga: '))
                new_subtotal = new_qty * new_price

                temp_file.write(trxn_id + '\n')
                temp_file.write(trxn_num + '\n')
                temp_file.write(new_product + '\n')
                temp_file.write(str(new_qty) + '\n')
                temp_file.write(str(new_price) + '\n')
                temp_file.write(str(new_subtotal) + '\n')
                found = True
            else:
                temp_file.write(trxn_id + '\n')
                temp_file.write(trxn_num + '\n')
                temp_file.write(product + '\n')
                temp_file.write(str(quantity) + '\n')
                temp_file.write(str(price) + '\n')
                temp_file.write(str(subtotal) + '\n')
            trxn_id = trxn_file.readline()
        trxn_file.close()
        temp_file.close()
        os.remove('trxn.txt')
        os.rename('temp.txt', 'trxn.txt')
        if found:
            print('\nFile telah diperbaharui.')
        else:
            print('\nTansaksi dengan ID tersebut tidak ditemukan didalam file.')
    except FileNotFoundError:
        print('File trxn.txt tidak dapat ditemukan.')
    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")   

# Fungsi untuk menghapus data transaksi
def delete_transaction():
    try:
        found = False
        print('\nDelete Data Transaksi')
        search = input('Silahkan masukkan Nomor Transaksi: ')
        trxn_file = open('trxn.txt', 'r')
        temp_file = open('temp.txt', 'w')
        trxn_id = trxn_file.readline()
        while trxn_id != '':
            trxn_num = trxn_file.readline()
            product = trxn_file.readline()
            quantity = trxn_file.readline()
            price = trxn_file.readline()
            subtotal = trxn_file.readline()

            trxn_id = trxn_id.rstrip('\n')
            trxn_num = trxn_num.rstrip('\n')
            product = product.rstrip('\n')
            quantity = quantity.rstrip('\n')
            price =  price.rstrip('\n')
            subtotal = subtotal.rstrip('\n')

            if trxn_num != search:
                temp_file.write(trxn_id + '\n')
                temp_file.write(trxn_num + '\n')
                temp_file.write(product + '\n')
                temp_file.write(str(quantity) + '\n')
                temp_file.write(str(price) + '\n')
                temp_file.write(str(subtotal) + '\n')
            else:
                print('\nID Transaksi:', trxn_id)
                print('Nomor Transaksi:', trxn_num)
                print('Nama Produk:', product)
                print('Qty:', quantity)
                print('Harga:', price)
                print('Subtotal:', subtotal)
                found = True
            trxn_id = trxn_file.readline()
        trxn_file.close()
        temp_file.close()
        os.remove('trxn.txt')
        os.rename('temp.txt', 'trxn.txt')
        if found:
            print('\nFile telah diperbaharui.')
        else:
            print('\nTansaksi dengan ID tersebut tidak ditemukan didalam file.')
    except FileNotFoundError:
        print('File trxn.txt tidak dapat ditemukan.')
    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}") 

# Fungsi utama untuk menyediakan opsi kepada pengguna
def main():
    while True:
        print('\n# # # # # # # # # # # # # # # #')
        print('Silahkan Pilih Menu')
        print('1. Daftar Transaksi Penjualan')
        print('2. Input Data Transaksi Baru')
        print('3. Edit Data Transaksi')
        print('4. Delete Data Transaksi')
        print('5. Exit')
        choice = input('\nMasukkan pilihan Anda: ')
        try:
            if choice == '1':
                show_transaction()
            elif choice == '2':
                add_transaction()
            elif choice == '3':
                modify_transaction()
            elif choice == '4':
                delete_transaction()
            elif choice == '5':
                print('\nTerima kasih telah menggunakan program ini. Sampai jumpa!\n')
                break
            else:
                print('Pilihan Anda tidak valid. Silahkan coba lagi')
        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga: {e}")

# Memanggil fungsi utama
main()
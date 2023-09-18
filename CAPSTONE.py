# Azka Redhia D M
# CAPSTONE MODULE 1

import colorama
from colorama import Fore

colorama.init(autoreset=True)

# ==========================================================================================================
# DATA DUMMY

daftar_film = {
    "Insidious": {
        "Genre": "Horror",
        "Durasi": 120,
        "Kategori Usia": "D 17+",
        "Jumlah Kursi": 15,
        "Harga Tiket": 40000,
    },
    "Ice Age": {
        "Genre": "Animation",
        "Durasi": 110,
        "Kategori Usia": "SU",
        "Jumlah Kursi": 15,
        "Harga Tiket": 35000,
    },
    "Mission Impossible": {
        "Genre": "Action",
        "Durasi": 160,
        "Kategori Usia": "D 17+",
        "Jumlah Kursi": 20,
        "Harga Tiket": 50000,
    },
    "The Avengers": {
        "Genre": "Action",
        "Durasi": 135,
        "Kategori Usia": "R 13+",
        "Jumlah Kursi": 20,
        "Harga Tiket": 45000,
    },
    "Jumanji": {
        "Genre": "Comedy",
        "Durasi": 130,
        "Kategori Usia": "R 13+",
        "Jumlah Kursi": 25,
        "Harga Tiket": 45000,
    },
    "Adventure Of Tintin": {
        "Genre": "Animation",
        "Durasi": 120,
        "Kategori Usia": "R 13+",
        "Jumlah Kursi": 20,
        "Harga Tiket": 40000,
    },
    "The Nun": {
        "Genre": "Horror",
        "Durasi": 110,
        "Kategori Usia": "R 17+",
        "Jumlah Kursi": 25,
        "Harga Tiket": 50000,
    },
    "Planet Earth": {
        "Genre": "Documentary",
        "Durasi": 180,
        "Kategori Usia": "SU",
        "Jumlah Kursi": 30,
        "Harga Tiket": 60000,
    },
}
daftar_key = (
    "Nama Film",
    "Genre",
    "Durasi",
    "Kategori Usia",
    "Jumlah Kursi",
    "Harga Tiket",
)
daftar_genre = ("Action", "Animation", "Comedy", "Documentary", "Horror")
daftar_kategori = ("SU", "R 13+", "D 17+", "D 21+")


# ==========================================================================================================
# 1. MENU READ (Menampilkan daftar film)
def menu_read():
    if len(daftar_film) != 0:
        print()
        print("=" * 45)
        print(
            """          
        ---MENU READ---
    
    1. Tampilkan Seluruh Data Film
    2. Tampilkan Data Sesuai Key
    3. Tampilkan Data Menggunakan Filter
    
    4. Kembali Ke Main Menu          
        """
        )
        print("=" * 45)
        user_input = input("Masukkan opsi yang ingin dipilih: ")
        print()

        if user_input == "1":
            menu_read_all()
        elif user_input == "2":
            menu_read_key()
        elif user_input == "3":
            menu_read_spec()
        elif user_input == "4":
            menu()
        else:
            print(Fore.RED + "Input yang Anda masukkan salah (╥﹏╥)")
            menu_read()
    else:
        print(Fore.RED + "\n\t--Data Film Kosong (╥﹏╥)--\n")
        input("Tekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
        menu()


# Menu Read Sub menu 1 --> untuk menampilkan seluruh data
def menu_read_all():
    while True:
        user_input = input("Apakah anda ingin melakukan sorting (y/n)? ")
        if user_input.lower() == "y":
            menu_sort(daftar_film)
            break
        elif user_input.lower() == "n":
            print("\nList Film Yang Sedang Tayang:")
            print_all(daftar_film)
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
    input("Tekan ENTER untuk kembali ke Menu Read ଘ(੭ˊᵕˋ)੭\n")
    menu_read()


# Menu Read Sub menu 2 --> untuk menampilkan data sesuai key
def menu_read_key():
    print()
    print("=" * 45)
    print("\n\t\t--DAFTAR FILM--\n")
    data_judul = []
    no = 1
    for i in daftar_film.keys():
        print(f"\t{no}. {i}")
        data_judul.append(i)
        no += 1

    print(f"\n\t{no}. Kembali ke Menu Utama")
    print()
    print("=" * 45)
    dict_film = {}
    while True:
        user_input = input("Masukkan nomor film yang ingin ditampilkan: ")
        if not user_input.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
        else:
            if int(user_input) < no and int(user_input) > 0:
                judul_film = data_judul[int(user_input) - 1]
                dict_film[judul_film] = daftar_film[judul_film]
                print_all(dict_film)
                input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
                menu()
                break
            elif int(user_input) == no:
                menu()
                break
            else:
                print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")


# Menu Read Sub menu 3 --> untuk menampilkan data spesifik
def menu_read_spec():
    print("=" * 45)
    print(
        """          
        --MENU FILTER--
            
    1. Keyword
    2. Genre Film
    3. Durasi
    4. Kategori Usia
    5. Jumlah Kursi
    6. Harga Tiket
    
    7. Kembali Ke Menu Read
"""
    )
    print("=" * 45)
    user_input = input("Masukkan opsi yang ingin dipilih: ")
    print()

    if user_input == "1":
        spec_film("Nama Film")
    elif user_input == "2":
        spec_film("Genre")
    elif user_input == "3":
        spec_film("Durasi")
    elif user_input == "4":
        spec_film("Kategori Usia")
    elif user_input == "5":
        spec_film("Jumlah Kursi")
    elif user_input == "6":
        spec_film("Harga Tiket")
    elif user_input == "7":
        menu_read()
    else:
        print(Fore.RED + "Input yang Anda masukkan salah (╥﹏╥)")
        input(Fore.RED + "Tekan ENTER untuk kembali\n")
        menu_read_spec()


# Fungsi untuk memfilter film berdasarkan kolom yang dipilih
def spec_film(column_name):
    hasil_filter = {}

    if column_name == "Nama Film":
        keyword = input("Masukkan keyword yang ingin ditampilkan: ").lower()

        for judul in daftar_film.keys():
            if keyword in judul.lower():
                hasil_filter[judul] = daftar_film[judul]
        print(f"\nList Film Dengan Keyword {keyword}: ")
        print_all(hasil_filter)
        input("\nTekan ENTER untuk kembali ke Menu Read ଘ(੭ˊᵕˋ)੭\n")
        menu_read()

    elif column_name == "Genre":
        print("=" * 45)
        print(
            """
        Pilih Genre:
              
        1. Action
        2. Animation
        3. Comedy
        4. Documentary
        5. Horror
              
        6. Kembali Ke Menu Sebelumnya
    """
        )
        print("=" * 45)
        filter_genre = input("Masukkan opsi yang ingin dipilih: ")
        if int(filter_genre) == 6:
            menu_read_spec()

        elif int(filter_genre) > 0 and int(filter_genre) <= 5:
            filter_genre = daftar_genre[int(filter_genre) - 1]
            for judul in daftar_film.keys():
                if filter_genre == daftar_film[judul]["Genre"]:
                    hasil_filter[judul] = daftar_film[judul]
            print(f"\nList Film Dengan Genre {filter_genre}: ")
            print_all(hasil_filter)
            input("\nTekan ENTER untuk kembali ke Menu Read ଘ(੭ˊᵕˋ)੭\n")
            menu_read()
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            spec_film("Genre")

    elif column_name == "Durasi":
        filter_min_max("Durasi")
    elif column_name == "Kategori Usia":
        print(
            """
        Pilih Kategori Usia:
        1. SU
        2. R 13+
        3. D 17+
        4. D 21+
              
        5. Kembali Ke Menu Sebelumnya
    """
        )
        filter_kategori = input("Masukkan opsi yang ingin dipilih: ")
        if int(filter_kategori) == 5:
            menu_read_spec()
        elif int(filter_kategori) > 0 and int(filter_kategori) <= 4:
            filter_kategori = daftar_kategori[int(filter_kategori) - 1]
            for judul in daftar_film.keys():
                if filter_kategori == daftar_film[judul]["Kategori Usia"]:
                    hasil_filter[judul] = daftar_film[judul]
            print(f"\nList Film Dengan Kategori Usia {filter_kategori}: ")
            print_all(hasil_filter)
            input("\nTekan ENTER untuk kembali ke Menu Read ଘ(੭ˊᵕˋ)੭\n")
            menu_read()
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            input("Tekan ENTER untuk kembali memilih Kategori Usia ଘ(੭ˊᵕˋ)੭\n")
            spec_film("Kategori Usia")

    elif column_name == "Jumlah Kursi":
        filter_min_max("Jumlah Kursi")
    elif column_name == "Harga Tiket":
        filter_min_max("Harga Tiket")


def print_all(nama_dict):
    if len(nama_dict) != 0:
        print("=" * 95)
        print(
            f"{daftar_key[0]: <25}|{daftar_key[1]: <15}|{daftar_key[2]: <10}|{daftar_key[3]: <15}|{daftar_key[4]: <15}|{daftar_key[5]: <10}"
        )
        print(
            "-------------------------+---------------+----------+---------------+---------------+-----------"
        )
        for i in nama_dict.keys():
            print(
                f"{i: <25}|{(daftar_film[i][daftar_key[1]]): <15}|{(daftar_film[i][daftar_key[2]]): <10}|{(daftar_film[i][daftar_key[3]]): <15}|{(daftar_film[i][daftar_key[4]]): <15}|{(daftar_film[i][daftar_key[5]]): <10}"
            )
        print("=" * 95)
    else:
        print(Fore.RED + "\n\t--Data Film Kosong (╥﹏╥)--")


def menu_sort(nama_dict):
    print("=" * 45)
    print(
        """          
            --MENU SORT--
            
        1. Judul
        2. Genre Film
        3. Durasi
        4. Kategori Usia
        5. Jumlah Kursi
        6. Harga Tiket
"""
    )
    print("=" * 45)
    user_input = input("Masukkan opsi yang ingin dipilih: ")
    print()

    if user_input == "1":
        menu_sort_judul(daftar_film)
    elif user_input == "2":
        menu_sort_column(nama_dict, "Genre")
    elif user_input == "3":
        menu_sort_column(nama_dict, "Durasi")
    elif user_input == "4":
        menu_sort_column(nama_dict, "Kategori Usia")
    elif user_input == "5":
        menu_sort_column(nama_dict, "Jumlah Kursi")
    elif user_input == "6":
        menu_sort_column(nama_dict, "Harga Tiket")
    else:
        print(Fore.RED + "Input yang Anda masukkan salah (╥﹏╥)")
        menu_sort(nama_dict)


def menu_sort_judul(nama_dict):
    print("=" * 45)
    print(
        """
                --SORTING--
          
            1. Ascending (A - Z)
            2. Descending (Z - A)
"""
    )
    print("=" * 45)
    while True:
        user_input = input("Masukan opsi yang ingin dipilih: ")
        print()
        if user_input == "1":
            print("\nList Film Yang Sedang Tayang (A - Z): ")
            print_all(sort_judul(nama_dict, False))
            break
        elif user_input == "2":
            print("\nList Film Yang Sedang Tayang (Z - A): ")
            print_all(sort_judul(nama_dict, True))
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")


def menu_sort_column(nama_dict, column):
    print("=" * 45)
    print(
        """
                --SORTING--
          
            1. Ascending
            2. Descending
"""
    )
    print("=" * 45)
    while True:
        user_input = input("Masukan opsi yang ingin dipilih: ")
        print()
        if user_input == "1":
            print(f"\nList Film Yang Sedang Tanyang (Sort Berdasarkan {column} ASC): ")
            print_all(sort_column(nama_dict, column, False))
            break
        elif user_input == "2":
            print(f"\nList Film Yang Sedang Tayang (Sort Berdasarkan {column} DESC): ")
            print_all(sort_column(nama_dict, column, True))
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")


def sort_judul(nama_dict, cond):
    nama_dict_sorted = {k: v for k, v in sorted(nama_dict.items(), reverse=cond)}
    return nama_dict_sorted


def sort_column(nama_dict, column, cond):
    nama_dict_sorted = {
        k: v
        for k, v in sorted(nama_dict.items(), key=lambda x: x[1][column], reverse=cond)
    }
    return nama_dict_sorted


def filter_min_max(column):
    hasil_filter = {}
    filter_min = input(f"Masukkan {column} minimum film : ")
    while True:
        if not filter_min.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
            filter_min = input(f"Masukkan {column} minimum dari film: ")
        else:
            if int(filter_min) < 0:
                print(Fore.RED + "\nInput harus lebih besar dari 0 (╥﹏╥)\n")
                filter_min = input(f"Masukkan {column} minimum dari film: ")
            else:
                break

    filter_max = input(f"Masukkan {column} maksimum dari film: ")
    while True:
        if not filter_max.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
            filter_max = input(f"Masukkan {column} maksimum dari film: ")
        else:
            if int(filter_max) < int(filter_min):
                print(
                    Fore.RED
                    + f"\nAngka harus lebih besar dari {column} minimum (╥﹏╥)\n"
                )
                filter_max = input(f"Masukkan {column} maksimum dari film: ")
            else:
                break
    # jika durasi minimum = durasi maksimum, maka data hanya memfilter film yang durasinya sama dengan durasi minimum
    if filter_min == filter_max:
        for judul in daftar_film.keys():
            if int(filter_min) == daftar_film[judul][column]:
                hasil_filter[judul] = daftar_film[judul]
        print(f"\nList Film Dengan {column} {filter_min}: ")
        print_all(hasil_filter)

    else:
        for judul in daftar_film.keys():
            if (
                int(filter_min) <= daftar_film[judul][column]
                and int(filter_max) >= daftar_film[judul][column]
            ):
                hasil_filter[judul] = daftar_film[judul]
        print(f"\nList Film Dengan {column} {filter_min} - {filter_max}: ")
        print_all(hasil_filter)
    input("\nTekan ENTER untuk kembali ke Menu Read ଘ(੭ˊᵕˋ)੭\n")
    menu_read()


# ==========================================================================================================
# 2. MENU CREATE (Membuat data film baru)
def menu_create():
    print()
    print("=" * 45)
    print(
        """          
            ---MENU CREATE---
          
        1. Create 1 Data Film
        2. Create Lebih Dari 1 Data Film
          
        3. Kembali Ke Main Menu          
    """
    )
    print("=" * 45)
    user_input = input("Masukkan opsi yang ingin dipilih: ")
    print()
    if user_input == "1":
        create_one()
        input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
        menu()
    elif user_input == "2":
        create_many()
    elif user_input == "3":
        menu()
    else:
        print(Fore.RED + "Input yang Anda masukkan salah (╥﹏╥)")
        menu_create()


# Menu Create Sub menu 1 --> Membuat 1 data baru
def create_one():
    new_film = {}  # dictionary kosong untuk menyimpan data-data baru yang di input
    duplicate = True
    empty = True
    # Mengecek apakah judul film duplikat atau tidak
    while duplicate or empty:
        judul_film = input(
            "\nMasukkan judul film baru yang ingin ditambahkan: "
        ).title()
        duplicate = False
        empty = False
        if len(judul_film) == 0 or judul_film.isspace():
            empty = True
        for i in daftar_film.keys():
            if i == judul_film:
                duplicate = True
                break
        if not duplicate and not empty:
            break
        elif empty:
            print(Fore.RED + "\nJudul film tidak boleh kosong (╥﹏╥)")
        elif duplicate:
            print(Fore.RED + "\nJudul film sudah ada pada data (╥﹏╥)")

    print(
        """
        Pilih Genre:
          
        1. Action
        2. Animation
        3. Comedy
        4. Documentary
        5. Horror
          """
    )
    user_input = input(f"Pilih genre untuk film {judul_film} (1-5): ")
    while True:
        if user_input == "1":
            genre_film = "Action"
            break
        elif user_input == "2":
            genre_film = "Animation"
            break
        elif user_input == "3":
            genre_film = "Comedy"
            break
        elif user_input == "4":
            genre_film = "Documentary"
            break
        elif user_input == "5":
            genre_film = "Horror"
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            user_input = input(f"Pilih genre untuk film {judul_film} (1-5): ")

    durasi_film = create_int("durasi", 60, 180, judul_film)

    print(
        """
        Pilih Kategori Usia:
          
        1. SU
        2. R 13+
        3. D 17+
        4. D 21+
          """
    )
    user_input = input(f"Pilih kategori usia untuk film {judul_film} (1-4): ")
    while True:
        if user_input == "1":
            kategori_film = "SU"
            break
        elif user_input == "2":
            kategori_film = "R 13+"
            break
        elif user_input == "3":
            kategori_film = "D 17+"
            break
        elif user_input == "4":
            kategori_film = "D 21+"
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            user_input = input(f"Pilih kategori usia untuk film {judul_film} (1-4): ")

    kursi_film = create_int("jumlah kursi", 10, 30, judul_film)

    tiket_film = create_int("tiket film", 25000, 70000, judul_film)
    # Menambahkan data-data yang sudah diinput ke dictionary
    new_film["Genre"] = genre_film
    new_film["Durasi"] = int(durasi_film)
    new_film["Kategori Usia"] = kategori_film
    new_film["Jumlah Kursi"] = int(kursi_film)
    new_film["Harga Tiket"] = int(tiket_film)

    print(
        f"\nNama Film : {judul_film} | Genre : {genre_film} | Durasi : {durasi_film} | Kategori : {kategori_film} | Jumlah Kursi : {kursi_film} | Harga Tiket : {tiket_film}"
    )
    yn = input("\nApakah anda yakin ingin menambah film diatas (y/n)? ")
    while True:
        # Jika input = y maka data film baru akan ditambah ke dictionary daftar_film
        if yn.lower() == "y":
            daftar_film[judul_film] = new_film
            print(Fore.GREEN + "\n\t --Data Baru Sudah Disimpan--")
            break
        elif yn.lower() == "n":
            print(Fore.RED + "\n\t --Data Baru Tidak Disimpan--")
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            yn = input("Apakah anda yakin ingin menambah film diatas (y/n)? ")


# Menu Create Sub menu 2 --> Membuat lebih dari 1 data baru
def create_many():
    while True:
        print(
            "Masukkan jumlah data film yang ingin dibuat (max 5)\nMasukkan angka 0 untuk kembali ke Menu Create "
        )
        num = input()
        if not num.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
        else:
            if int(num) == 0:
                menu_create()
                break
            elif int(num) > 5:
                print(Fore.RED + "\nAngka tidak boleh lebih dari 5 (╥﹏╥)\n")
            else:
                for i in range(int(num)):
                    print(f"\nData film ke-{i + 1}")
                    create_one()
                input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
                menu()
                break


# Fungsi untuk create data yang bentuknya merupakan integer
def create_int(column, min_num, max_num, judul_film):
    while True:
        num = input(
            f"\nMasukkan {column} untuk film {judul_film} ({min_num} - {max_num}): "
        )
        if not num.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)")
        else:
            if int(num) < min_num or int(num) > max_num:
                print(
                    Fore.RED
                    + f"\nAngka harus berada dalam range {min_num} - {max_num} (╥﹏╥)"
                )
            else:
                break
    return int(num)


# ==========================================================================================================
# 3. MENU UPDATE (Memodifikasi data dari suatu film)
def menu_update_film():
    print()
    print("=" * 45)
    # Mengecek apakah data film tidak kosong
    if len(daftar_film) != 0:
        print("\n\t\t--DAFTAR FILM--\n")
        data_judul = []
        no = 1
        # For Loop untuk menampilkan judul-judul dari film yang ada
        for i in daftar_film.keys():
            print(f"\t{no}. {i}")
            data_judul.append(i)
            no += 1

        print(f"\n\t{no}. Kembali ke Menu Utama")
        print()
        print("=" * 45)
        while True:
            user_input = input("Masukkan nomor film yang ingin diupdate: ")
            if not user_input.isdigit():
                print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
            else:
                if int(user_input) < no and int(user_input) > 0:
                    judul_film = data_judul[int(user_input) - 1]
                    menu_update(judul_film)
                    break
                elif int(user_input) == no:
                    menu()
                    break
                else:
                    print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
    # Saat data kosong, fungsi update tidak bisa jalan karena tidak ada data yang bisa dimodifikasi
    else:
        print(Fore.RED + "\n\t--Data Film Kosong (╥﹏╥)--\n")
        input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
        menu()


def menu_update(judul_film):
    print()
    print("=" * 45)
    print(
        """          
            ---MENU UPDATE---
          
        1. Update Seluruh Data Kolom
        2. Update Kolom Spesifik
          
        3. Kembali ke Menu Utama          
    """
    )
    print("=" * 45)
    user_input = input("Masukkan opsi yang ingin dipilih: ")
    print()
    if user_input == "1":
        update_all(judul_film)
    elif user_input == "2":
        update_column(judul_film)
    elif user_input == "3":
        menu()
    else:
        print("\nInput yang Anda masukkan salah (╥﹏╥)")
        menu_update(judul_film)


# Menu Update Sub menu 1 --> Mengupdate seluruh data pada film yang dipilih
def update_all(judul_film):
    global daftar_film
    daftar_film_copy = daftar_film.copy()
    print(f"\nData Film {judul_film} Saat Ini:")
    print("=" * 95)
    print(
        f"{daftar_key[0]: <25}|{daftar_key[1]: <15}|{daftar_key[2]: <10}|{daftar_key[3]: <15}|{daftar_key[4]: <15}|{daftar_key[5]: <10}"
    )
    print(
        "-------------------------+---------------+----------+---------------+---------------+-----------"
    )
    print(
        f"{judul_film: <25}|{(daftar_film[judul_film][daftar_key[1]]): <15}|{(daftar_film[judul_film][daftar_key[2]]): <10}|{(daftar_film[judul_film][daftar_key[3]]): <15}|{(daftar_film[judul_film][daftar_key[4]]): <15}|{(daftar_film[judul_film][daftar_key[5]]): <10}"
    )
    print("=" * 95)

    update_genre(judul_film, daftar_film_copy)
    print("=" * 45)
    update_durasi(judul_film, daftar_film_copy)
    print("=" * 45)
    update_kategori(judul_film, daftar_film_copy)
    print("=" * 45)
    update_kursi(judul_film, daftar_film_copy)
    print("=" * 45)
    update_tiket(judul_film, daftar_film_copy)
    print("\nData Baru:")
    print("=" * 95)
    print(
        f"{daftar_key[0]: <25}|{daftar_key[1]: <15}|{daftar_key[2]: <10}|{daftar_key[3]: <15}|{daftar_key[4]: <15}|{daftar_key[5]: <10}"
    )
    print(
        "-------------------------+---------------+----------+---------------+---------------+-----------"
    )
    print(
        f"{judul_film:<25}|{daftar_film_copy[judul_film][daftar_key[1]]:<15}|{daftar_film_copy[judul_film][daftar_key[2]]:<10}|{daftar_film_copy[judul_film][daftar_key[3]]:<15}|{daftar_film_copy[judul_film][daftar_key[4]]:<15}|{daftar_film_copy[judul_film][daftar_key[5]]:<10}"
    )
    print("=" * 95)
    while True:
        user_input = input("\nApakah anda ingin menyimpan data diatas (y/n)? ").lower()
        if user_input == "y":
            daftar_film = daftar_film_copy.copy()
            print(Fore.GREEN + "\n\t--Data baru sudah disimpan--")
            break
        elif user_input == "n":
            print(Fore.RED + "\n\t--Data baru tidak disimpan--")
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
    input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
    menu()


# Menu Update Sub menu 2 --> Mengupdate satu kolom pada film yang dipilih
def update_column(judul_film):
    print(f"\nData Film {judul_film} Saat Ini:")
    print("=" * 95)
    print(
        f"{daftar_key[0]: <25}|{daftar_key[1]: <15}|{daftar_key[2]: <10}|{daftar_key[3]: <15}|{daftar_key[4]: <15}|{daftar_key[5]: <10}"
    )
    print(
        "-------------------------+---------------+----------+---------------+---------------+-----------"
    )
    print(
        f"{judul_film: <25}|{(daftar_film[judul_film][daftar_key[1]]): <15}|{(daftar_film[judul_film][daftar_key[2]]): <10}|{(daftar_film[judul_film][daftar_key[3]]): <15}|{(daftar_film[judul_film][daftar_key[4]]): <15}|{(daftar_film[judul_film][daftar_key[5]]): <10}"
    )
    print("=" * 95)
    print(
        """                                   --DAFTAR KOLOM--
------------------------------------------------------------------------------------------------
1. Genre    2. Durasi      3. Kategori Usia       4. Jumlah Kursi        5. Harga Tiket

6. Kembali ke Menu Utama"""
    )
    print("=" * 95)
    pilih_column = input(f"Masukkan nomor yang ingin diubah dari film {judul_film}: ")
    if int(pilih_column) >= 1 and int(pilih_column) <= 5:
        if pilih_column == "1":
            update_genre(judul_film)
        elif pilih_column == "2":
            update_durasi(judul_film)
        elif pilih_column == "3":
            update_kategori(judul_film)
        elif pilih_column == "4":
            update_kursi(judul_film)
        elif pilih_column == "5":
            update_tiket(judul_film)
        input("\nTekan ENTER untuk kembali ke Menu Update ଘ(੭ˊᵕˋ)੭\n")
        menu_update_film()
    elif pilih_column == "6":
        menu()
    else:
        print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
        update_column(judul_film)


def update_genre(judul_film, nama_dict=daftar_film):
    print(
        """
        --DAFTAR GENRE--
          
        1. Action
        2. Animation
        3. Comedy
        4. Documentary
        5. Horror
          """
    )
    print("=" * 45)
    data_genre = nama_dict[judul_film]["Genre"]
    while True:
        genre_input = input("Pilih genre yang baru: ")
        if not genre_input.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
        else:
            if int(genre_input) < 0 or int(genre_input) > 5:
                print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            elif data_genre == daftar_genre[int(genre_input) - 1]:
                print(
                    Fore.RED + "\nGenre yang dipilih sama dengan data saat ini (╥﹏╥)\n"
                )
            else:
                genre_input = daftar_genre[int(genre_input) - 1]
                break
    update_confirmation(judul_film, genre_input, "Genre")


def update_durasi(judul_film, nama_dict=daftar_film):
    durasi_input = update_int(judul_film, "Durasi", 60, 180, nama_dict)
    update_confirmation(judul_film, durasi_input, "Durasi")


def update_kategori(judul_film, nama_dict=daftar_film):
    print(
        """
        --DAFTAR KATEGORI--
          
        1. SU
        2. R 13+
        3. D 17+
        4. D 21+
    """
    )
    print("=" * 45)
    data_kategori = nama_dict[judul_film]["Kategori Usia"]
    while True:
        kategori_input = input("Pilih kategori usia yang baru: ")
        if not kategori_input.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
        else:
            if int(kategori_input) < 0 or int(kategori_input) > 4:
                print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            elif data_kategori == daftar_kategori[int(kategori_input) - 1]:
                print(
                    Fore.RED
                    + "\nKategori yang dipilih sama dengan data saat ini (╥﹏╥)\n"
                )
            else:
                kategori_input = daftar_kategori[int(kategori_input) - 1]
                break
    update_confirmation(judul_film, kategori_input, "Kategori Usia")


def update_kursi(judul_film, nama_dict=daftar_film):
    kursi_input = update_int(judul_film, "Jumlah Kursi", 10, 30, nama_dict)
    update_confirmation(judul_film, kursi_input, "Jumlah Kursi")


def update_tiket(judul_film, nama_dict=daftar_film):
    tiket_input = update_int(judul_film, "Harga Tiket", 25000, 70000, nama_dict)
    update_confirmation(judul_film, tiket_input, "Harga Tiket")


def update_confirmation(judul_film, column_input, column_key, nama_dict=daftar_film):
    while True:
        yn = input(
            f"\nApakah anda ingin mengubah {column_key} film {judul_film} menjadi {column_input} (y/n)? "
        )
        if yn.lower() == "y":
            nama_dict[judul_film][column_key] = column_input
            print(Fore.GREEN + "\n\t--Data baru sudah disimpan--")
            break
        elif yn.lower() == "n":
            print(Fore.RED + "\n\t--Data baru tidak disimpan--")
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")


def update_int(judul_film, column, min_num, max_num, nama_dict):
    data_sekarang = nama_dict[judul_film][column]
    while True:
        data_input = input(f"Masukkan {column} yang baru ({min_num} - {max_num}): ")
        if not data_input.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
        else:
            if int(data_input) < min_num or int(data_input) > max_num:
                print(
                    Fore.RED
                    + f"\nAngka harus berada dalam range {min_num} - {max_num} (╥﹏╥)\n"
                )
            elif int(data_input) == data_sekarang:
                print(
                    Fore.RED
                    + "\n{column} yang dipilih sama dengan data saat ini (╥﹏╥)\n"
                )
            else:
                break
    return int(data_input)


# =========================================================================================================
# 4. MENU DELETE (Menghapus data)
def menu_delete():
    if len(daftar_film) != 0:
        print()
        print("=" * 45)
        print(
            """
              ---MENU DELETE---
        
        1. Hapus Film
        2. Hapus Semua Data

        3. Kembali Ke Menu Utama      
        
    """
        )
        print("=" * 45)
        user_input = input("Masukkan opsi yang ingin dipilih: ")
        print()
        while True:
            if user_input == "1":
                menu_delete_film()
                break
            elif user_input == "2":
                menu_delete_all()
                break
            elif user_input == "3":
                menu()
                break
            else:
                print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
                user_input = input("Masukkan opsi yang ingin dipilih: ")
    else:
        print(Fore.RED + "\n\t--Data Film Kosong (╥﹏╥)--\n")
        input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
        menu()


# Menu Delete Sub menu 1 --> Menghapus film spesifik
def menu_delete_film():
    print()
    print("=" * 45)
    print("\n\t\t--DAFTAR FILM--\n")
    data_judul = []
    no = 1
    for i in daftar_film.keys():
        print(f"\t{no}. {i}")
        data_judul.append(i)
        no += 1

    print(f"\n\t{no}. Kembali ke Menu Sebelumnya")
    print()
    print("=" * 45)
    while True:
        user_input = input("\nMasukkan nomor film yang ingin dihapus: ")
        if not user_input.isdigit():
            print(Fore.RED + "\nInput harus berupa angka (╥﹏╥)\n")
        else:
            if int(user_input) > no:
                print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
            elif int(user_input) == no:
                menu_delete()
                break
            else:
                judul_film = data_judul[int(user_input) - 1]
                # break
                while True:
                    yn = input(f"\nApakah anda yakin ingin menghapus film {judul_film} (y/n)? ")
                    if yn.lower() == "y":
                        del daftar_film[judul_film]
                        print(Fore.GREEN + "\n\t--Data sudah dihapus--")
                        break
                    elif yn.lower() == "n":
                        print(Fore.RED + "\n\t--Data tidak jadi dihapus--")
                        break
                    else:
                        print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
                input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
                menu()
                break

# Menu Delete Sub menu 2 --> Menghapus semua data
def menu_delete_all():
    while True:
        user_input = input("Apakah anda yakin ingin menghapus semua data (y/n)? ")
        if user_input.lower() == "y":
            daftar_film.clear()
            print(Fore.GREEN + "\n\t--Semua data sudah dihapus--")
            break
        elif user_input.lower() == "n":
            print(Fore.RED + "\n\t--Data tidak jadi dihapus--")
            break
        else:
            print(Fore.RED + "\nInput yang Anda masukkan salah (╥﹏╥)\n")
    input("\nTekan ENTER untuk kembali ke Menu Utama ଘ(੭ˊᵕˋ)੭\n")
    menu()


# =========================================================================================================
# MENU UTAMA


def menu():
    print("=" * 45)
    print(
        """
--- ヾ(＾∇＾) SELAMAT DATANG DI BIOSKOP XXXI ---         

                ---MENU---
          
            1. Daftar Film
            2. Tambah Film
            3. Update Film
            4. Hapus Film
          
            5. Exit
          """
    )
    print("=" * 45)

    user_input = input("Masukkan Opsi Yang Ingin Dipilih: ")
    if user_input == "1":
        menu_read()
    elif user_input == "2":
        menu_create()
    elif user_input == "3":
        menu_update_film()
    elif user_input == "4":
        menu_delete()
    elif user_input == "5":
        print(
            Fore.MAGENTA
            + """
        ---+｡:.ﾟTHANKヽ(*´∀)ﾉﾟYOU.:｡+ﾟ---
              """
        )
    else:
        print(Fore.RED + "\nOpsi Yang Anda Pilih Tidak Tersedia (╥﹏╥)")
        menu()


menu()

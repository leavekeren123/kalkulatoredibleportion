import streamlit as st

st.set_page_config (page_title= 'edibleportion', page_icon=':chicken', layout= 'wide')

def Menu():
    pilihan = st.sidebar.selectbox('Menu', ['Welcome', 'Anggota Kelompok', 'Apa Itu Edible Portion?', 'Perhitungan Edible Portion', 'Komposisi Pangan'])
    if   pilihan == 'Welcome': landing()
    elif pilihan == 'Anggota Kelompok': show_team_members()
    elif pilihan == 'Apa Itu Edible Portion?': definition_edible_portion()
    elif pilihan == 'Perhitungan Edible Portion': calculate_edible_portion_content()
    elif pilihan == 'Komposisi Pangan': composition_edible_portion()
    st. markdown(':fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish:')

def landing():
    st. title('Hai! Kami siap membantu anda! :chicken: :wave:')
    st. write('Aplikasi ini merupakan hasil project dari kami, kelompok 9 untuk memenuhi tugas akhir mata kuliah logika pemrograman komputer. Silahkan pilih menu yang ada!')

def show_team_members():
        st.subheader('Anggota Kelompok 9', divider='rainbow')
        st.write('Perkenalkan anggota kelompok kami yang terdiri dari')
        st.write ('''
          1. Bunga Sekar Ningrum (2320514)
          2. Delvina Neva Ghita Hannani (2320516)
          3. Dilla Aulia Efendi (2320518)
          4. Gea Veronika Caniago (2320525)
          5. Muhammad Syaukani Akbar (2320538)''')

def definition_edible_portion():
    st.subheader('Definisi Edible Portion', divider='rainbow')
    st.write ('Edible portion adalah bagian dari makanan yang dapat dimakan atau dikonsumsi setelah bagian-bagian yang tidak dapat dimakan atau tidak diinginkan telah dihilangkan.')
    st.subheader('Manfaat dan Fungsi Mengetahui Edible Portion', divider='rainbow')
    st.write ('''
            1. Pengelolaan Bahan Baku: Dengan mengetahui berapa persentase dari bahan baku yang sebenarnya dapat dimakan, produsen makanan dapat mengelola persediaan mereka dengan lebih efisien.
            2. Efisiensi Pengolahan: Mengetahui bagian yang dapat dimakan dari bahan mentah memungkinkan produsen makanan untuk mengoptimalkan proses pengolahan dan mengurangi pemborosan.
            3. Perencanaan Menu yang Lebih Sehat: Restoran atau katering yang memahami edible portion dari berbagai bahan makanan dapat merencanakan menu yang lebih sehat dan seimbang nutrisinya.
            4. Pengurangan Pemborosan Makanan: Dengan memahami berapa banyak dari bahan mentah yang sebenarnya dapat dimakan, individu dan bisnis dapat mengurangi pemborosan makanan dengan memanfaatkan sebanyak mungkin dari bahan tersebut.
            5. Manajemen Biaya: Dengan mengetahui berapa banyak dari bahan yang dapat dimakan, perusahaan makanan dan individu dapat mengelola biaya mereka dengan lebih baik dengan menghindari pembelian atau penggunaan bahan yang tidak diperlukan.
            6. Peningkatan Kesadaran Nutrisi: Memahami bagian makanan yang sebenarnya dapat dimakan membantu individu untuk membuat pilihan makanan yang lebih sehat dan memperhitungkan asupan nutrisi mereka dengan lebih baik.''')

def calculate_edible_portion_content():
    st.title('Kalkulator Edible Portion Pada Bahan Pangan')
    st.write ('Aplikasi ini berguna untuk mempermudah menghitung edible portion pada bahan pangan. Silahkan gulir kebawah dan masukkan bobot yang dapat dimakan dari bahan pangan atau sampel (dalam gram) dan bobot utuh bahan pangan atau sampel (dalam gram) pada layar.')
    daftar_produk = {
        'Daging':['Daging Ayam', 'Daging Sapi', 'Daging Kambing'],
        'Ikan': ['Ikan Bawal', 'Ikan Bandeng', 'Ikan Mas', 'Ikan Asin'],
        'Telur': ['Telur Ayam','Telur Bebek'],
        'Buah': ['Alpukat', 'Apel', 'Durian', 'Mangga', 'Melon'],
        'Sayur':['Bayam', 'Jamur Kuping', 'Kangkung', 'Timun', 'Labu siam'],
        'Serealia': ['Beras', 'Jagung Pipil'],
        'Umbi': ['Kentang', 'Talas', 'Bengkuang'],
        'Kacang-Kacangan': ['Kacang Hijau', 'Kacang Kedelai', 'Kacang Merah']
    }
    kategori_produk = st.selectbox('Pilih Kategori Produk:', list(daftar_produk.keys()))
    try:
        if daftar_produk[kategori_produk]: produk_pilihan = st.selectbox(f'Pilih Jenis{kategori_produk.lower()}:', daftar_produk[kategori_produk])
        else: produk_pilihan = kategori_produk
        bobot_yang_dapat_dimakan = st.number_input('Masukkan bobot yang dapat dimakan pada bahan pangan atau sampel (dalam gram)')
        st.write('bobot yang dapat dimakan pada bahan pangan atau sampel', bobot_yang_dapat_dimakan )
        bobot_utuh_bahan = st.number_input('Masukkan bobot utuh pada bahan pangan atau sampel (dalam gram)')
        st.write('bobot yang utuh pada bahan pangan atau sampel', bobot_utuh_bahan )
        hitung_edibleportion = st.button('Hitung Edible Portion')
        if hitung_edibleportion:
            perhitungan_edible_portion = bobot_yang_dapat_dimakan / bobot_utuh_bahan * 100
            st.write(f'Nilai edible portion dari bahan pangan atau sampel tersebut yaitu {produk_pilihan} adalah, {perhitungan_edible_portion} %')
    except Exception: st.write('Jumlah tidak boleh 0')

def composition_edible_portion():
    st.subheader('Berikut daftar % Edible Portion', divider='rainbow')
    st.write ('Dalam daftar ini dapat dilihat berapa jumlah Edible Portion yang baik dalam 100 gram bahan pangan.')
    st.write('Daging:')
    st.write ('''
      1. Daging Ayam: 58%
      2. Daging Sapi: 100%
      3. Daging Kambing: 100% ''')
    st.write('Ikan:')
    st.write ('''
      1. Ikan Bawal: 80%
      2. Ikan Bandeng: 80%
      3. Ikan Mas: 80% 
      4. Ikan Asin: 70% ''')
    st.write('Telur:')
    st.write ('''
      1. Telur Ayam: 89%
      2. Telur Bebek: 90% ''')
    st.write('Buah:')
    st.write ('''
      1. Alpukat: 61%
      2. Apel: 88%
      3. Durian: 22%
      4. Mangga: 65%
      5. Melon: 58,1% ''')
    st.write('Sayur:')
    st.write ('''
      1. Bayam: 71%
      2. Jamur Kuping: 100%
      3. Kangkung: 60%
      4. Timun: 55%
      5. Labu Siam: 83% ''')
    st.write('Serealia:')
    st.write ('''
      1. Beras: 100%
      2. Jagung Pipil: 100% ''')
    st.write('Umbi:')
    st.write ('''
      1. Kentang: 84%
      2. Talas: 86%
      3. Bengkuang: 85% ''')
    st.write('Buah:')
    st.write ('''
      1. Kacang Hijau: 100%
      2. Kacang Kedelai: 100%
      3. Kacang Merah: 100% ''')
    st.write ('Sumber dari Kementrian Kesehatan Republik Indonesia yaitu Tabel Komposisi Pangan Indonesia 2017')
    st.markdown("Terimakasih telah menggunakan aplikasi ini &mdash;\:fish::broccoli::potato::onion::sunflower::apple:")

if _name_ == '_main_':
    Menu()
import streamlit as st
from streamlit_option_menu import option_menu

#Navigasi Sidebar
with st.sidebar:
    selected = option_menu("Perhitungan Digital untuk Kuat Tekan & Titik Leleh", ['About','Dasar Teori','Hitung Kuat Tekan','Hitung Melting Point'], 
       default_index=1)

#Halaman Download Media
if (selected == 'About') :
    st.header('PPT mengenai pengenalan materi dan cara penggunaan aplikasi')
    import streamlit as st
    import base64
    
    with open(r'C:\Users\Zikrian\Documents\Mata Kuliah\ANFIS\PPT apk web.pdf', 'rb') as f:
        pdf_bytes = f.read()
    
    b64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    st.markdown(f'<a href="data:application/pdf;base64,{b64_pdf}" download="file.pdf">Download PDF file</a>', unsafe_allow_html=True)

  
    st.caption(':red[*aplikasi ini dibuat oleh kelompok 9 kelas 1H/Ankim Dual-System sebagai tugas akhir mata kuliah Logika dan Pemrograman Komputer]')
    
#Halaman Dasar Teori (Prinsip & Cara Kerja)
if (selected == 'Dasar Teori') :
    import streamlit as st

    tab1, tab2, tab3 = st.tabs(['Kuat Tekan','Melting Point','Rumus Literatur'])

    with tab1:
       st.header('Kuat Tekan')
       import streamlit as st
       st.subheader('Prinsip')
       st.caption('Kuat tekan adalah kemampuan benda untuk menerima gaya tekan persatuan luas. Kuat tekan merupakan salah satu indikator standardisasi bahan untuk menentukan kualitas atau nilai mutu bahan atau produk. Biasanya diperlukan untuk spesifikasi baha pangan. Semakin besar nilai kuat tekannya, maka semakin baik mutu strukturnya. Pengujian kuat tekan dilakukan dengan mengukur panjang, lebar, dan tebal sampel lalu sampel diletakkan diatas neraca dan diberi gaya (tekanan) pada bagian tengah sampel yang akan diuji. Akibatnya, sampel akan mengalami perubahan bentuk atau melenting ke bawah dan mencapai batas maksimum hingga akhirnya sampel patah atau retak.')
       st.subheader('Cara Kerja')
       st.caption('1. Diukur Panjang, Lebar, dan Tebal Sampel')
       ()
       st.caption('2. Letakkan sampel di pan neraca yang memiliki skala sesuai dengan kuat tekan')
       ()
       st.caption('3. Set skala di titik nol')
       ()
       st.caption('4. Tekan sampel dengan spatula sampai pecah atau retak')
       ()
       st.caption('5. Dibaca skala saat sampel menerima gaya maksimum')
       ()
       st.caption('6. Dilakukan Pengulangan sebanyak anggota kelompok')
       ()
    with tab2:
       st.header('Melting Point')
       import streamlit as st
       st.subheader('Prinsip')
       st.caption('Titik leleh merupakan temperatur suatu zat padat dimana benda tersebut akan berubah wujud menjadi zat cair. pada senyawa dengan berat molekul hampir sama,senyawa yang lebih polar dan strukturnya lebih simetris akan memiliki titik leleh yang lebih tinggi. Titik leleh suatu senyawa murni dapat ditentukan dengan pengamatan temperatur saat terjadi perubahan wujud dari padatan menjadi cair. Sampel akan dimasukan ke dalam pipa kapiler gelas dan dipanaskan dengan suhu tertentu secara merata hingga menjadi pelelehan pada sampel tersebut.')
        
       st.subheader('Cara Kerja')
       st.caption('1. Dimasukkan serbuk gula halus kedalam ujung terbuka pipa kapiler')
       ()
       st.caption('2. Diketuk-ketuk pipa kapiler ujung tertutup, sehingga serbuk gula masuk kedalam dasar kapiler ujung tertutup')
       ()
       st.caption('3. Dimasukkan pipa kapiler kedalam alat Digital Melting Point Apparatus')
       ()
       st.caption('4. Dinyalakan alat, lalu dilakukan pemanasan')
       ()
       st.caption('5. Diamati perubahan sampel saat pertama meleleh dan dicatat sebagai Smelt')
       ()
       st.caption('6. Kemudian diamati perubahan sampel saat meleleh sempurna dan dicatat sebagai Fmelt')

       
    with tab3:
       st.subheader('Rumus Kuat Tekan') 
       st.caption('a. Perhitungan Luas Sampel, :red[A = P x L]')
       ()
       st.caption('b. Perhitungan Gaya Tekan, :red[F = m x g]')
       ()
       st.caption('c. Perhitungan Kuat Tekan, :red[P = F / A]')
       
       st.subheader('Rumus Melting Point')
       st.caption(':red[ΔF (Melting Point) = Fmelt – Smelt]')

#Halaman Hitung Kuat Tekan
if (selected == 'Hitung Kuat Tekan') :
    st.title('Perhitungan Kuat Tekan')

    import streamlit as st
    st.subheader('_Input data berikut :_')
    
    panjang = st.number_input('Panjang Sampel (cm)', format='%.2f')
    lebar = st.number_input('Lebar Sampel (cm)', format='%.2f')
    massa = st.number_input('Massa Tekan (Kg)',  format='%.3f')
    gravitasi = st.number_input ('Percepatan Gravitasi (m/s^2)',  format='%.0f')

    tombol = st.button('Hitung')


    if tombol:
        luas_sampel = (panjang*lebar)/10000
        st.success(f'Nilai Luas Sampel (m^2) adalah {luas_sampel:.4f}')
        gaya_tekan = massa*gravitasi
        st.success(f'Nilai Gaya Tekan (N) adalah {gaya_tekan:.3f}')
        kuat_tekan = gaya_tekan/luas_sampel
        st.success(f'Nilai Kuat Tekan (N/m^2) adalah {kuat_tekan:.2f}')

#Halaman Hitung Melting Point
if (selected == 'Hitung Melting Point') :
    st.title('Perhitungan Melting Point')
    
    import streamlit as st
    
    Fmelt = st.slider ('Masukkan Nilai Suhu (Fmelt)',0,200)
    Smelt = st.slider ('Masukkan Niai Suhu (Smelt)',0,200)
    
    tombol = st.button ('Hitung ΔF (Melting Point)')
    
    if tombol :
        Delta_F = Fmelt-Smelt
        st.success (f'ΔF (Melting Point) yang diperoleh = {Delta_F}')

                            

   




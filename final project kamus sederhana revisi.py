import os

x={'abad':'eternity','abadi':'eternal','abjad':'alphabet','absterak':'abstract','abu':'dust','acar':'pickles','acuh':'indifirent','adab':'culture','adegan':'scene','adik laki-laki':'younger brother','adik perempuan':'younger sister',
    'administrasi':'administration','agama':'religion','agen':'agent','air':'water','ajaib':'wonderful','akal':'brains','akar':'root','akhir':'end','aksi':'action',
    'alamat':'address','alat':'tools','anak':'child','angka':'number','apa':'what','apabila':'whenever','api':'fire','arwah':'spirits','asap':'smoke','asin':'salty','awal':'beginning','awan':'cloud','ayam':'chicken',
    'bab':'chapter','babi':'pig','badai':'hurricame','badak':'rhinoceros','badan':'body','bagaimana':'how','bahaya':'danger','bahan':'material','baik':'good','bahasa':'language','baja':'steel','baju':'shirt','bakat':'ability',
    'bantal':'pillow','baris':'line','bawang':'onion','bayi':'baby','beda':'different','belajar':'study','benar':'true','besar':'big','bidadari':'angel','burung':'bird',
    'cabai':'papper','cakar':'claw','cat':'paint','celana':'pants','cemburu':'jealous','cinta':'love','cium':'kiss','cokelat':'chocolate','contoh':'example','corak':'design','cukur':'shaver','cuti':'holidays',
    'dada':'chest','dagang':'trader','daerah':'area','dandan':'outfit','darah':'blood','darat':'ground','dasar':'foundation','datar':'flat','daya':'power','detik':'second','dewa':'god','duduk':'sit',
    'edukasi':'education','ekonomi':'economis','emas':'gold','es':'ice','fakta':'fact','fantasi':'phantasy','fisik':'phisical','foto':'photo','fungsi':'function',
    'gagak':'crow','gajah':'elephant','gambar':'picture','garam':'salt','garis':'line','gelar':'title','gelas':'glass','gelombang':'wave','gigi':'tooth','gua':'cave','gratis':'free','gula':'sugar','gulung':'roll','gunung':'mountain',
    'hadiah':'reward','hadir':'present','harga':'price','hari':'day','hewan':'animal','hidung':'nose','hidup':'life','hormat':'respect','gambar':'image','keabadian':'immortal','menyisipkan':'insert','jalan':'road','jarak':'distance','jawab':'answer','jujur':'honest',
    'kaca':'mirror','kamus':'dictionary','kertas':'paper','laba-laba':'spider','lagu':'song','lompat':'jump','lucu':'funny','mahkota':'crown','mati':'dead','masalah':'problem','narkotik':'narcotic','negara':'state','orang':'people','orang tua':'parent',
    'otomatis':'automatic','padang pasir':'desert','pagi':'morning','panas':'hot','panjang':'long','pantai':'beach','penjara':'prison','perangkap':'trap','racun':'poison','raja':'king','rasa':'feeling','rumah':'house','sabun':'soap','sejarah':'history','semangat':'spirit','tali':'rope',
    'tameng':'shield','tanah':'earth','uang':'money','udara':'air','umur':'age','valid':'valid','verba':'verb','waktu':'time','warna':'colour','xenon':'xenon','ya':'yes','yayasan':'institute','zat':'matter','zaman':'period'}


def main():
    print("==================\n"
        "pilihan bahasa : \n"
        "==================\n"
        "(1). Indonesia - Inggris\n"
        "(2). Inggris - Indonesia\n"
    )
   
    pilihan = int(input("masukkan pilihan bahasa : " ))
    

    if pilihan == 1:
        print("Kamus Indonesia - Inggris")
        kamus(x)

    elif pilihan == 2:
        print("kamus Inggris - Indonesia")
        kamus1(x)
    else pilihan == :
        pass
        konfirmasi()
        

def kamus(x):
        a=input("Masukkan kata yang dicari : ")
        if a in x:
            print("<indonesia : inggris>")
            print(a,":",x[a])
        else:
            print("kata yang anda cari tidak ada")
        konfirmasi()

def kamus1(x):
        b=input("Masukkan kata yang dicari : ")
        x = {y:x for x,y in x.items()}
        if b in x:
            print("<indonesia : inggris>")
            print(b,":",x[b])
        else:
            print("tidak ada")
        konfirmasi()

def konfirmasi():
    while True:
        ulang = input("Apakah anda ingin mengulangi?(y/t): ")
        if ulang.title() == "Y":
            cls()
            main()
        elif ulang.title() == "T":
            cls()
            print("selamat tinggal")
            break
        break

def cls():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
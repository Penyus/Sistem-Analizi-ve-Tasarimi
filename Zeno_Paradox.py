import time
import sys
import random
from decimal import Decimal, getcontext


def say(text, wait=1.8):

    print(text)
    time.sleep(wait)


def daktilo_yazisi(metin, hiz=0.04, bekle=0):

    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(hiz)
    print() 
    time.sleep(bekle)




daktilo_yazisi("HAREKET ETMEK İMKANSIZDIR.\n", hiz=0.1, bekle=3)




say("Elealı Zenon bir gün evine doğru yürürken kendi kendine düşündü:")
say("'Önce şu on metrelik yolun yarısını gideyim.'")

say("Dediğini yaptı; beş saniye sonra yolun tam ortasındaydı.")
say("Hafifçe gülümsedi.")
say("'Güzel,' dedi, 'şimdi geriye yalnızca kalan yarısı kaldı.'")


say("Yürümeye devam etti.")
say("Kalan mesafenin yarısını, yani iki buçuk metreyi, iki buçuk saniyede aldı.")
say("Bir an durup etrafına baktı.")
say("Hâlâ evine varmamıştı.")
say("Önünde yine yolun yarısı uzanıyordu.")


say("Tekrar yürüdü.")
say("Yine mesafenin yarısını kat etti; bu kez yalnızca 1.25 saniye geçmişti.")

say("Fakat garip olan şuydu:")
say("Her seferinde yol kısalıyor, harcanan zaman azalıyor, ama Zenon bir türlü kapının önüne ulaşamıyordu.")
say("Her yarıya varış, ondan yeni bir 'yarı' daha istiyordu.")
say("Her adım, bitişe değil, yeni bir başlangıca açılıyordu sanki.")

say("Zenon kaşlarını çattı.")

daktilo_yazisi("'Tuhaf,' diye mırıldandı.")
daktilo_yazisi("'Her defasında sadece küçük bir zaman harcıyorum.'")
daktilo_yazisi("'Önce beş saniye, sonra iki buçuk, sonra bir virgül yirmi beş…'")
daktilo_yazisi("'Süreler küçülüyor. Ama önümdeki yol da bitmiyor.'")

say("Birden durdu.")
say("Aklına düşen düşünce, ayaklarını yere çivilemişti.")

daktilo_yazisi("'Bir dakika,' dedi kendi kendine.")
daktilo_yazisi("'Eğer her seferinde yolun yarısına varmak için bir miktar zaman harcıyorsam ve her vardığım noktada önümde yine yolun yarısı kalıyorsa…'")
daktilo_yazisi("'Bu harcadığım zamanların hepsini toplarsam ne olur?'")

daktilo_yazisi("Gözleri büyüdü.", bekle=1)


daktilo_yazisi("'Beş saniye… iki buçuk saniye… bir virgül yirmi beş… sonra daha da azları…'")
daktilo_yazisi("'Ama yine de zaman! Hep zaman!'")

daktilo_yazisi("Derin bir sessizlik içinde fısıldadı:", bekle=1)
daktilo_yazisi("'Eğer sonsuz sayıda küçük zaman harcamam gerekiyorsa…'")
daktilo_yazisi("'O halde eve varmam için sonsuz zaman geçmesi gerekir.'")
daktilo_yazisi("'Sonsuz zaman gerekiyorsa… Ben aslında hiç varamam.'", bekle=3)

daktilo_yazisi("Ve Zenon, yolun ortasında durmuş, evine birkaç adım kala, hareketin kendisinden şüphe eder hâlde düşünmeye devam etti.")
daktilo_yazisi("Belki de mesele yol değildi.")
daktilo_yazisi("Belki de mesele, hareketin ta kendisiydi.", bekle=3)



########## AI ALERT !!! #############


# --- EVREN AYARLARI ---
# Matematiksel hassasiyeti maksimuma çıkarıyoruz (Sonsuzluk için)
getcontext().prec = 100 

# Sabitler
PLANCK_UZUNLUGU = Decimal('1.616255e-35') # Fiziğin bittiği nokta
ASIL_KUTLE = Decimal('90.0') # Aşil 90 kg
ISIK_HIZI = Decimal('299792458') 

def olcek_belirle(mesafe):
    """Mesafeye göre evrensel ölçeği isimlendirir."""
    if mesafe > 1: return "MAKRO (İnsan Boyutu)"
    if mesafe > 1e-3: return "MİLİMETRİK (Böcek Boyutu)"
    if mesafe > 1e-6: return "MİKROSKOPİK (Hücre Boyutu)"
    if mesafe > 1e-9: return "NANOMETRİK (DNA Boyutu)"
    if mesafe > 1e-12: return "PİKOMETRİK (Atom Boyutu)"
    if mesafe > 1e-15: return "FEMTOMETRİK (Çekirdek Boyutu)"
    if mesafe > PLANCK_UZUNLUGU: return "KUANTUM ALANI (Belirsizlik)"
    return "META-FİZİKSEL (Saf Matematik)"

def enerji_hesapla(adim_mesafesi):
    """
    Her adımda harcanan efor. 
    Mesafe kısalsa da, o mesafeyi 'işlemek' için gereken bilişsel enerji sabittir.
    """
    # Basit İş Formülü: W = F * d (Burada kuvveti sabit varsayıyoruz)
    # Ancak paradoks gereği, adım sayısı arttıkça "Sistem Isısı" artar.
    return adim_mesafesi * ASIL_KUTLE * Decimal('9.8')

# --- SİMÜLASYON BAŞLATILIYOR ---
hedef = Decimal('10.0')
konum = Decimal('0.0')
toplam_zaman = Decimal('0.0')
toplam_enerji = Decimal('0.0')
adim_sayisi = 0

print("\n" + "#"*60)
print("EVREN SİMÜLASYONU V.2.0: 'ZENO'NUN LANETİ'".center(60))
print("Hedef: Mutlak Sıfır Noktası (Singularity)".center(60))
print("Başlangıç: CTRL+C ile Evreni Yırtana Kadar Devam Eder".center(60))
print("#"*60 + "\n")
time.sleep(2)

try:
    while True:
        adim_sayisi += 1
        
        # 1. HESAPLAMA: Mesafeyi Böl
        kalan_yol = hedef - konum
        adim_boyu = kalan_yol / 2
        konum += adim_boyu
        
        # 2. FİZİK: Enerji ve Zaman
        # Her adımda zamanın da azaldığını varsayalım (Zeno'nun dediği gibi)
        gecen_sure = adim_boyu / 2 # Hızın azaldığı bir senaryo
        toplam_zaman += gecen_sure
        anlik_enerji = enerji_hesapla(adim_boyu)
        toplam_enerji += anlik_enerji
        
        # 3. DURUM ANALİZİ
        olcek = olcek_belirle(kalan_yol)
        planck_uyarisi = ""
        if kalan_yol < PLANCK_UZUNLUGU:
            planck_uyarisi = " [!!! FİZİK KURALLARI ÇÖKTÜ !!!]"
            # Matematiksel hassasiyet artırılıyor
            if adim_sayisi % 50 == 0: getcontext().prec += 10

        # 4. GÖRSELLEŞTİRME (DASHBOARD)
        print("-" * 60)
        print(f"ADIM DÖNGÜSÜ: {adim_sayisi}")
        print(f"MEVCUT ÖLÇEK: {olcek}{planck_uyarisi}")
        print(f"KONUM       : {str(konum)[:25]}... m")
        print(f"KALAN BOŞLUK: {str(kalan_yol)[:25]}... m")
        print(f"TOPLAM ENERJİ: {toplam_enerji:.10f} Joule")
        
        # Kuantum Dalgalanması Efekti (Rastgele veri gürültüsü)
        if kalan_yol < 1e-10:
            flux = random.choice(["|", "/", "-", "\\"])
            print(f"KUANTUM DURUMU: Belirsiz {flux} (Schrödinger'in Kedisi Miyavlıyor)")
        
        print("-" * 60)
        
        # Hız kontrolü: Başta yavaş, sonra veri akışı hızlanır
        if adim_sayisi < 10:
            time.sleep(0.8)
        elif adim_sayisi < 50:
            time.sleep(0.1)
        else:
            time.sleep(0.01) # Matrix modu

except KeyboardInterrupt:
    print("\n\n" + "!"*60)
    print("SİMÜLASYON ACİL DURDURULDU".center(60))
    print("!"*60)
    print(f"\nSonuç Raporu:")
    print(f"- Toplam Adım: {adim_sayisi}")
    print(f"- Harcanan Enerji: {toplam_enerji} J")
    print(f"- Varılan Son Nokta: {konum}")
    print(f"- Kalan Mesafe: {hedef - konum}")
    print("\nZeno haklıydı. Matematiksel olarak hala boşluk var.")
    print("Aşil sonsuzluğun içinde dondu kaldı.")

########## AI ALERT !!! #############

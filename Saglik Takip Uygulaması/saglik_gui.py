import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class Kullanici:
    def __init__(self, ad, yas, cinsiyet):
        self.ad = ad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.saglik_kayitlari = []
        self.egzersizler = []
        self.ilaclar = []

    def kayit_ekle(self, kayit):
        self.saglik_kayitlari.append(kayit)

    def egzersiz_ekle(self, egzersiz):
        self.egzersizler.append(egzersiz)

    def ilac_ekle(self, ilac):
        self.ilaclar.append(ilac)

class SaglikKaydi:
    def __init__(self, tarih, kilo, nabiz, tansiyon):
        self.tarih = tarih
        self.kilo = kilo
        self.nabiz = nabiz
        self.tansiyon = tansiyon

    def __str__(self):
        return f"{self.tarih} - Kilo: {self.kilo}kg, Nabız: {self.nabiz}, Tansiyon: {self.tansiyon}"

class Egzersiz:
    def __init__(self, ad, sure, tekrar, egzersiz_turu):
        self.ad = ad
        self.sure = sure
        self.tekrar = tekrar
        self.egzersiz_turu = egzersiz_turu

    def __str__(self):
        return f"{self.ad} ({self.egzersiz_turu}) - Süre: {self.sure}dk, Tekrar: {self.tekrar}"

class Ilac:
    def __init__(self, ad, dozaj, zaman):
        self.ad = ad
        self.dozaj = dozaj
        self.zaman = zaman

    def __str__(self):
        return f"{self.ad} - Dozaj: {self.dozaj}mg, Zaman: {self.zaman}"

class UygulamaYonetici:
    def __init__(self):
        self.kullanicilar = {}

    def kullanici_ekle(self, kullanici):
        self.kullanicilar[kullanici.ad] = kullanici

    def kullanici_getir(self, ad):
        return self.kullanicilar.get(ad, None)

class SaglikApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kişisel Sağlık Takip Uygulaması")
        self.root.geometry("800x700")
        self.root.config(bg="white")  
        self.yonetici = UygulamaYonetici()

        self.ad_var = tk.StringVar()
        self.yas_var = tk.StringVar()
        self.cinsiyet_var = tk.StringVar()

        self.secili_kullanici = None

        self.init_ana_menu()

    def init_ana_menu(self):
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(pady=20, fill=tk.X)

        tk.Label(frame, text="Ad", font=("Helvetica", 14, "bold")).grid(row=0, column=0, pady=10, padx=10)
        tk.Entry(frame, textvariable=self.ad_var, font=("Helvetica", 14), width=30, bd=2, relief="solid").grid(row=0, column=1, pady=10, padx=10)

        tk.Label(frame, text="Yaş", font=("Helvetica", 14, "bold")).grid(row=1, column=0, pady=10, padx=10)
        tk.Entry(frame, textvariable=self.yas_var, font=("Helvetica", 14), width=30, bd=2, relief="solid").grid(row=1, column=1, pady=10, padx=10)

        tk.Label(frame, text="Cinsiyet", font=("Helvetica", 14, "bold")).grid(row=2, column=0, pady=10, padx=10)
        tk.Entry(frame, textvariable=self.cinsiyet_var, font=("Helvetica", 14), width=30, bd=2, relief="solid").grid(row=2, column=1, pady=10, padx=10)

        
        tk.Button(frame, text="Kullanıcı Oluştur", command=self.kullanici_olustur, font=("Helvetica", 14), width=20, bg="#4CAF50", fg="white", relief="raised", bd=5).grid(row=3, columnspan=2, pady=10)
        tk.Button(frame, text="Kullanıcı Seç ve Devam Et", command=self.kullanici_sec, font=("Helvetica", 14), width=20, bg="#2196F3", fg="white", relief="raised", bd=5).grid(row=4, columnspan=2, pady=10)

    def kullanici_olustur(self):
        ad = self.ad_var.get()
        yas = self.yas_var.get()
        cinsiyet = self.cinsiyet_var.get()

        if ad and yas and cinsiyet:
            k = Kullanici(ad, int(yas), cinsiyet)
            self.yonetici.kullanici_ekle(k)
            messagebox.showinfo("Başarılı", f"{ad} adlı kullanıcı oluşturuldu.")
        else:
            messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")

    def kullanici_sec(self):
        ad = self.ad_var.get()
        kullanici = self.yonetici.kullanici_getir(ad)
        if kullanici:
            self.secili_kullanici = kullanici
            self.init_kullanici_ekrani()
        else:
            messagebox.showerror("Hata", "Kullanıcı bulunamadı.")

    def init_kullanici_ekrani(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"{self.secili_kullanici.ad} için Sağlık Takip Paneli", font=("Helvetica", 16, "bold")).pack(pady=20)

       
        tk.Button(self.root, text="Sağlık Kaydı Ekle", command=self.saglik_kaydi_ekle, font=("Helvetica", 14), width=20, bg="#4CAF50", fg="white", relief="raised", bd=5).pack(pady=10)
        tk.Button(self.root, text="Egzersiz Ekle", command=self.egzersiz_ekle, font=("Helvetica", 14), width=20, bg="#2196F3", fg="white", relief="raised", bd=5).pack(pady=10)
        tk.Button(self.root, text="İlaç Ekle", command=self.ilac_ekle, font=("Helvetica", 14), width=20, bg="#FF9800", fg="white", relief="raised", bd=5).pack(pady=10)
        tk.Button(self.root, text="Verileri Görüntüle", command=self.veri_goster, font=("Helvetica", 14), width=20, bg="#FF5722", fg="white", relief="raised", bd=5).pack(pady=10)
        tk.Button(self.root, text="Rapor Oluştur", command=self.rapor_olustur, font=("Helvetica", 14), width=20, bg="#9C27B0", fg="white", relief="raised", bd=5).pack(pady=10)
        tk.Button(self.root, text="Çık", command=self.root.quit, font=("Helvetica", 14), width=20, bg="#f44336", fg="white", relief="raised", bd=5).pack(pady=10)

    def saglik_kaydi_ekle(self):
        pencere = tk.Toplevel()
        pencere.title("Sağlık Kaydı Ekle")

        vars = [tk.StringVar() for _ in range(4)]
        etiketler = ["Tarih", "Kilo", "Nabız", "Tansiyon"]

        for i, etiket in enumerate(etiketler):
            tk.Label(pencere, text=etiket, font=("Helvetica", 12, "bold")).grid(row=i, column=0, pady=10, padx=10)
            tk.Entry(pencere, textvariable=vars[i], font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=i, column=1, pady=10, padx=10)

        def kaydet():
            tarih, kilo, nabiz, tansiyon = [v.get() for v in vars]
            kayit = SaglikKaydi(tarih, float(kilo), int(nabiz), tansiyon)
            self.secili_kullanici.kayit_ekle(kayit)
            messagebox.showinfo("Başarılı", "Sağlık kaydı eklendi.")
            pencere.destroy()

        tk.Button(pencere, text="Kaydet", command=kaydet, font=("Helvetica", 12), width=20, bg="#4CAF50", fg="white", relief="raised", bd=5).grid(row=4, columnspan=2, pady=10)

    def egzersiz_ekle(self):
        pencere = tk.Toplevel()
        pencere.title("Egzersiz Ekle")

        ad = tk.StringVar()
        sure = tk.StringVar()
        tekrar = tk.StringVar()
        egzersiz_turu = tk.StringVar()

        tk.Label(pencere, text="Egzersiz Adı", font=("Helvetica", 12, "bold")).grid(row=0, column=0, pady=10)
        tk.Entry(pencere, textvariable=ad, font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=0, column=1, pady=10)

        tk.Label(pencere, text="Süre (dk)", font=("Helvetica", 12, "bold")).grid(row=1, column=0, pady=10)
        tk.Entry(pencere, textvariable=sure, font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=1, column=1, pady=10)

        tk.Label(pencere, text="Tekrar Sayısı", font=("Helvetica", 12, "bold")).grid(row=2, column=0, pady=10)
        tk.Entry(pencere, textvariable=tekrar, font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=2, column=1, pady=10)

        tk.Label(pencere, text="Egzersiz Türü", font=("Helvetica", 12, "bold")).grid(row=3, column=0, pady=10)
        tk.Entry(pencere, textvariable=egzersiz_turu, font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=3, column=1, pady=10)

        def kaydet():
            egzersiz = Egzersiz(ad.get(), int(sure.get()), int(tekrar.get()), egzersiz_turu.get())
            self.secili_kullanici.egzersiz_ekle(egzersiz)
            messagebox.showinfo("Başarılı", "Egzersiz eklendi.")
            pencere.destroy()

        tk.Button(pencere, text="Kaydet", command=kaydet, font=("Helvetica", 12), width=20, bg="#4CAF50", fg="white", relief="raised", bd=5).grid(row=4, columnspan=2, pady=10)

    def ilac_ekle(self):
        pencere = tk.Toplevel()
        pencere.title("İlaç Ekle")

        ad = tk.StringVar()
        dozaj = tk.StringVar()
        zaman = tk.StringVar()

        tk.Label(pencere, text="İlaç Adı", font=("Helvetica", 12, "bold")).grid(row=0, column=0, pady=10)
        tk.Entry(pencere, textvariable=ad, font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=0, column=1, pady=10)

        tk.Label(pencere, text="Dozaj (mg)", font=("Helvetica", 12, "bold")).grid(row=1, column=0, pady=10)
        tk.Entry(pencere, textvariable=dozaj, font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=1, column=1, pady=10)

        tk.Label(pencere, text="Alma Zamanı", font=("Helvetica", 12, "bold")).grid(row=2, column=0, pady=10)
        tk.Entry(pencere, textvariable=zaman, font=("Helvetica", 12), width=30, bd=2, relief="solid").grid(row=2, column=1, pady=10)

        def kaydet():
            ilac = Ilac(ad.get(), float(dozaj.get()), zaman.get())
            self.secili_kullanici.ilac_ekle(ilac)
            messagebox.showinfo("Başarılı", "İlaç eklendi.")
            pencere.destroy()

        tk.Button(pencere, text="Kaydet", command=kaydet, font=("Helvetica", 12), width=20, bg="#4CAF50", fg="white", relief="raised", bd=5).grid(row=3, columnspan=2, pady=10)

    def veri_goster(self):
        if self.secili_kullanici:
            veri_penceresi = tk.Toplevel(self.root)
            veri_penceresi.title(f"{self.secili_kullanici.ad} Verileri")

            
            tk.Label(veri_penceresi, text="Sağlık Kayıtları", font=("Helvetica", 14, "bold")).pack(pady=10)

            if self.secili_kullanici.saglik_kayitlari:
                for kayit in self.secili_kullanici.saglik_kayitlari:
                    tk.Label(veri_penceresi, text=str(kayit), font=("Helvetica", 12)).pack(pady=5)
            else:
                tk.Label(veri_penceresi, text="Hiç sağlık kaydı bulunmamaktadır.", font=("Helvetica", 12)).pack(pady=5)

           
            tk.Label(veri_penceresi, text="Egzersizler", font=("Helvetica", 14, "bold")).pack(pady=10)

            if self.secili_kullanici.egzersizler:
                for egzersiz in self.secili_kullanici.egzersizler:
                    tk.Label(veri_penceresi, text=str(egzersiz), font=("Helvetica", 12)).pack(pady=5)
            else:
                tk.Label(veri_penceresi, text="Hiç egzersiz kaydı bulunmamaktadır.", font=("Helvetica", 12)).pack(pady=5)

           
            tk.Label(veri_penceresi, text="İlaçlar", font=("Helvetica", 14, "bold")).pack(pady=10)

            if self.secili_kullanici.ilaclar:
                for ilac in self.secili_kullanici.ilaclar:
                    tk.Label(veri_penceresi, text=str(ilac), font=("Helvetica", 12)).pack(pady=5)
            else:
                tk.Label(veri_penceresi, text="Hiç ilaç kaydı bulunmamaktadır.", font=("Helvetica", 12)).pack(pady=5)

        else:
            messagebox.showwarning("Uyarı", "Önce bir kullanıcı seçmeniz gerekiyor.")

    def rapor_olustur(self):
        if self.secili_kullanici:
            rapor_penceresi = tk.Toplevel()
            rapor_penceresi.title("Rapor Oluştur")

            rapor = f"Kullanıcı Adı: {self.secili_kullanici.ad}\nYaş: {self.secili_kullanici.yas}\nCinsiyet: {self.secili_kullanici.cinsiyet}\n\nSağlık Kayıtları:\n"
            for kayit in self.secili_kullanici.saglik_kayitlari:
                rapor += f"{str(kayit)}\n"

            rapor += "\nEgzersizler:\n"
            for egzersiz in self.secili_kullanici.egzersizler:
                rapor += f"{str(egzersiz)}\n"

            rapor += "\nİlaçlar:\n"
            for ilac in self.secili_kullanici.ilaclar:
                rapor += f"{str(ilac)}\n"

            text_box = tk.Text(rapor_penceresi, font=("Helvetica", 12), wrap="word", height=20, width=50)
            text_box.insert(tk.END, rapor)
            text_box.pack(padx=10, pady=10)

            def yazdir():
                messagebox.showinfo("Rapor Yazdır", "Rapor yazdırma işlemi başlatıldı.")
                rapor_penceresi.destroy()

            tk.Button(rapor_penceresi, text="Yazdır", command=yazdir, font=("Helvetica", 14), bg="#4CAF50", fg="white").pack(pady=10)
        else:
            messagebox.showwarning("Uyarı", "Önce bir kullanıcı seçmeniz gerekiyor.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SaglikApp(root)
    root.mainloop()

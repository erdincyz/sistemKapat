#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from getpass import getuser
import os

"""
# systemctl default
# systemctl rescue
# systemctl emergency

# systemctl halt
# systemctl poweroff
# systemctl reboot
# systemctl suspend
# systemctl hibernate
# systemctl hybrid-sleep
"""

PROGRAM_KLASOR = os.path.dirname(os.path.abspath(__file__))
IKON_KLASOR = os.path.join(PROGRAM_KLASOR, "ikonlar")


#######################################################################
class SistemKapat:

    # ---------------------------------------------------------------------
    def __init__(self):
        self.pencere_olustur_frame()

    # ---------------------------------------------------------------------
    def dugmeleri_dondur(self):
        self.iptalBtn.config(state="disabled")
        self.cikisBtn.config(state="disabled")
        self.uyutBtn.config(state="disabled")
        self.yenidenBaslatBtn.config(state="disabled")
        self.kapatBtn.config(state="disabled")

    # ---------------------------------------------------------------------
    def iptal_et(self):
        self.dugmeleri_dondur()
        self.pencere.destroy()

    # ---------------------------------------------------------------------
    def _cikis_yap(self):
        self.dugmeleri_dondur()
        self.durumStrVar.set("Openbox' tan çıkılıyor, lütfen bekleyiniz...")
        os.system("openbox --exit")

    # ---------------------------------------------------------------------
    def _uyut(self):
        self.dugmeleri_dondur()
        self.durumStrVar.set("Uyku moduna geçiliyor, lütfen bekleyiniz...")
        os.system("systemctl suspend")
        self.pencere.destroy()

    # ---------------------------------------------------------------------
    def _yeniden_baslat(self):
        self.dugmeleri_dondur()
        self.durumStrVar.set("Yeniden başlatılıyor, lütfen bekleyiniz...")
        os.system("reboot")

    # ---------------------------------------------------------------------
    def _kapat(self):
        self.dugmeleri_dondur()
        self.durumStrVar.set("Bilgisayar kapatılıyor, lütfen bekleyiniz...")
        os.system("shutdown -h now")

    # ---------------------------------------------------------------------
    def pencere_olustur_frame(self):
        self.pencere = Tk()

        pencere_genislik = 550
        pencere_yukseklik = 75

        ekran_genislik = self.pencere.winfo_screenwidth()
        ekran_yukseklik = self.pencere.winfo_screenheight()

        x = int((ekran_genislik / 2) - (pencere_genislik / 2))
        y = int((ekran_yukseklik / 2) - (pencere_yukseklik / 2))

        self.pencere.geometry(f'{pencere_genislik}x{pencere_yukseklik}+{x}+{y}')
        # self.pencere.geometry('500x90+400+300')
        # self.pencere.geometry('500x90')
        self.pencere.configure(background='#333')
        self.pencere.title("Kullanıcı: " + getuser() + " Lütfen seçiniz")

        genislik = 70
        aralik = 5
        ustFrame = Frame(self.pencere, bg='#333')
        altFrame = Frame(self.pencere, bg='#333')
        ustFrame.pack(side=TOP, pady=(13, 4))
        altFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        iptal_ikon = PhotoImage(file=os.path.join(IKON_KLASOR, "iptal.png"))
        self.iptalBtn = Button(self.pencere, text='İptal', compound="left", image=iptal_ikon, width=genislik, bg='#333',
                               fg="#eee", relief="solid", font=('arial', 11, 'normal'),
                               command=self.iptal_et)
        self.iptalBtn.pack(in_=ustFrame, side=LEFT, padx=aralik)

        cikis_ikon = PhotoImage(file=os.path.join(IKON_KLASOR, "cikis.png"))
        self.cikisBtn = Button(self.pencere, text='Çıkış', compound="left", image=cikis_ikon, width=genislik, bg='#333',
                               fg="#eee", relief="solid", font=('arial', 11, 'normal'),
                               command=self._cikis_yap)
        self.cikisBtn.pack(in_=ustFrame, side=LEFT, padx=aralik)

        uyut_ikon = PhotoImage(file=os.path.join(IKON_KLASOR, "uyut.png"))
        self.uyutBtn = Button(self.pencere, text='Uyut', compound="left", image=uyut_ikon, width=genislik, bg='#333',
                              fg="#eee", relief="solid", font=('arial', 11, 'normal'),
                              command=self._uyut)
        self.uyutBtn.pack(in_=ustFrame, side=LEFT, padx=aralik)

        yeniden_baslat_ikon = PhotoImage(file=os.path.join(IKON_KLASOR, "yeniden_baslat.png"))
        self.yenidenBaslatBtn = Button(self.pencere, text='Yeniden', compound="left", image=yeniden_baslat_ikon,
                                       width=genislik,
                                       bg='#333', fg="#eee", relief="solid", font=('arial', 11, 'normal'),
                                       command=self._yeniden_baslat)
        self.yenidenBaslatBtn.pack(in_=ustFrame, side=LEFT, padx=aralik)

        kapat_ikon = PhotoImage(file=os.path.join(IKON_KLASOR, "kapat.png"))
        self.kapatBtn = Button(self.pencere, image=kapat_ikon, compound="left", text='Kapat', width=genislik, bg='#333',
                               fg="#eee", relief="solid", font=('arial', 11, 'normal'),
                               command=self._kapat)
        # self.kapatBtn.image = kapat_ikon
        self.kapatBtn.pack(in_=ustFrame, side=LEFT, padx=aralik)

        self.durumStrVar = StringVar()
        self.durumStrVar.set("")
        self.durumEtk = Label(self.pencere, textvariable=self.durumStrVar, bg='#333', fg="#eee",
                              font=('arial', 11, 'normal'))
        # ~ self.status.pack(in_=altFrame, anchor=CENTER, pady=(0,10))
        self.durumEtk.pack(in_=altFrame, anchor=CENTER)

        self.pencere.mainloop()


# ---------------------------------------------------------------------
def calistir():
    s = SistemKapat()


# ---------------------------------------------------------------------
if __name__ == "__main__":
    calistir()

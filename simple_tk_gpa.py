import tkinter as tk
from tkinter import messagebox
adlar = []
soyadlar = []
imtahana_qeder_bal = []
imtahan_bal = []
def elave_et():
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    imtahana_qeder = imtahana_qeder_entry.get()
    imtahan = imtahan_entry.get()

    if ad and soyad and imtahana_qeder and imtahan:
        try:
            imtahana_qeder = float(imtahana_qeder)
            imtahan = float(imtahan)
        except ValueError:
            messagebox.showerror("Xeta", "Bal dəyərləri rəqəm olmalidir")
            return

        adlar.append(ad)
        soyadlar.append(soyad)
        imtahana_qeder_bal.append(imtahana_qeder)
        imtahan_bal.append(imtahan)

        ad_entry.delete(0, tk.END)
        soyad_entry.delete(0, tk.END)
        imtahana_qeder_entry.delete(0, tk.END)
        imtahan_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Xeta", "Bütün melumatlari daxil edin!")

def neticeleri_chixar():
    if not adlar:
        messagebox.showerror("Xeta", "Evvelce melumatlari daxil edin!")
        return

    yekun_ballari = [iqb * 0.4 + ib * 0.6 for iqb, ib in zip(imtahana_qeder_bal, imtahan_bal)]
    
    neticeler_penceresi = tk.Toplevel()
    neticeler_penceresi.title("Neticeler")

    header = f"{'Ad':<15}{'Soyad':<15}{'İmtahana qeder bal':<20}{'İmtahan bali':<15}{'Yekun bali':<15}"
    tk.Label(neticeler_penceresi, text=header).pack()

    for ad, soyad, iqb, ib, yb in zip(adlar, soyadlar, imtahana_qeder_bal, imtahan_bal, yekun_ballari):
        nəticə = f"{ad:<15}{soyad:<15}{iqb:<20}{ib:<15}{yb:<15.2f}"
        tk.Label(neticeler_penceresi, text=netice).pack()

root = tk.Tk()
root.title("Telebe Melumatlari")

tk.Label(root, text="Adi").grid(row=0, column=0)
ad_entry = tk.Entry(root)
ad_entry.grid(row=0, column=1)

tk.Label(root, text="Soyadi").grid(row=1, column=0)
soyad_entry = tk.Entry(root)
soyad_entry.grid(row=1, column=1)

tk.Label(root, text="İmtahana qeder bali").grid(row=2, column=0)
imtahana_qeder_entry = tk.Entry(root)
imtahana_qeder_entry.grid(row=2, column=1)

tk.Label(root, text="İmtahan bali").grid(row=3, column=0)
imtahan_entry = tk.Entry(root)
imtahan_entry.grid(row=3, column=1)

elave_button = tk.Button(root, text="Elave et", command=elave_et)
elave_button.grid(row=4, column=0, columnspan=2)

neticeler_button = tk.Button(root, text="Neticeleri chixar", command=neticeleri_chixar)
neticeler_button.grid(row=5, column=0, columnspan=2)

root.mainloop()


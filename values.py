import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

BTC_TO_UAH = 2100000
ETH_TO_UAH = 66000
USDT_TO_UAH = 38

rates_to_uah = {
    "BTC": BTC_TO_UAH,
    "ETH": ETH_TO_UAH,
    "USDT": USDT_TO_UAH,
    "UAH": 1
}

def convert():
    try:
        amount_str = entry.get().strip()
        if not amount_str:
            result_label.configure(text="Error: enter amount")
            root.update()
            return
        amount = float(amount_str)
        if amount <= 0:
            result_label.configure(text="Помилка: сума повинна бути більше 0")
            root.update()
            return
    except ValueError:
        result_label.configure(text="Error: enter a number")
        root.update()
        return
    
    from_cur = from_option.get()
    to_cur = to_option.get()

    amount_in_uah = amount * rates_to_uah[from_cur]
    result = amount_in_uah / rates_to_uah[to_cur]

    if to_cur in ["BTC", "ETH", "USDT"]:
        result_str = f"{result:.6f}"
    else:
        result_str = f"{result:.2f}"

    result_label.configure(text=f"Pe3ynbTaT: {result_str} {to_cur}")
    root.update()

root = ctk.CTk()
root.title("Конвертер криптовалют")
root.geometry("400x300")

title_label = ctk.CTkLabel(root, text="Конвертер криптовалют", font=("Roboto", 18))
title_label.pack(pady=10)

entry = ctk.CTkEntry(root, placeholder_text="BBegn cymy")
entry.pack(pady=10)

from_option = ctk.CTkOptionMenu(root, values=["BTC", "ETH", "USDT", "UAH"])
from_option.pack(pady=5)
from_option.set("BTC")

to_option = ctk.CTkOptionMenu(root, values=["BTC", "ETH", "USDT", "UAH"])
to_option.pack(pady=5)
to_option.set("UAH")

button = ctk.CTkButton(root, text="KoHBepTyBaTn", command=convert)
button.pack(pady=10)

result_label = ctk.CTkLabel(root, text="")
result_label.pack(pady=10)

root.mainloop()
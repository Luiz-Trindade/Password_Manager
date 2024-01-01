'''
    Simple Password Manager Written In Python!
    GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

    Copyright (C) 2024  Luiz Gabriel Magalhães Trindade.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import sqlite3
from customtkinter import *
from pyperclip import copy
from PySimpleGUI import popup_quick_message as alert
from CTkTable import *

#Initial Configuration
conn = sqlite3.connect("_internal/data.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS dados (id INT PRIMARY KEY, info TEXT, password TEXT);")

#Main Function
def Main():
    def Add_Info():
        try:
            id_info = id.get()
            info_content = info.get()
            password_content = password.get()
            cursor.execute(f"INSERT INTO dados VALUES({id_info}, '{info_content}', '{password_content}');")
            conn.commit()
            alert("Added!", font=("Arial", 30, "bold"))
            all_info = cursor.execute("SELECT * FROM dados;")
            conn.commit()
            content = all_info.fetchall()
            table.configure(values=content)
            table.add_row(" ")
        except Exception as error:
            alert(error, font=("Arial", 30, "bold"))

    def Copy_Info():
        info_content = copy_info.get()
        cursor.execute(f"SELECT password FROM dados WHERE id={info_content};")
        content = cursor.fetchone()
        copy(content[0])
        alert("Copied!", font=("Arial", 30, "bold"))

    def Remove_Info():
        info_to_remove = remove_info.get()
        if info_to_remove == "ALL_INFO":
            try:
                cursor.execute("DROP TABLE IF EXISTS dados;")
                conn.commit()
                alert("All Info Deleted!", 30, "bold")
            except Exception as error:
                alert(error, font=("Arial", 30, "bold"))
        else:
            try:
                cursor.execute(f"DELETE FROM dados WHERE id={info_to_remove};")
                conn.commit()
                alert("Removed!", font=("Arial", 30, "bold"))
                all_info = cursor.execute("SELECT * FROM dados;")
                conn.commit()
                content = all_info.fetchall()
                table.configure(values=content)
                table.add_row(" ")
            except Exception as error:
                alert(error, font=("Arial", 30, "bold"))

    set_widget_scaling(1.3)
    app = CTk()
    app.title("Password Manager🛡️ 🔑")
    app.geometry("800x550")
    tabview = CTkTabview(master=app)
    tab1 = tabview.add("Add Info")
    tab2 = tabview.add("View Info")
    tab3 = tabview.add("Copy Info")
    tab4 = tabview.add("Remove Info")
    tabview.pack(pady=10, padx=10)

    id = CTkEntry(
        master=tab1,
        font=("Arial", 30, "bold"),
        width=600,
        placeholder_text="Id",
        justify="center"
    )
    id.pack(pady=10, padx=10)

    info = CTkEntry(
        master=tab1,
        font=("Arial", 30, "bold"),
        width=600,
        placeholder_text="Info",
        justify="center"
    )
    info.pack(pady=10, padx=10)

    password = CTkEntry(
        master=tab1,
        font=("Arial", 30, "bold"),
        width=600,
        placeholder_text="Password",
        justify="center",
        show="*"
    )
    password.pack(pady=10, padx=10)

    add_button = CTkButton(
        master=tab1,
        font=("Arial", 30, "bold"),
        text="Add!",
        command=Add_Info
    )
    add_button.pack(pady=50, padx=10)



    #Table
    all_info = cursor.execute("SELECT * FROM dados;")
    conn.commit()
    content = all_info.fetchall()
    scrollable_frame = CTkScrollableFrame(tab2, width=600, height=400)
    scrollable_frame.pack()
    table = CTkTable(master=scrollable_frame, row=len(content)+1, column=2, values=content)
    table.pack(expand=True, pady=10, padx=10)


    copy_info = CTkEntry(
        master=tab3,
        font=("Arial", 30, "bold"),
        width=600,
        placeholder_text="Info To Copy",
        justify="center"
    )
    copy_info.pack(pady=10, padx=10)

    copy_button = CTkButton(
        master=tab3,
        font=("Arial", 30, "bold"),
        text="Copy!",
        command=Copy_Info
        )
    copy_button.pack(pady=60, padx=10)


    remove_info = CTkEntry(
        master=tab4,
        font=("Arial", 30, "bold"),
        width=600,
        placeholder_text="Info To Remove",
        justify="center"
    )
    remove_info.pack(pady=10, padx=10)

    remove_button = CTkButton(
        master=tab4,
        font=("Arial", 30, "bold"),
        text="Remove!",
        command=Remove_Info
    )
    remove_button.pack(pady=60, padx=10)


    app.mainloop()

if __name__ == "__main__":
    Main()

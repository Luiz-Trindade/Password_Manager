<image src="https://www.gnu.org/graphics/gplv3-127x51.png">

# Password Manager Application 🛡️ 🔑

This is a password management application developed in Python, using the libraries `sqlite3`, `customtkinter`, `pyperclip`, `PySimpleGUI`, and `CTkTable`. The application allows you to add, view, copy, and remove password-related information.

## Initial Configuration
The application uses an SQLite database located at "_internal/data.db". If the "data" table doesn't exist, it is created with columns "id" (primary key), "info," and "password."

## Key Features

### Add Information
In the "Add Info" tab, you can enter an ID, information, and a password, then click the "Add!" button to add this data to the "data" table in the SQLite database. The ID is optional, but information and passwords are required. After addition, the table is updated, and an empty row is added.

### View Information
The "View Info" tab displays a scrollable table containing all the information stored in the "data" table. The table is initially loaded with the data present in the SQLite database.

### Copy Information
In the "Copy Info" tab, you can enter an ID and click the "Copy!" button to copy the password associated with that ID to the clipboard.

### Remove Information
In the "Remove Info" tab, you can enter an ID or the text "ALL_INFO" and click the "Remove!" button to remove the information associated with that ID or delete all information if "ALL_INFO" is provided. After removal, the table is updated, and an empty row is added.

## Notes
- Ensure you provide valid information and follow the application instructions to avoid errors.
- Be cautious when removing all information, as this will permanently delete all data in the table.
- If errors occur during operations, alert messages are displayed to provide user feedback.

The application is designed to provide a user-friendly graphical interface for managing passwords and related information. Be sure to customize and extend it as needed to meet the specific requirements of your use case.

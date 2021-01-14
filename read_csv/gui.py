import os
import smtplib
import tkinter as tk
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from os.path import basename
from tkinter.filedialog import asksaveasfilename, askopenfilenames
from tkinter import messagebox

files = []
deleted_file = []


def open_file():
    filez = askopenfilenames(filetypes=[("CSV Files", "*.csv")])
    txt_edit.config(state=tk.NORMAL)
    txt_edit.insert(tk.END, window.tk.splitlist(filez))
    files.append(filez)
    value = messagebox.askyesno(title="Add more?", message="Do you want to add more files?")
    if value:
        open_file()


def run_script1():
    print('')


#
#     if value:
#         txt_edit.delete("1.0", tk.END)
#         os.system('pyats run job job.py --html-logs .')
#         source_filepath = "eve_log/source_log.txt"
#         target_filepath = "eve_log/target_log.txt"
#         with open(source_filepath, "r") as input_file:
#             text = input_file.read()
#             txt_edit.insert(tk.END, text)
#         txt_edit.insert(tk.END, '\n')
#         with open(target_filepath, "r") as input_file:
#             text = input_file.read()
#             txt_edit.insert(tk.END, text)
#             txt_edit.config(state=tk.DISABLED)
# #
# #
# def run_script2():
#     txt_edit.delete("1.0", "end")
#     value = messagebox.askokcancel("askokcancel", "This action takes few minutes to execute. Do you want to continue?")
#     if value:
#         txt_edit.config(state=tk.NORMAL)
#         txt_edit.delete("1.0", tk.END)
#         os.system('pyats run job job.py --html-logs .')
#         # os.system('python target_interface.py')
#         filepath = "eve_log/report.txt"
#         with open(filepath, "r") as input_file:
#             text = input_file.read()
#             txt_edit.insert(tk.END, text)
#             window.title(f"Switch port Consolidation - {filepath}")
#         txt_edit.insert(tk.END, '\n')
#
#
# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     window.title(f"Switch port Consolidation - {filepath}")


def openNewWindow():
    newWindow = tk.Toplevel(window)
    newWindow.title("Edit files")
    tk.Label(newWindow, text="Click on files to remove from the list", bg='light pink').grid(row=0, column=0,
                                                                                             padx=(10, 10))
    a = 0
    for items in files:
        tk.Button(newWindow, text=items, command=remove(items)).grid(row=a, column=0, ipadx=10, ipady=10)
        a = a + 1
    for values in deleted_file:
        txt_edit.insert(tk.END, values)


def remove(file):
    deleted_file.append(file)
    files.remove(file)
    return


#
# def send_email(e1, newWindow):
#     subject = "Switch log file"
#     body = "Hi, \n\nSee the log file from switch attached in this mail. \n\nThank you, \nRespiro team."
#     sender_email = "respirotest0@gmail.com"
#     receiver_email = e1.get()
#     password = "respiroemail"
#
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = e1.get()
#     message["Subject"] = subject
#     message["Date"] = formatdate(localtime=True)
#
#     message.attach(MIMEText(body, "plain"))
#     filename = {"eve_log/source_log.txt", "TaskLog.job.html", "eve_log/target_log.txt", "eve_log/report.txt"}
#     for items in filename:
#         try:
#             with open(items, "rb") as fil:
#                 part = MIMEApplication(
#                     fil.read(),
#                     Name=basename(items)
#                 )
#                 # After the file is closed
#                 part['Content-Disposition'] = 'attachment; filename="%s"' % basename(items)
#                 message.attach(part)
#         except:
#             messagebox.showerror("Error", "There was an error while sending attachments. Run the script to generate "
#                                           "the attachments")
#
#
#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         server.ehlo()
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message.as_string())
#         newWindow.destroy()
#     except:
#         messagebox.showerror("Error", "There was an error while sending email")
#         print(e1)


window = tk.Tk()
window.title("Switch port Consolidation")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window, bg='pink')
fr_buttons = tk.Frame(window, bg='light blue')
btn_script4 = tk.Button(fr_buttons, text="Open source file", fg='green', bg='green', command=open_file)
btn_script1 = tk.Button(fr_buttons, text="Generate source and target switch interface log", command=openNewWindow,
                        fg='green', bg='light green')
# btn_script2 = tk.Button(fr_buttons, text="Generate  log to recommend port migration", command=run_script2,
#                         fg='green', bg='green')
# btn_script3 = tk.Button(fr_buttons, text="Run script to verify the port migration", fg='green', bg='green')
# btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file, fg='green', bg='light green')
# btn_email = tk.Button(fr_buttons, text="Send as email", command=openNewWindow, fg='green', bg='light green')
#
btn_script1.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
# btn_script2.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
# btn_script3.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
# btn_email.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
#
fr_buttons.grid(row=0, column=0, sticky="ns")
btn_script4.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

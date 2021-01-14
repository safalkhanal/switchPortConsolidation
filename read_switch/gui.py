import os
import smtplib
import tkinter as tk
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from os.path import basename
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox


def generatetestbed():
    filepath = askopenfilename(
        filetypes=[("Excel file", "*.xls")]
    )
    if not filepath:
        return
    print('pyats create testbed file --path ' + filepath + ' --output ./testbed.yaml')
    try:
        os.system('pyats create testbed file --path ' + filepath + ' --output ./testbed.yaml')
        btn_script1["state"] = "active"
        btn_script2["state"] = "active"
        btn_script3["state"] = "active"
    except:
        txt_edit.insert(tk.END, "Tesbed file format is wrong")


def run_script1():
    txt_edit.config(state=tk.NORMAL)
    value = messagebox.askokcancel("askokcancel", "This action takes few minutes to execute. Do you want to continue?")
    if value:
        try:
            os.system('pyats run job job.py --html-logs .')
            source_filepath = "eve_log/source_log.txt"
            target_filepath = "eve_log/target_log.txt"
            with open(source_filepath, "r") as input_file:
                text = input_file.read()
                txt_edit.insert(tk.END, text)
            txt_edit.insert(tk.END, '\n')
            with open(target_filepath, "r") as input_file:
                text = input_file.read()
                txt_edit.insert(tk.END, text)
                txt_edit.config(state=tk.DISABLED)
            btn_save["state"] = "active"
            btn_email["state"] = "active"
        except:
            txt_edit.insert(tk.END, "Error occurred while running the script")


def run_script2():
    txt_edit.delete("1.0", "end")
    value = messagebox.askokcancel("askokcancel", "This action takes few minutes to execute. Do you want to continue?")
    if value:
        btn_save["state"] = "active"
        btn_email["state"] = "active"
        txt_edit.config(state=tk.NORMAL)
        txt_edit.delete("1.0", tk.END)
        os.system('pyats run job job.py --html-logs .')
        # os.system('python target_interface.py')
        filepath = "eve_log/report.txt"
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
            window.title(f"Switch port Consolidation - {filepath}")
        txt_edit.insert(tk.END, '\n')


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Switch port Consolidation - {filepath}")


def openNewWindow():
    newWindow = tk.Toplevel(window)
    newWindow.rowconfigure(0, minsize=80, weight=1)
    newWindow.columnconfigure(1, minsize=80, weight=1)
    newWindow.configure(bg='#ededed')
    newWindow.title("Send email")
    l1 = tk.Label(newWindow, text="Email address: ", bg='#ededed')
    l1.grid(row=0, column=0, padx=(10, 10))
    e1 = tk.Entry(newWindow, bg='white')
    e1.grid(row=0, column=1, columnspan=10)
    btn_send_email = tk.Button(newWindow, text="Send email", command=lambda: send_email(e1, newWindow), fg='green',
                               bg='light green')
    btn_send_email.grid(row=1, column=1)


def send_email(e1, newWindow):
    subject = "Switch log file"
    body = "Hi, \n\nSee the log file from switch attached in this mail. \n\nThank you, \nRespiro team."
    sender_email = "respirotest0@gmail.com"
    receiver_email = e1.get()
    password = "respiroemail"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = e1.get()
    message["Subject"] = subject
    message["Date"] = formatdate(localtime=True)

    message.attach(MIMEText(body, "plain"))
    filename = {"eve_log/source_log.txt", "TaskLog.job.html", "eve_log/target_log.txt", "eve_log/report.txt"}
    for items in filename:
        try:
            with open(items, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(items)
                )
                # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(items)
                message.attach(part)
        except:
            messagebox.showerror("Error", "There was an error while sending attachments. Run the script to generate "
                                          "the attachments")

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        newWindow.destroy()
    except:
        messagebox.showerror("Error", "There was an error while sending email")


window = tk.Tk()
window.title("Switch port Consolidation")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window, bg='white')
fr_buttons = tk.Frame(window, bg='#b9e2f5')
txt_edit.config(state=tk.DISABLED)
btn_load = tk.Button(fr_buttons, text="Upload testbed excel file(*.xls)", command=generatetestbed, bg="red")
btn_load.config(fg='#000000')

btn_script1 = tk.Button(fr_buttons, text="Generate source and target switch interface log", command=run_script1)

btn_script2 = tk.Button(fr_buttons, text="Generate log to recommend port migration", command=run_script2,
                        activebackground='#a9a9a9')

btn_script3 = tk.Button(fr_buttons, text="Run script to verify the port migration", activebackground='#a9a9a9')

btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file, activebackground="#a9a9a9")

btn_email = tk.Button(fr_buttons, text="Send log files as email", command=openNewWindow, activebackground="#a9a9a9")

btn_load.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_script1.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_script2.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_script3.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_email.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
btn_save["state"] = "disable"
btn_script2["state"] = "disable"
btn_script3["state"] = "disable"
btn_script1["state"] = "disable"
btn_email["state"] = "disable"

window.mainloop()

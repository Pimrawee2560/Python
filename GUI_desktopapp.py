import tkinter as tk #trinker คือ modules python  as tk(ชื่อย่อ trinker)

def set_message():#ฟังก์ชันให้ปุ่ม ok รับข้อความในช่องข้อความเพื่อไปแสดงผล title_label.pack()
    text = text_input.get() #ดึงข้อความเที่เรากรอกข้าไปให้ออกมาใช้งานได้
    title_label.configure(text=text)


window = tk.Tk()    #1-5 #สำคัญในการสร้างapp
window.title('JustPython') #ชื่อโปรเจค
window.minsize(width=400, height=400) #กำหนดวามกว้าง

#UI
#text
title_label = tk.Label(master=window, text='เมื่อรักฮัน') #master จะใช้บอก Label ว่า lAbel จะไปถูกใส่ลงมทีไหน
title_label.pack()

#ช่องกรอกข้อความ
text_input = tk.Entry(master=window)
text_input.pack()

#ปุ่ม
ok_button = tk.Button(master=window, text= 'ok' , command=set_message)
ok_button.pack()

window.mainloop() #mainloop  จะเป็นคำสั่ง start app ของเรา #สำคัญในการสร้างapp
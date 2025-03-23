import tkinter as tk #trinker คือ modules python  as tk(ชื่อย่อ trinker)

def show_output():
    number =  int(number_input.get())#ดึงข้อความจาก  number_input  ออกมาเก็บเป็นตัวเลข /number_input.get() มันจะinput เป็นข้อความ ถ้าจะให้ input เป็นตัวเลขต้องใส่ int
    #ใช้เก็บข้อความที่แสดงผลลัพ
    
    #ทำให้ 0 ไม่สามารถคิดคำนวณได้
    if number == 0:
        output_label.configure(text='ไม่ใส่')
        return

    output = ' '
    for i in range(1,13): #ใช้ Loop เข้ามาช่วยให้คูณเริ่มต้นที่หนึ่ง สิ้นสุุดที่ 12
        output += str(number) + 'x' + str(i)#+=ช้กับข้อความได้โดยการต่อท้ายข้อความเดิมต่อไปเรื่อยๆ
        output += ' = ' + str(number * i) + '\n' 

    output_label.configure(text=output)

window = tk.Tk()    #1-5 #สำคัญในการสร้างapp
window.title('JustPython') #ชื่อโปรเจค
window.minsize(width=400, height=400) #กำหนดวามกว้าง

#UI
#text
title_label = tk.Label(master=window, text='สูตรคูณ') #master จะใช้บอก Label ว่า lAbel จะไปถูกใส่ลงมทีไหน
title_label.pack()

#ช่องกรอกข้อความ
number_input = tk.Entry(master=window)
number_input.pack()

#ปุ่ม
number_button = tk.Button(
    master=window, text= 'submit' ,
    command=show_output,width=15, height=2
    )
number_button.pack()

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop() #mainloop  จะเป็นคำสั่ง start app ของเรา #สำคัญในการสร้างapp
#width = 4
#lenght = 4
#height = 2
#box_area = widht * lenght * height

#การสร้างฟังชันใน python
#def get_box_area(): #def ชือฟังก์ชัน
    #width = 4 #คำสั่ง
    #lenght = 4
    #height = 2
    #box_area = width * lenght * height
    #print(box_area) 
    
#get_box_area() #32



def get_box_area(width, lenght, height): #def ชือฟังก์ชัน(ตัวแปรค่าที่รับ)
    box_area = width * lenght * height
    print(box_area) 
    
get_box_area(4, 10 , 2) 
get_box_area(width=1, lenght=1 , height=1) #ในกรณีที่จำไม่ได้




#return  กรณีที่ต้องการไม่ให้แสดงค่า print แต่ให้คืนค่า ,
def get_box_area(width, lenght, height): #def ชือฟังก์ชัน(ตัวแปรค่าที่รับ)
    box_area = width * lenght * height
    return box_area #ข้อมูลที่ต้องการคืนค่ากลับไป จะคืนค่าไปเก็บที่ บรรทัดที่ 22 และ 23
    
box1 = get_box_area(4, 10 , 2) 
box2 = get_box_area(width=1, lenght=1 , height=1) #ในกรณีที่จำไม่ได้

print(box1) #แสดงค่าที่เก็บใน box1=80



#return  ฟังก์ชันไปเจอคำว่า return เมื่อไหร่จะหลุดการทำงานของฟังก์ชันนั้นทันที
def get_box_area(width, lenght, height): #def ชือฟังก์ชัน(ตัวแปรค่าที่รับ)
    if width < 0 or lenght < 0 or height < 0: #ถ้ามีตัวใดตัวนึงมีค่าน้อยกว่า 0 
        return 0
    box_area = width * lenght * height #ถ้ามีตัวใดตัวนึงมีค่าน้อยกว่า 0  โค้ดจะไม่ทำงานต่อจะคืนค่าไปให้ด้านบน
    return box_area 
box1 = get_box_area(4, -10 , 2) 
box2 = get_box_area(width=1, lenght=1 , height=1) #ในกรณีที่จำไม่ได้

print(box1) #แสดงค่าที่เก็บใน box1 = 0
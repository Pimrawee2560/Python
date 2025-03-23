#โจทย์: ระบบการจัดการรายการหนังสือ
#สร้างคลาส Book ที่มีข้อมูลดังนี้:
#title: ชื่อหนังสือ (string)
#author: ผู้แต่ง (string)
#year: ปีที่ตีพิมพ์ (integer)
#price: ราคาของหนังสือ (float)

#สร้างคลาส Bookstore ที่มีฟังก์ชันต่างๆ ดังนี้:
#add_book(book): เพิ่มหนังสือเข้าไปในร้าน (เก็บในลิสต์)
#remove_book(title): ลบหนังสือจากร้านตามชื่อ
#search_book(title): ค้นหาหนังสือจากชื่อ หากพบให้แสดงข้อมูลของหนังสือ (ชื่อ, ผู้แต่ง, ปีที่ตีพิมพ์, ราคา)
#list_books(): แสดงรายชื่อหนังสือทั้งหมดในร้าน
#total_value(): คำนวณมูลค่ารวมของหนังสือในร้าน (ราคาของหนังสือทุกเล่มรวมกัน)

#ทดสอบการทำงานโดยสร้างหนังสือบางเล่มและเพิ่มเข้าไปในร้าน แล้วลองใช้ฟังก์ชันต่างๆ เช่น ค้นหาหนังสือ, ลบหนังสือ, และคำนวณมูลค่ารวม
#ตัวอย่างข้อมูล:
#ชื่อหนังสือ: "Python for Beginners"
#ผู้แต่ง: "John Doe"
#ปีที่ตีพิมพ์: 2021
#ราคา: 499.99 บาท

class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Price: {self.price}"

# 2. สร้างคลาส Bookstore
class Bookstore:
    def __init__(self):
        self.books = []  # เก็บหนังสือทั้งหมดในร้าน

    def add_book(self, book):
        """เพิ่มหนังสือเข้าไปในร้าน"""
        self.books.append(book)

    def remove_book(self, title):
        """ลบหนังสือจากร้านตามชื่อ"""
        self.books = [book for book in self.books if book.title != title]

    def search_book(self, title):
        """ค้นหาหนังสือจากชื่อ"""
        for book in self.books:
            if book.title == title:
                return str(book)
        return "Not Found"

    def list_books(self):
        """แสดงรายชื่อหนังสือทั้งหมดในร้าน"""
        if self.books:
            return "\n".join(str(book) for book in self.books)
        return "No books available."

    def total_value(self):
        """คำนวณมูลค่ารวมของหนังสือในร้าน"""
        return sum(book.price for book in self.books)

# 3. ทดสอบการทำงานของโปรแกรม
book1 = Book("Python for Beginners", "John Doe", 2021, 499.99)
book2 = Book("Learn Java", "Jane Smith", 2020, 399.50)
book3 = Book("Advanced C++", "James Brown", 2019, 599.75)

bookstore = Bookstore()
bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)

# แสดงหนังสือทั้งหมดในร้าน
print("Books in bookstore:")
print(bookstore.list_books())

# ค้นหาหนังสือ
print("\nSearching for 'Learn Java':")
print(bookstore.search_book("Learn Java"))

# ลบหนังสือ
bookstore.remove_book("Learn Java")
print("\nBooks after removing 'Learn Java':")
print(bookstore.list_books())

# คำนวณมูลค่ารวมของหนังสือในร้าน
print("\nTotal value of books in bookstore:")
print(bookstore.total_value())

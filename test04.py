#กรณี 1 print() มีข้อมูลหลายประเภท
# วิธี่ที่ 1 ใช้ ,
print('hello','hii',555,True,"hi")
#วิธีที่ 2 ใช้ + (ข้อมูลไหนที่ไม่ใช่ strint ต้องทำให้ strint ใช้ฟังก็ฃั่น str ())
#ไม่มีเว้น 1 space เหมือน ,
print('hello'+str('hii')+str(555)+str('True')+str("hi"))
print('hello'+str('hii')+'555'+str('True'),("hi"),(50*40*80/21))

# วิฑีที่ 3 ใช้เมธอด Format()
#(ข้อมูลที่ไม่ใช่ strint ให้ใส่ใน() ของformat เเละตำเเหน่งข้อมูลให่ไช้ {} เเทน)

print(' {} wow {} {} Hi {} {}'.format(88888,'True','frue'))
#index number 0 1 2 3 4 
print('{4} {2}'.format('a','b','c','d','e'))

#วิธีที่ 4 ใช้ F-strint โดยข้อมูลเเสดงในรูปแบบของ string โดยมี f อยู่ช้างหน้า
#(ช่อมูลที่ไม่ใฃ้ string ให้เขี่ยน.ส่ {} ณ ตำเเหน่งนั้นๆ เลย)
print(f'hello{555} wow {999} {True} Hi {50+20/8} {80*50+5}')
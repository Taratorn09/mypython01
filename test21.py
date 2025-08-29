#โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้
#	กรณีป้อนชั้นปี 1 แสดงข้อความ "Welcome Freshman"
#	กรณีป้อนชั้นปี 2 แสดงข้อความ "Welcome Sophomore"
#	กรณีป้อนชั้นปี 3 แสดงข้อความ "Welcome Junior"
#	กรณีป้อนชั้นปี 4 แสดงข้อความ "Welcome Senior"
#	กรณีป้อน ปีอื่นๆ  แสดงข้อความ "Oh, no ...."

print('-----------------------------')
print('ปรแกรมแสดงข้อความต้อนรับนักศึกษา')
print('-----------------------------')

name =input ('ป้อนชื่อ: ')
x = int (input ('ชั้นปีการศักษา:'))

if x == 1 :
  print(f"Welcome Freshman")
elif x == 2 :
  print(f"Welcome Sophomore")
elif x == 3 :
  print(f"Welcome Junior")
elif x == 4 :
  print(f"Welcome Senior")

else :
  print(f'Oh,on ..........')
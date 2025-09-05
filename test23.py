#คำสั่ง back,continue
# break ใน loop ทำงานเมื่อใดจบ loop ทำที
# continue ใน loop ทำงานเมื่อไดจบ loop เเค่รอบนั้นทันที เเล้วไปรอบต่อไป

for aa in range(5) :
  if aa == 2 :
    break
  print(aa , 'Hi')

print('**************')
for aa in range(5) :
  if aa == 2 :
    continue
  print(aa, 'Hi.....')





# สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากหักภาษีแล้ว 7% ของเงินเดือน  และหักค่าประกันสังคม 3% ของเงินเดือน
# โดยรับค่ารหัสพนักงาน ชื่อพนักงาน เงินเดือน ทางแป้นพิมพ์ และแสดงผลข้อมูลที่รับมา
# พร้อมกับรายละเอียดว่าต้องเสียภาษีกี่บาท หักค่าประกันสังคมกี่บาท และต้องจ่ายเงินเดือนสุทธิกี่บาท
print('*********************************')
print('โปรเเกรมคำนวณเงินเดือน')
print('*********************************')
emp_code = input('ป้อนรหัสพนักงาน ')
emp_name = input('ป้อนชื่อพนักงาน ')
emp_sleary = input('ป้อนเงินเดือน ')
print('*********************************')
tex = float(emp_sleary)  *7/100 #หรือ emp_salary*0.07
insurence = float(emp_sleary)  * 3 /100 #หรือ emp_salary*0.03
emp_sleary_net =float(emp_sleary) -tex -insurence
print(f'รหัส {emp_code} ชือ {emp_name} เงินเดือน {emp_sleary}')
print(f'หักภาษี {tex} บาท')
print(f'หักค่าประกันสังคม {insurence} บาท')
print(f'ต้องจ่ายเดือนเดือนสุทธิ {emp_sleary_net} บาท ')
print('**********************************')

#ใช้ ,
print('รหัส:',(emp_code), 'ชือ:',(emp_name),'เงินเดือน:',(emp_sleary))
print('หักภาษี :' ,(tex), 'บาท')
print('หักค่าประกันสังคม :',(insurence), 'บาท')
print('ต้องจ่ายเดือนเดือนสุทธิ :',(emp_sleary_net), 'บาท ')
print('**********************************')
#ใช้ +
print('รหัส:'+str(emp_code)+'ชือ:'+str(emp_name)+'เงินเดือน:'+str(emp_sleary))
print('หักภาษี :' +str(tex)+ 'บาท')
print('หักค่าประกันสังคม :'+str(insurence)+ 'บาท')
print('ต้องจ่ายเดือนเดือนสุทธิ :'+str(emp_sleary_net) +'บาท ')

#ใช้ format
print('รหัส: {} ชือ: {}  เงินเดือน: {} '.format (emp_code,emp_name,emp_sleary))
print('หักภาษี : {}  บาท'.format(tex))
print('หักค่าประกันสังคม : {} บาท'.format(insurence))
print('ต้องจ่ายเดือนเดือนสุทธิ : {} บาท' .format(emp_sleary_net))
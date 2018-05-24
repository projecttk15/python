#key-value
data={100:'Hoang' ,101:'Nam' ,102:'Binh'}
print (data)
#only 1 id 
dict = {'Ten': 'Hoang', 'Tuoi': 7, 'Ten': 'Nam'};
print ("dict['Ten']: ", dict['Ten'])

data1={'Id':100, 'Ten':'Thanh', 'Nghenghiep':'Developer'}
data2={'Id':101, 'Ten':'Chinh', 'Nghenghiep':'Trainer'}
print ("Id cua nhan vien dau tien la",data1['Id'])
print ("Id cua nhan vien thu hai la",data2['Id'])
print ("Ten cua nhan vien dau tien la:",data1['Ten'])
print ("Nghe nghiep cua nhan vien thu hai la:",data2['Nghenghiep'])
data1['Nghenghiep'] = 'Porting'
print (data1)
#del key
del data[101]
print(data)

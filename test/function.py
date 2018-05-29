def show(str):
	print("chuoi dc truyen vao ")
	print (str)
	return

# Phan dinh nghia ham o day
def sum( arg1, arg2 ):
   # Cong hai tham so va tra ve ket qua."
   total = arg1 + arg2
   print ("Ben trong ham : ", total)
   return total;

# Bay gio ban co the goi ham sum nay
total = sum( 10, 20 );
print ("Ben ngoai ham : ", total)

# Phan dinh nghia ham o day
def changeme( mylist ):
   "Thay doi list da truyen cho ham nay"
   mylist.append([1,2,3,4]);
   print ("Cac gia tri ben trong ham la: ", mylist)
   return

# Bay gio ban co the goi ham changeme function
mylist = [10,20,30];
print ("Cac gia tri ben ngoai truoc ham la: ", mylist)
changeme( mylist );
print ("Cac gia tri ben ngoai ham la: ", mylist)

# Phan dinh nghia ham o day
def changeme( mylist ):
   "Thay doi list da truyen cho ham nay"
   mylist = [1,2,3,4]; # Lenh nay gan mot tham chieu moi cho mylist
   print ("Cac gia tri ben trong ham la: ", mylist)
   return

# Bay gio ban co the goi ham changeme
mylist = [10,20,30];
changeme( mylist );
print ("Cac gia tri ben ngoai ham la: ", mylist)

#Phan dinh nghia ham
def msg(Id,Ten,Age=21):
	print (Id)
	print (Ten)
	print (Age)
	return
#Function call
msg(Id=100,Ten='Hoang',Age=20)
msg(Id=101,Ten='Thanh')
str2 = "world"
show(str2)

# Phan dinh nghia ham o day
def printinfo( arg1, *vartuple ):
   "In mot tham so da truyen"
   print ("Ket qua la: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Bay gio ban co the goi ham printinfo
printinfo( 10 )
printinfo( 70, 60, 50 )

#Phan dinh nghia ham
square=lambda x1: x1*x1

#Goi square nhu la mot ham
print ("Binh phuong cua so la",square(10))

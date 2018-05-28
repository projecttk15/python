var = 0
while (var<10):
	print (var)
	var+=1

#else in while
count = 0
while count < 5:
   print (count, "nho hon 5")
   count = count + 1
else:
   print (count, "lon hon 5")

#for
for l in 'Python':     # Vi du dau tien
   print ('Chu cai hien tai :', l)

qua = ['chuoi', 'tao',  'xoai']
for q in qua:        # Vi du thu hai
   print ('Ban co thich an :', q)

for index in range(len(qua)):
   print ('Ban co thich an :', qua[index])

#else in for
for num in range(10,20):  #de lap tu 10 toi 20
   for i in range(2,num): #de lap tren cac thua so cua mot so
      if num%i == 0:      #de xac dinh thua so dau tien
         j=num/i          #de uoc luong thua so thu hai
         print ('%d la bang %d * %d' % (num,i,j))
         break #de di chuyen toi so tiep theo, la vong FOR dau tien
   else:                  # else la mot phan cua vong lap
      print (num, 'la so nguyen to')

number = [1,2,5,3,6,9,4,5,8,3,1,4,6,9,43,7,8,3,6,8,4,58,8,3,5,7,3,43,6,34,4,6,67,45,54,7,43,8,45]
for n in range(len(number)-1):
	if(number[n] < number[n+1]):
		print(number[n], number[n+1])
#continue
var = 10                    # Vi du thu hai
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Gia tri bien hien tai la :', var)
#pass
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('Day la khoi pass')
   print ('Chu cai hien tai :', letter)

print ("Good bye!")

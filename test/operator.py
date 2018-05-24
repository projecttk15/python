#so sánh các vị trí ô nhớ của hai đối tượng
a=20
b=20
if( a is b):
	print  ("a,b co cung identity?")
else:
	print ('a, b la khac nhau?')
b=10
if( a is not b):
	print  ('a,b co identity khac nhau')
else:
	print ('a,b co cung identity')

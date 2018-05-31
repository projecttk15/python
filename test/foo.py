# Mo mot file
fo = open("foo.txt", "w")
fo.write( "Python la mot ngon ngu lap trinh tuyet voi.");

# Dong file da mo
fo.close()

# Mo mot file
fo = open("foo.txt", "wb")
print ("Ten cua file la: ", fo.name)
print ("File da duoc dong hay chua : ", fo.closed)
print ("Che do mode la : ", fo.mode)
#print ("Softspace la : ", fo.softspace)

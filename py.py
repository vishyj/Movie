#action = ['Avengers Endgame','SHAZAM!','Spider-man home coming','Spider man into the spiderverse']
#Scifi = ['the flash','arrow','legends of tomorrow','SuperGirl']
#TRASH = ['JAWS REVENGE','FROZEN','FROZEN 2','CATS']
#SCARY = ['The Nun','ANNABELE','IT','IT PART 2']
print("IF YOU LIKE Avengers Endgame type A, if you like the flash type B,if you like Jaws revenge type C,If you like the Nun type D")
x = input(">>>")
A = 0
B = 0
C = 0
D = 0
if x == "A":
	A = A + 1
elif x == "B":
	B = B + 1
elif x == "C":
	C = C + 1
elif x == "A":
	C = C + 1
print("IF YOU LIKE SHAZAM! type A, if you like ARROW type B,if you like Frozen type C,If you like Annabele type D")
x = input(">>>")
print("IF YOU LIKE Spider-man homecoming type A, if you like Legends of tomorrow type B,if you like Frozen 2 type C,If you like IT type D")
x = input(">>>")
print("IF YOU LIKE Spider man into the spiderverse type A, if you like SuperGirl type B,if you like CATS type C,If you like IT part 2 type D")
if A > B and A > C and A > D:
	print("You like Action Movies")
elif B > A and B > C and B > D:
	print("You like SciFi Movies")
elif C > B and C > A and C > D:
	print("You like Bad Movies")
elif D > A and D > C and D > B:
	print("You Like Scary Movies")

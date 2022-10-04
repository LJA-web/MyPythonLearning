#魔术师
print("魔术师")
def show_magicians(names):
	for name in names:
		print(name.title())

names = ['david copperfield', 'david blaine', 'liu qian']
show_magicians(names)


#了不起的魔术师
print("\n了不起的魔术师")
def make_great(a_names, b_names):
	while a_names:
		c_name = "the Great " + a_names.pop()
		b_names.append(c_name)

names = ['david copperfield', 'david blaine', 'liu qian']
b_names = []
make_great(names, b_names)
show_magicians(b_names)
print("\nlist names")
show_magicians(names)


#不变的魔术师
print("\n不变的魔术师")
def make_great(a_names, b_names):
	while a_names:
		c_name = "the Great " + a_names.pop()
		b_names.append(c_name)

names = ['david copperfield', 'david blaine', 'liu qian']
b_names = []
make_great(names[:], b_names)
show_magicians(b_names)
print("\nlist names")
show_magicians(names)

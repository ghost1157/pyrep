filename = 'input/txt'
lz = "local-zone: "
ld = "local-data: "
quotes = '"'
nd = " nodefault"
a = " A 127.0.0.1"
with open("input.txt", "r") as nameslst:
	with open("output.txt", "w") as readylist:
		for line in nameslst:
			line = line.strip()
			line = lz + quotes + line + "." + quotes + nd + "\n" + ld + quotes + line + "." + a + quotes + "\n"
			readylist.writelines(line)

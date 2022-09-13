import random;

x = [1, 2, 3, 4, 5];
a = 0;
f = f"{x[random.randint(0,4)]} {x[random.randint(0,4)]} {x[random.randint(0,4)]} {x[random.randint(0,4)]} {x[random.randint(0,4)]}";
while (f != "1 2 3 4 5"):
	print(f);
	a = a+1;
	f = f"{x[random.randint(0,4)]} {x[random.randint(0,4)]} {x[random.randint(0,4)]} {x[random.randint(0,4)]} {x[random.randint(0,4)]}";
	if (f == "1 2 3 4 5"):
		print(f"1 2 3 4 5\nYOU GOT IT\nIt took {a} attempts");
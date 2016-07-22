f = open("c:\python\countries.txt","r")
countries = []
for line in f:
	line = line.strip()
	countries.append(line)
	#print(line)
f.close()
print(countries)
print("Number of countries " + str(len(countries)))

for country in countries:
	#print(country)
	#print("#######")
	if country[0] == "T":
		print(country)
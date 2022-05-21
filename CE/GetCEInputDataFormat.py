f1 = open("./data1.txt")
f2 = open("./data2.txt")

data1 = f1.readlines()[0].split(" ")
data2 = f2.readlines()[0].split(" ")
f1.close()
f2.close()

len = min(len(data1),len(data2))

print (data1)
print (data2)

ce_data_format = ""
for i in range(len):
    ce_data_format+=data1[i]
    if i < len-2:
        ce_data_format+=','
print "ce data1:"
print (ce_data_format)

ce_data_format = ""
for i in range(len):
    ce_data_format+=data2[i]
    if i < len-2:
        ce_data_format+=','
print "ce data2:"
print (ce_data_format)

search_pattern = ""
search_data = ""
for i in range(len):
    if data1[i] == data2[i]:
        search_data+="\\x"+data1[i]
        search_pattern+= "x"
    else:
        search_data+="\\x"+data1[i]
        search_pattern+= "?"

print "search data:"
print search_data
print "search pattern"
print search_pattern
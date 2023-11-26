# dictionary is nothing but key value pairs
#d1 = {}   #dictionary
#d2 = ()   #tuple
#print(type(d1))
#print(type(d2))
#d22 ={"India":"Hindi","England":"English","Turkey":"Turkish"}
#print(d22["England"])
d22 ={"England":"English","Turkey":"Turkish",
      "India":{"H":" Hindi "," M ":" Marathi "," T ": "Telgu"}}
(d22["India"]["H"])
d22['pune']= 'marathi'
d22["banglore"]="kannad"
#print(d22)
del d22["banglore"]
#print(d22)
d4 = d22.copy()
del d4 ["England"]
print(d4)
print(d22.get("Turkey"))
d22.update({"Saudi":"Arabi"})
print(d22)
print(d22.keys())
print(d22.items())
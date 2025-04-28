#dic
{'hej':5,
'b':'c'}

image = {'color':'greyscale', 'size': 289983, 'type': 'jpg', 'address': 'https://upload.wikimedia.org/commons/7/7b/Moby_Dick_p510_illustration.jpg',
510: 'page in book'}

##print(image['address'])

##fst_sentence = { 1:'Call',2:'me',3:'Ishmeal' }

image['color'] = 'Black&White'
image['color'] = 'red'
#del image['color']
#print(image)

a = list(range(5))
for idx, el in enumerate(a):
    print(idx,el)


for key, value in image.items():
    print(key,value)

##print kun value via select alle værdier
for value in image.values():
    print(value)

##print kun value via select kun value
for _,value in image.items():
    print(value)

#'size' in image.values() return false!

## den kan ikke finde 'Python' så printer unknown
color_val = image.get('Python','unknown') 
print(color_val)



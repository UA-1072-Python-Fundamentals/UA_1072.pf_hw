import re
text = "IT academy softserve it IT ada"
resul = re.match("IT", text)
print(resul)
resul = re.search("IT", text)
print(resul)
print(resul.group(0))
resul = re.search("academy", text)
print(resul)
resul = re.findall("IT", text)
print(resul)
resul = re.findall("IT", text)
print(resul)
resul = re.findall("a.a", text)
print(resul)
text = "ererxerxxxerxxyxx"
resul = re.findall("erx*", text)
print(resul)
resul = re.findall("erx+", text)
print(resul)
resul = re.findall("rx{2}", text)
print(resul)




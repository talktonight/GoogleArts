from PIL import Image
foo = Image.open("sedutor.jpeg")

foo.save("sedutor85.jpeg", optimize=True, quality=85)
foo.save("sedutor75.jpeg", optimize=True, quality=75)
foo.save("sedutor65.jpeg", optimize=True, quality=65)
foo.save("sedutor55.jpeg", optimize=True, quality=55)

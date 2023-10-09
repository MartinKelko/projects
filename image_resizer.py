from PIL import Image

def resize_image(sizel, size2) :
    image = Image.open('voldis.jpeg')

    print(f"Current size : {image.size}" )

    resized_image = image.resize(( sizel, size2))

    resized_image.save('voldis-resized' + str(size1) + '.jpeg')

size1 = int(input( ' Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1, size2)

resize_image()

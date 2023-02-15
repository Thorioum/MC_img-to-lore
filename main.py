from PIL import Image
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y)) #returns the rgb values of the pixel coordinate
    a = (r, g, b)
    return a
print("type the item you want to put this on:")
item = input()
print("type the full path to the image you would like to use (Ex: C:\picture\example.jpg, __NO PNGS__):")
path = input()
img = Image.open(path, 'r')
print("please specify the size of the image you want to scale it to (keeping it below 2000 total pixels is a good guide):")
print("type width: ")
w = input()
print("type height: ")
h = input()
image = img.resize((int(w), int(h)), Image.Resampling.LANCZOS)
pix = image.load()
image.show();
command = "/give @p " + item + "{display:{Lore:["
i = 0
j = 0
ran = 0
while i < image.height:
    command += "\'"
    command += "["
    while j < image.width:
        r,g,b = pix[j,i]
        rgb = r,g,b
        hexval = rgb_to_hex(rgb)

        squares = "█"
        while(1) :
            if(j==image.width-1) : #stops index out of range exceptions
                break;
            r,g,b = pix[j,i]
            r1,g1,b1 = pix[j+1,i]
            rgb = r,g,b
            rgb2 = r1,g1,b1
            if(rgb_to_hex(rgb) == rgb_to_hex(rgb2)):
                j+=1
                squares += "█" #if the pixel next to it is the same color it doesnt create a new text parameter and instead adds another square
            else:
                break


        command += ("{\"text\":\"" + squares + "\",\"color\":\"#" + hexval + "\"") #adds the text with the hex value

        if ran == 0:
            command += ",\"italic\":false" # sets the first text on the line to not italic
        ran = 1
        command += "}"
        if j != image.width-1:
            command += ","

        j+=1

    command += "]"
    command += "\'"
    if i != image.height-1: 
        command += ","

    i+=1
    j=0
    ran = 0

command += "]}} 1"
print(command)

from PIL import Image
import pyperclip
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y)) #returns the rgb values of the pixel coordinate
    a = (r, g, b)
    return a
print("type the item you want to put this on:")
item = input()
print("type the full path to the image you would like to use (Ex: C:\picture\example.jpg):")
path = input()
img = Image.open(path, 'r')
print("please specify the size of the image you want to scale it to (keeping it below 2000 total pixels is a good guide for keeping it in a command block)\n RES 106x47 will fill an entire 1920x1080 gui scale 2 minecraft screen:")
print("type width: ")
w = input()
print("type height: ")
h = input()
image = img.resize((int(w), int(h)), Image.Resampling.LANCZOS)
pix = image.load()
image.show();
command = "{display:{Lore:["
i = 0
j = 0
ran = 0
isPng = 0 #checks if the image ends in png
if "png" in path:
    isPng = 1
while i < image.height:
    command += "\'"
    command += "["
    while j < image.width:
        if isPng == 1:
            r,g,b,a = pix[j,i]
            rgb = r,g,b
            hexval = rgb_to_hex(rgb)
        else:
            r,g,b = pix[j,i]
            rgb = r,g,b
            hexval = rgb_to_hex(rgb)

        squares = "█"
        while(1) :
            if(j==image.width-1) : #stops index out of range exceptions
                break;
            if isPng == 1:
                r,g,b,a = pix[j,i]
                r1,g1,b1,a1 = pix[j+1,i]
                rgb = r,g,b
                rgb2 = r1,g1,b1
            else:
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
command += "]}}"
pyperclip.copy(command)
print("/give @p " + item + command)
print("nbt data copied to clipboard")

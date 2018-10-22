from PIL import Image

infile = Image.open("ballpit.jpg")
infile = infile.convert('RGB')

outfile = Image.new("RGB", infile.size)


from Pillow import Image
import json

#create sample file. You don't have to do this in your real code.
img = Image.new("RGB", (10,10), "red")

#decode.
s = img.tobytes().decode("latin1")

#serialize.
with open("outputfile.json", "w") as file:
    json.dump(s, file)
import shutil
import os
from PIL import Image, ImageColor, ImageChops

def main():
  blocks = []
  with open("layers.txt", "r") as f:
    for line in f.readlines():
      if "#" in line:
        line, _ = line.split("#", 1)
      line = line.strip()
      if line == "": continue
      name, layers = line.split(":", 1)
      name = name.strip()
      layers = [(*l.strip().split(" "), ) for l in layers.split(",")]
      blocks.append((name, layers))
  for name, layers in blocks:
    img = None
    with Image.open("Layers/" + layers[0][0] + ".png") as im:
      img = Image.new("RGBA", im.size, (0, 0, 0, 0))
    for path, tint in layers:
      with Image.open("Layers/" + path + ".png") as layer:
        layer = layer.convert("RGBA")
        tint_img = Image.new("RGBA", layer.size, ImageColor.getrgb("#" + tint))
        img.alpha_composite(ImageChops.multiply(layer, tint_img))
    img.save(name + ".png")
    # os.remove("Blocks/" + name + ".png")
  l = []
  with open("texture_names.orig.txt", "r") as fr:
    with open("texture_names.txt~", "w+") as fw:
      for line in fr.readlines():
        line = line.strip()
        if line == "": continue
        if line.startswith("#"): continue
        name, _ = line.split(" ", 1)
        if name == "set": continue
        l.append(name)
        fw.write(line + "\n")
      for name in l:
        fw.write(f"set {name} nearest_neighbor true\n")
  shutil.move("texture_names.txt~", "texture_names.txt")


if __name__ == "__main__":
  main()

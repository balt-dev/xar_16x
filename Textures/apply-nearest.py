import shutil

def main():
  l = []
  with open("texture_names.orig.txt", "r") as fr:
    with open("texture_names.txt~", "w+") as fw:
      for line in fr.readlines():
        line = line.strip()
        if line == "": continue
        if line.startswith("#"): continue
        name, _ = line.split(" ", 1)
        l.append(name)
        fw.write(line + "\n")
      for name in l:
        fw.write(f"set {name} nearest_neighbor true\n")
  shutil.move("texture_names.txt~", "texture_names.txt")


if __name__ == "__main__":
  main()

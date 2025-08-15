from pathlib import Path
from PIL import Image

def main():
	with open("todo.png", "rb") as todo:
		todo_data = todo.read()

	total_count = 0
	small_count = 0
	for path in Path(".").rglob("*.png"):
		if "Layers" in f"{path}": continue
		small = False
		total_count += 1
		try:
			with Image.open(path) as im:
				if im.width <= 64 and im.height <= 32:
					small = True
			if small:
				small = False
				with open(path, "rb") as p:
					if p.read() != todo_data:
						small = True
		except:
			pass
		if small:
			small_count += 1
		else:
			with open(path, "wb") as f:
				f.write(todo_data)
				
	print(f"{(small_count / total_count * 100):.2f}% done ({small_count} / {total_count})")

if __name__ == "__main__":
	main()
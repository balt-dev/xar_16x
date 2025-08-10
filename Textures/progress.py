from pathlib import Path
from PIL import Image

def main():
	total_count = 0
	small_count = 0
	for path in Path(".").rglob("*.png"):
		if "Layers" in f"{path}": continue
		small = False
		total_count += 1
		try:
			with Image.open(path) as im:
				if im.width <= 64 and im.height <= 32:
					small_count += 1
					small = True
		except:
			pass
		if not small:
			with open(path, "w") as f:
				pass
				
	print(f"{(small_count / total_count * 100):.2f}% done ({small_count} / {total_count})")

if __name__ == "__main__":
	main()
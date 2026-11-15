from PIL import Image, ImageDraw
import pandas as pd

df = pd.read_csv('DS3.txt', sep='\\s+', header=None, engine = 'python')
print(df.head(5)) # 5 значень для перевірки відповідності даниїх

WIDTH, HEIGHT = 960, 540

img = Image.new("RGB", (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(img)

for index, row in df.iterrows():
  x = int(row[0]) 
  y = int(row[1])  

  # Перетворення координат:
  # За умовою (0,0) у нижньому лівому куті, вісь Y вгору.
  # У Pillow (0,0) у верхньому лівому куті, вісь Y вниз.
  canvas_x = x
  canvas_y = HEIGHT - 1 - y

  if 0 <= canvas_x < WIDTH and 0 <= canvas_y < HEIGHT:
    draw.point((canvas_x, canvas_y), fill="black")

output_file = "result_DS3.png"
img.save(output_file)
print(f"Зображення збережено як '{output_file}'.")

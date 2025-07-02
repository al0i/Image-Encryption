import time
start_total_time = time.time()

from PIL import Image
from utils.spiral_map_pixels import spiral_map_pixels

img = Image.open('img/hylson2.png')
start_snapshot_time = time.time()
spiral_map = spiral_map_pixels(img)
end_snapshot_time = time.time()
print("Time to spiral_map:",end_snapshot_time-start_snapshot_time)


start_snapshot_time = time.time()
for i in spiral_map:
    img.putpixel(i, spiral_map[i])
end_snapshot_time = time.time()
print("Time to set pixels in spiral:",end_snapshot_time-start_snapshot_time)

start_snapshot_time = time.time()
img.save('img/output.png')
end_snapshot_time = time.time()
print("Image generated successfully.")
print("Time to save image:",end_snapshot_time-start_snapshot_time)

end_total_time = time.time()
print("Total time:", end_total_time-start_total_time)
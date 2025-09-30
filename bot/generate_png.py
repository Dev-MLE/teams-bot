from PIL import Image

# Generate color.png (192x192)
color_img = Image.new("RGB", (192, 192), color=(0, 120, 212))  # Teams blue
color_img.save("color.png")

# Generate outline.png (32x32)
outline_img = Image.new("RGB", (32, 32), color=(255, 255, 255))  # White square
outline_img.save("outline.png")

print("color.png and outline.png created successfully.")

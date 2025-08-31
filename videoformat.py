import imageio
import os

# Define the directory where your images are stored
image_folder = "/home/ivision/CRN/r50_bbox1/"  

# Get all images sorted in order
images = []
for i in range(118):  # Since you have 60 images
    filename = os.path.join(image_folder, f"index-{i}.png")
    images.append(imageio.imread(filename))

# Save the images as a GIF
output_gif_path = os.path.join(image_folder, "output.gif")
imageio.mimsave(output_gif_path, images, duration=0.1)  # Adjust duration as needed

print(f"GIF saved at: {output_gif_path}")

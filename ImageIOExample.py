import imageio
import cv2
import os

# List of images
parent = 'Images/'
print(os.listdir(parent))

images = os.listdir(parent)
# Create a list to store the images
frames = []

# Open each image file and append it to the frames list
for image in images:
    img = os.path.join(parent, image)
    im_read = cv2.imread(img)
    im_read = cv2.cvtColor(im_read, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(src=im_read, dsize=(800, 800), interpolation=cv2.INTER_AREA)
    frames.append(resized)  # Append the resized image directly

# Save the frames as a GIF
imageio.mimsave('output.gif', frames, duration=5.00)

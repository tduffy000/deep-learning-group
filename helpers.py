import matplotlib.pyplot as plt

def plotImages(images_arr, number_images=5, img_size=20):
    fig, axes = plt.subplots(1, number_images, figsize=(img_size, img_size))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()

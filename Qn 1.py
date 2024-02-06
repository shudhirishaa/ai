import numpy as np
import cv2

def naive_template_matching(image, template):
    image_height, image_width = image.shape
    template_height, template_width = template.shape

    result = np.zeros((image_height - template_height + 1, image_width - template_width + 1))

    for y in range(result.shape[0]):
        for x in range(result.shape[1]):
            region = image[y:y + template_height, x:x + template_width]
            result[y, x] = np.sum(region * template)

    return result

def normalized_cross_correlation(image, template):
    image_height, image_width = image.shape
    template_height, template_width = template.shape

    result = np.zeros((image_height - template_height + 1, image_width - template_width + 1))

    template_mean = np.mean(template)
    template_std = np.std(template)

    for y in range(result.shape[0]):
        for x in range(result.shape[1]):
            region = image[y:y + template_height, x:x + template_width]
            region_mean = np.mean(region)
            region_std = np.std(region)
            result[y, x] = np.sum((region - region_mean) * (template - template_mean)) / (template_std * region_std)

    return result

# Example usage:
if __name__ == "__main__":
    # Load your image and template matrices using any method you prefer
    image = np.array([[1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 10],
                      [11, 12, 13, 14, 15],
                      [16, 17, 18, 19, 20]])

    template = np.array([[8, 9],
                         [13, 14]])

    # Uncomment one of the following lines to use the desired template matching algorithm
    result = naive_template_matching(image, template)
    # result = normalized_cross_correlation(image, template)

    print("Result:")
    print(result)

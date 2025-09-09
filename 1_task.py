import cv2 

def switch_r_g(image):
  """
    Swap the red and green channels of a BGR image.

    Args:
        image (numpy.ndarray): Input image in BGR channel order (as from cv2.imread).

    Returns:
        numpy.ndarray: Output image with the red and green channels exchanged (still BGR).
    """
  b, g, r = cv2.split(image)
  merged_image = cv2.merge((b, r, g))
  return merged_image

if __name__ == "__main__":
  image = cv2.imread('cat.jpg') 
  cv2.imshow('Merged Image', switch_r_g(image))
  cv2.waitKey(0)

  cv2.destroyAllWindows()

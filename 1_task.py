import cv2
import sys
import os

class ImageProcessingError(Exception):
    pass

class FileNotFoundError(ImageProcessingError):
    pass

class ImageLoadError(ImageProcessingError):
    pass

def switch_r_g(image):
    """
    Swap the red and green channels of a BGR image.

    Args:
        image (numpy.ndarray): Input image in BGR channel order (as from cv2.imread).

    Returns:
        numpy.ndarray: Output image with the red and green channels exchanged (still BGR).
    """
    if image is None:
        raise ValueError("Input image cannot be None")
    
    b, g, r = cv2.split(image)
    merged_image = cv2.merge((b, r, g))
    return merged_image


def check_image(image_path):
    """
    Check if image exists and can be loaded.
    
    Args:
        image_path (str): Path to the image file.
        
    Raises:
        FileNotFoundError: If file doesn't exist or is not a file
        InvalidFileFormatError: If file format is not supported
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Файл '{image_path}' не существует.")
    
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"'{image_path}' не является файлом.")

def load_image(image_path):
    """
    Load image from file path.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        numpy.ndarray: Loaded image
        
    Raises:
        ImageLoadError: If image cannot be loaded
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ImageLoadError(f"Не удалось загрузить изображение '{image_path}'. Возможно, файл поврежден или путь указан неверно.")
    return image

def main():
    try:
        image_path = input("Введите путь к изображению: ").strip().strip('"\'')
        check_image(image_path)
        
        image = load_image(image_path)
        
        processed_image = switch_r_g(image)
        
        cv2.imshow('Original', image)
        cv2.imshow('R-G Switched', processed_image)
        
        
        base_name, ext = os.path.splitext(image_path)
        output_path = f"{base_name}_switched{ext}"
        cv2.imwrite(output_path, processed_image)
        print(f"Обработанное изображение сохранено как: {output_path}")
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except ImageProcessingError as e:
        print(f"Ошибка обработки изображения: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
        sys.exit(0)
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


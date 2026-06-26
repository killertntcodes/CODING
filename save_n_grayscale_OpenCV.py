import cv2

image = cv2.imread('colorful image.jpg')  # Replace with your image path

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_gray_image = cv2.resize(gray_image, (224, 224))  # Resize to 224x224

cv2.imshow('Resized Grayscale Image', resized_gray_image)

key = cv2.waitKey(0)

if key == ord('s'):  # Press 's' to save the image
    cv2.imwrite('resized_grayscale_image.png', resized_gray_image)
    print("Image saved as 'resized_grayscale_image.png'")
else:
    print("Image not saved.")

cv2.destroyAllWindows()
print(f"Resized grayscale image shape: {resized_gray_image.shape}")
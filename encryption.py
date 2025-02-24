import cv2
import os

def encrypt_image(image_path, secret_message, password):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0

    for char in secret_message:
        img[n, m, z] = d[char]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3  # Cycle through RGB channels

    cv2.imwrite("encryptedImage.jpg", img)
    print("Message encrypted successfully in 'encryptedImage.jpg'.")

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    message = input("Enter the secret message: ")
    password = input("Set a password for decryption: ")

    encrypt_image(image_path, message, password)
    os.system("start encryptedImage.jpg")  # Open the image (Windows)

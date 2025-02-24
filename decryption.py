import cv2

def decrypt_image(encrypted_image_path, original_message_length, password):
    img = cv2.imread(encrypted_image_path)
    
    if img is None:
        print("Error: Encrypted image not found!")
        return

    c = {i: chr(i) for i in range(255)}
    
    n, m, z = 0, 0, 0
    decrypted_message = ""

    pas = input("Enter the decryption password: ")
    
    if password == pas:
        for _ in range(original_message_length):
            decrypted_message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3  # Cycle through RGB channels
        
        print("Decrypted message:", decrypted_message)
    else:
        print("Authentication failed! You are not authorized.")

if __name__ == "__main__":
    encrypted_image_path = input("D:\Steganography\extact\output.bmp")
    original_message_length = int(input("Enter the length of the original message: "))
    password = input("Enter the password set during encryption: ")

    decrypt_image(encrypted_image_path, original_message_length, password)

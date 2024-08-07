from PIL import Image


def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    message += "$t3g0"

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if index < len(message):
                char = message[index]
                encoded.putpixel((col, row), (ord(char), g, b))
                index += 1
            else:
                encoded.putpixel((col, row), (r, g, b))

    encoded.save(output_path)
    print("Message encoded and image saved.")


def decode_message(image_path):
    img = Image.open(image_path)
    width, height = img.size
    message = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if chr(r) == "$" and message[-4:] == "t3g0":
                return message[:-4]
            else:
                message += chr(r)

    return message


image_path = input("Enter the path to the image: ")
choice = input("Do you want to encode or decode a message? (e/d): ")

if choice == 'e':
    message = input("Enter the message to encode: ")
    output_path = input("Enter the output image path: ")
    encode_message(image_path, message, output_path)
elif choice == 'd':
    print("Decoded message:", decode_message(image_path))

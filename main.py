import boto3
import cv2

s3 = boto3.client('s3')
camera = cv2.VideoCapture(0)
client=boto3.client('rekognition')
labels = []
recyclable_items = ["Tin", "Can", "Paper", "Aluminum", "Can", "Magazine", "Foil", "Carton", "Cardboard", "Book", "Box", "Letter", "Envelope", "Cup", "Text"]
trash_items = ["Food", "Bread", "Pizza", "Coffee", "Chips", "Chip", "Porcelain", "Coffee Cup", "Plastic Bag"]

def is_recyclable(labels):
    recycle_labels = 0
    trash_labels = 0
    for label in labels:
        if label in recyclable_items:
            recycle_labels += 1
        if label in trash_items:
            return "Trash"
    if recycle_labels > 0:
        return "Recycle"
    else:
        return "Trash"

for i in range(10):
    return_value, img = camera.read()

cv2.imwrite('picture.jpg', img)

with open('picture.jpg', 'rb') as image:
    response = client.detect_labels(Image={'Bytes': image.read()})
    for label in response["Labels"]:
        labels.append(label["Name"])
    labels = labels[:5]

print(is_recyclable(labels))
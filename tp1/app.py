import cv2
from pathlib import Path

image_path = Path(__file__).resolve().parent / "test_visage.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print(f"Erreur : {image_path} introuvable")
else:
    cv2.imshow("Mon image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
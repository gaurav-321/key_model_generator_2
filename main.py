import cv2
import numpy as np


def create_obj(vtx):
    with open("test.obj", 'w') as out:
        for i, vertex in enumerate(vtx):
            out.write(f"v {vertex[0]} {vertex[1]} 0\n")
        faces = [str(vtx.index(x) + 1) for x in vtx]
        out.write(f"f {' '.join(faces)}")


img = cv2.imread("asset/key.jpg")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_grey[img_grey < 249] = 0
ret, thresh_img = cv2.threshold(img_grey, 100, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_tuple = ((x, cv2.contourArea(x)) for x in contours)
contours_tuple = sorted(contours_tuple, reverse=True, key=lambda x: x[1])
valid_contour = []
for c, a in contours_tuple:
    if a > 1000:
        valid_contour.append(c)
img_contours = np.zeros(img.shape)

points = [list(x[0]) for x in valid_contour[1]]
vertices = [x for x in points]
create_obj(vertices)
cv2.drawContours(img_contours, valid_contour[1:2], -1, (0, 255, 0), 1)
for i in range(len(vertices)):
    copy = img_contours.copy()
    cv2.putText(copy, f"{i}", (vertices[i][0], vertices[i][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
    cv2.circle(copy, (vertices[i][0], vertices[i][1]), 3, (0, 0, 255), -1)
    cv2.imshow("key", copy)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        quit()

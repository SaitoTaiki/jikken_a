import cv2
import numpy as np
import matplotlib.pyplot as plt


# template matching
def Template_matching(img, template):
    # get original image shape
    H, W, C = img.shape

    # subtract mean BGR
    _img = img - np.mean(img, axis=(0, 1))

    # get template image shape
    Ht, Wt, Ct = template.shape

    # subtract mean BGR
    _template = template - np.mean(img, axis=(0, 1))

    # Templete matching
    # prepare x, y index
    i, j = -1, -1
    # prepare evaluate value
    v = -1

    for y in range(H - Ht):
        for x in range(W - Wt):
            # get ZNCC value
            # get numerator of ZNCC
            _v = np.sum(_img[y : y + Ht, x : x + Wt] * _template)
            # devided numerator
            _v /= (np.sqrt(np.sum(_img[y : y + Ht, x : x + Wt] ** 2)) * np.sqrt(np.sum(template ** 2)))

            # if ZNCC is max
            if _v > v:
                v = _v
                i, j = x, y

    out = img.copy()
    # draw rectangle
    cv2.rectangle(out, pt1=(i, j), pt2=(i+Wt, j+Ht), color=(0,0,255), thickness=1)
    out = out.astype(np.uint8)

    return out

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# Read templete image
template = cv2.imread("imori_part.jpg").astype(np.float32)

# Template matching
out = Template_matching(img, template)


# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

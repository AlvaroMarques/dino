import cv2
import numpy as np
from os import getcwd

def get_template(name):
    return cv2.cvtColor(cv2.imread(getcwd()+'/templates/'+name),cv2.COLOR_BGR2GRAY)

def get_matching(template,total,threshold=0.8,algorithm = cv2.TM_CCOEFF_NORMED):

    res = cv2.matchTemplate(total,template,algorithm)
    return np.where(res >= threshold)
def rectlize(matching,total,template):
    w,h = template.shape[::-1]
    for pt in zip(*matching[::-1]):
        cv2.rectangle(total, pt, (pt[0]+w,pt[1]+h),0,2)
    return total
if __name__ == "__main__":
    template = get_template('dino.png')
    total = get_template('gamedino3.png')

    rectlize(get_matching(template,total),total,template)
    cv2.imwrite(getcwd()+"/yu.png",rectlize(get_matching(template,total),total,template))

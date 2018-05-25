from get_screen import get_screen
import templatematching as tm
import cv2
templates = ['dino.png','duck.png','cactus1.png','cactus2.png','cactus3.png','cactus4.png','cactus5.png','cactus6.png','pter1.png','pter2.png']
templates = list(map(tm.get_template,templates))


while True:
    frame = get_screen()
    matches = [tm.get_matching(template,frame) for template in templates]
    if (True if any(any(len(i)>0 for i in j) for j in matches) else False):
        for template,match in zip(templates,matches):

            tm.rectlize(match, frame,template)
    cv2.imshow('WindowName', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

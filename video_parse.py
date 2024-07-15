import cv2

def get_frames():
    cap = cv2.VideoCapture('G:/Programming/JML_contest/jml_sources/rat.mp4')
    i = 0
    # a variable to set how many frames you want to skip
    frame_skip = 10
    # a variable to keep track of the frame to be saved
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            frame_count += 1
            cv2.imwrite('G:/Programming/JML_contest/jml_sources/test_'+str(frame_count*frame_skip)+'.jpg', frame)
            i = 0
            continue
        i += 1

    cap.release()
    cv2.destroyAllWindows()

get_frames()
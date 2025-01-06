import cv2
import numpy as np
import copy 

def create_frames():
    return

# generates an image
def draw_board(letters, img_dims, lett_per_row, font_face, thickness, font_scale):
    img = np.zeros((img_dims, img_dims, 3), np.uint8)
        
    for i, c in enumerate(letters):
        row, col = i // lett_per_row, i % lett_per_row
        lett_dims = cv2.getTextSize(c, font_face, font_scale, thickness)[0]
        cell_dims = img_dims // lett_per_row
        x = col*(cell_dims) + (cell_dims // 2) - (lett_dims[0] // 2)
        y = row*(cell_dims) + (cell_dims // 2) + (lett_dims[1] // 2)
        cv2.putText(img, letters[i], (x, y), font_face, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
    return img

# augments an image
def draw_frame(frame, img_dims, lett_per_row, thickness, board_img):
    # preserve the original img
    board_copy = copy.deepcopy(board_img)
    for i in range(len(frame[0]) - 1):
        let_idx = frame[0][i]
        # print(let_idx)
        row, col = let_idx // lett_per_row, let_idx % lett_per_row
        cell_dims = img_dims // lett_per_row
        x1 = col*(cell_dims) + (cell_dims // 2)
        y1 = row*(cell_dims) + (cell_dims // 2)
        
        let_idx = frame[0][i + 1]
        row, col = let_idx // lett_per_row, let_idx % lett_per_row
        x2 = col*(cell_dims) + (cell_dims // 2)
        y2 = row*(cell_dims) + (cell_dims // 2)
    
        img = cv2.arrowedLine(board_copy, (x1, y1), (x2, y2), (0, 255, 0), thickness)

    return img

# returns list of imgs
def draw_frames(frames, img_dims, lett_per_row, thickness, board_img):
    rendered_frames = []
    for frame in frames:
        frame_img = draw_frame(frame, img_dims, lett_per_row, thickness, board_img)
        cv2.imshow('frame', frame_img)
        cv2.waitKey(75)
        rendered_frames.append(frame_img)
    return rendered_frames

# creates mp4
def create_mp4(frames, img_dims):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 10.0, (img_dims, img_dims), True)
    
    for frame in frames:
        out.write(frame)
        
    out.release()
    cv2.destroyAllWindows()
    
    return out

# plays mp4
def play_video(cap):
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
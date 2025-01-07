import cv2
import numpy as np
import copy 

def create_frames():
    return

def draw_word(thickness, font, font_scale, img, word_selected):
    textsize = cv2.getTextSize(word_selected, font, font_scale, thickness)[0]
    textX = (img.shape[1] - textsize[0]) // 2
    textY = (img.shape[0] + textsize[1]) // 2

    # add text centered on image
    cv2.putText(img, word_selected, (textX, textY ), font, font_scale, (255, 255, 255), 2)

def draw_arrows(frame, img_dims, lett_per_row, thickness, path_selected, img):
    for i in range(len(frame[0]) - 1):
        let_idx = path_selected[i]
        # print(let_idx)
        row, col = let_idx // lett_per_row, let_idx % lett_per_row
        cell_dims = img_dims // lett_per_row
        x1 = col*(cell_dims) + (cell_dims // 2)
        y1 = row*(cell_dims) + (cell_dims // 2)
        
        let_idx = frame[0][i + 1]
        row, col = let_idx // lett_per_row, let_idx % lett_per_row
        x2 = col*(cell_dims) + (cell_dims // 2)
        y2 = row*(cell_dims) + (cell_dims // 2)

        cv2.arrowedLine(img, (x1, y1), (x2, y2), (0, 255, 0), thickness)
        
def draw_letters(letters, img_dims, lett_per_row, font_face, thickness, font_scale, img):
    for i, c in enumerate(letters):
        row, col = i // lett_per_row, i % lett_per_row
        lett_dims = cv2.getTextSize(c, font_face, font_scale, thickness)[0]
        cell_dims = img_dims // lett_per_row
        x = col*(cell_dims) + (cell_dims // 2) - (lett_dims[0] // 2)
        y = row*(cell_dims) + (cell_dims // 2) + (lett_dims[1] // 2)
        cv2.putText(img, letters[i], (x, y), font_face, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

def draw_words_found(font_face, thickness, font_scale, frame, img):
    words_found = frame[2]
    # (133, 12) - theoretical max dimension of a word
    x = 0
    y = 12
    for word in words_found:
        word = word.lower()
        cv2.putText(img, word, (x, y), font_face, (font_scale - 1) / 2, (0, 0, 255), thickness - 1)
        y += 12
        # start new column at end of img
        if y >= 500: 
            x += 133
            y = 12
    
def draw_frame(frame, img_dims, lett_per_row, thickness, font, font_scale, font_face, board_letters):
    path_selected = frame[0]
    word_selected = frame[1]
    img = np.zeros((img_dims, img_dims, 3), np.uint8)
    
    # draws words found so far
    draw_words_found(font_face, thickness, font_scale, frame, img)
    
    # draws letters
    draw_letters(board_letters, img_dims, lett_per_row, font_face, thickness, font_scale, img)
    
    # draws arrows
    draw_arrows(frame, img_dims, lett_per_row, thickness, path_selected, img)
    
    # draws word selected
    draw_word(thickness, font, font_scale, img, word_selected)

    return img
    
# returns list of imgs
def draw_frames(frames, img_dims, lett_per_row, thickness, font, font_scale, board_letters, font_face):
    rendered_frames = []
    for frame in frames:
        frame_img = draw_frame(frame, img_dims, lett_per_row, thickness, font, font_scale, font_face, board_letters)
        cv2.imshow('frame', frame_img)
        cv2.waitKey(15)
        rendered_frames.append(frame_img)
    return rendered_frames

# creates mp4
def create_mp4(frames, img_dims):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (img_dims, img_dims), True)
    
    for frame in frames:
        out.write(frame)
        
    out.release()
    cv2.destroyAllWindows()
    
    return out

# plays mp4 ( not used )
def play_video(cap):
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
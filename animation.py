from PIL import Image, ImageTk


class Animation:
    def __init__(self, filename):
        self.image = Image.open(filename)
        self.frames = []

        seq = []
        frame_cnt = self.image.n_frames
        for i in range(frame_cnt - 1):
            seq.append(self.image.copy())
            self.image.seek(len(seq))

        first = seq[0].convert('RGBA')
        self.frames.append(ImageTk.PhotoImage(first))

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

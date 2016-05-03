import itertools

colorlist = [
     (255, 20, 147),
     (186, 85, 211),
     (102, 205, 170),
     (144, 238, 144),
     (0, 128, 0),
     (255, 69, 0),
     (123, 104, 238),
     (255, 215, 0),
     (154, 205, 50),
     (128, 128, 0),
     (0, 255, 255),
     (32, 178, 170),
     (127, 255, 212),
     (238, 130, 238),
     (138, 43, 226),
     (210, 105, 30),
     (255, 127, 80),
     (255, 0, 0),
     (255, 165, 0),
     (218, 165, 32),
     (240, 128, 128),
     (255, 228, 181),
     (0, 250, 154),
     (0, 191, 255),
     (165, 42, 42),
     (135, 206, 250),
     (240, 255, 255),
     (189, 183, 107),
     (107, 142, 35),
     (127, 255, 0),
     (100, 149, 237),
     (255, 160, 122)]

def yieldMaskColor():
    for c in itertools.cycle(colorlist):
        yield c

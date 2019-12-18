from manimlib.imports import *

class FlipTransform(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "show_coordinates": False,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 3,
    }
    def construct(self):
        transform = [[1, 1], [0, 1]]
        self.setup()
        self.wait(1)
        self.apply_matrix(transform)
        self.wait(2)
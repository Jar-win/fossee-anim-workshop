from manimlib.imports import *

class FancyCurve(Scene):
    def construct(self):
        a = 1
        b = -2
        curve = ParametricFunction(
                    lambda t: np.array([
                    (a+b)*np.cos(TAU*t) + b*np.cos(TAU*(a + b)/b*t),
                    (a + b)*np.sin(TAU*t) + b*np.sin(TAU*(a + b)/b*t),
                    0,
                    ]),
                    color = BLUE_C,
                    stroke_width = 2,
                )
        curve1 = ParametricFunction(
                    lambda t: np.array([
                    ((a+b)*np.cos(-TAU*t) + b*np.cos(-TAU*(a + b)/b*t)),
                    ((a + b)*np.sin(-TAU*t) + b*np.sin(-TAU*(a + b)/b*t)),
                    0,
                    ]),
                    color = BLUE_C,
                    stroke_width = 2,
                )
        self.play(ShowCreation(curve))
        self.play(ShowCreation(curve1))
        self.wait(2)



class ButterFly(Scene):
    def construct(self):
            butterfly = ParametricFunction(
            lambda t: np.array([
                (np.sin(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
                (np.cos(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
                0
            ]),
             t_min = 0, t_max = 40, step_size = 0.04, color = YELLOW
            )
            self.play(ShowCreation(butterfly),run_time=5)


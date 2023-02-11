from manim import *

class benAmiCircle(ImplicitFunction):
    def __init__(
        self,
        middle: Dot,
        radius: float = 1.0,
        color=GREEN,**kwargs
        ):
            self.__middle = middle
            a = middle.get_x()
            b = middle.get_y()
            super().__init__(
                func=lambda x, y: (x - a)**2 + (y-b)**2 - radius**2,
                color=color,
                **kwargs
            )


    def get_middle(self):
        return self.__middle
from manim import *

class Parabola(ImplicitFunction):
    def __init__(self, p_value=1, color=RED, **kwargs):
        """
        Creates a parabola in the form of y^2 = 2px

        Parameters
        -----------
        p_value - the p value of the parabola

        color - the color of the parabola

        **kwargs
        """
        self.__p_value = p_value
        super().__init__(
            lambda x, y: y**2 - 2*p_value*x,
            color=color,
            **kwargs
            )

    def get_p(self) -> int:
        return self.__p_value

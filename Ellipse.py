from manim import *

class benAmiEllipse(ImplicitFunction):
    def __init__(
        self,
        a: int,
        b: int,
        color=BLUE,
        **kwargs
        ):
        """
        A new ellipse class for manim

        **If a and b are the same will output a circle**

        This alternative exists so i could define ellipse with the a and b variables to make it easy on me when animating math homework

        Ellipse is in the form of: (X/a)^2 + (Y/b)^2 = 1

        Parameters
        ----------
        a - parameter a is the a variable in the ellipse equation

        b - parameter b is the b variable in the ellipse equation

        color - the color of the ellipse

        **kwargs"""
        self.__a = a
        self.__b = b

        super().__init__(
            func=lambda x, y: (x/a)**2 + (y/b)**2 - 1,
            color=color,
            **kwargs
            )


    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

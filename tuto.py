"""

https://www.reddit.com/r/manim/

good example
https://github.com/LalitPatidar/Mathmerizer
https://gist.github.com/Adirockzz95/06649145d7e6c4c147c02459fd2bc5af
https://medium.com/@a.ydobon/manim-examples-3ec2a6e985c5

latex

https://tex.stackexchange.com/questions/8857/how-to-type-special-accented-letters-in-latex

renderer
https://quicklatex.com/


"""
# from big_ol_pile_of_manim_imports import *
from manimlib.imports import *
import math


class Shapes(Scene):
    # A few simple shapes
    def construct(self):
        # circle = Circle()
        arc = Arc(start_angle=PI / 2, angle=PI / 3)
        poly = RegularPolygon(n=8, start_angle=0)
        square = Square()
        line = Line(np.array([3, 0, 0]), np.array([5, 0, 0]))
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, -1, 0]))

        # self.add(line)
        self.play(ShowCreation(arc))
        self.play(FadeOut(arc))

        # self.add(poly)
        self.play(ShowCreation(poly))
        # self.play(FadeOut(circle))
        # self.play(GrowFromCenter(square))
        # self.play(Transform(square, triangle))


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class Equation(Scene):
    def construct(self):
        title = TextMobject("Le discriminant").to_edge(UP).scale(1.5)
        self.play(Write(title), run_time=1)

        equation = TexMobject("a", "x^2 + bx + c = 0")
        equation.move_to(2 * UP)
        self.play(Write(equation))
        box_a = SurroundingRectangle(equation[0]).set_color(GREEN)
        self.play(ShowCreation(box_a))

        a_not_null = TexMobject("a \\neq 0")
        a_not_null.next_to(box_a, DOWN)
        self.play(Write(a_not_null))
        self.wait(1)

        a_not_null.generate_target()
        a_not_null.target.scale(0.8).to_edge(LEFT).shift(UP)
        self.play(MoveToTarget(a_not_null))

        step_2 = TexMobject("a \\left[ ", "x^2 + {b \\over a}x", " + {c \\over a} \\right] = 0")
        step_2.next_to(equation, DOWN)
        self.play(Write(step_2))
        accolade = Brace(step_2[1], BOTTOM)
        identity_text = accolade.get_text("Identit\\'e remarquable ?")
        self.play(GrowFromCenter(accolade), Write(identity_text))
        self.wait()

        self.remove(title)
        self.remove(equation)
        self.remove(box_a)
        step_2.to_edge(UP)
        self.remove(accolade)
        self.remove(a_not_null)
        self.remove(identity_text)

        box_a = SurroundingRectangle(step_2[1]).set_color(GREEN)
        self.play(ShowCreation(box_a))

        identity_1_rhs = TexMobject("= a^2 + 2ab + b^2")
        identity_1_rhs.move_to(UP * 1.8)
        identity_1_lhs = TexMobject("(a + b)^2 ")
        identity_1_lhs.next_to(identity_1_rhs, LEFT)
        self.play(
            Write(identity_1_lhs),
            Write(identity_1_rhs),
        )

        identity_2_lhs = TexMobject("(x + {b \\over 2a})^2 ")
        identity_2_rhs = TexMobject("= x^2 + ", "2", "{x{b \\over ", "2", "a}} + \\left( {b \\over 2a} \\right) ^2")
        identity_2_rhs.next_to(identity_1_rhs, DOWN, aligned_edge=LEFT)
        identity_2_lhs.next_to(identity_2_rhs, LEFT)
        self.play(Write(identity_2_lhs))
        self.wait()
        self.play(Write(identity_2_rhs))

        self.wait()
        # simplify the 2
        self.play(
            FadeOut(identity_2_rhs[1]),
            FadeOut(identity_2_rhs[3]),
        )

        identity_3_rhs = TexMobject("= ", "x^2 + {b \\over a}x ", "+ {b^2 \\over 4a^2}")
        identity_3_rhs.next_to(identity_2_rhs, DOWN, aligned_edge=LEFT)
        self.play(Write(identity_3_rhs))
        self.wait()

        equal = TexMobject("= ").next_to(identity_3_rhs, 2.0*DOWN, aligned_edge=LEFT)
        equal.shift(np.array([0.0, -0.5, 0.0]))
        self.play(Write(equal))
        b_over_a = identity_3_rhs[1].copy()
        animation = ApplyMethod(b_over_a.next_to, equal, LEFT)
        self.play(animation)
        self.wait()

        id2 = identity_2_lhs.copy()
        animation = ApplyMethod(id2.next_to, equal, RIGHT)
        self.play(animation)
        self.wait()

        b_square = identity_3_rhs[2].copy()
        minus_b_square = TexMobject("- {b^2 \\over 4a^2}")
        minus_b_square.next_to(id2, RIGHT)
        self.play(Transform(b_square, minus_b_square))

        # identity_4_lhs = TexMobject("x^2 + {b \\over a}x ")
        # identity_4_rhs = TexMobject("= (x + {b \\over 2a})^2 - {b^2 \\over 4a^2}")
        # identity_4_rhs.next_to(identity_3_rhs, DOWN, aligned_edge=LEFT)
        # identity_4_lhs.next_to(identity_4_rhs, LEFT)
        # self.play(Write(identity_4_lhs))
        # self.wait()
        # self.play(Write(identity_4_rhs))



        # delta = TexMobject("\\Delta = b^2 - 4ac")
        # delta.next_to(equation, 3 * DOWN)
        # solution = TexMobject("x_{1,2} = {-b \\pm \\sqrt{\\Delta} \\over 2a}")
        # solution.next_to(delta, 3 * DOWN)
        # whole = VGroup(equation, delta, solution)
        # whole.generate_target()
        # whole.target.scale(0.8)
        # whole.target.to_edge(LEFT)
        # self.play(Write(whole))
        # self.play(MoveToTarget(whole.copy()))
        # self.wait()
        # self.play(FadeOut(whole))
        # self.play(FadeOut(whole.copy()))


class IdentiteTrick(Scene):
    def construct(self):
        identity_1_rhs = TexMobject("= a^2 + 2ab + b^2")
        identity_1_rhs.move_to(UP * 1.8)
        identity_1_lhs = TexMobject("(a + b)^2 ")
        identity_1_lhs.next_to(identity_1_rhs, LEFT)
        self.play(
            Write(identity_1_lhs),
            Write(identity_1_rhs),
        )

        identity_2_lhs = TexMobject("(x + {b \\over a})^2 ")
        identity_2_rhs = TexMobject("= x^2 + ", "2", "{x{b \\over ", "a}} + \\left( {b \\over a} \\right) ^2")
        identity_2_rhs.next_to(identity_1_rhs, DOWN, aligned_edge=LEFT)
        identity_2_lhs.next_to(identity_2_rhs, LEFT)
        self.play(Write(identity_2_lhs))
        self.wait()
        self.play(Write(identity_2_rhs))

        identity_3_lhs = TexMobject("(x + {b \\over 2a})^2 ")
        identity_3_rhs = TexMobject("= x^2 + ", "2", "{x{b \\over ", "2", "a}} + \\left( {b \\over 2a} \\right) ^2")
        identity_3_rhs.next_to(identity_2_rhs, DOWN, aligned_edge=LEFT)
        identity_3_lhs.next_to(identity_3_rhs, LEFT)
        self.play(Write(identity_3_lhs))
        self.wait()
        self.play(Write(identity_3_rhs))



class ElbowExample(Scene):
    def construct(self):
        triangle = Polygon(ORIGIN, 3 * UP, 4 * RIGHT)
        elbow = Elbow(color=RED)
        elbow.set_points_as_corners([RIGHT, RIGHT + UP, UP])
        # elbow.set_width(elbow.width, about_point=RIGHT+np.array([-0.1, 0.1, 0.0]))
        elbow.set_width(elbow.width, about_point=ORIGIN)
        # self.add(triangle)
        self.play(ShowCreation(triangle))
        # self.wait(1)
        self.play(FadeInFromLarge(elbow))

        vector = Vector(direction=RIGHT)
        end_point = np.array([2.0, 1.0, 0.0])
        animation = ApplyMethod(vector.shift, end_point)
        self.play(animation)

        angle = math.radians(90)
        annotated_triangle = VGroup(triangle, elbow)
        animation = Rotate(annotated_triangle, angle=angle, about_point=ORIGIN)
        self.play(animation)

        wave = FunctionGraph(np.sin, x_min=-5, x_max=5)
        self.play(ShowCreation(wave))

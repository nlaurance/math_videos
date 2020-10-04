from manimlib.imports import *


class UsingBraces(Scene):

    # Using braces to group text together
    def construct(self):
        eq1A = TexMobject("4x^2 + 3 \\times y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x - 2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))


class UsingBracesConcise(Scene):
    # A more concise block of code with all columns aligned
    def construct(self):
        eq1_text = ["4", "x^3", "+", "3", "y_0", "=", "0"]
        eq2_text = ["5", "x", "-", "2", "y", "=", "3"]
        eq1_mob = TexMobject(*eq1_text)
        eq2_mob = TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x": RED_B,
            "y": GREEN_C
        })
        eq2_mob.set_color_by_tex_to_color_map({
            "x": RED_B,
            "y": GREEN_C
        })
        for i, item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i], LEFT)
        eq1 = VGroup(*eq1_mob)
        eq2 = VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq_group = VGroup(eq1, eq2)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1), Write(eq2))
        self.play(GrowFromCenter(braces), Write(eq_text))


class Identite2(Scene):
    def construct(self):
        # identity_1 = TexMobject("(a + b)^2", " = ", "a^2 + 2ab + b^2").scale(1.5)
        identity_1 = TexMobject("(", "a", " + ", "b", ")^2", " = ", "a", "^2 + 2", "a", "b", " + ", "b", "^2").scale(
            1.5)
        identity_1.shift(UP * 1.8)
        identity_1.set_color_by_tex_to_color_map({
            "a": BLUE_D,
            "b": YELLOW_C
        })
        self.play(
            Write(identity_1, run_time=6.2),
        )

        identity_2 = TexMobject("(a - b)^2", " = ", "a^2 - 2ab + b^2").scale(1.5)
        self.play(
            Write(identity_2),
        )

        identity_3 = TexMobject("(a + b)(a-b)", " = ", "a^2 - b^2").scale(1.5)
        identity_3.shift(DOWN * 1.8)
        self.play(
            Write(identity_3),
        )


class Identite(Scene):
    def construct(self):
        title = TextMobject("Identit\\'es remarquables").to_edge(UP).scale(1.5)
        self.play(Write(title), run_time=1)

        identity_1_lhs = TexMobject("(a + b)^2 ").scale(1.5)
        identity_1_eq = TexMobject(" = ").scale(1.5)
        identity_1_rhs = TexMobject("a^2 + 2ab + b^2").scale(1.5)
        identity_1_eq.move_to(UP)
        identity_1_lhs.next_to(identity_1_eq, LEFT)
        identity_1_rhs.next_to(identity_1_eq, RIGHT)
        self.play(
            Write(identity_1_eq),
        )
        self.wait()
        self.play(
            Write(identity_1_lhs),
            Write(identity_1_rhs),
        )

        # identity_2_lhs = TexMobject("(a - b)^2 ").scale(1.5)
        # identity_2_rhs = TexMobject("= a^2 - 2ab + b^2").scale(1.5)
        # identity_2_rhs.next_to(identity_1_rhs, 2 * DOWN, aligned_edge=LEFT)
        # identity_2_lhs.next_to(identity_2_rhs, LEFT)
        # self.play(Write(identity_2_lhs))
        # self.play(Write(identity_2_rhs))
        #
        # identity_3_lhs = TexMobject("(a - b)(a + b) ").scale(1.5)
        # identity_3_rhs = TexMobject("= a^2 - b^2").scale(1.5)
        # identity_3_rhs.next_to(identity_2_rhs, 2*DOWN, aligned_edge=LEFT)
        # identity_3_lhs.next_to(identity_3_rhs, LEFT)
        # self.play(Write(identity_3_lhs))
        # self.play(Write(identity_3_rhs))


class Develop(Scene):
    def construct(self):
        size = 1.35
        vert_spacing = 1.2

        identity_1_lhs = TexMobject("(a+b)^2 ").scale(size)
        identity_1_rhs = TexMobject("=(", "a", "+", "b", ")\\times(", "a", "+", "b", ")").scale(size)
        a1, b1, a2, b2 = identity_1_rhs[1], identity_1_rhs[3], identity_1_rhs[5], identity_1_rhs[7]
        identity_1_rhs.move_to(UP * 2)
        identity_1_lhs.next_to(identity_1_rhs, LEFT)
        self.play(Write(identity_1_lhs))
        self.play(Write(identity_1_rhs))

        arrow_margin = 0.1

        identity_2 = TexMobject("= a \\times a", " + a \\times b ", "+ b \\times a ", "+ b \\times b").scale(size)
        identity_2.next_to(identity_1_rhs, 2.7 * DOWN, aligned_edge=LEFT)
        id2_part1, id2_part2, id2_part3, id2_part4 = identity_2

        self.play(ShowCreation(CurvedArrow(a1.get_top() + arrow_margin,
                                           a2.get_top() + arrow_margin, angle=-TAU / 4.0)))
        self.play(Write(id2_part1))
        self.play(ShowCreation(CurvedArrow(a1.get_top() + arrow_margin,
                                           b2.get_top() + arrow_margin, angle=-TAU / 4.0)))
        self.play(Write(id2_part2))
        self.play(ShowCreation(CurvedArrow(b1.get_bottom() - arrow_margin,
                                           a2.get_bottom() - arrow_margin)))
        self.play(Write(id2_part3))
        self.play(ShowCreation(CurvedArrow(b1.get_bottom() - arrow_margin,
                                           b2.get_bottom() - arrow_margin)))
        self.play(Write(id2_part4))

        identity_3 = TexMobject("= a^2 + ", "ab", " + ", "ba", " + b^2").scale(size)
        ab, ba = identity_3[1], identity_3[3]
        identity_3.next_to(identity_2, 2 * DOWN, aligned_edge=LEFT)
        self.play(Write(identity_3))
        self.wait(2)
        self.play(Transform(ba, ab.copy().move_to(ba)))

        identity_4 = TexMobject("= a^2 + 2ab + b^2").scale(size)
        identity_4.next_to(identity_3, 2 * DOWN, aligned_edge=LEFT)
        self.play(Write(identity_4))

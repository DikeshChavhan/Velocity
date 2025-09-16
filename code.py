from manim import *

class PeakBallVelocity(Scene):
    def construct(self):
        # Title
        title = Text("Measuring Peak Ball Velocity in Cricket using a Camera", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Why it matters
        points = VGroup(
            Text("• Performance indicator", font_size=28),
            Text("• Detects fatigue effect", font_size=28),
            Text("• Improves training & technique", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        heading = Text("Why Peak Ball Velocity Matters", font_size=32).to_edge(UP)
        self.play(Write(heading))
        self.play(FadeIn(points, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(points), FadeOut(heading))

        # Equipment
        eq_heading = Text("Equipment Needed", font_size=32).to_edge(UP)
        equipment = VGroup(
            Text("• Camera & Tripod", font_size=28),
            Text("• Calibration Rod", font_size=28),
            Text("• Computer/Software", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(eq_heading))
        self.play(FadeIn(equipment, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(eq_heading), FadeOut(equipment))

        # Camera setup
        setup_heading = Text("Camera Setup", font_size=32).to_edge(UP)
        diagram = VGroup(
            Text("Bowler → Ball → Stumps", font_size=28),
            Text("Camera at 90° to ball flight", font_size=28),
            Text("Calibration rod near stumps", font_size=28)
        ).arrange(DOWN)
        self.play(Write(setup_heading))
        self.play(FadeIn(diagram, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(setup_heading), FadeOut(diagram))

        # Recording
        rec_heading = Text("Recording Ball Flight", font_size=32).to_edge(UP)
        rec = VGroup(
            Text("• Record in slow motion", font_size=28),
            Text("• Track ball across frames", font_size=28),
            Text("• Use calibration rod for scale", font_size=28)
        ).arrange(DOWN)
        self.play(Write(rec_heading))
        self.play(FadeIn(rec, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(rec_heading), FadeOut(rec))

        # Velocity Calculation
        vel_heading = Text("Velocity Calculation", font_size=32).to_edge(UP)
        formula = MathTex("Velocity = \\frac{Distance}{Time}").scale(1.2)
        self.play(Write(vel_heading))
        self.play(Write(formula))
        self.wait(2)

        # Numerical Example
        ex1 = Text("Ball travels: 18 m", font_size=28).next_to(formula, DOWN)
        ex2 = Text("Time: 0.6 s", font_size=28).next_to(ex1, DOWN)
        ex3 = Text("Velocity = 30 m/s ≈ 108 km/h", font_size=28).next_to(ex2, DOWN)
        self.play(Write(ex1))
        self.wait(1)
        self.play(Write(ex2))
        self.wait(1)
        self.play(Write(ex3))
        self.wait(3)
        self.play(FadeOut(vel_heading), FadeOut(formula), FadeOut(ex1), FadeOut(ex2), FadeOut(ex3))

        # Results
        res_heading = Text("Results & Advantages", font_size=32).to_edge(UP)
        res = VGroup(
            Text("• Accurate & Reliable", font_size=28),
            Text("• Non-invasive", font_size=28),
            Text("• Research-friendly", font_size=28)
        ).arrange(DOWN)

        self.play(Write(res_heading))
        self.play(FadeIn(res, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(res_heading), FadeOut(res))

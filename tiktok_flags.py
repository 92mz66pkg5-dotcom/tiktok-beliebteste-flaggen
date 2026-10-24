from manim import *
import os

class FlagsTikTok(Scene):
    def construct(self):
        self.camera.background_color = "#0a0a1a"
        
        # ===== INTRO: Globe + Airplane =====
        # Simple clean globe
        globe = Circle(radius=2.2, color=BLUE_B, fill_opacity=0.15, stroke_width=3)
        equator = Arc(radius=2.2, angle=PI, start_angle=0, color=BLUE_C, stroke_width=1.5)
        meridians = VGroup(*[
            Arc(radius=2.2, angle=PI, start_angle=i*PI/4, color=BLUE_C, stroke_width=1)
            for i in range(4)
        ])
        continents = VGroup(
            # Simple landmass shapes
            Ellipse(width=1.8, height=1.0, color=GREEN_B, fill_opacity=0.4).shift(LEFT*0.6 + UP*0.3),
            Ellipse(width=1.2, height=1.5, color=GREEN_B, fill_opacity=0.4).shift(RIGHT*0.8 + DOWN*0.2),
            Ellipse(width=0.9, height=0.7, color=GREEN_B, fill_opacity=0.4).shift(LEFT*0.3 + DOWN*0.9),
        )
        globe_group = VGroup(globe, equator, meridians, continents)
        globe_group.move_to(ORIGIN)
        
        # Airplane (simple clean shape)
        plane_body = Triangle(fill_color=WHITE, fill_opacity=1, stroke_width=0).scale(0.25).rotate(-PI/2)
        plane_wing = Ellipse(width=0.7, height=0.15, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        plane_tail = Triangle(fill_color=WHITE, fill_opacity=1, stroke_width=0).scale(0.12).rotate(PI/4).shift(LEFT*0.25)
        airplane = VGroup(plane_wing, plane_body, plane_tail)
        airplane.scale(0.9)
        
        # Orbit path
        orbit_radius = 3.0
        airplane.move_to(RIGHT * orbit_radius)
        
        self.play(FadeIn(globe_group, scale=0.8), run_time=1.2)
        self.play(FadeIn(airplane), run_time=0.4)
        
        # Circle around globe
        self.play(
            Rotate(airplane, angle=2*PI, about_point=ORIGIN, rate_func=linear),
            run_time=3.0
        )
        
        # Fade out globe
        self.play(FadeOut(globe_group), FadeOut(airplane), run_time=0.6)
        
        # ===== TITLE =====
        title = Text(
            "Die beliebtesten Flaggen\nder Welt",
            font_size=48,
            color=WHITE,
            weight=BOLD,
            line_spacing=0.9
        )
        subtitle = Text(
            "Kennst du sie und ihre Länder?",
            font_size=32,
            color=GRAY_A
        )
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.4)
        title_group.move_to(ORIGIN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title_group), run_time=0.5)
        
        # ===== FLAGS =====
        flags_data = [
            ("flags/jp.png", "Japan"),
            ("flags/ca.png", "Kanada"),
            ("flags/fr.png", "Frankreich"),
            ("flags/de.png", "Deutschland"),
        ]
        
        for flag_path, country in flags_data:
            # Flag image
            flag = ImageMobject(flag_path)
            flag.set_height(3.5)
            flag.move_to(UP * 0.8)
            
            # White clean circle / point
            dot = Dot(radius=0.18, color=WHITE).next_to(flag, DOWN, buff=0.5)
            
            # Country name
            name = Text(country, font_size=52, color=WHITE, weight=BOLD)
            name.next_to(dot, DOWN, buff=0.35)
            
            group = Group(flag, dot, name)
            
            self.play(
                FadeIn(flag, scale=0.9),
                FadeIn(dot, scale=0.5),
                run_time=0.6
            )
            self.play(Write(name), run_time=0.5)
            self.wait(1.4)
            self.play(FadeOut(group), run_time=0.4)
        
        # End card
        end_text = Text("Welche kanntest du?", font_size=42, color=WHITE)
        self.play(FadeIn(end_text), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(end_text), run_time=0.5)

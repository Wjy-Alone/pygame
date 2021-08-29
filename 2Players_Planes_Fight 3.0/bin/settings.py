class Settings():
    def __init__(self):
        self.screen_size = (487,704)
        self.screen_name = "Plane Fight"
        self.plane_speed = 1
        self.plane_leave = 4

        self.FPS = 120

        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60,60,60)
        self.bullet_max = 10

        self.enemy_plane_speed = 0.4

        self.reset_time = 2

        self.score = 0
        with open('score_max.txt') as score_num:
            score_max = score_num.read()
        self.his_score_max = score_max

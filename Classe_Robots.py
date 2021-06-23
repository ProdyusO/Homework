class Robot:
    def __init__(self, height, weight, speed):
        self.height = height
        self.weight = weight
        self.speed = speed

    def company(self):
        print('Boston Dynamics')


class SpotMini(Robot):
    def __init__(self, height, weight, speed, work_t):
        super().__init__(height, weight, speed)
        self.work_t = work_t

    def info(self):
        print(f"""Model SpotMini
                  Height = {self.height} meters
                  Weight = {self.weight} kg
                  Speed = {self.speed}  km/h
                  Working time = {self.work_t} minutes """)


class Atlas(Robot):
    def __init__(self, height, weight, speed, jump_height):
        super().__init__(height, weight, speed)
        self.jump_height = jump_height

    def info(self):
        print(f"""Model Atlas
                     Height = {self.height} meters
                     Weight = {self.weight} kg
                     Speed = {self.speed} km/h
                     Jump height = {self.jump_height} meters""")

    def render(self, color):
        print(f'Rendered with color {color}')


class Handle(Robot):
    def __init__(self, height, weight, speed, hand_height):
        super().__init__(height, weight, speed)
        self.hand_height = hand_height

    def info(self):
        print(f"""Model Handle
                     Height = {self.height} meters
                     Hand Height = {self.hand_height} meters
                     Weight = {self.weight} kg
                     Speed = {self.speed} km/h""")

    def scale(self, scale_factor):
        print(f'Scaled with scale_factor {scale_factor}')


s = SpotMini(0.5, 20, 10, 60)
s.company()
s.info()
a = Atlas(2, 80, 20, 0.7)
a.company()
a.info()
a.render('Green')
h = Handle(5, 15, 10, 1.5)
h.company()
h.info()
h.scale(2)

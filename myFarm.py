# Farm Class
class Animals:
    staff_in_belly = 0

    def __init__(self, name):
        self.name = name

    def feed(self):
        self.staff_in_belly += 1
        if self.staff_in_belly > 3:
            self.poop()
            return self.should_go_to_restRoom()

        else:
            return f'{self.name} is eating'

    def should_go_to_restRoom(self):
        return f'{self.name} is not hungry and is going to the restroom to poop'

    def poop(self):
        self.staff_in_belly = 0

    def talk(self, sound=None):
        if sound is None:
            return f'Hey, I am {self.name} and I say Nothing'
        else:
            return f'{self.name} says {sound}'

    def isHungry(self):
        if self.staff_in_belly < 2:
            return f'{self.name} is Hungry'
        else:
            return f'{self.name} is not Hungry at all!!'


class Duck(Animals):
    def talk(self, sound='quack quack'):
        return super().talk(sound)


class Cow(Animals):
    def talk(self, sound='Mow Mow'):
        return super().talk(sound)


class Sheep(Animals):
    def talk(self, sound='Baa Baa'):
        return super().talk(sound)

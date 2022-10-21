# track1 == track2  # маршруты равны, если равны их длины
# track1 != track2  # маршруты не равны, если не равны их длины
# track1 > track2  # True, если длина пути для track1 больше, чем для track2
# track1 < track2  # True, если длина пути для track1 меньше, чем для track2

import math


class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.track = [TrackLine(start_x, start_y)]

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    def get_distance(self):
        lst = [(i.to_x, i.to_y) for i in self.track]
        res = 0
        for i in range(1, len(lst)):
            x1, x0 = lst[i][0], lst[i - 1][0]
            y1, y0 = lst[i][1], lst[i - 1][1]
            distance = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
            res += distance
        return int(res)

    def __eq__(self, other):
        if isinstance(other, Track):
            return self.get_distance() == other.get_distance()
        else:
            raise ValueError('It\'s not a Track object!')

    def __lt__(self, other):
        if isinstance(other, Track):
            return self.get_distance() < other.get_distance()
        else:
            raise ValueError('It\'s not a Track object!')

    def __len__(self):
        return self.get_distance()


class TrackLine:
    def __init__(self, to_x, to_y, max_speed=0):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

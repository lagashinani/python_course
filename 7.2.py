class Track():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show(self):
        print("<" + self.title + "-" + str(self.duration) + ">")

    def __str__(self):
        return self.title + "-" + str(self.duration) + "min"

    def __lt__(self, other):
        return self.duration < other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def __eq__(self, other):
        return self.duration == other.duration

    def __ne__(self, other):
        return self.duration != other.duration

    def __ge__(self, other):
        return self.duration >= other.duration

    def __gt__(self, other):
        return self.duration > other.duration


class Album():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []

    def get_tracks(self):
        for track in self.tracks:
            track.show()

    def add_track(self, track):
        self.tracks.append(track)

    def get_duration(self):
        print("Total Duration of " + self.title 
              + ": " + str(sum(map(lambda x: x.duration, self.tracks))))

    def __str__(self):
        res = "Artist: " + self.artist + "\nTitle: " + self.title + "\nTracks:\n"
        for track in self.tracks:
            res += ("\t" + str(track) + "\n")
        return res


greatest_album = Album("True", "Avicii")
greatest_album.add_track(Track("Wake Me Up", 4))
greatest_album.add_track(Track("Addicted to You", 2))
greatest_album.add_track(Track("Hey Brother", 4))

greatest_album.get_duration()
greatest_album.get_tracks()


elvis_album = Album("Elvis Presley", "Elvis Aaron Presley")
elvis_album.add_track(Track("Tutti Frutti", 2))
elvis_album.add_track(Track("Blue Suede Shoes", 2))
elvis_album.add_track(Track("Money Honey", 3))

elvis_album.get_duration()
elvis_album.get_tracks()


print()
print(Track("Wake Me Up", 4))
print()
print(elvis_album)

print(Track("Wake Me Up", 4) > Track("Addicted to You", 2))
print(Track("Wake Me Up", 4) < Track("Addicted to You", 2))
print(Track("Wake Me Up", 4) >= Track("Addicted to You", 2))
print(Track("Wake Me Up", 4) <= Track("Addicted to You", 2))
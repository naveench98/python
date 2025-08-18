def my_songs():
    yield "Song1"
    yield "Song2"
    yield "Song3"

dj = my_songs()           # it will get the elements one by one

print(next(dj))  # Song1
print(next(dj))  # Song2
print(next(dj))  # Song3

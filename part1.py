import re
with open('E:\code\AoC\day13\input.txt', "r") as data:
    data = data.read().split("\n")

earliest_departure_time, raw_ids = int(data[0]), data[1]
ids = re.findall('\d{1,3}', raw_ids)
ids = list(map(int,ids))
ids.sort()

#Question:
#What is the ID of the earliest bus you can take to the airport multiplied
#by the number of minutes you'll need to wait for that bus?

#Since the earliest departure is a high number it makes sense that the answer
#would be one of the bigger ids, after I saw the earliest departure times for each id
#I confirmed this

#making a dictionary for each bus id and adding the times for each of them
bus_trips = {id:[0] for id in ids}
for id in ids:
    n = 0
    while earliest_departure_time > id*n:
        n = n + 1 
        bus_trips[id].append(id*n)

#print(earliest_departure_time, 'this is the earliest departure time')
closest_departure_times = list()
for id in ids:
    closest_departure_times.append((bus_trips[id][-1], id))

#print(closest_departure_times)
#the structure are tuples with (closest_departure_time, id)
#we want to use the last one preferably after the last comment before making the dict

minutes = closest_departure_times[-1][0]-earliest_departure_time
answer = minutes*closest_departure_times[-1][1]
print(answer)
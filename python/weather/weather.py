class Storm:
    def __init__(self, i, o, s, y, n):
        self._id = i
        self._origin = o
        self._storm_num = s
        self._year = y
        self._name = n
        self._observations = []

    def add_observations(self, obs):
        self._observations.append(obs)

    def __repr__(self):
        return 'id =  {}\norigin = {}\nstorm_number = {}\nyear = {}\nname = {}\nobservations = {}'.format(
            self._id, self._origin, self._storm_num, self._year, self._name, self._observations)

    def get_id(self):
        return self._id

    def get_origin(self):
        return self._origin

    def get_storm_num(self):
        return self._storm_num

    def get_year(self):
        return self._year

    def get_name(self):
        return self._name

    def get_observations(self):
        return self._observations

    id = property(get_id)
    origin = property(get_origin)
    storm_num = property(get_storm_num)
    year = property(get_year)
    name = property(get_name)
    observations = property(get_observations)


class Observation(Storm):
    def __init__(self, s, d, t, st, lat, lon, mw, mp):
        self._storm = s
        self._date = d
        self._time = t
        self._status = st
        self._latitude = lat
        self._longitude = lon
        self._max_wind = mw
        self._min_pressure = mp

    def __repr__(self):
        return 'id =  {}\nstorm = {}\ndate = {}\ntime = {}\nstatus = {}\nlatitude = {}\nlongitude = {}\nmax_wind = {}\nmin_pressure = {}'.format(
            self._storm, self._date, self._time, self._status, self._latitude, self._longitude, self._max_wind, self._min_pressure
        )

    def get_storm(self):
        return self._storm

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_status(self):
        return self._status

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitude

    def get_max_wind(self):
        return self._max_wind

    def get_min_pressure(self):
        return self._min_pressure

    storm = property(get_storm)
    date = property(get_date)
    time = property(get_time)
    status = property(get_status)
    latitude = property(get_latitude)
    longitude = property(get_longitude)
    max_wind = property(get_max_wind)
    min_pressure = property(get_min_pressure)


# Driver Code :
storm1 = Storm(1, "christmas island", 1, 1965, "una")
storm2 = Storm(1, "madagascar", 2, 1965, "iris")
storm3 = Storm(1, "taiwan", 3, 1949, "irma")

observation1_storm1 = Observation(
    storm1, 1965, 1200, 'WV', '10', '80', 100, 90)


observation2_storm1 = Observation(
    storm1, 1965, 1200, 'Wv', '10', '80', 90, 80)

observation1_storm2 = Observation(
    storm1, 1965, 1200, 'WV', '10', '80', 120, 90)


observation2_storm2 = Observation(
    storm1, 1965, 1200, 'Wv', '10', '80', 110, 80)


origin_year_dict = {
    storm1: ("christmas island", 1965),
    storm2: ("madagascar", 1965),
    storm3: ("taiwan", 1949)
}


status_dict = {
    'WV': [
        (storm1, [observation1_storm1, observation2_storm1]),
        (storm1, [observation1_storm1, observation2_storm1]),
        (storm2, [observation1_storm2, observation2_storm2])
    ]
}


def status_storms(status_code):
    '''returns a alphabetically sorted list of storms with the given status code'''

    # initialize an empty list to store the storm names
    storm_names = []

    # loop over the data in the status_dict dictionary, with the given status code
    for data in status_dict[status_code]:

        # add the name of the storm to the list
        storm_names.append(data[0].name)

    # convert the list to set, to remove all duplicates
    # and use the sorted() function to sort it and return it
    return sorted(set(storm_names))

# call the function, and print its output for testing
print(status_storms('WV'))


# initialize an empty dictionary to keep the count of the number of storms each year
year_count = {}

# loop over the origin_year_dict dictionary and unpack it's contents
for storm, origin_year in origin_year_dict.items():

    # access the year from the origin_year tuple by indexing
    year = origin_year[1]

    # update the number of storms for the year, in the year_count dictionary
    if year in year_count:
        year_count[year] += 1
    else:
        year_count[year] = 1

# unpact the year_count dictionary, and display the year, and number of storms that year
for year, count in year_count.items():
    print(f"year: {year}, number of storms: {count}")



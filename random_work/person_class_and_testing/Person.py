class Person:
    counter = 0
    current_year = 2020
    is_christmas = False

    def __init__(self, full_name: str, year: int):
        # increase the counter by 1 so that we can assign ID
        Person.counter += 1
        self.id = Person.counter

        # check if the full name is valid
        if len(full_name.split()) > 1:
            self.full_name = full_name
        else:
            self.full_name = "Guy Incognito"

        # check the inputted year
        if 0 < year <= self.current_year:
            self.year = year
        else:
            self.year = 2000

    def get_full_name(self):
        """returns the full name of the person"""
        return self.full_name

    def get_year(self):
        """returns the year of the person"""
        return self.year

    def get_id(self):
        """returns the ID number of the person"""
        return self.id

    def get_age(self):
        """returns the age of the person"""
        return self.current_year - self.get_year()

    def get_friendly_name(self):
        """returns the first name of the person"""
        token = self.full_name.split()
        if self.is_christmas:
            output = token[0] + " " + chr(0x1F384)
            return output
        return token[0]

    def __str__(self):
        """returns the id, then name year"""
        output = f"{self.get_id()}: {self.get_full_name()}, {self.get_year()}"
        return output

    @classmethod
    def celebrate_new_year(cls):
        cls.is_christmas = True
        cls.current_year += 1
        return

    @classmethod
    def go_back_to_work(cls):
        cls.is_christmas = False

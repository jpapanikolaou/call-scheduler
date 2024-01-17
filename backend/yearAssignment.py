import datetime
import random

class Doctor:
    def __init__(self, name):
        self.name = name
        self.preferences = {}

    def set_preference(self, day, preference):
        self.preferences[day] = preference

    def get_preference(self, day):
        return self.preferences.get(day, 0)

class SchedulingSystem:
    def __init__(self, year, doctors):
        self.year = year
        self.doctors = {doctor.name: doctor for doctor in doctors}
        self.schedule = self.generate_year_dates(year)
        self.disputed_call = {}
        self.fairness_list = {}

    def generate_year_dates(self, year):
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)
        delta = datetime.timedelta(days=1)
        return {start_date + delta * i: None for i in range((end_date - start_date).days + 1)}

    def generate_random_preferences(self):
        for day in self.schedule:
            for doctor in self.doctors.values():
                preference = random.randint(-10, 10)
                doctor.set_preference(day, preference)

    def create_undisputed_schedule(self):
        for day in self.schedule:
            day_preferences = [(doctor, doctor.get_preference(day)) for doctor in self.doctors.values()]
            day_preferences.sort(key=lambda x: x[1], reverse=True)

            if len([pref for _, pref in day_preferences if pref > 0]) > 1:
                self.disputed_call[day] = [(doc.name, pref) for doc, pref in day_preferences if pref > 0]
            else:
                self.schedule[day] = day_preferences[0][0].name

        self.update_fairness_list()

    def update_fairness_list(self):
        self.fairness_list = {doctor: 0 for doctor in self.doctors.keys()}
        for day, doctor_name in self.schedule.items():
            if doctor_name is not None:
                self.fairness_list[doctor_name] += 1

    def get_schedule(self):
        return self.schedule

    def get_fairness_list(self):
        return self.fairness_list

# Testing the system for a full year
doctors = [Doctor('Doctor A'), Doctor('Doctor B'), Doctor('Doctor C')]
scheduling_system = SchedulingSystem(2024, doctors)
scheduling_system.generate_random_preferences()
scheduling_system.create_undisputed_schedule()

# Retrieve the schedule and fairness list
year_schedule = scheduling_system.get_schedule()
year_fairness_list = scheduling_system.get_fairness_list()

# Due to the large size of the data, let's print a summary
print("Number of Disputed Calls:", len(scheduling_system.disputed_call))
print("Fairness List:", year_fairness_list)
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
    def __init__(self, days, doctors):
        self.days = days
        self.doctors = {doctor.name: doctor for doctor in doctors}  # Changed to dictionary for easier access
        self.schedule = {day: None for day in days}
        self.disputed_call = {}
        self.fairness_list = {}

    def generate_random_preferences(self):
        for day in self.days:
            for doctor in self.doctors.values():
                preference = random.randint(-10, 10)
                doctor.set_preference(day, preference)

    def create_undisputed_schedule(self):
        for day in self.days:
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

    def resolve_disputed_calls(self):
        for day, disputes in self.disputed_call.items():
            disputes.sort(key=lambda x: x[1], reverse=True)
            least_worked_doctors = [doc for doc, days in self.fairness_list.items() 
                                    if days == min(self.fairness_list.values())]

            for doctor_name, _ in disputes:
                if doctor_name in least_worked_doctors:
                    self.schedule[day] = doctor_name
                    self.fairness_list[doctor_name] += 1
                    break

        self.update_fairness_list()

    def sanity_check_and_redistribute(self):
        while max(self.fairness_list.values()) - min(self.fairness_list.values()) > 1:
            max_days_doctor = max(self.fairness_list, key=self.fairness_list.get)
            min_days_doctor = min(self.fairness_list, key=self.fairness_list.get)

            smallest_delta = float('inf')
            day_to_switch = None

            for day, doctor_name in self.schedule.items():
                if doctor_name == max_days_doctor:
                    preference_max = self.doctors[doctor_name].get_preference(day)
                    preference_min = self.doctors[min_days_doctor].get_preference(day)
                    delta = abs(preference_max - preference_min)
                    if delta < smallest_delta:
                        smallest_delta = delta
                        day_to_switch = day

            if day_to_switch:
                self.schedule[day_to_switch] = min_days_doctor
                self.fairness_list[max_days_doctor] -= 1
                self.fairness_list[min_days_doctor] += 1

            self.update_fairness_list()
    def test_scheduling_system(self):
            # Generate random preferences
            self.generate_random_preferences()

            # Create undisputed schedule
            self.create_undisputed_schedule()
            print("Initial Schedule (Undisputed):")
            print(self.get_schedule())
            print("Fairness List after Undisputed Schedule:")
            print(self.get_fairness_list())

            # Resolve disputed calls
            self.resolve_disputed_calls()
            print("\nSchedule after Resolving Disputed Calls:")
            print(self.get_schedule())
            print("Fairness List after Resolving Disputed Calls:")
            print(self.get_fairness_list())

            # Perform sanity check and redistribute
            self.sanity_check_and_redistribute()
            print("\nFinal Schedule after Sanity Check and Redistribution:")
            print(self.get_schedule())
            print("Final Fairness List:")
            print(self.get_fairness_list())

    def get_fairness_list(self):
        return self.fairness_list

    def get_schedule(self):
        return self.schedule

    def get_disputed_call(self):
        return dict(sorted(self.disputed_call.items()))

# Testing the system
days = list(range(1, 15))
doctors = [Doctor('Doctor A'), Doctor('Doctor B'), Doctor('Doctor C')]

scheduling_system = SchedulingSystem(days, doctors)
scheduling_system.generate_random_preferences()
scheduling_system.create_undisputed_schedule()
scheduling_system.resolve_disputed_calls()
scheduling_system.sanity_check_and_redistribute()

# Retrieve the schedule and fairness list
resolved_schedule = scheduling_system.get_schedule()
resolved_fairness_list = scheduling_system.get_fairness_list()

resolved_schedule, resolved_fairness_list
'''
Final outputs: a schedule, and a list ensuring that everyone gets as close
to equal on days of call as possible
'''

print(resolved_schedule)
print(resolved_fairness_list)


from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_first_name(self):
        return self.first_name
    def set_first_name(self, name):
        self.first_name = name
    def get_last_name(self):
        return self.last_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    @abstractmethod
    def compute_salary(self):
        pass
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary
    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary
    def compute_salary(self):
        return self.salary + 200
    
class HourlyEmployee(Employee):
        def __init__(self, first_name, last_name, worked_hours, value_hour):
            super().__init__(first_name, last_name)
            self.worked_hours = worked_hours
            self.value_hour = value_hour
        def get_worked_hours(self):
            return self.worked_hours
        def set_worked_hours(self, new_worked_hours):
            self.worked_hours = new_worked_hours
        def get_value_hour(self):
            return self.value_hour
        def set_value_hour(self, new_value_hour):
            self.value_hour = new_value_hour
        def compute_salary(self):
            return self.value_hour * self.worked_hours
        
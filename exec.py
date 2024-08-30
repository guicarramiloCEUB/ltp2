from aula import Employee, FulltimeEmployee, HourlyEmployee

if __name__ == '__main__':
    employee1 = FulltimeEmployee('Emily', 'Pereira', 1400)
    employee2 = HourlyEmployee("Arras", "Buceta", 20, 200)
    print(employee1.get_full_name())
    employee1.set_first_name('Dela')
    print(employee1.get_full_name())
    employee1.set_last_name('Sexo')
    print(employee1.get_full_name() + " " + str(employee1.get_salary()))
    print(employee1.compute_salary())
    
    print(employee2.get_full_name())
    employee2.set_first_name('Dela')
    print(employee2.get_full_name())
    employee2.set_last_name('Sexo')
    print(employee2.get_full_name() + " " + str(employee2.compute_salary()))
    print(employee2.compute_salary())
    
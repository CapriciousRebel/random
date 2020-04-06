def ask_first_name():
    first_name = input("Enter first name: ")
    return first_name


def ask_last_name():
    last_name = input("Enter last name: ")
    return last_name


def ask_salary():
    current_salary = input("Enter current salary: ")
    return float(current_salary)


def calculate_salary(salary):
    if salary < 40000:
        salary *= 1.05
    else:
        salary = 1.02*salary + 1200

    return salary


def display_results(first_name, last_name, new_salary):
    print(f"New salary for {first_name} {last_name}: ${new_salary}")


# Driver code :

first_name = ask_first_name()
last_name = ask_last_name()
current_salary = ask_salary()

new_salary = calculate_salary(current_salary)

display_results(first_name, last_name, new_salary)

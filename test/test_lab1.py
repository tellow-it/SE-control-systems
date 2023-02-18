# valid users
from datetime import date
import pytest
from app.schem.department import Department
from app.schem.employee import Employee
from app.utils.department import get_max_min_sum_salary

# data for test
emp1 = Employee(id=1, name='Ivan', surname='Tikhonov', salary=20000,
                date_of_acceptance=date(year=2022, month=7, day=11))
emp2 = Employee(id=2, name='Kostya', surname='Sobolev', salary=20000,
                date_of_acceptance=date(year=2022, month=9, day=1))
emp3 = Employee(id=3, name='Andrey', surname='Tikhonov', salary=2000000,
                date_of_acceptance=date(year=2000, month=7, day=1))
emp4 = Employee(id=4, name='Kirill', surname='honov', salary=40000,
                date_of_acceptance=date(year=2000, month=7, day=1))
emp5 = Employee(id=5, name='Victor', surname='Lon', salary=10000,
                date_of_acceptance=date(year=2000, month=7, day=1))

dep1 = Department(id=1, name='SOFT', employees=[emp1, emp2, emp3])
dep12 = Department(id=12, name='SOFT12', employees=[emp1, emp2, emp3])
dep2 = Department(id=2, name='Zavod1', employees=[emp1, emp2, ])
dep3 = Department(id=3, name='Zavod2', employees=[emp2, emp5])
dep4 = Department(id=4, name='Zavod3', employees=[emp4, emp5])


# test

def test_success_create_employee():
    emp = Employee(id=1, name='Ivan', surname='Tikhonov', salary=20000,
                   date_of_acceptance=date(year=2022, month=7, day=11))

    assert emp.id == 1
    assert emp.name == 'Ivan'
    assert emp.surname == 'Tikhonov'
    assert emp.salary == 20000
    assert emp.date_of_acceptance == date(year=2022, month=7, day=11)


def test_fail_create_employee():
    with pytest.raises(ValueError):
        Employee(id=2, name='I', surname='Tikhonov', salary=0,
                 date_of_acceptance=date(year=2022, month=7, day=1))
        Employee(id=2, name='Iv', surname='T', salary=0, date_of_acceptance='date(year=2022, month=7, day=1)')


def test_success_get_exp_employee():
    emp = Employee(id=1, name='Ivan', surname='Tikhonov', salary=20000,
                   date_of_acceptance=date(year=2022, month=7, day=11))
    assert emp.get_experience() == 0


def test_fail_get_exp_employee():
    emp = Employee(id=1, name='Ivan', surname='Tikhonov', salary=20000,
                   date_of_acceptance=date(year=2018, month=7, day=11))
    assert emp.get_experience() != 2


def test_success_create_dep():
    dep = Department(id=1, name='SOFT', employees=[emp1, emp2, emp3])
    assert dep.id == 1
    assert dep.name == 'SOFT'
    assert dep.employees == [emp1, emp2, emp3]


def test_fail_create_dep():
    with pytest.raises(ValueError):
        Department(id=1, name='K', employees=[emp2, emp5])


def test_min_max_sum_salary():
    deps = [dep1, dep2, dep3, dep4]
    max_sum, min_sum = get_max_min_sum_salary(list_deps=deps)
    assert max_sum == [dep1]
    assert min_sum == [dep3]


def test_min_max_sum_salary_2():
    deps = [dep1, dep12, dep2, dep3, dep4]
    max_sum, min_sum = get_max_min_sum_salary(list_deps=deps)
    assert max_sum == [dep1, dep12]
    assert min_sum == [dep3]




from datetime import date
from pydantic import BaseModel, validator
from dateutil.relativedelta import relativedelta


class Employee(BaseModel):
    id: int
    name: str
    surname: str
    salary: int
    date_of_acceptance: date

    def get_experience(self):
        return relativedelta(date.today(), self.date_of_acceptance).years

    @validator('name')
    @classmethod
    def validate_name(cls, name: str) -> str:
        if len(name) <= 1 or len(name) > 50:
            raise ValueError('Length name must be between (2, 50)')
        return name

    @validator('surname')
    @classmethod
    def validate_surname(cls, surname: str) -> str:
        if len(surname) <= 1 or len(surname) > 50:
            raise ValueError('Length name must be between (2, 50)')
        return surname

    @validator('salary')
    @classmethod
    def validate_salary(cls, salary: int) -> int:
        if not isinstance(salary, int):
            raise ValueError('Salary must be integer')
        elif salary <= 0:
            raise ValueError('Salary must be more then 0 :)')
        return salary

    @validator('date_of_acceptance')
    @classmethod
    def validate_date_of_acceptance(cls, date_of_acceptance: date) -> date:
        if date_of_acceptance > date.today():
            raise ValueError('Date acceptance must me les then today')
        elif not isinstance(date_of_acceptance, date):
            raise ValueError('Date acceptance must be date type (datetime)')
        return date_of_acceptance

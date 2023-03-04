from typing import List

from pydantic import BaseModel, validator

from app.schem.employee import Employee


class Department(BaseModel):
    id: int
    name: str
    employees: List[Employee]

    @validator('name')
    def validate_name(cls, name) -> str:
        if len(name) <= 1 or len(name) > 200:
            raise ValueError('Length name must be between (2, 200)')
        return name

    def sum_salary_department(self) -> int:
        return sum([emp.salary for emp in self.employees])

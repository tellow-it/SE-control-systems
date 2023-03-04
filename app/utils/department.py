from typing import List, Tuple, Dict

from app.schem.department import Department


def get_max_min_sum_salary(list_deps: list[Department]) -> Tuple[List[Department], List[Department]]:
    list_sum_salary: list = [dep.sum_salary_department() for dep in list_deps]
    list_count_emp: list = [len(dep.employees) for dep in list_deps]

    min_sum_dep: int = min(list_sum_salary)
    max_sum_dep: int = max(list_sum_salary)

    hasheble_deps: List[Tuple[int, int]] = [(dep.id, len(dep.employees)) for dep in list_deps]
    deps_sum: Dict[Tuple[int, int]: int] = dict(zip(hasheble_deps, list_sum_salary))

    max_count_emp_min_sum_sal: int = min(list_count_emp)
    max_count_emp_max_sum_sal: int = min(list_count_emp)

    for dep, sum_salary in deps_sum.items():
        if sum_salary == min_sum_dep:
            if dep[1] >= max_count_emp_min_sum_sal:
                max_count_emp_min_sum_sal = dep[1]
        elif sum_salary == max_sum_dep:
            if dep[1] >= max_count_emp_max_sum_sal:
                max_count_emp_max_sum_sal = dep[1]

    result_min_dep = [dep for dep in list_deps if
                      dep.sum_salary_department() == min_sum_dep and len(dep.employees) == max_count_emp_min_sum_sal]
    result_max_dep = [dep for dep in list_deps if
                      dep.sum_salary_department() == max_sum_dep and len(dep.employees) == max_count_emp_max_sum_sal]

    return result_max_dep, result_min_dep

"""Module to process csv data file."""

from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    """Read and process csv jobs data."""

    def get_max_salary(self) -> int:
        """Returns max salary."""
        max_salary = 0
        for job in self.jobs_list:
            str_salary = job["max_salary"]
            salary = int(str_salary) if str_salary.isnumeric() else 0
            max_salary = salary if salary > max_salary else max_salary
        return max_salary

    def get_min_salary(self) -> int:
        """Return min salary."""
        min_salary = float("inf")
        for job in self.jobs_list:
            str_salary = job["min_salary"]
            salary = (
                int(str_salary) if str_salary.isnumeric() else float("inf")
            )
            min_salary = salary if salary < min_salary else min_salary
        return min_salary if min_salary != float("inf") else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass

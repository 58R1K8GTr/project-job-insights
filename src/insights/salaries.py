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
        """Return a boolean to show if the salary is compatible."""
        try:
            salary = int(salary)
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
        except (ValueError, KeyError, TypeError) as error:
            raise ValueError(error)
        if min_salary > max_salary:
            raise ValueError("Min salary is greater than max salary.")
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        """Returns a list of filtered jobs with a determinated range salary."""
        result_jobs = []
        for job in jobs:
            try:
                salary_matches = self.matches_salary_range(job, salary)
            except ValueError:
                continue
            if salary_matches:
                result_jobs.append(job)
        return result_jobs

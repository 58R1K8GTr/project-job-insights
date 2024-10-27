"""Module to process data from csv file."""

import csv
from typing import NoReturn
from typing import List, Dict, TypeAlias

JobsType: TypeAlias = Dict[str, int | str]


class ProcessJobs:
    """Read and process csv jobs data."""

    def __init__(self) -> None:
        self.jobs_list = []

    def read(self, file_name: str) -> NoReturn:
        """Read a csv file and store dicts."""
        with open(file_name, "r", encoding="utf8") as file:
            reader = csv.reader(file)
            header = next(reader)
            self.jobs_list.extend((dict(zip(header, job)) for job in reader))

    def get_unique_job_types(self) -> List[str]:
        """Return unique job types."""
        return list(set([job["job_type"] for job in self.jobs_list]))

    def filter_by_multiple_criteria(
        self, jobs: JobsType, criteria: JobsType
    ) -> List[Dict]:
        """Filter jobs by criteria."""
        unique_jobs = {
            frozenset(job.items())
            for job in jobs
            if all(job.get(key) == criteria[key] for key in criteria)
        }
        return list(map(dict, unique_jobs))

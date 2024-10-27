"""Module to process csv data file."""

from typing import List
from src.insights.jobs import ProcessJobs


class ProcessIndustries(ProcessJobs):
    """Read and process csv jobs data."""

    def get_unique_industries(self) -> List[str]:
        """Return unique industries from jobs."""
        return list({job["industry"] for job in self.jobs_list})

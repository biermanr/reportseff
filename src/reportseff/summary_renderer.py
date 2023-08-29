"""Module for rendering summary output."""
from typing import List

from .job import Job
from .output_renderer import OutputRenderer


class SummaryRenderer(OutputRenderer):
    """A collection of formatting options for rendering summary output."""

    def __init__(self) -> None:
        """Initialize summary renderer."""
        self._query_columns = [
            "AdminComment",
            "AllocCPUS",
            "Elapsed",
            "JobID",
            "JobIDRaw",
            "MaxRSS",
            "NNodes",
            "REQMEM",
            "State",
            "Timelimit",
            "TotalCPU",
        ]

    def format_jobs(self, jobs: List[Job]) -> str:
        """Given list of jobs, build summary output.

        Args:
            jobs: List of job objects

        Returns:
            Formatted summary as single string
        """
        return f"There were {len(jobs)} jobs"

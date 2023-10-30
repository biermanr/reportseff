"""Module for rendering summary output."""
import collections
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
        total_jobs = f"Summary information for {len(jobs)} job(s)"

        state_counter = collections.Counter(j.state for j in jobs)
        job_states_header = "Number of jobs in each state:"
        job_states_table = "\n".join(
            f"- {s}: {n} job(s)" for s, n in state_counter.items()
        )
        job_states = job_states_header + "\n" + job_states_table

        summary = "\n\n".join((total_jobs, job_states))
        return summary

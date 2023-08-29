"""Module for defining the OutputRenderer abstract base class."""
from abc import ABC, abstractmethod
from typing import List

from .job import Job


class OutputRenderer(ABC):
    """Abstract base class for reportseff output renderers."""

    @abstractmethod
    def format_jobs(self, jobs: List[Job]) -> str:
        """Abstract method for formatting jobs that all output renderers must implement.

        Args:
            jobs: List of job objects

        Returns:
            Formatted output as single string
        """

    @property
    def query_columns(self) -> List[str]:
        """Getter for query_columns property.

        Returns:
            _query_columns: List[str] of query columns for SACCT
        """
        return self._query_columns

    @query_columns.setter
    def query_columns(self, values: List[str]) -> None:
        """Setter for query_columns property.

        Args:
            values: List of query columns to fetch from SACCT
        """
        self._query_columns = values

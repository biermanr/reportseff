"""Test operation of output summary renderer object."""

from reportseff import summary_renderer


def test_renderer_format_jobs(some_jobs):
    """Can render summary output from multiple jobs."""
    renderer = summary_renderer.SummaryRenderer()
    result = renderer.format_jobs(some_jobs)
    assert result == (
        "Summary information for 7 job(s)\n\n"
        "Number of jobs in each state:\n"
        "- COMPLETED: 2 job(s)\n"
        "- PENDING: 1 job(s)\n"
        "- RUNNING: 1 job(s)\n"
        "- CANCELLED: 1 job(s)\n"
        "- TIMEOUT: 1 job(s)\n"
        "- OTHER: 1 job(s)"
    )

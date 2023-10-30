"""Sub-conftest: Collect common fixtures."""
import pytest

from reportseff import job as job_module


@pytest.fixture
def some_jobs():
    """A few test jobs."""
    jobs = []
    job = job_module.Job("24371655", "24371655", None)
    job.update(
        {
            "JobID": "24371655",
            "State": "COMPLETED",
            "AllocCPUS": "1",
            "REQMEM": "1Gn",
            "TotalCPU": "00:09:00",
            "Elapsed": "00:10:00",
            "Timelimit": "00:20:00",
            "MaxRSS": "",
            "NNodes": "1",
            "NTasks": "",
        }
    )
    jobs.append(job)
    job = job_module.Job("24371656", "24371656", None)
    job.update(
        {
            "JobID": "24371656",
            "State": "PENDING",
            "AllocCPUS": "1",
            "REQMEM": "1Gn",
            "TotalCPU": "00:09:00",
            "Elapsed": "00:10:00",
            "Timelimit": "00:20:00",
            "MaxRSS": "",
            "NNodes": "1",
            "NTasks": "",
        }
    )
    jobs.append(job)
    job = job_module.Job("24371657", "24371657", None)
    job.update(
        {
            "JobID": "24371657",
            "State": "RUNNING",
            "AllocCPUS": "1",
            "REQMEM": "1Gn",
            "TotalCPU": "00:09:00",
            "Elapsed": "00:10:00",
            "Timelimit": "00:20:00",
            "MaxRSS": "",
            "NNodes": "1",
            "NTasks": "",
        }
    )
    jobs.append(job)
    job = job_module.Job("24371658", "24371658", None)
    job.update(
        {
            "JobID": "24371658",
            "State": "CANCELLED",
            "AllocCPUS": "1",
            "REQMEM": "1Gn",
            "TotalCPU": "00:09:00",
            "Elapsed": "00:00:00",
            "Timelimit": "00:20:00",
            "MaxRSS": "",
            "NNodes": "1",
            "NTasks": "",
        }
    )
    jobs.append(job)
    job = job_module.Job("24371659", "24371659", None)
    job.update(
        {
            "JobID": "24371659",
            "State": "TIMEOUT",
            "AllocCPUS": "1",
            "REQMEM": "2Gn",
            "TotalCPU": "00:04:00",
            "Elapsed": "00:21:00",
            "Timelimit": "00:20:00",
            "MaxRSS": "",
            "NNodes": "1",
            "NTasks": "",
        }
    )
    jobs.append(job)
    job = job_module.Job("24371660", "24371660", None)
    job.update(
        {
            "JobID": "24371660",
            "State": "OTHER",
            "AllocCPUS": "1",
            "REQMEM": "2Gn",
            "TotalCPU": "00:09:00",
            "Elapsed": "00:12:05",
            "Timelimit": "00:20:00",
            "MaxRSS": "",
            "NNodes": "1",
            "NTasks": "",
        }
    )
    jobs.append(job)
    job = job_module.Job("24371661", "24371661", None)
    job.update(
        {
            "JobID": "24371661",
            "State": "COMPLETED",
            "AllocCPUS": "1",
            "REQMEM": "2Gn",
            "TotalCPU": "00:08:00",
            "Elapsed": "00:10:05",
            "Timelimit": "00:30:00",
            "MaxRSS": "1Gn",
            "NNodes": "1",
            "NTasks": "",
        }
    )
    jobs.append(job)
    return jobs

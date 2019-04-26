import click

from paperspace import client, config
from paperspace.cli import common
from paperspace.commands import jobs as jobs_commands


@click.group("jobs", help="Manage gradient jobs")
def jobs_group():
    pass


@jobs_group.command("delete", help="Delete job")
@click.option(
    "--jobId",
    "job_id",
    required=True,
)
@common.api_key_option
def delete_job(job_id, api_key=None):
    jobs_api = client.API(config.CONFIG_HOST, api_key=api_key)
    command = jobs_commands.DeleteJobCommand(api=jobs_api)
    command.execute(job_id)


@jobs_group.command("stop", help="Stop running job")
@click.option(
    "--jobId",
    "job_id",
    required=True,
)
@common.api_key_option
def stop_job(job_id, api_key=None):
    jobs_api = client.API(config.CONFIG_HOST, api_key=api_key)
    command = jobs_commands.StopJobCommand(api=jobs_api)
    command.execute(job_id)


@jobs_group.command("list", help="List jobs with optional filtering")
@common.api_key_option
def list_jobs(api_key):
    jobs_api = client.API(config.CONFIG_HOST, api_key=api_key)
    command = jobs_commands.ListJobsCommand(api=jobs_api)
    command.execute()

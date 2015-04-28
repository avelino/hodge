#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from cookiecutter.main import cookiecutter


@click.group()
def cmds():
    pass


@cmds.command()
@click.argument('site_name', type=str)
def init(site_name):
    click.echo(u'Hodge init new project...')
    repo_name = site_name.lower().replace(' ', '-')
    app_name = repo_name.replace("-", "")
    extra_context = {
        'site_name': site_name,
        "repo_name": repo_name,
        "app_name": app_name,
        "pkg_name": app_name
    }
    cookiecutter(
        'https://github.com/avelino/hodge-init.git',
        extra_context=extra_context,
        no_input=True)


def main():
    cmds()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import click
from cookiecutter.main import cookiecutter
from slugify import slugify
from jinja2 import Environment, PackageLoader


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
        "pkg_name": app_name,
        "content_folder": "content"
    }
    cookiecutter(
        'https://github.com/avelino/hodge-init.git',
        extra_context=extra_context,
        no_input=True)


@cmds.command()
def newpost():
    if not os.path.isfile("./hodge.toml"):
        click.echo(u'hodge.toml (config) not exist!')
        exit(0)

    click.echo(u'Hodge new post create...')
    obj = {}
    obj["title"] = click.prompt('Title', type=str)
    obj["slug"] = slugify(obj["title"])
    obj["tags"] = click.prompt('Tags (hodge, static)', type=str)


def main():
    cmds()

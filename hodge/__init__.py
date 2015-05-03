#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io
import shutil
import click
import http.server
import socketserver
import markdown2
from cookiecutter.main import cookiecutter
from slugify import slugify
from jinja2 import Template, Environment, FileSystemLoader
from datetime import datetime
from click.testing import CliRunner

from .utils import walk_dir


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
@click.option('--title', type=str, prompt=True)
@click.option('--date', type=str,
              default=datetime.now(),
              prompt=True)
def newpost(title, date):
    if not os.path.isfile("./hodge.toml"):
        click.echo(u'hodge.toml (config) not exist!')
        exit(0)

    click.echo(u'Hodge new post create...')

    obj = {}
    obj["title"] = title
    obj["date"] = date.strftime("%Y/%m/%d %H:%M:%S")
    slug = slugify(obj["title"])
    obj["slug"] = click.prompt('Slug', type=str, default=slug)
    obj["tags"] = click.prompt('Tags (hodge, static)', type=str,
                               default=", ".join(obj["title"].split(" ")))
    obj["file"] = click.prompt(
        "File name",
        type=str,
        default=date.strftime("%Y_%m_%d_{}.md".format(obj["slug"])))

    template_path = os.path.join(os.path.dirname(__file__), "templates")
    tmp = Template(io.open(os.path.join(template_path, "newpost.md")).read())
    if not os.path.isdir("./content"):
        os.mkdir("./content")

    with io.open("./content/{}".format(obj["file"]), "wb") as f:
        f.write(tmp.render(**obj).encode())

    return obj


@cmds.command()
def build():
    if not os.path.isfile("./hodge.toml"):
        click.echo(u'hodge.toml (config) not exist!')
        exit(0)

    click.echo(u'Hodge build...')
    template_path = os.path.join("theme", "default")
    env = Environment(autoescape=True,
                      loader=FileSystemLoader(template_path))
    template_content = env.get_template('content.html')

    shutil.rmtree("./build", ignore_errors=True)

    index = []

    for filename in walk_dir("./content"):
        text = io.open(filename, "rb").read()
        html = markdown2.markdown(text, extras=["metadata"])
        meta = html.metadata
        content = {"content": html, "meta": meta}
        content["meta"]["uri"] = "/{}.html".format(meta.get("slug"))

        if not os.path.isdir("./build"):
            os.mkdir("./build")

        with open("./build/{}.html".format(meta.get("slug")), "w") as fh:
            fh.write(template_content.render(**content))

        click.echo("- {}".format(meta.get("slug")))

        index.append(content)

    template_index = env.get_template('index.html')
    content = {"posts": index}
    with open("./build/index.html", "w") as fh:
        fh.write(template_index.render(**content))


@cmds.command()
@click.argument('port', type=int, default=3000)
def server(port):
    click.echo(u'Hodge run...')

    # Run Build
    runner = CliRunner()
    runner.invoke(build)

    # Open folder build
    os.chdir("build")

    # Run simple http server
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    click.echo(u'Serving HTTP on http://127.0.0.1:{}'.format(port))
    httpd.serve_forever()


def main():
    cmds()

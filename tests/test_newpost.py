# -*- coding: utf-8 -*-
import os
import shutil
from datetime import datetime
from click.testing import CliRunner
from slugify import slugify
from hodge import init, newpost


class TestNewPost(object):
    def setUp(self):
        os.chdir(os.path.dirname(__file__))
        project_path = os.path.join(os.path.dirname(__file__), "test_newpost")

        shutil.rmtree(project_path, ignore_errors=True)
        self.runner = CliRunner()
        self.runner.invoke(init, ['test_newpost'])

        os.chdir(project_path)
        self.title = "A test create new post"
        self.slug = slugify(self.title)
        self.date = datetime.now()
        self.file_name = self.date.strftime("%Y_%m_%d_{}.md".format(self.slug))

        self.result = self.runner.invoke(newpost, [self.title, self.date])

    def test_exist_hodge_conf(self):
        assert os.path.isfile("hodge.toml")

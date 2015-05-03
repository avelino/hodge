# -*- coding: utf-8 -*-
import os
import shutil
from click.testing import CliRunner
from hodge import init


class TestInit(object):
    def setUp(self):
        shutil.rmtree("./test_1", ignore_errors=True)
        self.runner = CliRunner()
        self.result = self.runner.invoke(init, ['test_1'])

    def test_create_environment(self):
        assert os.path.isdir("./test_1")

    def test_exist_hodge_conf(self):
        assert os.path.isfile("./test_1/hodge.toml")

    def test_exist_content_folder(self):
        assert os.path.isdir("./test_1/content")

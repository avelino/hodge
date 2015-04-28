# -*- coding: utf-8 -*-
import os


def walk_dir(path):
    for root, dirs, files in os.walk(path):
        if '.git' in dirs:
            dirs.remove('.git')
        if '.hg' in dirs:
            dirs.remove('.hg')
        if '.svn' in dirs:
            dirs.remove('.svn')
        for f in files:
            path = os.path.join(root, f)
            yield path

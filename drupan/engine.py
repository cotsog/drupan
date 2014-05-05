# -*- coding: utf-8 -*-
"""
    drupan.engine

    The engine is part of drupan that holds all plugins and subsystems
    together and runs the actual site creation process.
"""

from .site import Site
from .config import Config
from .template import Render
from .serve import http


class Engine(object):
    """Drupan engine doing all the work"""
    def __init__(self):
        self.site = Site()
        self.config = Config()
        self.reader = None
        self.writer = None
        self.plugins = list()
        self.render = None

    def prepare_engine(self):
        """get all subsystems and plugins setup"""
        self.reader = __import__(
            "drupan.inout.{0}".format(self.config.reader),
            fromlist=["Reader"]
        ).Reader(self.site, self.config)

        self.writer = __import__(
            "drupan.inout.{0}".format(self.config.writer),
            fromlist=["Writer"]
        ).Writer(self.site, self.config)

        for name in self.config.plugins:
            plugin = __import__(
                "drupan.plugins.{0}".format(name),
                fromlist=["Plugin"]
            ).Plugin(self.site, self.config)
            self.plugins.append(plugin)

        self.render = Render(self.site, self.config)

    def run(self):
        """run the site generation process"""
        self.reader.run()
        for plugin in self.plugins:
            plugin.run()
        self.render.run()
        self.writer.run()

    def serve(self):
        """serve the generated site"""
        http(self.config.get_option("writer", "directory"))

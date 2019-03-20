from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.nn.api.manager import Manager
from cloudmesh.common.console import  Console
from cloudmesh.common.util import path_expand
from pprint import pprint


class NnCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_nn(self, args, arguments):
        """
        ::

          Usage:
                nn start
                nn stop

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """

        m = Manager()

        if arguments.start:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.stop:
            print("option b")
            m.list("just calling list without parameter")


        Console.error("This is just a sample")
        return ""


# Copyright (c) 2021 Ansible, Inc.
# All Rights Reserved
import sys

from awx.main.utils.common import get_custom_venv_choices, get_custom_venv_pip_freeze
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """Returns either the pip freeze from the path passed in the argument"""

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            type=str,
            nargs='?',
            default='',
            help='run this with a path to a virutal environment as an argument to see the pip freeze data',
        )

    def handle(self, *args, **options):
        super(Command, self).__init__()
        if options.get('path'):
            pip_data = get_custom_venv_pip_freeze(options.get('path'))
            if pip_data:
                print(pip_data)
        else:
            print("missing argument: please include a path argument following the command.")

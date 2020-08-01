__version__ = "2020.8.0.dev0"

__title__ = "firefly"
__description__ = "Firefly is a modern game engine in python"
__url__ = "https://github.com/ambye85/firefly/"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"

__author__ = "Ashley Morton-Bye"
__email__ = "ambye85@example.com"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2020 Ashley Morton-Bye"

from .firefly import greet

__all__ = [
    "greet",
]


# import os
# import sys

import importlib_metadata

from .vnpy_gateway.ib_gateway import IbGateway
from .vnpy_datafeed.ib_datafeed import IbDatafeed as Datafeed
from .vnpy_datamanager import DataManagerApp, ui


# from .ib_gateway import IbGateway
# from .ib_datafeed import IbDatafeed

try:
    __version__ = importlib_metadata.version("vnpy_ib")
except importlib_metadata.PackageNotFoundError:
    __version__ = "dev"
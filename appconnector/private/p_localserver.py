from ..qt import QtNetwork, QtCore
from .p_server import Server


class LocalServer(QtNetwork.QLocalServer, metaclass=Server):

    def __init__(self, *args, **kwargs):

        """
        initialise server
        """

        QtNetwork.QLocalServer.__init__(self, *args, **kwargs)

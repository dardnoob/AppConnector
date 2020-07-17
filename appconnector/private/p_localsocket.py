from ..qt import QtCore, QtNetwork
from .p_socket import Socket


class LocalSocket(QtNetwork.QLocalSocket, metaclass=Socket):

    def __init__(self, *args, **kwargs):

        """
        initialise socket object
        """

        QtNetwork.QLocalSocket.__init__(self, *args, **kwargs)

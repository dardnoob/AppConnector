from ..qt import QtCore, QtNetwork
from .p_socket import Socket


class TcpSocket(QtNetwork.QTcpSocket, metaclass=Socket):

    def __init__(self, *args, **kwargs):

        """
        initialise socket object
        """

        QtNetwork.QTcpSocket.__init__(self, *args, **kwargs)

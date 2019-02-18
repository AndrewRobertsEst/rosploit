# Node class definition for common communication of scripts
import json
import socket
import xmlrpc.client


class Node:
    """
        Defines a Ros node class, which allows a common structure for passing information about ros nodes
    """

    def __init__(self, ip_addr: str, port: str, notes: str = ''):
        try:
            socket.inet_aton(ip_addr)
        except socket.error:
            print("Invalid IP address given to create node")
            raise
        self.ip_addr = ip_addr
        self.port = port
        self.notes = notes
        self.server = xmlrpc.client.ServerProxy((self.ip_addr, self.port))
        self.pub_topics = []
        self.sub_topics = []

    def to_json(self):
        return json.dumps({"ip_addr": self.ip_addr, "port": self.port, "notes": self.notes}, sort_keys=True, indent=4)

    @classmethod
    def from_json(cls, o):
        classdict = json.loads(o)
        cls.ip_addr = classdict['ip_addr']
        cls.port = classdict['port']
        cls.notes = classdict['notes']
        return cls(ip_addr=cls.ip_addr, port=cls.port, notes=cls.notes)
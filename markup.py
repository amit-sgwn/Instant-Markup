import sys,re
from handler import *
from util import *
from rules import *

class Parser:
    """
    A Parser reads text file ,applying rules and controlling a handler.
    """

    def __init__(self,handler):
        self.handler = handler
        self.rules = []
        self.filters = []

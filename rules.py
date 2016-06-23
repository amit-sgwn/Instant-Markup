class Rule:
    """

    Base class for all rules.
    """
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return 1


class Rule:
    """

    Base class for all rules.
    """
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return 1

class HeadingRule(Rule):
    """
    A heading is a single line having at most 70 characters and that doesn't
    end with a colon.
    """

    type ='heading'
    def condition(block):
        return not '\n' in block and len(block)<=70 and not block[-1]==':'
class TitleRule(HeadingRule):
    """
    Title is the first block in any html document provided that
    it is a heading.
    """
    type ='title'
    first=1
    def condition(self,block):
        
    

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
        if not self.first:
            return 0
        self.first =0
        return HeadingRule.condition(self,block)

class ListItemRule(Rule):
    """
    A list is a paragraph  that begin with a Hyphen. As a part of the
    formatting,the hyphen is removed.
    """

    type='listitem'
    def condition(self,block):
        return block[0] =='-'
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return 1

class ListRule(ListItemRule):
    """
    Alist begin between a block that is not a list item and a
    subsequent list item . It ends after the last consecutive list item
    """

    type='list'
    inside=0

    def condition(self,block);
        return 1
    def action(self,block,handler):
        if not self.inside and ListItemRule.condition(self,block):
            handler.start(self.type)
            handler.inside=1
        elif self.inside and ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside=0
        return 0

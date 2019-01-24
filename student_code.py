import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        if isinstance(fact, Fact):
            for i in self.facts:
                if i == fact:
                    return
            self.facts.append(fact)
        # elif isinstance(fact, Rule):
        #     for i in self.rules:
        #         if i == fact:
        #             return
        #     self.rules.append(fact)

        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        bindingslist = ListOfBindings()
        for i in self.facts:
            if match(i.statement, fact.statement, bindings=None) != False:

                bindingslist.add_bindings(match(i.statement, fact.statement, bindings=None), i)

        print("Asking {!r}".format(fact))
        return bindingslist


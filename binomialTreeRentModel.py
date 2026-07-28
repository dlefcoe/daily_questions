'''
author: darren**2
date: 2019

rent model.

there exists a situation where a tenant renting a property can either pay their rent, u, with a probability P
or can only pay part of the rent, d, with a probability (1-p).

We work out the fair value, v of the rent as follows:
v = [u * p] + [d * (1-p)]

given one can assume the fair value v and a probability of getting paid for the period
construct a binomial tree that computed the child legs.

the function would be
f(v, p) returns u, d

step 2:
assuming we know the outcomes
compute (and store) the next values on the tree

'''

class Node:
    """Class to represent a node."""
    def __init__(self, val=None, prob=None, recovery=None, rent=None):
        self.up = self.dn = None
        Node.recovery = recovery or Node.recovery
        Node.prob = prob or Node.prob
        Node.rent = rent or Node.rent
        self.val = val or self.getfairvalue()

    def getfairvalue(self):
        """Get fair value (only called if not set on object creation)."""
        good = Node.prob * Node.rent
        bad = (1 - Node.prob) * Node.rent * Node.recovery
        return good + bad


    def __repr__(self):
        """Define output of print function."""
        if self.up or self.dn:
            return(f"{self.val}[{self.up},{self.dn}]")
        return str(self.val)

    def mkupdn(self):
        """Create child nodes."""
        self.up = Node(Node.prob * self.val)
        self.dn = Node((1 - Node.prob) * self.val * Node.recovery)


root = Node(prob=0.99, recovery=0.15, rent=1000)
root.mkupdn()
root.up.mkupdn()
root.dn.mkupdn()

print(root)



"""
output is:
925.0[900.0,24.999999999999993]

"""

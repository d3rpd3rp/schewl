# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from pacman import Directions
from game import Agent
from heuristics import scoreEvaluation
import random
import sys

sys.setrecursionlimit(10000)

class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
        return actions[random.randint(0,len(actions)-1)]

class GreedyAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        legal = state.getLegalPacmanActions()
        # get all the successor state for these actions
        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(scoreEvaluation(state), action) for state, action in successors]
        # get best choice
        bestScore = max(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # return random action from the list of the best actions
        return random.choice(bestActions)

class node:
    def __init__ (self, state, prevAction, parent, depth):
        self.state = state
        self.children = None
        self.visited = False
        self.parent = parent
        self.prevAction = prevAction
        self.depth = depth
        self.successState = state.isWin()
        if state.isLose():
            self.isDead = True
        else:
            self.isDead = False
    
    def addChild(self, node):
        self.children.append(node)
    
    def retParent(self):
        return(self.parent)

    def markVisited(self):
        self.visited = True
    
    def prevAction(self):
        return(self.prevAction())

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return

    def traceback(self, Node, actionSequence):
        actionSequence.append(Node.prevAction())        
        traceback(Node.retParent())
        return (actionSequence)

    def BFS(self, Node, state, depth):
        #print ('top of BFS: state is of type {} and state.isWin() has value {}'.format(type(state), state.isWin()))  
        #print ('top of BFS: Node is of type {} and Node.successState() has value {}'.format(type(Node), Node.successState))  
        if Node.successState:
            actionSequence = []
            actionSequence = traceback(self, Node, actionSequence)
            return (actionSequence)
        elif Node.isDead:
            return
        else:
            #def __init__ (self, state, prevAction, parent, depth):
            if (Node.depth < depth):
                children = []
                successorState = []
                legal = state.getLegalPacmanActions()
                for action in legal:
                    index = 0
                    successorState.append(state.generateSuccessor((0, action), action))
                    print('generate successor returns state type {} and value {}'.format(type(successorState[index]), successorState[index]))
                    #print ('creating first child: successorState is of type {} and successorState[index] is type {}'.format(type(successorState), type(successorState[index])))
                    #print ('creating first child: successorState[index][0] is {}'.format(successorState[index][0]))
                    c = node(successorState[index][0], action, Node, depth+1)
                    if not c.isDead:
                        children.append(c)
                        print('found {} viable children at depth {}'.format(len(children), depth+1))
                        index += 1
                depth += 1
                for child in children:
                    BFSAgent.BFS(self, child, Node.state, depth)

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP
        #def __init__ (self, state, prevAction, parent, depth):
        root = node(state, None, None, 0)
        #print ('state is of type {} and isWin has value {}'.format(type(state), state.isWin()))
        #print ('root is of type {} and root.state.isWin() has value {}'.format(type(root), root.state.isWin()))        
        return BFSAgent.BFS(self, root, state, 1)

class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write DFS Algorithm instead of returning Directions.STOP
        return Directions.STOP

class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP
        return Directions.STOP

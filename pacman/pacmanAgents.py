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

    def addChild(self, node):
        self.children.append(node)
    
    def retParent(self):
        return(self.parent)

    def markVisited(self):
        self.visited = True
    
    def prevAction(self):
        return(self.prevAction())
    
    def isDead(self):
        if self.state.isLose():
            self.dead = True
        else:
            self.dead = False

    def traceback(self, actionSequence):
        actionSequence.append(Node.prevAction())        
        traceback(Node.retParent())
        return (actionSequence)

    def BFS(self, depth, KnownStates):
        #print ('top of BFS: state is of type {} and state.isWin() has value {}'.format(type(state), state.isWin()))  
        #print ('top of BFS: Node is of type {} and Node.successState() has value {}'.format(type(Node), Node.successState))
        print('top of BFS call...')
        if self.successState:
            actionSequence = []
            actionSequence = traceback(actionSequence)
            return (actionSequence)
        elif self.isDead():
            return
        else:
            print('inside BFS else...self.depth is {} and depth is {}'.format(self.depth, depth))
            #def __init__ (self, state, prevAction, parent, depth):
            if (self.depth < depth):
                #print('after depth check, before legal assignment...')
                children = []
                legal = self.state.getLegalPacmanActions()
                #print('after get legal assignment...')
                index = 0
                for action in legal:
                    print('action is {}'.format(action))
                    if action is not None:
                        print('after action is None test...')     
                        successorState = self.state.generateSuccessor(0, action)
                        #print('state.generateSuccessor((0, action), action is {}'.format(state.generateSuccessor(0, action)))
                        #print('generate successor returns state type {} and value {}'.format(type(successorState[index]), successorState[index]))
                        #print ('creating first child: successorState is of type {} and successorState[index] is type {}'.format(type(successorState), type(successorState[index])))
                        #print ('creating first child: successorState[index] is: \n{}'.format(successorState[index]))
                        c = node(successorState, action, self, depth)
                        print('length of known states is {}'.format(len(KnownStates)))
                        if len(KnownStates) == 0:
                            KnownStates.append(successorState)
                            children.append(c)
                            index += 1
                        else:
                            for i in range(0, (len(KnownStates)), 1):
                                if KnownStates[i] is successorState:
                                    break
                                elif i == len(KnownStates):
                                    KnownStates.append(successorState)
                                    addChild = True
                                    if not c.isDead() and addChild:
                                        children.append(c)
                                        index += 1
                print('found {} viable children at depth {}'.format(len(children), depth))
                if len(children) > 0:
                    depth += 1
                    for child in children:
                        print('child info: \nstate:\n{}\nprevAction: {}\ntype(parent): {}\ndepth:{}'.format(child.state, child.prevAction, type(child.parent), child.depth))
                        print('available actions for child: {}'.format(child.state.getLegalPacmanActions()))
                        child.BFS(depth, KnownStates)

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP
        #def __init__ (self, state, prevAction, parent, depth):
        root = node(state, None, None, 0)
        known_states = []
        #print ('state is of type {} and isWin has value {}'.format(type(state), state.isWin()))
        #print ('root is of type {} and root.state.isWin() has value {}'.format(type(root), root.state.isWin()))        
        return root.BFS(1, known_states)

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

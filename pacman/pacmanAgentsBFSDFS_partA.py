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

sys.setrecursionlimit(100000)

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
    def __init__ (self, state, prevAction = None, parent = None, depth = 0, bfsSearchDepth = 0):
        self.state = state
        self.prevAction = prevAction
        self.parent = parent
        self.depth = depth
        self.bfsSearchDepth = bfsSearchDepth
        if state is not None:
            self.successState = state.isWin()
        else:
            self.successState = False
        self.children = []
        self.visited = False
        self.bfsPathMember = False

    def addChild(self, node):
        self.children.append(node)

    def isDead(self):
        if self.state.isLose():
            self.dead = True
        else:
            self.dead = False

    def traceback(self):
        #print('from backward to forward the sequence is: ')
        sequence = []
        if self.parent == None:
            sequence.append(self.prevAction )
            return (sequence)
        sequence.append(self.prevAction)
        #print('{}, '.format(self.prevAction))
        nextNode = self.parent
        sequence.append(nextNode.prevAction)
        while nextNode.parent is not None:
            nextNode = nextNode.parent
            if nextNode.prevAction is not None:
                sequence.append(nextNode.prevAction)
        return(sequence)


def BFS(state, Node = None, lastAction = None, depth = None):
    global controlCounter, knownStates, nodes, moves, counter, ceilingBest, treeDepth
    """
    #print('control counter is now {}'.format(controlCounter))
    if controlCounter > 500:
        print ('controlcounter hit...knownStates is now size {}'.format(len(knownStates)))
        return
    """
    if Node is not None:
        if Node.bfsSearchDepth < 1:
            print('failed depth check...')
            return

    if state.isWin():
        Node.successState = True
        Node.prevAction = lastAction
        nodes[state] = Node
        knownStates[state] = scoreEvaluation(state)
        moves = Node.traceback()
        moves.append(action)
        return (moves) 
    elif state.isLose():
        print('Lost in current state is lose...')
        Node.successState = False
        Node.prevAction = lastAction
        nodes[state] = Node
        knownStates[state] = scoreEvaluation(state)
        moves = Node.traceback()
        moves.append(action)
        return (moves) 
    else:
        #print('BFS else: state is type {} and Node is type {}.'.format(type(state), type(Node)))
        if Node is not None:
            Node.bfsSearchDepth -= 1
        legal = state.getLegalPacmanActions()
        for action in legal:
            if action is not None:
                #print('action in else is {}'.format(action))
                if (counter > 5000):
                    #print('counter for successor hit {}'.format(counter))
                    v=list(knownStates.values())
                    k=list(knownStates.keys())
                    #print ('k[v.index(max(v))] returns type {} and value {}'.format(type(k[v.index(max(v))]), k[v.index(max(v))]))
                    soFarBestState = k[v.index(max(v))]
                    #print('the best state so far var resolved as type: {} and value {}'.format(type(soFarBestState), soFarBestState))
                    if soFarBestState not in nodes.keys():
                        print('soFarBestState not found in keys.')
                        #not sure about this creature....
                        soFarBestNode = node(state, prevAction = Node.prevAction, parent = Node.parent, depth = Node.depth)
                        nodes[soFarBestState] = soFarBestNode
                    soFarBestNode = nodes[soFarBestState]
                    #print('the best node so far var resolved as type: {} and value {}'.format(type(soFarBestNode), soFarBestNode))
                    if ceilingBest < max(v):
                        print('found new ceilingBest at {}'.format(max(v)))
                        ceilingBest = max(v)
                        moves = soFarBestNode.traceback()
                        print('computing moves...')
                    #do i remove this return here? how to properly end recursion...
                    return
                    #print('trying to return moves in max succcesor test...with high score of {}'.format(scoreEvaluation(soFarBestState)))
                    #print('moves is of type {} and value {}'.format(type(moves), moves))
                else:
                    counter += 1
                    #print('Next call to successor is number {}.'.format(counter))
                    successorState = state.generateSuccessor(0, action)
                    if successorState not in knownStates:
                        #print('in new successor state under action loop...')
                        c = node(successorState, action, Node, depth)
                        if successorState.isWin():
                            Node.prevAction = lastAction
                            nodes[successorState] = c
                            knownStates[successorState] = scoreEvaluation(successorState)
                            moves = c.traceback()
                            print('trying to return moves in winning state...')
                            return (moves) 
                        elif successorState.isLose():
                            #print('Lost in successor state.')
                            knownStates[successorState] = scoreEvaluation(state)
                        else:
                            knownStates[successorState] = scoreEvaluation(successorState)
                            #print('knownStates is size {}'.format(len(knownStates)))
                            c.bfsSearchDepth = 1
                            nodes[state] = c
                            BFS(successorState, Node = c, lastAction = action)
        treeDepth += 1
        #print('Current depth is {}.'.format(treeDepth))

def DFS(state, Node = None, lastAction = None, depth = None):
    global knownStates, nodes, moves, counter, ceilingBest, treeDepth
    """
    #print('control counter is now {}'.format(controlCounter))
    if controlCounter > 500:
        print ('controlcounter hit...knownStates is now size {}'.format(len(knownStates)))
        return
    """
    if state.isWin():
        print('is win test for state...')
        Node.successState = True
        Node.prevAction = lastAction
        nodes[state] = Node
        knownStates[state] = scoreEvaluation(state)
        moves = Node.traceback()
        moves.append(lastAction)
        return (moves) 
    elif state.isLose():
        print('Lost in current state is lose...')
        Node.successState = False
        Node.prevAction = lastAction
        nodes[state] = Node
        knownStates[state] = scoreEvaluation(state)
    else:
        legal = state.getLegalPacmanActions()
        checkNum = len(legal)
        n = None
        for action in legal:
            checkNum -= 1
            if action is not None:
                if (counter > 5000):
                    v=list(knownStates.values())
                    k=list(knownStates.keys())
                    soFarBestState = k[v.index(max(v))]
                    if soFarBestState not in nodes.keys():
                        print('soFarBestState not found in keys.')
                        soFarBestNode = node(state, prevAction = Node.prevAction, parent = Node.parent, depth = Node.depth)
                        nodes[soFarBestState] = soFarBestNode
                        n  = soFarBestNode
                    soFarBestNode = nodes[soFarBestState]
                    if n is None:
                        n = soFarBestNode
                    if ceilingBest < max(v):
                        print('found new ceilingBest at {}'.format(max(v)))
                        ceilingBest = max(v)
                        n = soFarBestNode
                    if checkNum < 1:
                        #print('checkNum is now {}'.format(checkNum))
                        return (n.traceback()) 
                else:
                    counter += 1
                    successorState = state.generateSuccessor(0, action)
                    if successorState not in knownStates:
                        c = node(successorState, action, Node, depth)
                        if successorState.isWin():
                            Node.prevAction = lastAction
                            nodes[successorState] = c
                            knownStates[successorState] = scoreEvaluation(successorState)
                            moves = c.traceback()
                            return (moves) 
                        elif successorState.isLose():
                            knownStates[successorState] = scoreEvaluation(state)
                        else:
                            knownStates[successorState] = scoreEvaluation(successorState)
                            nodes[state] = c
                            DFS(successorState, Node = c, lastAction = action)
        treeDepth += 1

def AStar (state, Node = None):
    global knownStates, nodes, moves, counter
    if state in knownStates:
        if state in nodes:
            print('found state in AStar, both in knownStates and nodes.')
            #performs a single depth search for cheapest node
            AStarSearch(state, nodes[state], depth = Node.depth)
            AStarSearch()
            print('returned winNode of type {} and values {}'.format(type(winNode), winNode))
            moves = winNode.traceback()
            print('moves is {}'.format(moves))
    else:
        knownStates[state] = scoreEvaluation(state)
        n = node(state, Node.prevAction, Node.parent, Node.depth)
        nodes[state] = n
        winNode = AStarDFSsearch(state, nodes[state])
        print('returned winNode of type {} and values {}'.format(type(winNode), winNode))
        moves = winNode.traceback()

def AStarSearch(state, Node = None, lastAction = None, depth = None):
    global controlCounter, knownStates, nodes, moves, counter, ceilingBest
    #ONLY EXPAND NODES WITH LOWEST COST
    if state.isWin():
        Node.successState = True
        Node.prevAction = lastAction
        nodes[state] = Node
        knownStates[state] = depth - (scoreEvaluation(state) - scoreEvaluation(root.state))
    else:
        legal = state.getLegalPacmanActions()
        checkNum = len(legal)
        n = None
        for action in legal:
            if action is not None:
                successorState = state.generateSuccessor(0, action)
                if successorState not in knownStates:
                    c = node(successorState, action, Node)
                    nodes[successorState] = c
                    knownStates[successorState] = depth - (scoreEvaluation(successorState) - scoreEvaluation(root.state))
                else:
                    knownStates[successorState] = depth - (scoreEvaluation(successorState) - scoreEvaluation(root.state))
                    nodes[successorState] = c


class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        global root, nodes, trackState
        return

    # GetAction Function: Called with every frame
    def getAction(self, state):
        global nodes, knownStates, root, moves, trackState, counter, ceilingBest
        if trackState is not type(state):
            trackState = type(state)
            print('state is now of type {} and value \n{}.'.format(type(state), state))
        root = node(state, None, None, 0)
        root.bfsSearchDepth = 1
        nodes.clear()
        nodes[state] = root
        knownStates.clear()
        knownStates[state] = scoreEvaluation(state)
        ceilingBest = -1
        counter = 0
        moves = []
        BFS(state, Node = root)
        if ((len(moves)) == 0):
            print('returned a moves list with a lenght 0. Trying to reassign junk in directions var...')
            direction = direction
        elif ((len(moves)) == 1):
            direction = moves[0]
        else:
            direction = moves[-1]
        print('direction is {}'.format(direction))
        if direction is 'North':
            return Directions.NORTH
        if direction is 'South':
            return Directions.SOUTH
        if direction is 'East':
            return Directions.EAST
        if direction is 'West':
            return Directions.WEST
        

        

class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return

    # GetAction Function: Called with every frame
    def getAction(self, state):
        global nodes, knownStates, root, moves, trackState, counter, ceilingBest
        if trackState is not type(state):
            trackState = type(state)
            print('state is now of type {} and value \n{}.'.format(type(state), state))
        root = node(state, None, None, 0)
        nodes.clear()
        nodes[state] = root
        knownStates.clear()
        knownStates[state] = scoreEvaluation(state)
        ceilingBest = -1
        counter = 0
        moves = []
        moves = DFS(state, Node = root)
        if ((len(moves)) == 0):
            direction = None
        elif ((len(moves)) == 1):
            direction = moves[0]
        else:
            direction = moves[-1]
        print('direction is {}'.format(direction))
        if direction is 'North':
            return Directions.NORTH
        if direction is 'South':
            return Directions.SOUTH
        if direction is 'East':
            return Directions.EAST
        if direction is 'West':
            return Directions.WEST
        if direction is None:
            return Directions.STOP

class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return

    # GetAction Function: Called with every frame
    def getAction(self, state):
        global knownStates, nodes, root, GdepthCosts
        root = node(state, None, None, 0)
        nodes.clear()
        nodes[state] = root
        GdepthCosts[0] = 0
        knownStates.clear()
        knownStates[state] = 0 - (scoreEvaluation(state) - scoreEvaluation(root.state))
        ceilingBest = -1
        counter = 0
        moves = []
        AStar(state, root, depth = 0)
        if ((len(moves)) == 0):
            print('No moves passed after AStar call.')
        if ((len(moves)) == 1):
            direction = moves[0]
        else:
            direction = moves[-1]
        print('direction is {}'.format(direction))
        if direction is 'North':
            return Directions.NORTH
        if direction is 'South':
            return Directions.SOUTH
        if direction is 'East':
            return Directions.EAST
        if direction is 'West':
            return Directions.WEST

#global vars
knownStates = {}
moves = []
nodes = {}

#test/tmp global vars
counter = 0
trackState = ''
ceilingBest = -1
treeDepth = 0
root = node(None) 
GdepthCosts = []

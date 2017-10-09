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

#global vars
knownStates = {}
moves = []
nodes = {}

#test/tmp global vars
counter = 0
trackState = ''

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

def compareStateAttr(state1, state2):

    if state1.data._foodEaten:
        if state2.data._foodEaten:
            state1foodEaten = getattr(state1.data, '_foodEaten')
            state2foodEaten = getattr(state2.data, '_foodEaten')
            if state1.data._foodEaten != state2.data._foodEaten:
                print('first state has __foodEaten as {} and second as {}'.format(state1.data._foodEaten, state2.data._foodEaten))
        else:
            print('second state has no __foodEaten attribute.')
    else:
        print('first state has no __foodEaten attribute.')

    if state1.data.layout:
        if state2.data.layout:
            state1layout = getattr(state1.data, 'layout')
            state2layout = getattr(state2.data, 'layout')
            print('state1layout is of type {}'.format(type(state1layout)))
            if state1layout == state2layout:
                print('layouts equal.')
            else:
                print('state1layout as\n{}\n and second as\n{}'.format(state1layout, state2layout))
        else:
            print('second state has no layout.Layout attribute.')
    else:
        print('first state has no layout.Layout attribute.')

    if state1.data.food:
        if state2.data.food:
            if state1.data.food != state2.data.food:
                print('first state has food as {} and second as {}'.format(state1.data.food, state2.data.food))
        else:
            print('second state has no food attribute.')
    else:
        print('first state has no food attribute.')
    
    if state1.data._foodAdded:
        if state2.data._foodAdded:
            if state1.data._foodAdded != state2.data._foodAdded:
                print('first state has _foodAdded as {} and second as {}'.format(state1.data._foodAdded, state2.data._foodAdded))
        else:
            print('second state has no _foodAdded attribute.')
    else:
        print('first state has no _foodAdded attribute.')
    
    if state1.data.agentStates:
        if state2.data.agentStates:
            if state1.data.agentStates != state2.data.agentStates:
                print('first state has agentStates as {} and second as {}'.format(state1.data.agentStates, state2.data.agentStates))
        else:
            print('second state has no agentStates attribute.')
    else:
        print('first state has no agentStates attribute.')

    if state1.data._win:
        if state2.data._win:
            if state1.data._win != state2.data._win:
                print('first state has _win as {} and second as {}'.format(state1.data._win, state2.data._win))
        else:
            print('second state has no _win attribute.')
    else:
        print('first state has no _win attribute.')

    if state1.data._eaten:
        if state2.data._eaten:
            if state1.data._eaten != state2.data._eaten:
                print('first state has _eaten as {} and second as {}'.format(state1.data._eaten, state2.data._eaten))
        else:
            print('second state has no _eaten attribute.')
    else:
        print('first state has no _eaten attribute.')

    if state1.data.score:
        if state2.data.score:
            if state1.data.score != state2.data.score:
                print('first state has score as {} and second as {}'.format(state1.data.score, state2.data.score))
        else:
            print('second state has no score attribute.')
    else:
        print('first state has no score attribute.')

    if state1.data._agentMoved:
        if state2.data._agentMoved:
            if state1.data._agentMoved != state2.data._agentMoved:
                print('first state has _agentMoved as {} and second as {}'.format(state1.data._agentMoved, state2.data._agentMoved))
        else:
            print('second state has no _agentMoved attribute.')
    else:
        print('first state has no _agentMoved attribute.')

    if state1.data._lose:
        if state2.data._lose:
            if state1.data._lose != state2.data._lose:
                print('first state has _lose as {} and second as {}'.format(state1.data._lose, state2.data._lose))
        else:
            print('second state has no _lose attribute.')
    else:
        print('first state has no _lose attribute.')

    if state1.data.scoreChange:
        if state2.data.scoreChange:
            if state1.data.scoreChange != state2.data.scoreChange:
                print('first state has scoreChange as {} and second as {}'.format(state1.data.scoreChange, state2.data.scoreChange))
        else:
            print('second state has no scoreChange attribute.')
    else:
        print('first state has no scoreChange attribute.')

    if state1.data.capsules:
        if state2.data.capsules:
            if state1.data.capsules != state2.data.capsules:
                print('first state has capsules as {} and second as {}'.format(state1.data.capsules, state2.data.capsules))
        else:
            print('second state has no capsules attribute.')
    else:
        print('first state has no capsules attribute.')

    if state1.data._capsuleEaten:
        if state2.data._capsuleEaten:
            if state1.data._capsuleEaten != state2.data._capsuleEaten:
                print('first state has _capsuleEaten as {} and second as {}'.format(state1.data._capsuleEaten, state2.data._capsuleEaten))
        else:
            print('second state has no _capsuleEaten attribute.')
    else:
        print('first state has no _capsuleEaten attribute.')

class node:
    def __init__ (self, state, prevAction = None, parent = None, depth = 0):
        self.state = state
        self.prevAction = prevAction
        self.parent = parent
        self.depth = depth
        self.successState = state.isWin()
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
        sequence = []
        if self.parent == None:
            return (sequence)
        sequence.append(self.prevAction)
        nextNode = self.parent
        sequence.append(self.prevAction)
        while nextNode.depth > 1:
            sequence.append(self.prevAction)
            nextNode = nextNode.parent
        return (sequence)


def BFS(state, Node = None, lastAction = None, depth = 1):
    global controlCounter, knownStates, nodes, moves, counter
    """
    #print('control counter is now {}'.format(controlCounter))
    if controlCounter > 500:
        print ('controlcounter hit...knownStates is now size {}'.format(len(knownStates)))
        return
    """
    if Node.depth >= depth and depth > 2:
        print('failed depth check...')
        return
    elif state.isWin():
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
        legal = state.getLegalPacmanActions()
        for action in legal:
            if action is not None:
                #print('action in else is {}'.format(action))
                if (counter > 5000):
                    v=list(knownStates.values())
                    k=list(knownStates.keys())
                    #print ('k[v.index(max(v))] returns type {} and value {}'.format(type(k[v.index(max(v))]), k[v.index(max(v))]))
                    soFarBestState = k[v.index(max(v))]
                    #print('the best state so far var resolved as type: {} and value {}'.format(type(soFarBestState), soFarBestState))
                    soFarBestNode = nodes[soFarBestState]
                    #print('the best node so far var resolved as type: {} and value {}'.format(type(soFarBestNode), soFarBestNode))
                    moves = soFarBestNode.traceback()
                    moves.append(action)
                    print('trying to return moves in max succcesor test...with high score of {}'.format(scoreEvaluation(soFarBestState)))
                    #print('moves is of type {} and value {}'.format(type(moves), moves))
                    return (moves)
                if state.generateSuccessor(0, action) is not None:
                    counter += 1
                    print('Next call to successor is number {}.'.format(counter))
                    successorState = state.generateSuccessor(0, action)
                    if successorState not in knownStates:
                        c = node(successorState, action, Node, depth)
                        if successorState.isWin():
                            Node.prevAction = lastAction
                            Node.successState = True
                            nodes[state] = Node
                            knownStates[state] = scoreEvaluation(state)
                            moves = Node.traceback()
                            moves.append(action)
                            print('trying to return moves in winning state...')
                            return (moves) 
                        elif successorState.isLose():
                            print('Lost in successor state is lose')
                            knownStates[state] = scoreEvaluation(state)
                        else:
                            knownStates[successorState] = scoreEvaluation(successorState)
                            #print('knownStates is size {}'.format(len(knownStates)))
                            nodes[state] = Node
                            nextDepth = depth + 1
                            BFS(successorState, c, action, nextDepth)
        depth += 1
        print('Current depth is {}.'.format(depth))


class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        global root, nodes, trackState
        root = node(state, None, None, 0)
        nodes[state] = root
        knownStates[state] = scoreEvaluation(state)
        trackState = type(state)
        return

    # GetAction Function: Called with every frame
    def getAction(self, state):
        global nodes, knownStates, root, moves, trackState
        #is the root.state eq to the state here?
        if trackState is not type(state):
            print('state is now of type {} and value {}.'.format(type(state), state))
        #here if the state is already found, it's because it has been seen before and shouldn't be expanded
        #so what should the action be? reversal? nothing?
        #random for now
        #print ('the value of this "if nodes[state]" is {} and type {}.'.format(((nodes[state])), type((nodes[state]))))
        if nodes[state]:
            terminalState = BFS(state, Node = nodes[state])
            direction = moves[-1]
            if direction is 'North':
                return Directions.NORTH
            if direction is 'South':
                return Directions.SOUTH
            if direction is 'East':
                return Directions.EAST
            if direction is 'West':
                return Directions.WEST
        else:
            terminalState = BFS(state)
            direction = moves[-1]
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

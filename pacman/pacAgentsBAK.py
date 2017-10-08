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
    def __init__ (self, state, prevAction, parent, depth):
        self.state = state
        self.children = []
        self.visited = False
        self.parent = parent
        self.prevAction = prevAction
        self.depth = depth
        self.successState = state.isWin()
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
        nextNode = self.parent
        sequence.append(self.prevAction)
        while (nextNode.parent is not None):
            nextNode = nextNode.parent
            nextNode = self.parent
            sequence.append(self.prevAction)
        return (sequence)


def BFS(state):
    global controlCounter, knownStates
    controlCounter += 1
    """
    #print('control counter is now {}'.format(controlCounter))
    if controlCounter > 500:
        print ('controlcounter hit...knownStates is now size {}'.format(len(knownStates)))
        return
    """
    if state.isWin():
        return (state) 
    elif state.isLose():
        return (state)
    else:
        children = []
        legal = state.getLegalPacmanActions()
        for action in legal:
            if action is not None:
                successorState = state.generateSuccessor(0, action)
                if successorState not in knownStates:
                        if successorState.isWin():
                            return (successorState) 
                        elif successorState.isLose():
                            return (successorState)
                        else:
                            knownStates[successorState] = action
                            #print('knownStates is size {}'.format(len(knownStates)))
                            BFS(successorState)


class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        global knownStates, controlCounter
        knownStates = {}
        controlCounter = 0  
        return

    # GetAction Function: Called with every frame
    def getAction(self, state):
        #here if the state is already found, it's because it has been seen before and shouldn't be expanded
        #so what should the action be? reversal? nothing?
        #random for now
        if state in knownStates:
            actions = state.getLegalPacmanActions()
            knownStates[state] = actions[random.randint(0,len(actions)-1)]
            return (knownStates[state])

        else:
            #print('knownStates is of type {} and has {}'.format(type(knownStates), knownStates))
            terminalState = BFS(state)
            print('reached terminal state. of type {} and value {}'.format(type(terminalState), terminalState))
            #print('trying to search for high score states...from {} known states.'.format(len(knownStates)))
            #print('max score so far is {}'.format(max(list(knownStates.viewvalues()))))
            print('Number of knownStates after running BFS with recursion control is {} and the keys are: \n{}'.format(len(knownStates), list(knownStates.viewkeys())))
            return Directions.STOP
      
        

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

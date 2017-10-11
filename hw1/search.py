# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def generalSearch(problem, frontier, heuristic=None, cal_cost=False):
    if heuristic == None:
        def heuristic(state, problem):
            return 0

    in_frontier = dict()
    visit = dict()

    start_states = (problem.getStartState(), 0)
    frontier.push(start_states)
    in_frontier[problem.getStartState()] = 0
    visit[problem.getStartState()] = ('dummy_state', 'dummy_action')

    while not frontier.isEmpty():
        now_state, now_cost = frontier.pop()
        now_cost -= heuristic(now_state, problem)
        del in_frontier[now_state]

        if problem.isGoalState(now_state):
            actions = []
            while now_state != problem.getStartState():
                now_state, prv_action = visit[now_state]
                actions.append(prv_action)
            return actions[::-1]

        successors = problem.getSuccessors(now_state)
        for successor in successors:
            nextState = successor[0]
            prv_action = successor[1]
            one_step_cost = successor[2]
            total_cost = now_cost + one_step_cost + heuristic(nextState, problem)
            if nextState in in_frontier and cal_cost:
                frontier.update((nextState, in_frontier[nextState]), total_cost)
            if nextState in visit or nextState in in_frontier:
                continue
            visit[nextState] = (now_state, prv_action)
            now = (nextState, total_cost)
            frontier.push(now)
            in_frontier[nextState] = total_cost
    raise ValueError("Solution Not Found")

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    return generalSearch(problem, stack)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    return generalSearch(problem, queue)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    def priorityFunction(item):
        # item: (nextState, cost)
        return item[1]
    priorty_queue_with_function = util.PriorityQueueWithFunction(priorityFunction)
    return generalSearch(problem, priorty_queue_with_function, None, True)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    def priorityFunction(item):
        # item: (nextState, cost)
        return item[1]
    priorty_queue_with_function = util.PriorityQueueWithFunction(priorityFunction)
    return generalSearch(problem, priorty_queue_with_function, heuristic, True)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

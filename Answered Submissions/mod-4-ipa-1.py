'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT from_member
    #INPUT to_member
    #INPUT social_graph
    
    from_follow_list = social_graph[from_member]["following"]
    to_follow_list = social_graph[to_member]["following"]

    #"friends" if fromMember and toMember follow each other,
    if to_member in from_follow_list and from_member in to_follow_list:
        return "friends"

    #"follower" if fromMember follows toMember,

    elif to_member in from_follow_list:
        return "follower"

    #"followed by" if fromMember is followed by toMember,

    elif from_member in to_follow_list:
        return "followed by"

    #"no relationship" if neither fromMember nor toMember follow each other.

    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT board
    
    #GET the unique symbol of the board
    unique_characters = list(set(i for j in board for i in j))
    
    #REMOVE " " str
    unique_characters = list(filter(None, unique_characters))

    #GET win conditions for each symbol
    one = unique_characters[0]
    one_win = [one]*len(board)
    
    two = unique_characters[1]
    two_win = [two]*len(board)

    #GET list of HORIZONTALS
    horizon = []
    for i in board:
        horizon += [i]

    #GET list of VERTICALS
    vertboard = [x for x in zip(*board)]
    vert = []
    for i in vertboard:
        i = list(i)
        vert += [i]

    #GET list of DIAGONAL TOP(L) to DOWN(R)
    dtldr = [[board[i][i] for i,v in enumerate(board)]]

    #GET list of DIAGONAL TOP(R) to DOWN(L)
    dtrdl = [[board[i][len(board)-1-i] for i,v in enumerate(board)]]

    #COMBINE all for comparison
    compare = horizon + vert + dtldr + dtrdl
    
    #CONDITION if win condition is present in list of all
    if one_win in compare:
        return str(one)
    elif two_win in compare:
        return str(two)
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #first_stop = INPUT
    #second_stop = INPUT
    #route_map = INPUT

    total_time = 0
    stoplist = [] 
    stop_timelist = []
    revisedlist = []
    
    #CREATE lists of all entry stops and all corresponding time
    for routes in route_map.keys():
        enter_point = routes[0]
        stoplist += [enter_point]

        stop_timelist += [route_map[routes]["travel_time_mins"]]
    
    #CREATE new dictionary routes based on entry points
    new_route_dict = {}
    for stops in stoplist:
        new_time_travel = {}
        new_time_travel["travel_time_mins"] = stop_timelist[stoplist.index(stops)]
        new_route_dict[stops] = new_time_travel

    start_index = stoplist.index(first_stop)
    
    #CREATE revised list of routes with the first stop being the first entry spot
    for stops in stoplist:
        while len(revisedlist) < len(stoplist):
            revisedlist += [stoplist[start_index % len(stoplist)]]
            start_index += 1

    #LOOP add travel time of each entry point to total time until it reaches the last entry
    for stops in revisedlist:
        if revisedlist.index(stops) < revisedlist.index(second_stop):
            total_time += new_route_dict[stops]['travel_time_mins']

        else:
            total_time = total_time

    return total_time
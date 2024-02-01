def perceive(current_state):
    return current_state

def decide_action(perceived_state):
    cleanliness = perceived_state.get('cleanliness', False)
    obstacle_present = perceived_state.get('obstacle', False)
    room_occupied = perceived_state.get('occupied', False)

    if cleanliness:
        return 'clean_room'
    elif obstacle_present:
        return 'avoid_obstacle'
    elif room_occupied:
        return 'wait'
    else:
        return 'move_rooms'

def perform_action(decided_action):
    if decided_action == 'clean_room':
        return 'Cleaning rooms'
    elif decided_action == 'avoid_obstacle':
        return 'Avoiding obstacle'
    elif decided_action == 'wait':
        return 'Waiting for the room to clear'
    elif decided_action == 'move_rooms':
        return 'Moving to the next room'
    else:
        return 'Unknown'

state = {
    'cleanliness': input("Is the room clean? (True/False): ") == 'True',
    'obstacle': input("Is there an obstacle? (True/False): ") == 'True',
    'occupied': input("Is the room occupied? (True/False): ") == 'True'
}

perceived_state = perceive(state)

actions = ['clean_room', 'avoid_obstacle', 'wait']

for action in actions:
    action_result = perform_action(action)
    print(action_result)




       
       
       

    


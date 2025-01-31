import heapq

from puzzle8.board import Board

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dijkstra(etat_initial):
    """Implémente l'algorithme de Dijkstra pour résoudre le puzzle 8"""
    
    pq = [(0, etat_initial)]  
    visites = set()
    visites.add(etat_initial)
    etat_precedent = {etat_initial: None}
# def is_valid_move(pos, move):
#     """Checks whether a move is valid."""
#     row, col = divmod(pos, 3)
#     new_row, new_col = row + move[0], col + move[1]
#     return (0 <= new_row < 3 and 0 <= new_col < 3)


# def swap(state, pos1, pos2):
#     """Swaps to adjacent numbers."""
#     state_list = list(state)
#     state_list[pos1], state_list[pos2] = state_list[pos2], state_list[pos1]
#     return ''.join(state_list)


# def dijkstra(initial_state, final_state):
#     """Implements Dijkstra's algorithm to solve the puzzle."""
#     pq = [(0, initial_state)]  # (distance, state)
#     visited = set()
#     visited.add(initial_state)
#     previous_state = {initial_state: None}

    while pq:
        current_cost, current_state = heapq.heappop(pq)

        if current_state == final_state:
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = previous_state[current_state]
            return path[::-1] 
        
        empty_position = current_state.index('0')
        
        for move in moves:
            if is_valid_move(empty_position, move):
                new_row, new_col = divmod(empty_position, 3)
                new_row, new_col = new_row + move[0], new_col + move[1]
                new_position = new_row * 3 + new_col
                new_state = swap(current_state, empty_position, new_position)
                
                if new_state not in visited:
                    visited.add(new_state)
                    heapq.heappush(pq, (current_cost + 1, new_state))
                    previous_state[new_state] = current_state
        
    return None
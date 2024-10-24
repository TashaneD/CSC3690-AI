# Minimax algorithm
def minimax(node, depth, maximizingPlayer, scores, height):
    # If depth is the height of the tree, return the score of the node
    if depth == height:
        return scores[node]
    # if this the maximising player, choose max child node using the max function
    if maximizingPlayer:
        best = float('-inf')  # Initialize to the lowest possible value

        # For each child in the binary, select the max value using max function
        for i in range(2):
            val = minimax(node * 2 + i, depth + 1, False, scores, height)
            best = max(best, val)
        return best
    # If it is the minimizing player, select the minimum child node using the min ufnction
    else:
        best = float('inf')  # Initialize to the highest possible value

        # Recur for all child nodes
        for i in range(2):
            val = minimax(node * 2 + i, depth + 1, True, scores, height)
            best = min(best, val)
        return best

def calculate_height(n):
    height = 0
    while n > 1:
        n //= 2  # Keep dividing the length by 2
        height += 1
    return height

if __name__ == "__main__":
    # Scores are the leaf nodes
    scores = [3, 5, 17, 8, -2, 5, -1, 7]

    height = calculate_height(len(scores))

    optimal_value = minimax(0, 0, True, scores, height)
    print("The optimal value is:", optimal_value)


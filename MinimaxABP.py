# Minimax algorithm with alpha-beta pruning
def minimax(node, depth, maximizingPlayer, scores, height, alpha, beta):
    # If depth is the height of the tree, return the score of the node
    if depth == height:
        return scores[node]

    # Maximizing player
    if maximizingPlayer:
        best = float('-inf')

        # Check both child nodes
        for i in range(2):
            val = minimax(node * 2 + i, depth + 1, False, scores, height, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)  # Update alpha

            # Prune if beta is less than or equal to alpha
            if beta <= alpha:
                break
        return best

    # Minimizing player
    else:
        best = float('inf')

        # Check both child nodes
        for i in range(2):
            val = minimax(node * 2 + i, depth + 1, True, scores, height, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)  # Update beta

            # Prune if beta is less than or equal to alpha
            if beta <= alpha:
                break
        return best


# To calculate tree height based on number of leaf nodes
def calculate_height(n):
    height = 0
    while n > 1:
        n //= 2
        height += 1
    return height


if __name__ == "__main__":
    # Scores are terminal nodes
    scores = [3, 5, 17, 8, -2, 5, -1, 7]

    height = calculate_height(len(scores))

    # Initialize alpha and beta
    optimal_value = minimax(0, 0, True, scores, height, float('-inf'), float('inf'))
    print("The optimal value is:", optimal_value)

def minimax(depth, nodeIndex, maximizingPlayer, values):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values)
            best = max(best, val)

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values)
            best = min(best, val)

        return best


def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        for i in range(2):
            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Input leaf node values
print("Enter 8 leaf node values separated by spaces:")
values = list(map(int, input().split()))

if len(values) != 8:
    print("Please enter exactly 8 values.")
else:
    print("\nChoose Algorithm")
    print("1. Minimax")
    print("2. Alpha-Beta Pruning")

    choice = int(input("Enter choice (1 or 2): "))

    if choice == 1:
        result = minimax(0, 0, True, values)
        print("Optimal value using Minimax:", result)

    elif choice == 2:
        result = alphabeta(
            0,
            0,
            True,
            values,
            float('-inf'),
            float('inf')
        )
        print("Optimal value using Alpha-Beta Pruning:", result)

    else:
        print("Invalid Choice")


code = """
Enter 8 leaf node values separated by spaces:
3 5 2 9 12 5 23 23

Choose Algorithm
1. Minimax
2. Alpha-Beta Pruning
Enter choice (1 or 2): 1

Optimal value using Minimax: 12

Or:

Enter choice (1 or 2): 2

Optimal value using Alpha-Beta Pruning: 12
"""

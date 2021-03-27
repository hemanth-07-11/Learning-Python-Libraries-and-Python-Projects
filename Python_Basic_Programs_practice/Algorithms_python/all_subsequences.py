def generate_all_subsequences(sequence):
    create_state_space_tree(sequence, [], 0)


def create_state_space_tree(sequence, current_subsequence, index):
    if index == len(sequence):
        print(current_subsequence)
        return

    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.pop()

print("Enter the elements")
sequence = list(map(int, input().split()))

generate_all_subsequences(sequence)


def generate_all_permutations(sequence):
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])

def create_state_space_tree(sequence, current_sequence, index, index_used):

    if index == len(sequence):
        print(current_sequence)
        return

    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            create_state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = False


print("Enter the elements")
sequence = list(map(int, input().split()))
generate_all_permutations(sequence)


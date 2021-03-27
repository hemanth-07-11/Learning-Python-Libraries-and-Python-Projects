def generate_all_combinations(n: int, k: int) -> [[int]]:
    result = []
    create_all_state(1, n, k, [], result)
    return result

def create_all_state(increment, total_number, level, current_list, total_list):
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()

def print_all_state(total_list):
    for i in total_list:
        print(*i)

if __name__ == "__main__":
    n = 4
    k = 2
    total_list = generate_all_combinations(n, k)
    print_all_state(total_list)

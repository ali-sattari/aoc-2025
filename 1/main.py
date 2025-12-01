from pprint import pprint

def solution_p1(input: list[str]) -> int:
    position = 50
    zeros = 0
    for index, move in enumerate(input):
        position, _ = move_in_dir(position, move[0], int(move[1:]))
        if position == 0:
            zeros += 1

    return zeros

def solution_p2(input: list[str]) -> int:
    position = 50
    zeros = 0
    for index, move in enumerate(input):
        position, move_zeros = move_in_dir(position, move[0], int(move[1:]))
        zeros += move_zeros

    return zeros

def move_in_dir(position: int, dir: str, steps: int) -> tuple[int, int]:
    # steps can be more than 100, we need to adjust for this
    initial_zeros = steps // 100
    steps %= 100
    zeros = 0

    if dir == 'L':
        position -= steps
    elif dir == 'R':
        position += steps

    if position < 0:
        position += 100
        zeros += 1
    elif position > 99:
        position -= 100
        zeros += 1

    return position, zeros+initial_zeros

def input_to_list(input: str) -> list[str]:
    with open(input, 'r') as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    p1_sample_answer = 3
    p1_sample_result = solution_p1(input_to_list('./p1_sample.input'))
    print("Part 1 sample:", p1_sample_result == p1_sample_answer, p1_sample_result)
    print("Part 1 main:", solution_p1(input_to_list('./p1_main.input')))

    p2_sample_answer = 6
    p2_sample_result = solution_p2(input_to_list('./p1_sample.input'))
    print("Part 2 sample:", p2_sample_result == p2_sample_answer, p2_sample_result)
    # print("Part 2 main:", solution_p2(input_to_list('./p1_main.input')))

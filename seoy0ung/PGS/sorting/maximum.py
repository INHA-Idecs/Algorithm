def solution(numbers):
    answer = ''
    num_str = list(map(str, numbers))
    num_str.sort(key=lambda num: num * 3, reverse=True)

    return str(int("".join(num_str)))

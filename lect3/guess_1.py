# def my_personal_sum(
#         x: int | float, 
#         y: int
#         ) -> int:
#     answer = x + y
#     return answer

def my_personal_sum(*args, **kwargs) -> int | float:
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    answer = 0
    for i in args:
        answer += 1
    return answer

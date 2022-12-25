# This is a sample Python script.
import inspect


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def pprint(ss):
    for s in ss:
        print(s)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from dataclasses import dataclass, astuple, asdict

@dataclass(frozen=True, order=True)
class Comments:
    id: int
    text: str

    def __post_init__(self) ->None:
        if not 0 < self.id <= 10:
            raise ValueError("Id mist be between 1 to 11")


def tom(a: 'Range of numbers' = 10, b: 'second param' = 1) -> 'highest value or None':
    """# line 1 sample"""
    print("parameters {0} and {1}".format(a, b))
    for x in range(1, a):
        print(x)
    return str(x+1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # con = Comments(10, "this is tom")
    # print(con)
    # print(astuple(con))
    # print(asdict(con))
    # pprint(inspect.getmembers(Comments, inspect.isfunction))
    a = tom(300)
    print("a = {0}".format(a))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

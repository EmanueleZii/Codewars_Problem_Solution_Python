'''
<summary>
    Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

    Examples:

    Inputs: "abc", "bc"
    Output: true

    Inputs: "abc", "d"
    Output: false
    Level : 7kyu
</summary>
'''

def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False

def main():
    text = "hello world"
    ending = "world"
    print(solution(text, ending))

if __name__ == '__main__':
    main()

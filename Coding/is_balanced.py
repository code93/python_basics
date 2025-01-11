def is_balanced(parantheses):
    stack = []
    opening = set({'(','{','['})
    closing = set({')','}',']'})
    pairs = dict({
        ')':'(',
        ']':'[',
        '}':'{'

    })

    for c in parantheses:
        if c in opening:
            stack.append(c)
        elif c in closing:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
import textwrap

def wrap(string, max_width):
    count = 0
    ans = []
    
    while count < len(string): 
        ans.append((string[count : count + max_width]))
        count += max_width
        
    return "\n".join(str(s) for s in ans)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

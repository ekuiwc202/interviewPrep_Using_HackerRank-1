if __name__ == '__main__':
    N = int(input())
    cmd = []
    ans = []
    for i in range(N):
        
        cmd.append(list(input().split()))
        
        if cmd[i][0] == "insert":
            ans.insert(int(cmd[i][1]),int(cmd[i][2]))
            
        elif cmd[i][0] == "remove":
            ans.remove(int(cmd[i][1]))
            
        elif cmd[i][0] == "append":
            ans.append(int(cmd[i][1]))
            
        elif cmd[i][0] == "sort":
            ans.sort()
            
        elif cmd[i][0] == "pop":
            ans.pop()
            
        elif cmd[i][0] == "reverse":
            ans.reverse()
            
        elif cmd[i][0] == "print":
            print(ans)
            
            

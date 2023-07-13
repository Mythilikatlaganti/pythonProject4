N = int(input())
m=[]
for i in range(0,N):
    cmd=input().split()
    if cmd[0]=="insert":
        m.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="remove":
        m.remove(int(cmd[1]))
    elif cmd[0]=="append":
        m.append(int(cmd[1]))
    elif cmd[0]=="pop":
        m.pop()
    elif cmd[0]=="print":
        print(m)
    elif cmd[0]=="sort":
        m.sort()
    else:
        m.reverse()
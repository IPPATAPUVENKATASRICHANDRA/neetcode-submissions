class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if '0000' in deadends:
            return -1

        def children(lock):
            res=[]
            for i in range(4):
                digit=str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                digit=str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+digit+lock[i+1:])                

            return res
        
        q=deque()
        # [lock,turns]
        q.append(['0000',0])
        visit=set(deadends)


        while q:
            l,t=q.popleft()
            if l==target:
                return t
            for child in children(l):
                if child not in visit:
                    visit.add(child)
                    q.append([child,t+1])
        
        return -1
            
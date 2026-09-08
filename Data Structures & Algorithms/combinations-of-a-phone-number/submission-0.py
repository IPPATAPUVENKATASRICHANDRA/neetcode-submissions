class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits)<=0:
            return []
        glb=[]
        d_w={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }


        def bt_lc(comb,i):

            if len(comb)>len(digits):
                return
            if len(comb)==len(digits):
                glb.append(''.join(comb))
                return

            for j in d_w[digits[i]]:
                comb.append(j)
                bt_lc(comb,i+1)
                comb.pop()

        bt_lc([],0)

        return glb
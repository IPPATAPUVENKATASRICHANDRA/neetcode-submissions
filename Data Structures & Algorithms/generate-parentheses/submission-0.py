class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        glb=[]
        def bt_gpar(s,pa_o,pa_c):

            if pa_o>n or pa_c>n:
                return
            
            if pa_c>pa_o:
                return
            
            if pa_o==n and pa_c==n:
                glb.append(s)
                return

            bt_gpar(s+'(',pa_o+1,pa_c) 
            bt_gpar(s+')',pa_o,pa_c+1)

        s=''
        bt_gpar(s,0,0)

        return glb

            
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        
        s_list = list(s)
        T_num = len(s_list)//(2*numRows-2)
        T_element_num = 2*numRows-2
        Res_num = len(s_list) - T_num* (2*numRows-2)

        new_list = []
        for i in range(numRows):
            for t in range(T_num):
                new_list.append(s_list[t*T_element_num+i])
                if i>0 and numRows-1>i:
                    new_list.append(s_list[(t+1)*T_element_num - i])

            if (T_num*T_element_num + i) < len(s_list):
                new_list.append(s_list[T_num*T_element_num + i])
            if Res_num>numRows:
                if i==numRows-1:
                    continue
                if ((T_num+1)*T_element_num -i) < len(s_list):
                    new_list.append(s_list[(T_num+1)*T_element_num - i])

        return "".join(new_list) 

s = "ABCDE"
numRows = 4
so = Solution()

print(so.convert(s,numRows))
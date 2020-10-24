class Reverse:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        x_list = list(x_str)

        x_list.reverse()

        while x_list[0]==0:
            x_list.pop(0)
        if x_list[-1] == "-":
            x_list.insert(0,"-")
            x_list = x_list[:-1]
        x_int = "".join(x_list)
        x_int = int(x_int)
        if x_int>(-2**31) and x_int<(2**31):
            return x_int
        else:
            return 0


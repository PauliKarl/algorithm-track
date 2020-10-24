class Solution:
    """
    请实现 copyRandomList 函数，复制一个复杂链表。
    在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
    还有一个 random 指针指向链表中的任意节点或者 null。
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        深度优先搜索+记录已经访问元素
        """
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        visited = {}
        return dfs(head)

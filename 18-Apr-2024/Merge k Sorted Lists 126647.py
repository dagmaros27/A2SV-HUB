# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        heap = []
        ans = []
        heads = []
        ll = []
        
        for head in lists:
            if head:
                heap.append(head.val)
                heads.append(head.val)
                ll.append(head)

        heapify(heap)

        while heap:
            mnm = heappop(heap)

            mnm_idx = heads.index(mnm)

            ans.append(ll[mnm_idx])

            if ll[mnm_idx].next:
                ll[mnm_idx] = ll[mnm_idx].next
                heads[mnm_idx] = ll[mnm_idx].val
                heappush(heap, heads[mnm_idx])
            else:
                del heads[mnm_idx]
                del ll[mnm_idx]

        for i in range(len(ans) - 1):
            ans[i].next = ans[i + 1]

        return ans[0] if ans else None
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* prev=NULL;
        ListNode* s=head;
        ListNode* f=head;
        while(f!=NULL && f->next!=NULL){
            prev=s;
            s=s->next;
            f=f->next->next;
        }
        if(s==head)
            return head->next;
        prev->next=s->next;
        return head;
    }
};

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
    int pairSum(ListNode* head) {
        ListNode* p1=head;
        ListNode* p2=head;
        while(p2!=NULL){
            p1=p1->next;
            p2=p2->next->next;
        }
        ListNode* prev=NULL;
        ListNode* next=NULL;
        while(p1!=NULL){
            next=p1->next;
            p1->next=prev;
            prev=p1;
            p1=next;
        }
        int m=0;
        while(prev!=NULL){
            m=max(m,head->val+prev->val);
            head=head->next;
            prev=prev->next;
        }
        return m;
    }
};

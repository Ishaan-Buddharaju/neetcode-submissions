class MinStack {
    // worst case
private: 
    stack<int> stk;
public:
    MinStack() {

    }
    
    void push(int val) {
        stk.push(val);
    }
    
    void pop() {
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        int minimum = stk.top();
        stack<int> temp;
        while (stk.size()) {
            minimum = min(minimum, stk.top());
            temp.push(stk.top());
            stk.pop();
        }

        while(temp.size()) {
            stk.push(temp.top());
            temp.pop();
        }
        return minimum;
    }
};

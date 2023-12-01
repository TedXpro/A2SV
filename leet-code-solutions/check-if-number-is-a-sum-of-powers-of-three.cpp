class Solution {
public:
    bool checkPowersOfThree(int n) {
        for(int index = 15; index >= 0; index--){
            int num = pow(3, index);
            if(num <= n)
                n -= num;
            if(n == 0) return true;
        }
        return false;
    }
};
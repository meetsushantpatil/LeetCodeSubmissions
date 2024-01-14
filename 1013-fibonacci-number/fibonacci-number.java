class Solution {
    public int fib(int n) {

        int result = 0;
        int lastResult = 1;
        int secondLastResult = 0;
        
        if(n == 0 || n == 1 ){
            return n;
        }

        for (int i=2;i<=n;i++){
                result = lastResult + secondLastResult;
                secondLastResult = lastResult;
                lastResult = result;
            }

        return result;

        
    }
}
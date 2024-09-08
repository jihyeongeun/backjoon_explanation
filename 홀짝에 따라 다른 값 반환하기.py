class Solution {
    public int solution(int n) {
        int answer = 0;
        if(n%2 == 1){
            //이하 홀수들의 합
            for(int i = 0; i <= n; i ++){
                if(i%2 == 1){
                    answer += i;
                }
            }
        } else {
            //이하 짝수들의 제곱의 합
             for(int i = 0; i <= n; i ++){
                 if(i%2 == 0){
                     answer += i*i;
                 }
             }
        }
        return answer;
    }
}
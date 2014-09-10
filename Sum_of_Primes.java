public class Main {
    public static void main(String args[]){
        int 
        nums = 2,cnt = 0,sum = 0;
        
        while(cnt < 1000){if(PR(nums)){sum += nums;cnt++;}nums++;}
        System.out.println(sum);}
    private static boolean PR(int nums){
        for(int i=2;i<=nums/2;i++){
            if(nums%i==0){return false;}}
        return true;}}
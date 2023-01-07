
bool isPalindrome(long long x){
    long long res=0,num=x;
    if(x<0){
        return false;
    }
        while(x!=0)
        {
             res=res*10+x%10;
             x=x/10;
        }
    return num==res;
}

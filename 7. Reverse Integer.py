int reverse(long long x){
    long long res=0,num=x;
    while(x!=0){
        if(x%10==0){
            num=x/10;
            res=res*10+x%10;
            x=x/10;
        }
        else{
             res=res*10+x%10;
             x=x/10;
        }
    } 
    if(res>2147483647 || res<-2147483648){
        return 0;
    }
    else{
    return res;
    }
}

double myPow(double x, int n){
    if(n==1){
        return x;
    }
    if(n==0){
        return 1;
    }
    if(n<0){
        return myPow(1/x,-n);
    }
    double r=myPow(x,n/2);
    if(n&1){
        return r*r*x;
    }
    return r*r;

}

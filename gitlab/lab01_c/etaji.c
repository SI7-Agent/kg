#include <stdio.h>
#include <math.h>
int pod(int nom){
    float p;
    int a;
    p = nom/27;
    a = nom % 27;
    if (a > 0){
        p = p+1;
    }
    return(p);
};
int etag(int nom){
    int a,et;
    et = (a / 3)+1;
    a = nom % 27;

    if (a % 3 == 0 && et<9){
        et=et-1;
    }
    if (nom % 27 == 0){
        et=9;
    }
    return(et);
};
int main()
{
    int nom;
    int d,t;
    scanf("%d",&nom);
    if (nom < 0){
        printf("Nomer < 0");
    }
    else
    {
    d = pod(nom);
    t = etag(nom);
    printf("%d,%d",d,t);
    }
}


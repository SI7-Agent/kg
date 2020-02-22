#include <stdio.h>
#include <math.h>

float dlin(int x1,int y1,int x2,int y2){
    return(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)));
};
int main()
{
    int x1,y1,x2,y2,x3,y3;
    scanf("%d %d",&x1,&y1);
    scanf("%d %d",&x2,&y2);
    scanf("%d %d",&x3,&y3);
    float a = dlin(x1,y1,x2,y2);
    float b = dlin(x2,y2,x3,y3);
    float c = dlin(x1,y1,x3,y3);
    if (a<(b+c)||b<(a+c)||c<(a+b))
    {
     printf("Treugolnic sushestv");
}
    else
    {
    printf("Treugolnic ne sushestv");
    }
}

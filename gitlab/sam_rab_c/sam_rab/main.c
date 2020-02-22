#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

int main()
{

    FILE *file;
    file = fopen("test.txt", "w");
    printf("Input your IP with number of 1 in submask\n");
    char str[20];
    gets(str);
    fputs(str, file);
    fclose(file);
    file = fopen("test.txt", "r");
    int m[5];
    char p;
    fscanf(file, "%d", &m[0]);
    if ((m[0] > 255)||(m[0] < 0))
    {
        fclose(file);
        printf("\nYour file has invalid data");
        return -1;
    }
    int i = 1;
    while ((p = getc(file)) != EOF)
    {
        if (fscanf(file, "%d", &m[i]) == 1)
        {
            if (((m[i] > 255)||(m[i] < 0))||(m[4] > 32))
            {
                fclose(file);
                printf("\nYour file has invalid data");
                return -1;
            }
            i++;
        }
        else
        {
            fclose(file);
            printf("\nYour file has invalid data");
            return -1;
        }
    }
    //------------

    int mask1[8];
    int mask2[8];
    int mask3[8];
    int mask4[8];

    int k = 0;
    while (k < 8)
    {
        if (m[4] > 0)
        {
            mask1[k] = 1;
            m[4]--;
        }
        else
        {
            mask1[k] = 0;
        }
        k++;
    }
    k = 0;
    while (k < 8)
    {
        if (m[4] > 0)
        {
            mask2[k] = 1;
            m[4]--;
        }
        else
        {
            mask2[k] = 0;
        }
        k++;
    }
    k = 0;
    while (k < 8)
    {
        if (m[4] > 0)
        {
            mask3[k] = 1;
            m[4]--;
        }
        else
        {
            mask3[k] = 0;
        }
        k++;
    }
    k = 0;
    while (k < 8)
    {
        if (m[4] > 0)
        {
            mask4[k] = 1;
            m[4]--;
        }
        else
        {
            mask4[k] = 0;
        }
        k++;
    }
    //__________________________
    int mask11 = mask1[0]*128 + 64*mask1[1] + mask1[2]*32 + 16*mask1[3] + mask1[4]*8 + 4*mask1[5] + mask1[6]*2 + mask1[7];
    int mask21 = mask2[0]*128 + 64*mask2[1] + mask2[2]*32 + 16*mask2[3] + mask2[4]*8 + 4*mask2[5] + mask2[6]*2 + mask2[7];
    int mask31 = mask3[0]*128 + 64*mask3[1] + mask3[2]*32 + 16*mask3[3] + mask3[4]*8 + 4*mask3[5] + mask3[6]*2 + mask3[7];
    int mask41 = mask4[0]*128 + 64*mask4[1] + mask4[2]*32 + 16*mask4[3] + mask4[4]*8 + 4*mask4[5] + mask4[6]*2 + mask4[7];

    int ch1 = mask11 & m[0];
    int ch2 = mask21 & m[1];
    int ch3 = mask31 & m[2];
    int ch4 = mask41 & m[3];

    printf("\nYour mask in dec:");
    printf("\n%d", ch1);
    printf(".%d", ch2);
    printf(".%d", ch3);
    printf(".%d", ch4);

    getch();
    fclose(file);
}

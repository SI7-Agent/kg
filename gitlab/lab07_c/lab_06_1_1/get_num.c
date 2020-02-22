int get_num(int *p, int k, int i)
{
    int x, y;
    int chislo = 0;
    int b = 0;
    for (b; b < k; b++)
    {
        int schit = 0;
        int b1 = 0;
        for (b1; b1 < i; b1++)
        {
            if (*(p+b1+2) < 0)
            {
                if (schit == b)
                {
                    x = *(p+b1+2);
                    break;
                }
                schit++;
            }
        }
        schit = 0;
        b1 = 0;
        for (b1; b1 < i; b1++)
        {
            if (*(p+i+1-b1) >= 0)
            {
                if (schit == b)
                {
                    y = *(p+i+1-b1);
                    break;
                }
                schit++;
            }
        }
        chislo += x*y;
    }
    return chislo;
}

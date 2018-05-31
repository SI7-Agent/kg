int get_k(int *p, int razmer)
{
    int k;
    int pl = 0;
    int min = 0;
    int i = 0;
    for (i; i < razmer; i++)
    {
        if (*(p+i+2)>= 0)
        {
            pl++;
        }
        else
        {
            min++;
        }
    }
    if (pl >= min)
        return min;
    else
        return pl;
}

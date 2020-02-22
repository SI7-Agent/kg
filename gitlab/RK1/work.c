int get_zero(int cols, float *array)
{
    int flag = -1;
    for (int i = 0; i<cols; i++)
        if (array[i] == 0)
        {
            flag = i;
            break;
        }

    return flag;
}

int get_negative(int cols, float *array)
{
    int flag = -1;
    for (int i = 0; i<cols; i++)
        if (array[i] < 0)
            flag = i;

    return flag;
}

void transmit(int rows, int cols, float **matrix)
{
    int flag_zero;
    int flag_negative;
    for (int i = 0; i< rows; i++)
    {
        flag_zero = get_zero(cols, matrix[i]);
        flag_negative = get_negative(cols, matrix[i]);
        if ((flag_zero != -1)&&(flag_negative != -1))
        {
            float tmp = matrix[i][flag_zero];
            matrix[i][flag_zero] = matrix[i][flag_negative];
            matrix[i][flag_negative] = tmp;
        }
    }
}

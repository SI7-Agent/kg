#include <stdio.h>
#include <stdlib.h>

/**
 –ó–∞–ø–æ–ª–Ω—è–µ—Ç –º–∞—Å—Å–∏–≤ array_orig –¥–∞–Ω–Ω—ã–º–∏ –∏–∑ —Ñ–∞–π–ª–∞ f.

 * @param f
 * @param array_orig
 */

void read_array(FILE *f, int *array_orig, int *array_orig_end)
{
    int num;
    fseek(f, 0, SEEK_SET);

    while(fscanf(f, "%d", &num) == 1)
    {
        *array_orig = num;
        if (array_orig != array_orig_end)
            array_orig++;
    }
}

/**
 –í—ã–≤–æ–¥–∏—Ç –Ω–∞ —ç–∫—Ä–∞–Ω –º–∞—Å—Å–∏–≤ array_start.

 * @param array_start
 * @param array_end
 */

void output(int *array_start, int *array_end)
{
    int size = array_end - array_start;
    for (int i = 0; i < size; i++)
    {
        printf("%d\n", *array_start);
        if (array_start != array_end)
            array_start++;
    }
}

/**
 –ó–∞–ø–∏—Å—ã–≤–∞–µ—Ç –º–∞—Å—Å–∏–≤ array_start –≤ —Ñ–∞–π–ª f.

 * @param f
 * @param array_start
 * @param array_end
 */

void record (FILE *f, int *array_start, int *array_end)
{
    int size = array_end - array_start;
    for (int i = 0; i < size; i++)
    {
        fprintf(f, "%d ", *array_start);
        if (array_start != array_end)
            array_start++;
    }
}

/**
 —ÓÁ‰‡ÂÚ ÔÛÒÚÓÈ ‚˚ıÓ‰ÌÓÈ Ù‡ÈÎ ‚ ÒÎÛ˜‡ˇı Ó¯Ë·ÓÍ, ÔÂ‰ÛÒÏÓÚÂÌÌ˚ı ‚ ÔÓ„‡ÏÏÂ.

 * @param argv
 */

void record_empty(char *argv[])
{
    FILE *f_out_error = fopen(argv[2], "w");
    fprintf(f_out_error, "%s", "");
    fclose(f_out_error);
}


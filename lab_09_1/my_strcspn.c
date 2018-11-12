/**
 Выполняет поиск первого вхождения
 в строку string любого из символов строки key, и
 возвращает количество символов до найденного первого вхождения.

 * @param string
 * @param key
 * @return
 */

int my_strcspn(char *string, char *key)
{
    int i = 0, j = 0;
    int bytes = -1;
    while (string[i])
    {
        j = 0;
        while (key[j])
        {
            if (string[i] == key[j])
            {

                if (bytes == -1)
                {
                    if ((!string[i]) && (!key[j]))
                        bytes = 0;
                    else
                        bytes = i;
                }
            }
            j++;
        }
        i++;
    }
    return bytes;
}


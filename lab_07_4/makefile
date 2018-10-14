%.o : %.c *.h
	gcc -std=c99 -Wall -Werror -pedantic -c $<

app.exe: main.o mysort.o key.o output.o record.o tick.o qsort.o read_array_test.o
	gcc -std=c99 -Wall -Werror -pedantic -o app.exe main.o mysort.o key.o output.o record.o tick.o qsort.o read_array_test.o
	
test.exe: test.o mysort.o key.o get_pos_test.o get_size_test.o read_array_test.o
	gcc -std=c99 -Wall -Werror -pedantic -o test.exe test.o mysort.o key.o get_pos_test.o get_size_test.o read_array_test.o
	
clean:
	del *.o *.exe
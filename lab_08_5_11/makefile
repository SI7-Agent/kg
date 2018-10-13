%.o : %.c *.h
	gcc -std=c99 -Wall -Werror -pedantic -c $<

app.exe: main.o output.o get_sum.o get_multy.o get_determ.o fill_matrix.o allocate_matrix.o record.o
	gcc -std=c99 -Wall -Werror -pedantic -o app.exe main.o output.o get_sum.o get_multy.o get_determ.o fill_matrix.o allocate_matrix.o record.o
	
test.exe: test.o
	gcc -std=c99 -Wall -Werror -pedantic -o test.exe test.o
	
clean:
	del *.o *.exe
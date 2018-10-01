%.o : %.c *.h
	gcc -c $<

app.exe: main.o mysort.o key.o output.o record.o tick.o
	gcc -o app.exe main.o mysort.o key.o output.o record.o tick.o
	
test.exe: test.o mysort.o key.o get_pos_test.o get_size_test.o read_array_test.o
	gcc -o test.exe test.o mysort.o key.o get_pos_test.o get_size_test.o read_array_test.o
	
clean:
	del *.o *.exe
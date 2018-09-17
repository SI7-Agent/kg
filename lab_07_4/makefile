main.o: main.c
	gcc -c main.c
	
test.o: test.c
	gcc -c test.c

key.o: key.c
	gcc -c key.c
	
mysort.o: mysort.c
	gcc -c mysort.c
	
key_test.o: key_test.c
	gcc -c key_test.c
	
mysort_test.o: mysort_test.c
	gcc -c mysort_test.c
	
get_pos_test.o: get_pos_test.c
	gcc -c get_pos_test.c
	
get_size_test.o: get_size_test.c
	gcc -c get_size_test.c
	
read_array_test.o: read_array_test.c
	gcc -c read_array_test.c

app.exe: main.o mysort.o key.o
	gcc -o app.exe main.o mysort.o key.o
	
test.exe: test.o mysort_test.o key_test.o get_pos_test.o get_size_test.o read_array_test.o
	gcc -o test.exe test.o mysort_test.o key_test.o get_pos_test.o get_size_test.o read_array_test.o
	
clean:
	del *.o *.exe
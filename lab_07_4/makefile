CC := gcc
CFLAGS := -std=c99 -Wall -Werror -pedantic
OBJ := mysort.o key.o tick.o read_array_test.o get_size_test.o

%.o : %.c *.h
	$(CC) $(CFLAGS) -c $<

app.exe: main.o $(OBJ)
	$(CC) $(CFLAGS) -o app.exe main.o $(OBJ)
	
test.exe: test.o $(OBJ)
	$(CC) $(CFLAGS) -o test.exe test.o $(OBJ)
	
clean:
	del *.o *.exe
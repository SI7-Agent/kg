CC := gcc
CFLAGS := -std=c99 -Wall -Werror -pedantic
OBJ := func.o work.o 

%.o : %.c *.h
	$(CC) $(CFLAGS) -c $<

app.exe: main.o $(OBJ)
	$(CC) $(CFLAGS) -o app.exe main.o $(OBJ)
	
test.exe: test.o tests.o $(OBJ)
	$(CC) $(CFLAGS) -o test.exe test.o tests.o $(OBJ)
	
clean:
	del *.o *.gch *.exe
CC := gcc
CFLAGS := -std=c99 -Wall -Werror -pedantic
OBJ := create_matr.o work.o

%.o : %.c *.h
	$(CC) $(CFLAGS) -c $<

app.exe: main.o $(OBJ)
	$(CC) $(CFLAGS) -o app.exe main.o $(OBJ)
	
clean:
	del *.o *.exe
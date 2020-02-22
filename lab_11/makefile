CC := gcc
CFLAGS := -std=c99 -Wall -Werror -pedantic
OBJ := func.o test.o

%.o : %.c *.h
	$(CC) $(CFLAGS) -c $<

app.exe: main.o $(OBJ)
	$(CC) $(CFLAGS) -o app.exe main.o $(OBJ) -lm
	
clean:
	del *.o *.gch *.exe

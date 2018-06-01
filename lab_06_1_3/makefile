main.o: main.c
	gcc -c main.c -o main.o

test.o: test.c
	gcc -c test.c -o test.o

main: main.c
	gcc -c main.c -o main.o
	gcc -o main.exe main.o

test: test.c
	gcc -c test.c -o test.o
	gcc -o test.exe test.o

app.exe: main.c
	gcc -c main.c -o main.o 
	gcc -o main.exe main.o 
	./main.exe

test.exe: test.c
	gcc -c test.c -o test.o
	gcc -o test.exe test.o
	./test.exe

clean:
	rm *.o *.exe
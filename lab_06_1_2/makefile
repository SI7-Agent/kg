main.o: main.c
	gcc -c main.c -o main.o

main: main.c
	gcc -c main.c -o main.o
	gcc -o main.exe main.o

app.exe: main.c
	gcc -c main.c -o main.o 
	gcc -o main.exe main.o 
	./main.exe

clean:
	rm *.o *.exe
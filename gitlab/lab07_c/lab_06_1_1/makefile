func.o: get_num.c
	gcc -c get_num.c -o get_num.o

func.o: get_k.c
	gcc -c get_k.c -o get_k.o

main.o: main.c
	gcc -c main.c -o main.o

main: get_num.c get_k.c main.c
	gcc -c get_num.c -o get_num.o
	gcc -c get_k.c -o get_k.o
	gcc -c main.c -o main.o
	gcc -o main.exe get_num.o get_k.o main.o

app.exe: get_num.c get_k.c main.c
	gcc -c get_num.c -o get_num.o 
	gcc -c get_k.c -o get_k.o 
	gcc -c main.c -o main.o 
	gcc -o main.exe get_num.o get_k.o main.o 
	./main.exe 

clean:
	rm *.o *.exe
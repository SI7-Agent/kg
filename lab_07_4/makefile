%.o : %.c *.h
	gcc -c $<

app.exe: main.o mysort.o key.o
	gcc -o app.exe main.o mysort.o key.o
	
test.exe: main.o mysort.o key.o
	gcc -o test.exe main.o mysort.o key.o
	
clean:
	del *.o *.exe
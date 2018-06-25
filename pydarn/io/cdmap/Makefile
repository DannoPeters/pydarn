CC=gcc 
CCFLAGS=-Wall -pedantic -Wextra -fPIC -std=c99 
LDFLAGS=
INCLUDEDIRS=-I/usr/include/python3.4m/
SOURCES=$(wildcard *.c)
OBJECTS=$(SOURCES:.c=.o)
TARGET=dmap

all:$(TARGET)

$(TARGET):$(OBJECTS)
	$(CC) -o $@ $^ $(LDFLAGS)

%.o: %.c %.h
	$(CC) $(CCFLAGS) -c $< $(INCLUDEDIRS)

%.o: %.c
	$(CC) $(CCFLAGS) -c $< $(INCLUDEDIRS)

clean:
	rm -f *.o $(TARGET)

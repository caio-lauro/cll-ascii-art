CC = gcc
CFLAGS = -Wall -Werror -Wunused -g
LDFLAGS = -lm -g

SRCDIR = src
INCLUDEDIR = include
BUILDDIR = build

SRCFILES = $(wildcard $(SRCDIR)/*.c)
INCLUDEFILES = $(wildcard $(INCLUDEDIR)/%.h)
BUILDFILES = $(patsubst $(SRCDIR)/%.c, $(BUILDDIR)/%.o, $(SRCFILES))

all: mkbuilddir main

main: $(BUILDFILES)
	@ echo "Compiling build files into executable"
	$(CC) $(CFLAGS) $(BUILDFILES) -o $@ $(LDFLAGS)

mkbuilddir:
	mkdir -p $(BUILDDIR)

$(BUILDDIR)/main.o: $(SRCDIR)/main.c
	@ echo "Compiling $<"
	$(CC) $(CFLAGS) -c $< -o $@ $(LDFLAGS)

$(BUILDDIR)/%.o: $(SRCDIR)/%.c $(INCLUDEDIR)/%.h
	@ echo "Compiling $<"
	$(CC) $(CFLAGS) -c $< -o $@ $(LDFLAGS)

.SILENT: mkbuilddir

.PHONY: clean

clean:
	rm -rf $(BUILDDIR) main
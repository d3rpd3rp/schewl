#grabbed this from blog.markloiseau.com
obj-m := hookme_exp.o
KDIR := /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)
CC := gcc
ccflags-y += -g -DDEBUG


all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

debug:
	$(MAKE) -C $(KDIR) M=$(PWD) modules EXTRA_CFLAGS="$(ccflags-y)"

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean

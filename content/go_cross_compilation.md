Title: Cross Compilation in Go
Date: 2016-06-24
Category: Programming
Tags: tech, code
Slug: go-cross-compilation
Author: Prasanna Venkadesh

Recently I have started to explore the Go programming language or golang in short. Go is a compiled language which can produce standalone binaries for the go programs, which means the receiver of this binary need not have go compiler and the libraries that this program is dependent installed on their machine, instead they can just run the binary and the program will be executed.

This is also the same case with C and C++. If you have used GCC (GNU Compiler Collection) then you could have come across something called cross-compilation in gcc. Compilation means converting from source code to binary, while cross compilation means producing binaries that can be used on other target architectures too.

For example, I am writing code in my laptop which is running Linux kernel and the cpu & operating system architectures are 64-bit (often represented as amd64 or x86\_64). When I compile this source code on my laptop, I will get a binary. I can execute this binary and can also distribute. But the only constraint is this binary is build for 64bit architecture and linux based machines only. Therefore if someone who runs 32bit or ARM based architectures even with Linux kernel, they cannot use this binary.

In order to overcome this, gcc allows developers to do cross compilation. Similarly go compiler also has this feature inbuilt. Here is how we do it

    env GOOS=linux GOARCH=arm go build somefile.go

In the above command, I am setting values for two environment variables GOOS and GOARCH respectively where GOOS is the name of the kernel used in target operating system and GOARCH is the name of the cpu architecture used in the target computer hardware. Succeeding that is the go command to build binary from the source code `somefile.go`. It will take few seconds to build the binary, once that is done now the binary can be used to execute the program in the target machine.

To know the valid and available GOOS and GOARCH values that go accepts, [go here](https://golang.org/doc/install/source#environment)

Note: Producing binaries and distributing them is very good from users usability point of view. It will be convinient for users to just double click on something to see it work (in fact that's how most of them were training through Microsoft Windows). As a free software activist, I appeal that we should also consider the users freedom point of view and give them links to access the source code of the same program that they use in their computer in the binary. The users have the right to know what is being executed in their machines.

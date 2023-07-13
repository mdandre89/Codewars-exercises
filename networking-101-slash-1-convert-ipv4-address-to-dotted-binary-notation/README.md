# Networking 101/1: Convert IPv4 address to Dotted Binary Notation

 - URL:[https://www.codewars.com/kata/6288de23ab7ede0031602521](https://www.codewars.com/kata/6288de23ab7ede0031602521)
 - Id: 6288de23ab7ede0031602521
 - Language: python
 - Completed on: 2022-06-28T16:47:59.303Z
 - Tags: Networks,Bits,Fundamentals,Binary
 - Description:
### Introduction

Both the IPv4 address and subnet mask is made up of 32 bits. The bits are divided into four sections called octets (groups of eight). Each octet can have a number in the range 0 to 255 (unsigned 8-bit integers).

When learning IPv4 addressing it is essential to know how the Binary Number System works as well as having the right tools for the task you are facing. But, you are lacking a good peace of code to visualize the IPv4 addresses and subnet masks in binary form...

### The Assignment

~~~if:c
Your task is to implement a function `void ipv4_to_binary(const char *ipv4_addr, char ipv4_binary[36])` which takes in an IPv4 address `ipv4_addr` and writes the result converted into **Dotted Binary Notation** in the output parameter `ipv4_binary`, a pre-allocated character buffer large enough to hold the result. The function has no return value.
~~~
~~~if:python
Your task is to implement a funtion `def ipv4_to_binary(ipv4_addr: str) -> str`
which takes in an IPv4 address `ipv4_addr`, converts it into **Dotted Binary Notation** and returns it as a string.
~~~

Here are a few examples of input (left) and output (right):

    192.168.0.33    = 11000000.10101000.00000000.00100001
    255.255.255.0   = 11111111.11111111.11111111.00000000

    10.55.0.13      = 00001010.00110111.00000000.00001101
    255.255.255.252 = 11111111.11111111.11111111.11111100

`192.168.0.33` in the example above is the **Dotted Decimal Notation** and 
`11000000.10101000.00000000.00100001` is the corresponding **Dotted Binary Notation**.

>Having a function that prints an address this way might make it easier when making various *bitwise* calculations later on (in subsequent katas).

### Testing

The tests will challenge your function with addresses in the full 32-bit range (`0.0.0.0 - 255.255.255.255`) and ***nothing else***.

### Links
Check out these links for more information:
* https://en.wikipedia.org/wiki/IPv4#Addressing
* https://en.wikipedia.org/wiki/Binary_number


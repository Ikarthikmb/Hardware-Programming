# 4 X 1 - Multiplexer

**Aim**: To design 4x1 multiplexer using Xilinx software 

**Apparatus**: Xilinx software, Computer

**Code**:

    module mux_4to1_assign ( input [3:0] a,                 // 4-bit input called a
                             input [3:0] b,                 // 4-bit input called b
                             input [3:0] c,                 // 4-bit input called c
                             input [3:0] d,                 // 4-bit input called d
                             input [1:0] sel,               // input sel used to select between a,b,c,d
                             output [3:0] out);             // 4-bit output based on input sel

       // When sel[1] is 0, (sel[0]? b:a) is selected and when sel[1] is 1, (sel[0] ? d:c) is taken
       // When sel[0] is 0, a is sent to output, else b and when sel[0] is 0, c is sent to output, else d
       assign out = sel[1] ? (sel[0] ? d : c) : (sel[0] ? b : a); 

    endmodule

**RTL Schematic:**
![4x1 multiplexer](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/Verilog-examples/images/image3.png)

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

![4x1 multiplexer RTL Schematic](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/Verilog-examples/images/image3.png)

**Hardware Schematic:**

![4x1 multiplexer Hardware Schematic](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/Verilog-examples/images/image2.png)

## Testbench:

        module tb_4to1_mux;

           // Declare internal reg variables to drive design inputs
           // Declare wire signals to collect design output
           // Declare other internal variables used in testbench
           reg [3:0] a;
           reg [3:0] b;
           reg [3:0] c;
           reg [3:0] d;
           wire [3:0] out;
           reg [1:0] sel;
           integer i;

           // Instantiate one of the designs, in this case, we have used the design with case statement
           // Connect testbench variables declared above with those in the design
           mux_4to1_case  mux0 (   .a (a),
                                   .b (b),
                                   .c (c),
                                   .d (d),
                                   .sel (sel),
                                   .out (out));

           // This initial block is the stimulus
           initial begin
              // Launch a monitor in background to display values to log whenever a/b/c/d/sel/out changes
              $monitor ("[%0t] sel=0x%0h a=0x%0h b=0x%0h c=0x%0h d=0x%0h out=0x%0h", $time, sel, a, b, c, d, out);

               // 1. At time 0, drive random values to a/b/c/d and keep sel = 0
              sel <= 0;
              a <= $random;
              b <= $random;
              c <= $random;
              d <= $random;

              // 2. Change the value of sel after every 5ns
              for (i = 1; i < 4; i=i+1) begin
                 #5 sel <= i;
              end

              // 3. After Step2 is over, wait for 5ns and finish simulation
              #5 $finish;
           end
        endmodule

### Simulation:
![4x1 multiplexer RTL Schematic](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/Verilog-examples/images/image3.png)

**Result:** Thus the simulation and design of  4x1 multiplexer is studied using Xilinx software.


`default_nettype none
`timescale 1ns/1ps

module tb ();

  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in;
  reg [7:0] uio_in;

  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

  // DUT
  tt_um_upcounter dut (
    .ui_in(ui_in),
    .uo_out(uo_out),
    .uio_in(uio_in),
    .uio_out(uio_out),
    .uio_oe(uio_oe),
    .ena(ena),
    .clk(clk),
    .rst_n(rst_n)
  );

  // clock
  initial clk = 0;
  always #5 clk = ~clk;

  initial begin
    ena = 1;
    ui_in = 0;
    uio_in = 0;

    rst_n = 0;
    #20;
    rst_n = 1;

    #200;
    $finish;
  end

endmodule

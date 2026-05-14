/*
 * 8-bit Up Counter
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_upcounter (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // always enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // active-low reset
);

    // 8-bit counter register
    reg [7:0] counter;

    // Counter logic
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            counter <= 8'b00000000;
        else
            counter <= counter + 1'b1;
    end

    // Connect counter to output
    assign uo_out = counter;

    // Unused bidirectional IOs
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Prevent unused signal warnings
    wire _unused = &{ui_in, uio_in, ena, 1'b0};

endmodule

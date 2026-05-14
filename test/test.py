import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_upcounter(dut):

    cocotb.start_soon(Clock(dut.clk, 10, units="us").start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1

    await ClockCycles(dut.clk, 1)  # important delay

    for i in range(10):
        await ClockCycles(dut.clk, 1)
        val = int(dut.uo_out.value)
        assert val == i + 1, f"Expected {i+1}, got {val}"

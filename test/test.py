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
    await ClockCycles(dut.clk, 3)

    dut.rst_n.value = 1

    for i in range(10):
        await ClockCycles(dut.clk, 1)
        assert int(dut.uo_out.value) == i, f"Expected {i}, got {dut.uo_out.value}"

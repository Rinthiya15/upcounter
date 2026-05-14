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
    await ClockCycles(dut.clk, 2)

    dut.rst_n.value = 1

    expected = 0

    for _ in range(10):
        await ClockCycles(dut.clk, 1)
        expected += 1
        assert int(dut.uo_out.value) == expected

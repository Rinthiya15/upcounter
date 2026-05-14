import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_upcounter(dut):

    cocotb.start_soon(Clock(dut.clk, 10, unit="us").start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    # release reset
    dut.rst_n.value = 1

    # ⚠️ IMPORTANT: wait 1 cycle BEFORE checking
    await ClockCycles(dut.clk, 1)

    expected = 0

    for i in range(10):
        val = int(dut.uo_out.value)
        assert val == expected, f"Expected {expected}, got {val}"
        expected += 1
        await ClockCycles(dut.clk, 1)

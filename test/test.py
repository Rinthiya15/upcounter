# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_upcounter(dut):

    dut._log.info("Starting Up Counter Test")

    # Create 100 KHz clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)

    # Release reset
    dut.rst_n.value = 1

    dut._log.info("Reset released")

    # Check counter increments
    for expected_count in range(10):

        await ClockCycles(dut.clk, 1)

        actual_count = int(dut.uo_out.value)

        dut._log.info(
            f"Expected={expected_count + 1}, Actual={actual_count}"
        )

        assert actual_count == (expected_count + 1), \
            f"Counter mismatch: expected {expected_count + 1}, got {actual_count}"

    dut._log.info("Up Counter Test Passed")

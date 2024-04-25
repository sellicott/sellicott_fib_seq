# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")


    for i in range(0, 10):
        dut._log.info(f"Test n={i}")
        fib_n = await get_fib_n(dut, i)
        calc_fib = calc_fib_n(i)
        dut._log.info(f"hw fib: {fib_n}, sw fib: {calc_fib}")
        assert fib_n == calc_fib

async def get_fib_n(dut, n):
    # Set the input values you want to test
    dut.ui_in.value = n
    dut.uio_in.value = 1

    # Wait for one clock cycle, then clear the strobe pin
    await ClockCycles(dut.clk, 1)
    dut.uio_in.value = 0
    busy_val = ~~(dut.uio_out.value & 0x02)

    if busy_val:
        await FallingEdge(dut.uio_out)

    return dut.uo_out.value

def calc_fib_n(n):
    a = 0
    b = 1
    c = 0
    if n == 0:
        return a

    for i in range(2, n):
        c = a + b
        a = b
        b = c

    return b


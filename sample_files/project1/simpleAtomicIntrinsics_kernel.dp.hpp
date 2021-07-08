#include <CL/sycl.hpp>
#include <dpct/dpct.hpp>
/*
 * Copyright 1993-2015 NVIDIA Corporation.  All rights reserved.
 *
 * Please refer to the NVIDIA end user license agreement (EULA) associated
 * with this source code for terms and conditions that govern your use of
 * this software. Any use, reproduction, disclosure, or distribution of
 * this software and related documentation outside the terms of the EULA
 * is strictly prohibited.
 *
 */

/* Simple kernel demonstrating atomic functions in device code. */

#ifndef _SIMPLEATOMICS_KERNEL_H_
#define _SIMPLEATOMICS_KERNEL_H_

////////////////////////////////////////////////////////////////////////////////
//! Simple test kernel for atomic instructions
//! @param g_idata  input data in global memory
//! @param g_odata  output data in global memory
////////////////////////////////////////////////////////////////////////////////
void
testKernel(int *g_odata, sycl::nd_item<3> item_ct1)
{
    // access thread id
    const unsigned int tid =
        item_ct1.get_local_range().get(2) * item_ct1.get_group(2) +
        item_ct1.get_local_id(2);

    // Atomic addition
    /*
    DPCT1039:0: The generated code assumes that "&g_odata[0]" points to the
    global memory address space. If it points to a local memory address space,
    replace "dpct::atomic_fetch_add" with "dpct::atomic_fetch_add<int,
    sycl::access::address_space::local_space>".
    */
    sycl::atomic<int>(sycl::global_ptr<int>(&g_odata[0])).fetch_add(10);

    // Atomic subtraction (final should be 0)
    /*
    DPCT1039:1: The generated code assumes that "&g_odata[1]" points to the
    global memory address space. If it points to a local memory address space,
    replace "dpct::atomic_fetch_sub" with "dpct::atomic_fetch_sub<int,
    sycl::access::address_space::local_space>".
    */
    sycl::atomic<int>(sycl::global_ptr<int>(&g_odata[1])).fetch_sub(10);

    // Atomic maximum
    /*
    DPCT1039:2: The generated code assumes that "&g_odata[2]" points to the
    global memory address space. If it points to a local memory address space,
    replace "dpct::atomic_fetch_max" with "dpct::atomic_fetch_max<int,
    sycl::access::address_space::local_space>".
    */
    sycl::atomic<int>(sycl::global_ptr<int>(&g_odata[2])).fetch_max(tid);

    // Atomic minimum
    /*
    DPCT1039:3: The generated code assumes that "&g_odata[3]" points to the
    global memory address space. If it points to a local memory address space,
    replace "dpct::atomic_fetch_min" with "dpct::atomic_fetch_min<int,
    sycl::access::address_space::local_space>".
    */
    sycl::atomic<int>(sycl::global_ptr<int>(&g_odata[3])).fetch_min(tid);

    // Atomic AND
    /*
    DPCT1039:4: The generated code assumes that "&g_odata[4]" points to the
    global memory address space. If it points to a local memory address space,
    replace "dpct::atomic_fetch_and" with "dpct::atomic_fetch_and<int,
    sycl::access::address_space::local_space>".
    */
    sycl::atomic<int>(sycl::global_ptr<int>(&g_odata[4]))
        .fetch_and(2 * tid + 7);

    // Atomic OR
    /*
    DPCT1039:5: The generated code assumes that "&g_odata[5]" points to the
    global memory address space. If it points to a local memory address space,
    replace "dpct::atomic_fetch_or" with "dpct::atomic_fetch_or<int,
    sycl::access::address_space::local_space>".
    */
    sycl::atomic<int>(sycl::global_ptr<int>(&g_odata[5])).fetch_or(1 << tid);

    // Atomic XOR
    /*
    DPCT1039:6: The generated code assumes that "&g_odata[6]" points to the
    global memory address space. If it points to a local memory address space,
    replace "dpct::atomic_fetch_xor" with "dpct::atomic_fetch_xor<int,
    sycl::access::address_space::local_space>".
    */
    sycl::atomic<int>(sycl::global_ptr<int>(&g_odata[6])).fetch_xor(tid);
}

#endif // #ifndef _SIMPLEATOMICS_KERNEL_H_

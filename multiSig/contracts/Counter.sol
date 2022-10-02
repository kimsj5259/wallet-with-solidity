// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.0;

contract Counter {
    // 카운터 값
    uint value; 

    // 초기 카운터 값을 설정
    function initialize (uint x) public {
        value = x;
    }

    // 현재 카운터 값
    function get() view public returns (uint) {
        return value;
    }

    // 카운터값 증가
    function increment (uint n) public {
        value = value + n;
    }

    // 카운터값 감소
    function decrement (uint n ) public {
        value = value - n;
    }
}

// solidity 레퍼런스용 코드
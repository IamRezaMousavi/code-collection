%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   Reza Mousavi
% @Last Modified time: 2026-03-20 20:37:54
%

clc;
clear;
close all;

while true
    num = input("Please type a number:");
    if isPrime(num)
        disp("Number is PRIME");
    else
        disp("Number is NOT prime");
    end

    ANS = input("Are you want to continue [Yes/No]?","s");
    if strcmpi(ANS, "NO") || strcmpi(ANS, "N")
        break;
    end
end

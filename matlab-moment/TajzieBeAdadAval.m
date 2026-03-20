%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   Reza Mousavi
% @Last Modified time: 2026-03-20 20:54:21
%

clc;
clear;
close all;

function primeFactors = getPrimeFactors(num)
    primeFactors = [];

    while mod(num, 2) == 0
        primeFactors = [primeFactors 2];
        num = num / 2;
    end

    for i = 3:2:sqrt(num) 
        while mod(num, i) == 0
            primeFactors = [primeFactors i];
            num = num / i;
        end
        if num < i 
            break;
        end
    end

    if num > 1
        primeFactors = [primeFactors num];
    end
end

number = input("Please enter a number:");
result = getPrimeFactors(number) 

if isempty(result)
    disp(['The number ', num2str(number), ' has no prime factors (it might be 0 or 1, or negative).']);
else
    fprintf('The prime factorization of %d is: [%s]\n', number, num2str(result));
end

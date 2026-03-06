%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   S.Reza Mousavi
% @Last Modified time: 2021-12-31 23:19:47
%

clc;
clear;
close all;

n = input("Please Enter a number:");
answer = [];

for i = 2:n
    isPrime = 1;
    for j = 2:(i^(1/2))
       if mod(i, j) == 0
          isPrime = 0;
          break;
       end
    end
    if isPrime == 1
       answer = [answer i]; 
    end
end
disp(answer);

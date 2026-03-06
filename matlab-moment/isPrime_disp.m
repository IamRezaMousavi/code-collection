%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   S.Reza Mousavi
% @Last Modified time: 2021-12-31 23:22:49
%

clc;
clear;
close all;

while true
    num = input("Please type a number:");
    IsPrime = true;
    for i = 2 : num^(1/2)
        if mod(num, i) == 0
            IsPrime = false;
            disp("Number is NOT prime");
            break;
        end
    end
    if IsPrime
        disp("Number is PRIME");
    end
    ANS = input("Are you want to continue [Yes/No]?","s");
    if strcmpi(ANS, "NO") || strcmpi(ANS, "N")
        break;
    end
end

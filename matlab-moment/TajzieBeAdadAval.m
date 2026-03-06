%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   S.Reza Mousavi
% @Last Modified time: 2021-12-31 23:25:25
%

clc;
clear;
close all;

number = input("Please enter a number:");
answer = [];
for i = 2:number
    while mod(number, i) == 0
        answer = [answer i];
        disp(num2str(answer));
        number = number / i;
    end
end

disp(" ");
disp("The Answer is [" + num2str(answer) + "].");

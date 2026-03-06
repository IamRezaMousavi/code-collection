%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   S.Reza Mousavi
% @Last Modified time: 2021-12-31 23:21:09
%

clc;
clear;
close all;

x = linspace(0, 1.4, 300);
A = 0.1 : 0.1 : 4;
color = hsv(numel(A));

i = 0;
figure;
for a = A
    i = i + 1;
    y = x .^ a;
    plot(x, y, "color", color(i, :));
    hold on;
end

input("Please Enter a key...");

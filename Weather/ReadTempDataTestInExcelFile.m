clc;
clear;
close all;

Data = xlsread('TempDataTestByExcel.xls');
disp("Data is:");
disp(Data);

t = 1:4:60;
tt = linspace(0,60,100);
PData = spline(t,Data,tt);

plot(t,Data, "o");
hold on;grid on;
plot(tt,PData, "r");

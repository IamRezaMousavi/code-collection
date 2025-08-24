clc;
clear;
close all;

Data = randi([1 100],1,15);
Data = sort(Data);
t = 1:3:45;
tt = linspace(0,45,100);
PData = spline(t,Data,tt);

plot(t,Data, "-o");
hold on;grid on;
plot(tt,PData, "r", "LineWidth", 1.5);

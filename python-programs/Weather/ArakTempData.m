clc;
clear;
close all;

Temp = xlsread('ArakTempData.xls');

TempData = Temp(1,:);
TempTime = Temp(2,:);

TempData = TempData - 273.15;

figure;
plot(TempTime,TempData);grid on;

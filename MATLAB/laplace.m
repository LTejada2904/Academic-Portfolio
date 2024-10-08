%% ELEN 3420 Signal & Systems
% Chapter 3
% Example 1
% Prof. Ruben Flores
%%
clc; clear; close all;

syms t s

% Part 1
x1 = ((t)^2)*exp(-3*(t))*stp_fn(t);
x1 = laplace(x1);               % Finds Laplace transform
x1 = collect(x1);               % Combining terms
x1 = simplify(x1, 'steps', 10); % Simplify expression to its minimum expression
pretty(x1)                      % shows result to easier to understand

[num, den] = numden(x1);        % separate num and den expressions
TFnum = sym2poly(num);          % form matrix with poly coefficients
TFden = sym2poly(den);          % form matrix with poly coefficients
sysX1 = tf(TFnum,TFden)         % forms tf object (s-plane) of X1
figure;
pzplot(sysX1); grid on          % plots poles and root locations
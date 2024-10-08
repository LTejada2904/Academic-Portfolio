clc; clear; close all

xp = @(t) 2*stp_fn(t) + 2*stp_fn(t-2) - 4*stp_fn(t-4)

x = 0;
To = 1;
N = 5;
t = linspace(-N*To,N*To,1000*N);

for n=-N:N
    x = x + xp (t-n*To);
end

plot(t,x,'LineWidth',5);grid on
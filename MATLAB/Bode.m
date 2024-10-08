% Define the transfer function
numerator = 12.889 * [1, 5, 4];
denominator = [1, 8, 25, 26];
% Create transfer function object
sys = tf(numerator, denominator);
% Plot the Bode plot
bode(sys);
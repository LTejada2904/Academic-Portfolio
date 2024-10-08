% Function to calculate cubic roots
function roots = cubicFormula(A, B, C, D)
    % Normalize coefficients
    a = B / A;
    b = C / A;
    c = D / A;

    % Intermediate terms for cubic formula
    delta_0 = a^2 - 3 * b;
    delta_1 = 2 * a^3 - 9 * a * b + 27 * c;

    % Discriminant for cubic equation
    discriminant = (delta_1^2) - 4 * (delta_0^3);

    % Calculate complex cube roots
    C1 = ((delta_1 + sqrt(discriminant)) / 2)^(1/3);
    
    % Avoid division by zero
    if abs(C1) < 1e-10
        C1 = ((delta_1 - sqrt(discriminant)) / 2)^(1/3);
    end

    % Complex cube root of unity
    omega = -0.5 + 0.5 * sqrt(3) * 1i;

    % Calculate the cubic roots
    root1 = -1/3 * a + C1 + delta_0 / C1;
    root2 = -1/3 * a + omega * C1 + delta_0 / (omega * C1);
    root3 = -1/3 * a + omega^2 * C1 + delta_0 / (omega^2 * C1);

    % Return the roots
    roots = [root1, root2, root3];
end

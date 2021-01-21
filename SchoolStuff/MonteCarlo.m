x = [0:0.01:1];
y = [0:0.01:1];
z = [0:0.01:1];
u = [0:0.01:1];
v = [0:0.01:1];
I1 = y.^3.*exp(-2.*z).*cos(u).*sin(x).*v.^5;
I2 = y.^3.*exp(-2.*z).*cos(u).*sin(x).*(-1);
plot(x, y, z, u, v, I1, x, y, z, u, v, I2, 'k');
hold on;
n = 0;
for i = 1:1000
    x_i = 2*rand - 1;
    y_i = 2*rand - 1;
    z_i = 2*rand - 1;
    u_i = 2*rand - 1;
    v_i = 2*rand - 1;
    if 
    
end

A = n/1000

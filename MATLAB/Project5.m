format long
f = @(t,u) u^2 - 2*u^4;
y0=0.005;

[t,u]=am2(f,[0 400], y0,200);
u(95:105)
plot(t,u)
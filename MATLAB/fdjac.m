function J=fdjac(f,x0,y0)
    delta=sqrt(eps);
    m=length(y0);
    n=length(x0);
    J=zeros(m,n);
    I=eye(n);
    for j = 1:n
        J(:,j)=(f(x0+delta*I(:,j))-y0)/delta;
    end
end
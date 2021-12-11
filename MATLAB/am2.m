function [t,u]=am2(dudt,tspan,u0,n)
    a=tspan(1);
    b=tspan(2);
    h=(b-a)/n;
    t= tspan(1) + (0:n)'*h;
    m=numel(u0);
    u=zeros(m,n+1);
    u(:,1)=u0(:);
    for i = 1:n
        known = u(:,i) + h/2*dudt(t(i),u(:,i));
        unew=levenberg(@trapzero,known);
        u(:,i+1) = unew(:,end);
    end
    
    u=u.';
    function F = trapzero(z)
        F=z-h/2*dudt(t(i+1),z)-known;
    end
end
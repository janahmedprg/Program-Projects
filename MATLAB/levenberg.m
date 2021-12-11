function x = levenberg(f,x1)
    tol=1e-12;
    if nargin<3,tol=1e-12;end
    ftol=tol; xtol=tol; maxiter=40;
    x=x1(:); fk=f(x1);
    k=1;s=Inf;
    Ak=fdjac(f,x(:,1),fk);
    jac_is_new=true;
    I=eye(length(x));
    lambda=10;
    while(norm(s) > xtol) && (norm(fk) > ftol) && (k<maxiter)
        B= Ak'*Ak + lambda*I;
        z=Ak'*fk;
        s=-(B\z);
        xnew=x(:,k)+s; fnew=f(xnew);
        if norm(fnew)<norm(fk)
            y=fnew-fk;
            x(:,k+1)=xnew; fk=fnew;
            k=k+1;
            lambda= lambda/10;
            Ak=Ak+(y-Ak*s)*(s'/(s'*s));
            jac_is_new=false;
        else
            lambda = lambda*4;
            if ~jac_is_new
                Ak=fdac(f,x(:,k),fk);
                jac_is_new = true;
            end
        end
    end
    if(norm(fk)>1e-2)
        warning('Iteration did not find a root')
    end
end
tic

A = load('Catedraldescriptors.txt' , '-ascii');
B = load('UASLPdescriptors.txt' , '-ascii');
C = load('Cajadescriptors.txt' , '-ascii');
%n= 400;
%s=40;
%A1 = A(s:n+s-1, :);
%B1 = B(s:n+s-1, :);
%C1 = C(s:n+s-1, :);
t1=rows(A);
t2= rows(B);
t3= rows(C);

%I = [A1; B1; C1];
I= [A; B; C];


I = transpose (I);

O = [[ones(1,t1);zeros(1,t1);zeros(1,t1)],[zeros(1,t2); ones(1,t2); zeros(1,t2)],[zeros(1,t3);zeros(1,t3);ones(1,t3)]];
%O = [[ones(1,n);zeros(1,n);zeros(1,n)],[zeros(1,n);ones(1,n);zeros(1,n)],[zeros(1,n);zeros(1,n);ones(1,n)]];

net4 = newff(min_max(I),[60 3], {"tansig","purelin"}, "trainlm", "learngdm", "mse");
%net.trainParam.epochs= 50;
net4 = train(net4, I, O);

save net4;

timeElapsed = toc
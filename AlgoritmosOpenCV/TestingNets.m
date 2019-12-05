load net;
A1= load('TCatedraldescriptors.txt' , '-ascii');
B1 = load('TUASLPdescriptors.txt', '-ascii');
C1 = load('TCajadescriptors.txt', '-ascii');

I = [A1; B1; C1];
I = transpose (I);

Y = sim(net, I);

Y= round(Y);
contA=0;
contB=0;
contC=0;

t1=rows(A1);
t2= rows(B1);
t3= rows(C1);

n= columns(I);

n
%Loop to know if all the outputs are correctly
for i=1:n
  if i<=t1
    if Y(1,i) == 1 && Y(2,i) == 0 && Y(3,i) == 0
      contA=contA+1;
    end 
   end

   if t1<i<=(t1+t2)
      if Y(1,i) == 0 && Y(2,i) == 1 && Y(3,i) == 0
        contB=contB+1;
      end
   end  
   if (t1+t2)<i<=(t2+t3)
    if Y(1,i) == 0 && Y(2,i) == 0 && Y(3,i) == 1
      contC=contC+1;
    end
   end
    
end

contA
contB
contC

res = t1-contA
res1 = t2-contB
res2 = t3-contC
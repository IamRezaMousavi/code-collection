%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   S.Reza Mousavi
% @Last Modified time: 2021-12-31 23:22:49
%

function IsPrime = isPrime(number)
    if number < 2
        disp("The number must be greater than 2");
    end
    for i = 2:sqrt(number)
        IsPrime = true;
        if mod(number, i) == 0
            IsPrime = false;
            break;
        end
    end
end

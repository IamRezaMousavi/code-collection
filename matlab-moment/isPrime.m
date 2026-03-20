%
% @Author: S.Reza Mousavi
% @Date:   2021-12-23 18:32:56
% @Last Modified by:   Reza Mousavi
% @Last Modified time: 2026-03-20 20:38:03
%

function IsPrime = isPrime(number)
    if number < 2
        IsPrime = false;
        return;
    end
    if number == 2
        IsPrime = true;
        return;
    end
    if mod(number, 2) == 0
        IsPrime = false;
        return;
    end
    limit = sqrt(number);
    for i = 3:2:limit
        if mod(number, i) == 0
            IsPrime = false;
            return;
        end
    end
    IsPrime = true;
end

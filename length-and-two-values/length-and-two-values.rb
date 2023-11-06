def alternate(n, first, second)
  ls = []
  for i in 1..n do
    if i.even? 
        ls.push(second)
    else
        ls.push(first)
    end
  end
  return ls
end
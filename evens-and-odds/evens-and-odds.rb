def evensAndOdds(n)
  if n.even?
    return n.to_s(2)
  else
    return n.to_s(16)
  end
end
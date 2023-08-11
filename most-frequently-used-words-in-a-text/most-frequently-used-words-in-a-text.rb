def top_3_words(text)
  text.downcase.gsub(/ ' /, '').scan(/[a-z']+/).each_with_object(Hash.new(0)){|w,h| h[w.downcase]+=1}.sort_by{|w, fr|-fr}.to_h.keys[0,3]
end
function reverseWords(st) {
  return st.replace(/[A-z!?.,]*/gi,function(m){return m.split('').reverse().join('')})
}
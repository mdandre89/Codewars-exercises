function pigIt(st){
  return st.split(" ").map(i=>i.substr(1)+i[0]+"ay").join(" ")
}
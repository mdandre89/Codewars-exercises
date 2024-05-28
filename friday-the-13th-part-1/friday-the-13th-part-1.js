function killcount(counselors, jason){
  return counselors.filter(a => a[1]<jason).map(l=>l[0])
}
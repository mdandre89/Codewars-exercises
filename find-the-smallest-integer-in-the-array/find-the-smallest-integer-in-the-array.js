class SmallestIntegerFinder {
  findSmallestInt(args) {
    return args.reduce((a,b)=> a>b ? b : a);
  }
}
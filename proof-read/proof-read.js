function proofread (str) { 
return str.toLowerCase().replace(/ie/g,"ei").split(". ").map(s=>s.charAt(0).toUpperCase() + s.slice(1)).join(". ")
} 


proofread ("ShE deCIeved HiM.");
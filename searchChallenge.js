function SearchingChallenge(str) { 

  // code goes here 
  let brackets={
    ")":"(",
    "}":"{",
    "]":"["
  } 
  let stackArr=[]
  let res=0
  for(let i=0;i<str.length;i++){
    if(str[i]==="(" || str[i]==="{" || str[i]==="[" ){
      
      stackArr.push(str[i])
      // console.log(stackArr,"adding")
    }
    else if(stackArr[stackArr.length-1 ]=== brackets[str[i]]){
      // console.log(stackArr,"removing",brackets[str[i]],str[i])
      if(stackArr.length!=0){
      res+=1
      }
      stackArr.pop()
      
    }
    // else {
    //   continue
    // }
  }
  if(stackArr.length==0){
  // console.log(res,"ress",stackArr)

    return  `1 ${res}`
  }
  else {
    return 0
  }
  // return str; 

}
   SearchingChallenge("(c[od]er))b(yt[i])")
// keep this function call here 
// console.log(SearchingChallenge(readline()));
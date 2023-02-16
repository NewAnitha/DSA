// reverse an array 

// const reverseArray=(arr,start,end)=>{
//     while(start<end){
//         let temp= arr[start]
//         arr[start]=arr[end]
//         arr[end]=temp
//         console.log(start,end,arr[start],arr[end])
//         start++
//         end--
//     }
//     return arr
// }


//recursive function
// const reverseArray=(arr,start,end)=>{
//         let temp= arr[start]
//         arr[start]=arr[end]
//         arr[end]=temp
//         if(start+1<end-1){
//             reverseArray(arr,start+1,end-1)
//         }
//         return arr

// }
// console.log(reverseArray([1,2,3,4,5],0,4))


// Rotation of Array

// const leftRotationArray=(arr,d,n)=>{
//     let temp = new Array(n)
//     let k=0;
//     for(let i=d;i<n;i++){
//         temp[k]=arr[i]
//         k++
//     }
//     for(let i=0;i<d;i++){
//         temp[k]=arr[i]
//         k++
//     }

//     return temp
// }
// console.log(leftRotationArray([1,2,3,4,5,6],3,6))

// const rightRotationArray=(arr,n,k)=>{
//     k=k%n
//     let temp=[]
//     for(let i=0;i<n;i++){
//         if(i<k){
//             temp.push(arr[n+i-k])
//         }
//         else{
//             temp.push(arr[i-k])
//         }
//     }
//     return temp
// }
// console.log(rightRotationArray([1,2,3,4,5,6],6,3))


const insertInArray=(arr,pos,val)=>{

    for(let i;i>pos;i--){
        arr[i+1]=arr[i]
    }
    console.log(arr,"arrrr");
    arr[pos]=val

    return arr
}
console.log(insertInArray([1,2,4,5],2,3));
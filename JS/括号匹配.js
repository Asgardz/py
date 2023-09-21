var isVaild = function(s){

    var stack = []
    for( let i = 0; i < s.length; i++){
        start = s[i];
        if(start == '(' || start == '{' || start =='['){
            stack.push(s[i]);
        }else{
            end = stack[stack.length-1];
            if(start == ')' && end == '(' || 
            start == ']' && end == '[' ||
            start == '}' && end == '{'
            ){
                stack.pop();
            }else{
                return false;
            }
        }
    }
    return stack.length == 0;
}

console.log(isVaild('(){}'));
console.log(isVaild('({})'));
console.log(isVaild('(]{'));
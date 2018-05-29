/*  */
function reverseInteger(x) {
  let num = x
  let reversedNum = 0
  while(num){
    const lastDigit = num%10
    num = (num - lastDigit) / 10
    reversedNum = (reversedNum * 10) + lastDigit
  }
  /** Need review these bounds again */
  if (reversedNum >= 2147483647 || reversedNum <= -2147483647) {
      return 0;
  }

  return reversedNum
};
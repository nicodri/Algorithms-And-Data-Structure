#include <stdint.h>
#include <stdio.h>

// Naive recursive computation: O(2^n) in time and O(1) in memory
int fib_recursive(int n){
  if (n == 1){
    return 0;
  }
  if (n == 2){
    return 1;
  }
  return fib_recursive(n - 1) + fib_recursive(n - 2);
}

// Efficient computation: O(n) in time and O(1) in memory
int fib_efficient(int n){
  int new;
  int current[] = {0, 1};
  if ((n == 1) || (n == 2)) return current[n-1];

  for(int i=3; i<=n; i++){
    new = current[0] + current[1];
    current[0] = current[1];
    current[1] = new;
  } 
  return current[1];
}

int main(int argc, char **argv)
{
  int test[] = {10, 20, 30};
  for (int k=0; k<3; k++)
  printf("Test with n=%d, f_recursive = %d f_efficient = %d\n", test[k],
         fib_recursive(test[k]), fib_efficient(test[k]));
}

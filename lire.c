#include<stdio.h>
int main(){
    FILE *ptr;
    ptr = fopen("index.txt","r");
    if(ptr==NULL){
        perror("505 error");
    }
    
    return 0;
}
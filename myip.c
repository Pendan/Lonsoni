#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include "hacking.h"

int main(int argc, char *argv[]) {
int sockfd;
struct hostent *host_info;
struct sockaddr_in target_addr;
unsigned char buffer[4096];

if((host_info = gethostbyname("www.ipchicken.com")) == NULL)   //controllo errori random
	fatal("looking up hostname");

if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1)		//pure
	fatal("in socket");

target_addr.sin_family = AF_INET;
target_addr.sin_port = htons(80);				//roba che tocca fare per aprire connessioni
target_addr.sin_addr = *((struct in_addr *)host_info->h_addr);
memset(&(target_addr.sin_zero), '\0', 8); // Riempie con zeri il resto della struttura.
	if (connect(sockfd, (struct sockaddr *)&target_addr, sizeof(struct sockaddr)) == -1)  //connetto ad un sito che restituisce il tuo ip
		fatal("connecting to target server");
send_string(sockfd, "GET\r\n");   //chiedo index.html
if(!recv_line(sockfd, buffer)) {    

if(strncasecmp(buffer, "<", 1)== 0) {
int length = 21;
printf("Your ip adress is: %*.*s \n",length, length, buffer+1547);  //dalla sorgente della pagina html estraggo la stringa col mio ip
exit(0);
}
}
printf("IP line not found\n");  //casomai dovesse cambiare tutto anche di una virgola
exit(1);
}


